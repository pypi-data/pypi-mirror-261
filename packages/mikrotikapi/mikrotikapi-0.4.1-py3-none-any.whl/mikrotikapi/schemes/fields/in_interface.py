from enum import Enum

from mikrotikapi.schemes.fields import field_gen


class InInterfaceController(str, Enum):
    all_ethernet = "all-ethernet"
    all_pop = "all-pop"
    all_vlan = "all-vlan"
    all_wireless = "all-wireless"
    all_ether1 = "all-ether1"


in_interface: InInterfaceController = field_gen(
    None,
    "in_interface",
)
