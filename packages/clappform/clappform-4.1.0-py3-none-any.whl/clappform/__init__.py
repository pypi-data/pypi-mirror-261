"""
Clappform API Wrapper
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022 Clappform B.V..
:license: MIT, see LICENSE for more details.
"""
__requires__ = ["requests==2.28.1", "Cerberus==1.3.4", "pandas==1.5.2"]
# Python Standard Library modules
from urllib.parse import urlparse
from dataclasses import asdict
from concurrent import futures
from itertools import chain
from queue import Queue
import tempfile
import math
import time
import os

from typing import Generator

# PyPi modules
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout, ConnectTimeout
import requests as r

from cerberus import Validator
from pandas import DataFrame
import numpy as np

# clappform Package imports.
from . import dataclasses as dc
from .exceptions import (
    HTTPError,
    PaginationTotalError,
    PaginationKeyError,
)


# Metadata
__version__ = "4.1.0"
__author__ = "Clappform B.V."
__email__ = "info@clappform.com"
__license__ = "MIT"
__doc__ = "Clappform Python API wrapper"


class Clappform:
    """:class:`Clappform <Clappform>` class is used to more easily interact with an
    Clappform environement through the API.

    :param str base_url: Base URL of a Clappform environment e.g.
        ``https://app.clappform.com``.
    :param str username: Username used in the authentication :meth:`auth <auth>`.
    :param str password: Password used in the authentication :meth:`auth <auth>`.
    :param int workers: Number of workers to use in ThreadPoolExecutor and
         Connectionpool. Defaults to ``min(32, os.cpu_count() + 4)``.
    :param int tries: Number of times to try (not retry) before giving up.
    :param int backoff_factor: Backoff factor to multiply delay with.

    Most routes of the Clappform API require authentication. For the routes in the
    Clappform API that require authentication :class:`Clappform <Clappform>` will do
    the authentication for you.

    In the example below ``c.get(r.App())`` uses a route which requires authentication.
    :class:`Clappform <Clappform>` does the authentication for you.

    Usage::

        >>> from clappform import Clappform
        >>> import clappform.dataclasses as r
        >>> c = Clappform(
        ...     "https://app.clappform.com",
        ...     "j.doe@clappform.com",
        ...     "S3cr3tP4ssw0rd!",
        ... )
        >>> apps = c.get(r.App())
        >>> for app in apps:
        ...     print(app.name)

    The :meth:`get`, :meth:`create`, :meth:`update` and :meth:`delete`
    methods can act on any object that implements the
    :class:`clappform.dataclasses.ResourceType` interface.

    The currently supported resources are:
      - :class:`clappform.dataclasses.App`
      - :class:`clappform.dataclasses.Collection`
      - :class:`clappform.dataclasses.Query`
      - :class:`clappform.dataclasses.Actionflow`
      - :class:`clappform.dataclasses.Questionnaire`
      - :class:`clappform.dataclasses.User`
    """

    _auth: dc.Auth = None

    def __init__(  # pylint: disable=R0913
        self,
        base_url: str,
        username: str,
        password: str,
        workers: int = min(32, os.cpu_count() + 4),
        tries: int = 4,
        backoff_factor: int = 1,
    ):
        self._base_url: str = f"{base_url}/api"

        #: Number of times to try (not retry) before giving up.
        self.tries: int = 4

        #: Backoff factor to multiply delay with.
        self.backoff_factor: int = 1

        #: List of HTTP status codes to force a try on.
        self.status_forcelist: list[int] = [502, 503, 504]

        #: Session for all HTTP requests.
        self.session: r.sessions.Session = r.Session()
        self.session.headers.update({"User-Agent": self._default_user_agent()})
        self.session.mount(
            self._base_url,
            HTTPAdapter(
                max_retries=Retry(
                    total=self.tries - 1,  # Total of 3 retries.
                    backoff_factor=self.backoff_factor,
                    status_forcelist=[502, 503, 504],
                ),
                pool_maxsize=workers,
            ),
        )

        #: Username to use in the :meth:`auth <auth>`
        self.username: str = username

        #: Password to use in the :meth:`auth <auth>`
        self.password: str = password

        #: Number of workers to use in ThreadPoolExecutor and Connectionpool.
        #: defaults to: ``min(32, os.cpu_count() + 4)``.
        self.workers: int = workers

        #: Default request keyword arguments.
        self.request_kwargs: dict = {
            "timeout": 10,
            "allow_redirects": True,
            "verify": True,
            "stream": False,
            "cert": None,
        }

        #: ThreadPoolExecut obj to submit large amount of requests to.
        self.executor = futures.ThreadPoolExecutor(max_workers=workers)

    def _default_user_agent(self) -> str:
        """Return a string with version of requests and clappform packages."""
        requests_ua = r.utils.default_user_agent()
        return f"clappform/{__version__} {requests_ua}"

    def _request(self, method: str, path: str, **kwargs) -> dict:
        updated_kwargs = self.request_kwargs.copy()
        updated_kwargs.update(kwargs)

        delay, sleep_for, tries, immediate_retry = 1, 0, self.tries, True
        while tries >= 1:
            time.sleep(sleep_for)
            try:
                resp = self.session.request(
                    method, f"{self._base_url}{path}", **updated_kwargs
                )
                if resp.status_code in self.status_forcelist:
                    raise ConnectTimeout(
                        f"received a '{resp.status_code}' status code", response=resp
                    )
                break
            except Timeout:
                tries -= 1
                if immediate_retry:
                    immediate_retry = not immediate_retry
                if tries <= 0:
                    raise
                delay *= 2
                sleep_for = self.backoff_factor * delay

        doc = resp.json()
        try:
            resp.raise_for_status()
        except r.exceptions.HTTPError as exc:
            raise HTTPError(
                doc["message"],
                code=doc["code"],
                response_id=doc["response_id"],
                response=resp,
            ) from exc
        return doc

    def _private_request(self, method: str, path: str, **kwargs):
        """Implements :meth:`_request` and adds Authorization header."""
        if "Authorization" not in self.session.headers:
            self.auth()
        elif not self._auth.is_token_valid():
            self.auth()

        return self._request(method, path, **kwargs)

    def auth(self) -> None:
        """Sends an authentication request. Gets called whenever authentication is
        required.

        The :attr:`_auth` attribute is set to a newly constructed
        :class:`clappform.dataclasses.Auth` object.
        """
        document = self._request(
            "POST",
            "/auth",
            json={"username": self.username, "password": self.password},
        )
        self._auth = dc.Auth(**document["data"])
        self.session.headers.update(
            {"Authorization": f"Bearer {self._auth.access_token}"}
        )

    def verify_auth(self) -> dc.ApiResponse:
        """Verify against the API if the authentication is valid.

        :returns: API response object
        :rtype: clappform.dataclasses.ApiResponse
        """
        document = self._private_request("POST", "/auth/verify")
        return dc.ApiResponse(**document)

    def _remove_nones(self, original: dict) -> dict:
        return {k: v for k, v in original.items() if v is not None}

    def _seperate_id_from_item(self, original: dict) -> tuple[str, dict]:
        try:
            item_id = original.pop("_id")  # `_id` is MongoDB generated unique id
        except KeyError as exc:
            raise KeyError("could not find '_id' in item") from exc
        if not isinstance(item_id, str):
            raise TypeError(
                f"value of item['_id'] is not of type {str}, got {type(item_id)}"
            )
        return (item_id, original)

    def get(self, resource, item=None):
        """Get a one or list of resources.

        :param resource: Any object of :class:`clappform.dataclasses.ResourceType`
        :param item: Optional only useful when resource argument is of type
            :class:`clappform.dataclasses.Collection`.
        :type item: dict

        Usage::

            >>> from clappform import Clappform
            >>> import clappform.dataclasses as r
            >>> c = Clappform(
            ...     "https://app.clappform.com",
            ...     "j.doe@clappform.com",
            ...     "S3cr3tP4ssw0rd!"
            ... )
            >>> collection = c.get(r.Collection(id="clappform", slug="us_presidents"))
            >>> c.get(collection, item={"_id", "6475c76276ffd5e8da000b2c"})
            {'_id': '6475c76276ffd5e8da000b2c', 'name': "George Washington"}

        :returns: One or a list of resources
        """
        kwargs = {"method": "GET", "path": resource.one_or_all_path()}
        # Custom behavior when arguments are specific types.
        if isinstance(resource, dc.Collection) and isinstance(item, dict):
            item_id, _ = self._seperate_id_from_item(item)
            document = self._private_request("GET", resource.one_item_path(item_id))
            document["data"]["_id"] = item_id  # Adding item's id back into response.
            return document["data"]

        document = self._private_request(**kwargs)

        # `type(resource)` is e.g. `dc.App`
        if isinstance(document["data"], list):
            return [type(resource)(**x) for x in document["data"]]
        if isinstance(document["data"], dict):
            return type(resource)(**document["data"])
        raise TypeError(
            f"'data' key-value is not {list} or {dict}, got {type(document['data'])}"
        )

    def create(self, resource, item=None):
        """Crete a resource.

        :param resource: Any object of :class:`clappform.dataclasses.ResourceType`
        :param item: Optional only useful when resource argument is of type
            :class:`clappform.dataclasses.Collection`.
        :type item: dict

        Usage::

            >>> from clappform import Clappform
            >>> import clappform.dataclasses as r
            >>> c = Clappform(
            ...     "https://app.clappform.com",
            ...     "j.doe@clappform.com",
            ...     "S3cr3tP4ssw0rd!"
            ... )
            >>> new_app = r.App(
            ...     id="uspresidents",
            ...     name="US Presidents",
            ...     description="US Presidents Dashboard",
            ...     settings={}
            ... )
            >>> c.create(new_app)
            App(collections=0, default_page='', description='US Presidents Dashboard...

        :returns: Newly created resource
        """
        # Custom behavior when arguments are of a specific type.
        if isinstance(resource, dc.Collection) and isinstance(item, dict):
            document = self._private_request(
                "POST", resource.create_item_path(), json={"data": item}
            )
            return document["data"]
        if isinstance(resource, dc.Questionnaire):
            document = self._private_request(
                "POST",
                resource.create_path(),
                json={"name": resource.name, "settings": resource.settings},
            )
            return dc.Questionnaire(**document["data"])

        payload = self._remove_nones(asdict(resource))
        document = self._private_request("POST", resource.create_path(), json=payload)
        return type(resource)(**document["data"])

    def update(self, resource, item=None):
        """Update a resource.

        :param resource: Any object of :class:`clappform.dataclasses.ResourceType`
        :param item: Optional only useful when resource argument is of type
            :class:`clappform.dataclasses.Collection`.
        :type item: dict

        Usage::

            >>> from clappform import Clappform
            >>> import clappform.dataclasses as r
            >>> c = Clappform(
            ...     "https://app.clappform.com",
            ...     "j.doe@clappform.com",
            ...     "S3cr3tP4ssw0rd!"
            ... )
            >>> app = c.get(r.App(id="uspresidents"))
            >>> app.description = "Dashboard of US Presidents"
            >>> c.update(app)
            App(collections=0, default_page='', description='Dashboard of US Preside...

        :returns: Updated resource
        """
        # Custom behavior when arguments are specific types.
        if isinstance(resource, dc.Collection) and isinstance(item, dict):
            item_id, item = self._seperate_id_from_item(item)
            document = self._private_request(
                "PUT", resource.one_item_path(item_id), json={"data": item}
            )
            document["data"]["_id"] = item_id  # Adding item's id back into response.
            return document["data"]
        if isinstance(resource, dc.Questionnaire):
            document = self._private_request(
                "PUT",
                resource.one_path(),
                json={"name": resource.name, "settings": resource.settings},
            )
            return dc.Questionnaire(**document["data"])

        payload = self._remove_nones(asdict(resource))
        if isinstance(resource, dc.User):
            del payload["email"]

        document = self._private_request("PUT", resource.one_path(), json=payload)
        return type(resource)(**document["data"])

    def delete(self, resource, item=None):
        """Delete a resource.

        Usage::

            >>> from clappform import Clappform
            >>> import clappform.dataclasses as r
            >>> c = Clappform(
            ...     "https://app.clappform.com",
            ...     "j.doe@clappform.com",
            ...     "S3cr3tP4ssw0rd!",
            ... )
            >>> app = c.get(r.App(id="uspresidents"))
            >>> c.delete(app)
            ApiResponse(code=200, message='Successfully deleted app with ID: uspresi...

        :returns: Confirmation of deletion.
        :rtype: :class:`clappform.dataclasses.ApiResponse`
        """
        # Custom behavior when arguments are specific types.
        if isinstance(resource, dc.Collection) and item is not None:
            oids: list[str] = None
            if isinstance(item, list):
                # `0` element of `_seperate_id_from_item` is an item's id.
                oids = [self._seperate_id_from_item(x)[0] for x in item]
            if isinstance(item, dict):
                oids = [self._seperate_id_from_item(item)[0]]
            if isinstance(oids, list):
                document = self._private_request(
                    "DELETE", resource.create_item_path(), json={"oids": oids}
                )
                return dc.ApiResponse(**document)
            t = type(item)
            raise TypeError(
                f"item keyword argument is not of type {list} or {dict}, got {t}"
            )

        document = self._private_request("DELETE", resource.one_path())
        return dc.ApiResponse(**document)

    def aggregate_dataframe(
        self, options: dict, max_workers=None
    ) -> Generator[list[dict], None, None]:
        """Aggregate a dataframe

        :param dict options: Options for dataframe aggregation.
        :param int max_workers: Optional number of workers to use in thread pool.

        :returns: Generator to read dataframe
        :rtype: Generator
        """
        v = Validator(
            {
                "app": {"type": "string"},
                "collection": {"type": "string"},
                "type": {"type": "string"},
                "limit": {"min": 10, "max": 500},
                "sorting": {
                    "type": "dict",
                    "allow_unknown": True,
                    "schema": {
                        "ASC": {"type": "list"},
                        "DESC": {"type": "list"},
                    },
                },
                "search": {
                    "type": "dict",
                    "allow_unknown": True,
                    "schema": {
                        "input": {"type": "string"},
                        "keys": {"type": "list"},
                    },
                },
                "item_id": {
                    "type": "string",
                    "nullable": True,
                },
                "deep_dive": {"type": "dict"},
            },
            require_all=True,
        )
        v.validate(options)

        path = "/dataframe/read_data?extended=true"
        payload = v.document

        document = self._private_request("POST", path, json=payload)
        if "total" not in document:
            raise PaginationKeyError(missing_key="total", data=document)
        if document["total"] == 0:
            raise PaginationTotalError(total=document["total"], data=document)
        yield document["data"]

        pages_to_get = math.ceil(document["total"] / options["limit"])
        if pages_to_get == 1:
            pass
        else:
            for result in self.executor.map(
                lambda x: self._private_request(
                    "POST", f"{path}&next_page={x}", json=payload
                ),
                range(
                    options["limit"],
                    pages_to_get * options["limit"],
                    options["limit"],
                ),
            ):
                yield result["data"]

    def read_dataframe(
        self, query, limit: int = 100, max_workers=None
    ) -> Generator[list[dict], None, None]:
        """Read a dataframe.

        :param query: Query to for retreiving data. When Query is of type
            :class:`clappform.dataclasses.Collection` everything inside the collection
            is retreived.
        :type query: :class:`clappform.dataclasses.Query` |
            :class:`clappform.dataclasses.Collection`
        :param int limit: Amount of records to retreive per request.
        :param int max_workers: Optional number of workers to use in thread pool.

        Usage::

            >>> from clappform import Clappform
            >>> import clappform.dataclasses as r
            >>> import pandas as pd
            >>> c = Clappform(
            ...     "https://app.clappform.com",
            ...     "j.doe@clappform.com",
            ...     "S3cr3tP4ssw0rd!"
            ... )
            >>> query = c.get(r.Query(slug="foo")
            >>> list_df = []
            >>> for chunck in c.read_dataframe(query):
            ...     list_df.extend(chunck)

        :returns: Generator to read dataframe
        :rtype: Generator
        """
        path = "/dataframe/read_data?extended=true"
        payload = {"limit": limit}

        if isinstance(query, dc.Query):
            payload["query"] = query.slug
        elif isinstance(query, dc.Collection):
            payload["app"] = query.app
            payload["collection"] = query.slug
        else:
            t = type(query)
            raise TypeError(
                f"query arg must be of type {dc.Query} or {dc.Collection}, got {t}"
            )

        document = self._private_request("POST", path, json=payload)
        if "total" not in document:
            raise PaginationKeyError(missing_key="total", data=document)
        if document["total"] == 0:
            raise PaginationTotalError(total=document["total"], data=document)
        yield document["data"]

        pages_to_get = math.ceil(document["total"] / limit)
        if pages_to_get == 1:
            pass
        else:
            for result in self.executor.map(
                lambda x: self._private_request(
                    "POST", f"{path}&next_page={x}", json=payload
                ),
                range(limit, pages_to_get * limit, limit),
            ):
                yield result["data"]

    def write_dataframe(
        self,
        df: DataFrame,
        collection: dc.Collection,
        size: int = 100,
        max_workers=None,
    ):
        """Write Pandas DataFrame to collection.

        :param df: Pandas DataFrame to write to collection
        :type df: :class:`pandas.DataFrame`
        :param collection: Collection to hold DataFrame records
        :type collection: :class:`clappform.dataclasses.Collection`
        :param int size: Size of each chunk. Defaults to: ``100``
        :param interval_timeout: Optional time to sleep per request, defaults to:
            ``0.0``.
        :type interval_timeout: int
        """
        # Transform DataFrame to be JSON serializable
        for col in df.columns:
            df[col] = df[col].replace([np.nan, np.inf, -np.inf], None)
        df = df.replace([np.nan, np.inf, -np.inf], None)

        # Split DataFrame up into chunks.
        for chunk in [df[i : i + size] for i in range(0, df.shape[0], size)]:
            # `TemporaryFile` And `force_ascii=False` force the chunck to be `UTF-8`
            # encoded.
            with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as fd:
                chunk.to_json(fd, orient="records", force_ascii=False)
                fd.seek(0)  # Reset pointer to begin of file for reading.
                self._private_request(
                    "POST",
                    collection.dataframe_path(),
                    headers={"Content-Type": "application/json"},
                    data=fd.read().encode("utf-8"),
                )

    def empty_dataframe(self, collection) -> dc.ApiResponse:
        """Empty a dataframe.

        :param collection: Collection to append data to.
        :type collection: clappform.dataclasses.Collection

        :returns: API response object
        :rtype: clappform.dataclasses.ApiResponse
        """
        if not isinstance(collection, dc.Collection):
            t = type(collection)
            raise TypeError(f"collection arg must be of type {dc.Collection}, got {t}")
        document = self._private_request("DELETE", collection.dataframe_path())
        return dc.ApiResponse(**document)

    def _export_actions_from_groups(self, groups: list[dict]) -> list[dict]:
        actions = []
        for group in groups:
            for page in group["pages"]:
                for row in page["rows"]:
                    for module in row["modules"]:
                        if "actions" not in module["selection"]:
                            continue
                        for action in module["selection"]["actions"]:
                            actions.append(action)
        return actions

    def export_app(self, app) -> dict:
        """Export an app.

        :param app: App to export
        :type app: :class:`str` | :class:`clappform.dataclasses.App`

        :returns: Exported App
        :rtype: dict
        """
        if not isinstance(app, dc.App):
            raise TypeError("app argument is not of type {dc.App}, got {type(app)}")

        app.extended = True
        app = self.get(app)
        actions = self._export_actions_from_groups(app.groups)

        actionflows = [
            self.get(dc.Actionflow(id=x["actionflowId"]["id"]))
            for x in filter(
                lambda x: "type" in x
                and x["type"] == "actionflow"
                and "actionflowId" in x
                and x["actionflowId"] is not None
                and "id" in x["actionflowId"],
                actions,
            )
        ]
        questionnaires = [
            self.get(dc.Questionnaire(id=x["template"]["id"]))
            for x in filter(
                lambda x: "type" in x
                and x["type"] == "questionnaire"
                and "template" in x
                and x["template"] is not None
                and "id" in x["template"],
                actions,
            )
        ]
        import_entries_document = self._private_request("GET", "/import?extended=true")
        # Non-iterable value `app.collections` is used in an iterating context
        # (not-an-iterable). `extended=True` In `self.get_app` will change
        # `dc.App.collections` to a `list`.
        # pylint: disable=E1133
        import_entries = list(
            filter(
                lambda x: x["collection"] in [x["slug"] for x in app.collections],
                import_entries_document["data"],
            )
        )
        # pylint: enable=E1133
        version = self.get(dc.Version())
        return {
            "apps": [asdict(app)],
            "collections": app.collections,
            "form_templates": [asdict(x) for x in questionnaires],
            "action_flows": [asdict(x) for x in actionflows],
            "import_entry": import_entries,
            "config": {
                "timestamp": int(time.time()),
                "created_by": self.username,
                "enviroment": urlparse(self._base_url).hostname,
                "api_version": version.api,
                "web_application_version": version.web_application,
                "web_server_version": version.web_server,
                "deployable": True,
            },
        }

    def import_app(self, app: dict, data_export: bool = False) -> dc.ApiResponse:
        """Import an app.

        :param dict app: Exported app object.

        :returns: Api Response Object
        :rtype: clappform.dataclasses.ApiResponse
        """
        config = app.pop("config")
        if not config["deployable"]:
            # pylint: disable=W0719
            raise Exception("app is not deployable")
        # pylint: enable=W0719

        if not isinstance(data_export, bool):
            t = type(data_export)
            raise TypeError(f"data_export is not of type {bool}, got {t}")
        app["delete_mongo_data"] = data_export
        document = self._private_request("POST", "/transfer/app", json=app)
        return dc.ApiResponse(**document)

    def _transfer_collection(self, collection, dest):
        queue = Queue()
        for chunk in self.read_dataframe(collection):
            queue.put(chunk)
            # pylint: disable=W0212
            yield dest.executor.submit(dest._transfer_write, collection, queue)
            # pylint: enable=W0212
        queue.join()

    def _transfer_write(self, collection, queue):
        chunk = queue.get_nowait()
        resp = self._private_request(
            method="POST", path=collection.dataframe_path(), json=chunk
        )
        queue.task_done()
        return resp

    def transfer_collections(
        self, src: dict, dest, max_workers=None
    ) -> Generator[dc.ApiResponse, None, None]:
        """Transfer data from collection(s) from an app to a destination.

        Destination is an instance of the :class:`clappform.Clappform`. This method
        recreates all the data from all collections of an app to the same app and
        collections on another :class:`clappform.Clappform`.

        :param src: App dictionary or the value of running :meth:`export_app`.
        :type src: dict
        :param dest: Destination clappform environment.
        :type dest: :class:`clappform.Clappform`

        :returns: Generator of :class:`clappform.dataclasses.ApiResponse`
        :rtype: Generator
        """
        if not isinstance(dest, Clappform):
            t = type(dest)
            raise TypeError(f"destination is not of type {Clappform}, got, {t}")

        if isinstance(src, dict):
            cs = [dc.Collection(**x) for x in src["collections"]]
        else:
            raise TypeError("Could not get collections from src")
        for future in chain.from_iterable(
            [self._transfer_collection(c, dest) for c in cs]
        ):
            yield future.result()

    def current_user(self, extended: bool = False) -> dc.User:
        """Get :class:`clappform.dataclasses.User` object of the current user.

        :param bool extended: Optional retreive fully expanded user, defaults
            to ``false``.

        :returns: User object.
        :rtype: clappform.dataclasses.User
        """
        extended = dc.ResourceType.bool_to_lower(extended)
        document = self._private_request("GET", f"/user/me?extended={extended}")
        return dc.User(**document["data"])
