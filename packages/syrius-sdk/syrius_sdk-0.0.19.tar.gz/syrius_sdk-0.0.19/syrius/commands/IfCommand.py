from typing import List

from syrius.commands.abstract import Command
from syrius.commands.abstract import Logical
from syrius.commands.abstract import Loop


class IfCommand(Logical):
    """ """
    id: int = 1
    condition: Command
    then: Command | List[Command] | Loop | Logical
