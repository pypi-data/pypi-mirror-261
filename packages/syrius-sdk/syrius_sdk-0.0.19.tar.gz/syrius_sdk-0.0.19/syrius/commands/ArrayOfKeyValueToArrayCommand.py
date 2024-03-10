from typing import Any

from syrius.commands.abstract import Command
from syrius.types import InputType


class ArrayOfKeyValueToArrayCommand(Command):
    """ """
    id: int = 28
    array: InputType[list[Any]]
    filtered_by: InputType[str]