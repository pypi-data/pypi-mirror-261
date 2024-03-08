from __future__ import annotations

import json
import logging
import re
from asyncio import sleep
from typing import TypeVar, Generic, Any, List, Type
import urllib3
from aiohttp import (
    ClientSession,
    BasicAuth,
    ClientTimeout,
    ClientConnectorError,
)

from pydantic import parse_obj_as, BaseModel
from requests import Session
from requests_toolbelt import sessions as sessions_toolbelt

from mikrotikapi.exceptions import NotCreated, CustomException
from mikrotikapi.schemes import (
    ErrorResponseScheme,
    BadRequest,
    PeersScheme,
    PingScheme,
)

headers = {"content-type": "application/json"}


logger = logging.getLogger(__name__)
# urllib3.disable_warnings()

api_urls = {
    "ip_firewall_mangle": "/rest/ip/firewall/mangle",
    "interface": "/rest/interface",
    "interface_wireguard_peers": "/rest/interface/wireguard/peers",
}

M = TypeVar("M")


async def action(
    func: Session.put,
    scheme_: M,
):

    def patch_kwargs(v):
        return {
            "url": v.api_path(),
            "ssl": False,
            "data": v.model_dump_json(by_alias=True, exclude_none=True),
        }

    kwargs_for_patch = patch_kwargs(scheme_)

    async with func(**kwargs_for_patch) as response:
        if response.ok:
            data = await response.json(encoding="windows-1251")
            if isinstance(scheme_, BaseModel):

                return True, type(scheme_)(**data)

            return False, f"{type(scheme_)} is not pydantic model"

        elif response.status == 400 or response.status == 401:
            print(await response.text())
            return False, await response.text()


