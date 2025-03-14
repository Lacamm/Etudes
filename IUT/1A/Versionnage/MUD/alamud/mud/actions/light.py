# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import LightOnEvent, LightOffEvent, LightOnWithEvent

class LightOnAction(Action2):
    EVENT = LightOnEvent
    ACTION = "light-on"
    RESOLVE_OBJECT = "resolve_for_use"

class LightOffAction(Action2):
    EVENT = LightOffEvent
    ACTION = "light-off"
    RESOLVE_OBJECT = "resolve_for_use"

class LightOnWithAction(Action3):
    EVENT = LightOnWithEvent
    ACTION = "light-on-with"
    RESOLVE_OBJECT = "resolve-for-operate"
    RESOLVE_OBJECT2 = "resolve-for-use"