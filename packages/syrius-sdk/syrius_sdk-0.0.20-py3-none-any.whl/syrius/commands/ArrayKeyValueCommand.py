from typing import Any
from typing import Dict

from syrius.commands.abstract import Command
from syrius.types import InputType


class ArrayKeyValueCommand(Command):
    """ """
    id: int = 26
    kvstore: InputType[Dict[str, Any]]