class Objects(Generic[M]):
    def __init__(self):
        self.server = None
        self.auth = None
        self.model_scheme: M = None
        self.client_session_kwargs = None

    def session_init(self) -> Session:
        s = sessions_toolbelt.BaseUrlSession(base_url=self.server)
        try:
            s.auth = self.auth
            s.verify = False
            return s
        finally:
            s.close()

    def objects(self, model_scheme: M | None = None):
        self.model_scheme = model_scheme
        return self

    async def all(self, proplist=None) -> List[Type[M]]:
        # if not self.server:
        #     raise CustomException(f"Server is {self.server}")

        if not self.model_scheme.api_path():
            raise CustomException(
                f"api_path is {self.model_scheme.api_path()}"
            )

        async with ClientSession(**self.client_session_kwargs) as session:
            params = {".proplist": proplist} if proplist else None
            path = self.model_scheme.api_path()

            async with session.get(path, ssl=False, params=params) as response:
                logger.info(response.url)
                try:
                    if response.ok:
                        # logger.debug(await response.json(encoding="windows-1251"))
                        response_json = await response.json(
                            encoding="windows-1251"
                        )
                        # adapter = TypeAdapter(self.model_scheme)
                        if isinstance(response_json, list):
                            # objects = adapter.json_schema()
                            objects = parse_obj_as(
                                list[self.model_scheme], response_json
                            )
                        elif isinstance(response_json, dict):
                            objects = self.model_scheme(**response_json)

                    else:
                        logger.info(await response.text())
                        raise CustomException("Response is not OK")
                except ClientConnectorError as e:
                    logger.exception(e)
                except Exception as e:
                    logger.exception(str(e))
                else:
                    return objects

    async def all_json(self, proplist=None) -> list[any]:
        # if not self.server or not self.model_scheme.api_path():
        #     raise Exception
        if not self.model_scheme.api_path():
            raise CustomException(
                f"api_path is {self.model_scheme.api_path()}"
            )

        async with ClientSession(**self.client_session_kwargs) as session:
            params = {".proplist": proplist} if proplist else None
            path = self.model_scheme.api_path()

            async with session.get(path, ssl=False, params=params) as response:
                try:
                    objects = await response.json(encoding="windows-1251")
                    print(1231231313123123)
                except Exception as e:
                    logger.exception(e)
                    error = ErrorResponseScheme(
                        **(await response.json(encoding="windows-1251"))
                    )
                    logger.exception(error)

                else:
                    return objects

    async def get(self, _id) -> Type[M]:
        if not self.model_scheme.api_path():
            raise CustomException(
                f"api_path is {self.model_scheme.api_path()}"
            )
        async with ClientSession(**self.client_session_kwargs) as session:
            patch = self.model_scheme.api_path()
            async with session.get(f"{patch}/{_id}", ssl=False) as response:
                try:
                    if response.ok:
                        logger.debug(
                            await response.json(encoding="windows-1251")
                        )
                        response_json = await response.json(
                            encoding="windows-1251"
                        )
                        if isinstance(response_json, dict):
                            objects = self.model_scheme(**response_json)

                    else:
                        logger.info(await response.text())
                        raise CustomException("Response is not OK")
                except ClientConnectorError as e:
                    logger.exception(e)
                except Exception as e:
                    logger.exception(str(e))
                else:
                    return objects

    async def get_or_none(self, **kwargs) -> Type[M]:
        _all = await self.filter(**kwargs)
        try:
            return _all[0]
        except IndexError:
            return None

    async def first(self, **kwargs) -> Type[M] | None:
        _all = await self.filter(**kwargs)

        try:
            return _all[0]
        except IndexError:
            return None

    async def get_reserved_ip_generator(self) -> list[str] | None:
        async with ClientSession(**self.client_session_kwargs) as session:
            url = PeersScheme.api_path()
            reserved = self.reserved_ip

            params = {".proplist": "allowed-address"}
            patch_kwargs = {"url": url, "ssl": False, "params": params}
            async with session.get(**patch_kwargs) as response:
                if response.ok:
                    response_json = await response.json(
                        encoding="windows-1251"
                    )

                    l = list(
                        map(
                            lambda x: x["allowed-address"].split("/")[0],
                            response_json,
                        )
                    )

                    return l + reserved

                return None

    @staticmethod
    async def get_free_ip(reserved_ip, network):
        for host in network.hosts():
            if str(host) not in reserved_ip:
                yield host

    async def filter(self, **kwargs):
        _all = await self.all()
        if not kwargs:
            return _all

        def filtered(x):
            for k, v in kwargs.items():
                splitting = k.split("__")
                key = splitting[0]
                attribute = getattr(x, key)

                if len(splitting) > 1:
                    pattern = splitting[1]

                    if pattern == "search":
                        search = re.search(v, str(attribute))
                        if not search:
                            return False

                    elif pattern == "search_iexact":
                        search = re.search(v, str(attribute), re.IGNORECASE)
                        if not search:
                            return False

                    elif pattern == "match":
                        match = re.match(v, str(attribute))
                        if not match:
                            return False

                    elif pattern == "in":
                        if attribute is not None:
                            if isinstance(attribute, list) or isinstance(
                                attribute, str
                            ):
                                if not isinstance(v, list):
                                    v = [v]

                                if not set(v).issubset(set(attribute)):
                                    return False
                            else:
                                return False
                        else:
                            return False

                    elif pattern == "exist":
                        return bool(attribute) == bool(v)
                    elif pattern == "one_is":
                        if attribute is not None:
                            if isinstance(attribute, list) or isinstance(
                                attribute, str
                            ):
                                if not isinstance(v, list):
                                    v = [v]

                                if not any(item in attribute for item in v):
                                    return False
                            else:
                                return False
                        else:
                            return False

                else:
                    if attribute != v:
                        return False
            return True

        return list(filter(filtered, _all))

    async def delete(self, obj=None, **kwargs) -> True | str:
        if obj:
            _id = obj.id
        else:
            _id = kwargs["id"]

        model_scheme = self.model_scheme
        url = model_scheme.api_path(_id)
        patch_kwargs = {"url": url, "ssl": False}

        async with ClientSession(**self.client_session_kwargs) as session:
            async with session.delete(**patch_kwargs) as response:
                if response.ok:
                    return "Profile deleted"

    async def update_or_create(
        self, defaults, obj=None, **kwargs
    ) -> True | str:
        pass

    async def create(
        self, single_or_multiple_schemas: M | [M] | None = None, **kwargs
    ) -> True | str:

        if single_or_multiple_schemas:
            scheme = single_or_multiple_schemas
        else:
            scheme = self.model_scheme

        async with ClientSession(**self.client_session_kwargs) as session:

            if not single_or_multiple_schemas and kwargs:
                try:
                    return await action(session.put, scheme)

                except Exception:
                    raise NotCreated

            elif isinstance(single_or_multiple_schemas, list):
                result_list = []
                for scheme in single_or_multiple_schemas:
                    created, scheme_ = await action(session.put, scheme)
                    result_list.append([created, scheme_])

                return result_list

            else:
                return await action(session.put, scheme)

        #
        # # try:
        # #     pass
        # # except ClientConnectorError as e:
        # #     return e

    async def update(self, obj, **kwargs) -> Type[M] | list[Type[M]]:

        if self.model_scheme:
            model_scheme = self.model_scheme
        else:
            model_scheme = obj

        async def patch(_id, data):
            url = self.model_scheme.api_path(_id)
            patch_kwargs = {"url": url, "ssl": False, "data": data}
            async with ClientSession(**self.client_session_kwargs) as session:
                async with session.patch(**patch_kwargs) as resp:
                    logger.debug(await resp.text())
                    if resp.ok:
                        return self.model_scheme(**(await resp.json()))

        if isinstance(obj, list):
            objs_list = []
            for i in obj:
                # _id, _data = i.id, i.json(by_alias=True)
                _id, _data = i.id, i.json()
                objs_list.append(await patch(_id, _data))

            return objs_list

        elif isinstance(obj, str):
            model: BaseModel = self.model_scheme(**kwargs)
            _id, _data = obj, model.model_dump_json(
                # by_alias=True,
                exclude_none=True,
            )
            return await patch(_id, _data)

        else:
            _id, _data = obj.id, obj.model_dump_json(
                # by_alias=True,
                exclude_none=True,
            )
            logger.debug(_id)
            logger.debug(_data)

            return await patch(_id, _data)


