from .action import Action2
from mud.events import EatEvent

class EatAction(Action2):
    EVENT = EatEvent
    ACTION = "eat"
    RESOLVE_OBJECT = "resolve_for_use"

    