from enum import Enum

from mikrotikapi.schemes.fields import field_gen


class OutInterfaceController(str, Enum):
    all_ethernet = "all-ethernet"
    all_pop = "all-pop"
    all_vlan = "all-vlan"
    all_wireless = "all-wireless"
    all_ether1 = "all-ether1"


out_interface: OutInterfaceController = field_gen(
    None,
    "out_interface",
)
