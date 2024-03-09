from enum import Enum
from pydantic import Field


class ChainController(str, Enum):
    srcnat = "srcnat"
    dstnat = "dstnat"
    input = "input"
    output = "output"


chain: ChainController = Field(default=ChainController.srcnat)