class ROSApi(Objects):
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        reserved_ip: list = None,
    ):
        super().__init__()
        self.username = username
        self.password = password
        self.reserved_ip = reserved_ip
        self.client_session_kwargs = {
            "base_url": url,
            "auth": BasicAuth(self.username, self.password, encoding="utf-8"),
            "headers": headers,
            "timeout": ClientTimeout(connect=15),
        }

    async def ping(
        self, params: dict
    ) -> tuple[PingScheme | None, BadRequest | None]:
        async with ClientSession(
            base_url=self.server, auth=self.auth, headers=headers
        ) as session:
            try:
                async with session.post(
                    PingScheme.api_path(), data=json.dumps(params), ssl=False
                ) as response:
                    r_json = await response.json(encoding="windows-1251")
                    if response.ok:
                        return parse_obj_as(list[PingScheme], r_json)[0], None

                    return None, BadRequest(**r_json)
            except Exception as e:
                logger.exception(e)
                return None, None

    @staticmethod
    def is_bad_ping(ping_model: PingScheme):
        if ping_model.status == "bad interface":
            return True, "bad interface"
        if ping_model.status == "timeout":
            return True, "timeout"
        if ping_model.status == "interface not available":
            return True, "interface not available"
        if ping_model.status == "could not make socket":
            return True, "could not make socket"
        if ping_model.status == "no route to host":
            return True, "no route to host"
        if ping_model.packet_loss == 100:
            return True, "packet_loss"

        return False, None
