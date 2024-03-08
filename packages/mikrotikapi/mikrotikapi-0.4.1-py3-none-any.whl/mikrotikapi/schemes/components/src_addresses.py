from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    IPvAnyNetwork,
    ConfigDict,
    AliasChoices,
    field_validator,
    field_serializer,
)

from mikrotikapi.utils.split_and_join import (
    split_ip_network_values,
    join_ip_network_values,
)


class SrcAddresses(BaseModel):

    src_address_list: Annotated[
        list[IPvAnyNetwork | str],
        Field(
            None,
            serialization_alias="src-address-list",
            json_schema_extra={
                "avalidation_alias": AliasChoices(
                    "src-address-list",
                    "src_address_list",
                ),
            },
        ),
    ]

    @field_validator("src_address_list", mode="before")
    def src_address_list_validate(cls, v) -> list:
        return split_ip_network_values(v)

    @field_serializer("src_address_list")
    def src_address_list_serialize(self, to_addresses: list, _info):
        return join_ip_network_values(to_addresses)

    model_config = ConfigDict(populate_by_name=True)
