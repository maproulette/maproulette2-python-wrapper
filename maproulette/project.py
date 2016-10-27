#!/usr/bin/env python

import os
import json
from .base import MapRouletteObject


class Project(MapRouletteObject):
    """A MapRoulette Project."""

    READONLY = ["id"]

    @property
    def path(self):
        return os.path.join("project", str(self._id))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def __init__(self, id=None):
        self._id = id
        self._name = None
        self._description = None
        self._enabled = None

    def __str__(self):
        return json.dumps({
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "enabled": self._enabled
        })

    #TODO support groups