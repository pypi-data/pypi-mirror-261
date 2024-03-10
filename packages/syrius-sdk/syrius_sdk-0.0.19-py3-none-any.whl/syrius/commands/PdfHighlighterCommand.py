from typing import List

from syrius.commands.abstract import Command
from syrius.types import InputType


class PdfHighlighterCommand(Command):
    """ """
    id: int = 27
    filename: InputType[str]
    texts: InputType[List[str]]
