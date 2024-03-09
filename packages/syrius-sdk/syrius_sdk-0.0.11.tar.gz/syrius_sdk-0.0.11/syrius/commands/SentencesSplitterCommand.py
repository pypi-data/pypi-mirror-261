from syrius.commands.abstract import Command
from syrius.types import InputType


class SentencesSplitterCommand(Command):
    id: int = 25
    text: InputType[str]
    sentence_max_char: InputType[int]
    overlap: InputType[int]