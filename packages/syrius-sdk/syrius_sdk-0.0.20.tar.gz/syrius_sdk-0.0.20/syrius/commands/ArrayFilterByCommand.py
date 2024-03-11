from typing import Any, List
from typing import Dict

from syrius.commands.abstract import Command
from syrius.types import InputType


class ArrayFilterByCommand(Command):
    """ """
    id: int = 29
    array: InputType[Dict[str, Any] | List[Any]]
    filter_by: InputType[str]
