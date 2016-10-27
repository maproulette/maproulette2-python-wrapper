#!/usr/bin/env python

import os
import json
from .base import MapRouletteObject


class Task(MapRouletteObject):

    READONLY = ["id"]

    @property
    def paths(self):
        return os.path.join("task", str(self._id))

    @property
    def id(self):
        """The task identifier, as assigned by MapRoulette"""
        return self._id

    @property
    def name(self):
        """The name of the task that you want to assign"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def parent(self):
        """The id of the parent Challenge"""
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def instruction(self):
        return self._instruction

    @instruction.setter
    def instruction(self, value):
        self._instruction = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def __init__(self, id=None):
        super(Task, self).__init__()
        self._id = id
        self._name = None
        self._parent = None
        self._instruction = None
        self._location = None

    def __str__(self):
        return json.dumps([{
            "id": self._id,
            "name": self._name,
            "parent": self._parent,
            "instruction": self._instruction,
            "location": self._location
        }])


class TaskCollection(object):
    """A collection of Tasks"""

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

    def add_task(self, task):
        self._tasks.append(task)

    def __init__(self):
        super(TaskCollection, self).__init__()
        self._tasks = []

    def __str__(self):
        return json.dumps(tasks)
