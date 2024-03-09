from syrius.commands.abstract import Command
from syrius.types import InputType


class UnstructuredCommand(Command):
    id: int = 23
    text: InputType[str]