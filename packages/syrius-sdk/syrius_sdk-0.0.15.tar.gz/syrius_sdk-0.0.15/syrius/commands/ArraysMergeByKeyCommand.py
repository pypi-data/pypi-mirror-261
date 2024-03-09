from typing import Any

from syrius.commands.abstract import Command
from syrius.types import InputType


class ArraysMergeByKeyCommand(Command):
    id: int = 1
    initial: InputType[list[dict[str, Any]]]
    to_combine: InputType[list[dict[str, Any]]]
    key: str