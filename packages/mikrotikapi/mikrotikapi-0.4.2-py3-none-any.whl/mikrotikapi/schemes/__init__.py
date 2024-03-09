from enum import Enum

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    computed_field,
    ConfigDict,
)

from mikrotikapi.utils.to_camel_case import to_camel_case

from .identity import IdentityScheme
from .l2tp_client import L2TPClientScheme
from .mangle import MangleScheme
from .nat import NatScheme
from .profile import ProfileScheme
from .routing_tables import TableScheme
from .routing_tables_new import IPRouteScheme
from .sercret import SecretScheme


class InterfaceScheme(BaseModel):
    class TypeChoice(str, Enum):
        ETHER = "ether"
        WG = "wg"

        L2TP_IN = "l2tp-in"
        L2TP_OUT = "l2tp-out"

        OVPN_IN = "ovpn-in"
        OVPN_OUT = "ovpn-out"

        SSTP_IN = "sstp-in"
        SSTP_OUT = "sstp-out"

    id: str = Field(alias=".id")
    actual_mtu: int = Field(default=None, frozen=True, alias="actual-mtu")
    mtu: int = Field(default=None, frozen=True)
    disabled: bool
    last_link_up_time: str = Field(
        default=None, alias="last-link-up-time", frozen=True
    )
    last_link_down_time: str = Field(
        default=None, alias="last-link-down-time", frozen=True
    )
    default_name: str = Field(default=None, alias="default-name", frozen=True)
    mac_address: str = Field(default=None, alias="mac-address", frozen=True)
    link_downs: int = Field(default=None, alias="link-downs")
    name: str

    comment: str = Field(default=None)
    running: bool = Field(default=None, frozen=True)
    type: TypeChoice

    @field_validator("name")
    def name_validate(cls, name) -> str:
        try:
            return name.upper()
        except AttributeError:
            return name

    @computed_field
    @property
    def link_name(self) -> str:
        try:
            return f"{to_camel_case(self.name)}"
        except AttributeError:
            return self.name

    @computed_field
    @property
    def name_en(self) -> str:
        try:
            return f"{self.comment.split(':')[0]}"
        except (AttributeError, IndexError):
            return None

    @computed_field
    @property
    def name_ru(self) -> str | None:
        try:
            return f"{self.comment.split(':')[1]}"
        except (AttributeError, IndexError):
            return None

    @computed_field
    @property
    def tariffs(self) -> list | None:
        try:
            tariffs = self.comment.split(":")[2]
            return tariffs.strip("][").split(", ")
        except (AttributeError, IndexError):
            return None

    @computed_field
    @property
    def flag(self) -> str | None:
        try:
            return f":{self.comment.split(':')[3]}:"
        except (AttributeError, IndexError):
            return None

    @staticmethod
    def api_path():
        return "/rest/interface"

    model_config = ConfigDict(populate_by_name=True)


class InterfacesScheme(BaseModel):
    interfaces: list[InterfaceScheme] | None = None


class ErrorResponseScheme(BaseModel):
    detail: str
    error: int
    message: str


class PeersScheme(BaseModel):
    @staticmethod
    def api_path(_id=None):
        if _id:
            return f"/rest/interface/wireguard/peers/{_id}"
        return "/rest/interface/wireguard/peers"

    id: str = Field(alias=".id", exclude=True)
    allowed_address: str = Field(default=None, alias="allowed-address")
    comment: str
    current_endpoint_address: str = Field(
        alias="current-endpoint-address", exclude=True
    )
    endpoint_address: str = Field(alias="endpoint-address")
    endpoint_port: int = Field(alias="endpoint-port", exclude=True)
    disabled: bool
    interface: str
    public_key: str = Field(alias="public-key")

    # Exclude Fields
    rx: int | None = Field(None, exclude=True)
    tx: int | None = Field(None, exclude=True)

    @field_validator("interface")
    def convert_to_upper_case(cls, name):
        return name.upper()

    @computed_field
    @property
    def link_name_to_upper_validate(self) -> str:
        try:
            return to_camel_case(self.interface)
        except AttributeError:
            return None

    model_config = ConfigDict(populate_by_name=True)


class WireGuardScheme(BaseModel):
    @staticmethod
    def api_path():
        return "/rest/interface/wireguard"

    id: str = Field(alias=".id")
    name: str
    disabled: bool
    running: bool
    listen_port: int | None = Field(None, alias="listen-port")
    private_key: str | None = Field(None, alias="private-key")
    public_key: str | None = Field(None, alias="public-key")
    allowed_host: str | None = Field(None, alias="allowed-host")


class BadRequest(BaseModel):
    detail: str | None = None
    error: int
    message: str


class PingScheme(BaseModel):
    status: str | None = None
    avg_rtt: str | None = Field(None, alias="avg-rtt")
    host: str | None = None
    max_rtt: str | None = Field(None, alias="max-rtt")
    min_rtt: str | None = Field(None, alias="min-rtt")
    packet_loss: int = Field(alias="packet-loss")
    received: int
    sent: int
    seq: int
    size: int | None = None
    time: str | None = None
    ttl: int | None = None

    @staticmethod
    def api_path():
        return "/rest/ping"

    model_config = ConfigDict(populate_by_name=True)
