from typing import List

from syrius.commands.abstract import Command
from syrius.commands.abstract import LocalCommand
from syrius.commands.abstract import Logical
from syrius.commands.abstract import Loop


class ForCommand(Loop):
    """ """
    id: int = 1
    array: Command
    then: Command | List[Command] | Loop | Logical | LocalCommand
