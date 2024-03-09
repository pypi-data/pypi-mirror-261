from typing import Any

from syrius.commands.abstract import Command
from syrius.types import InputType


class ArrayLengthCommand(Command):
    id: int = 2
    array: InputType[list[Any]]
