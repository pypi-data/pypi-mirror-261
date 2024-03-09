from pydantic import (
    BaseModel,
    Field,
    IPvAnyNetwork,
    ConfigDict,
    AliasChoices,
    field_serializer,
    field_validator,
    IPvAnyAddress,
)

from mikrotikapi.schemes.fields import field_gen
from mikrotikapi.utils.split_and_join import (
    split_ip_network_values,
    join_ip_network_values,
)


class DstAddresses(BaseModel):
    dst_address_list: list[IPvAnyAddress | IPvAnyNetwork | str] = field_gen(
        None, name="dst_address_list"
    )

    @field_validator("dst_address_list", mode="before")
    def dst_addresses_validate(cls, v) -> list:
        return split_ip_network_values(v)

    @field_serializer("dst_address_list")
    def dst_addresses_serialize(self, to_addresses: list, _info):
        return join_ip_network_values(to_addresses)

    model_config = ConfigDict(populate_by_name=True)
