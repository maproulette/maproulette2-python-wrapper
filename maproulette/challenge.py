#!/usr/bin/env python

import os
import json
from .base import MapRouletteObject


class Challenge(MapRouletteObject):

    READONLY = ["id", "featured"]

    @property
    def path(self):
        return os.path.join("challenge", self._id)

    @property
    def id(self):
        """The identifier that MapRoulette assigns to the Challenge."""
        return self._id

    @property
    def name(self):
        """The name for the Challenge."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        """The description for the Challenge."""
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def parent(self):
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
    def difficulty(self):
        """The challenge's difficulty"""
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def blurb(self):
        """The challenge Blurb (short description)"""
        return self._blurb

    @blurb.setter
    def blurb(self, value):
        self._blurb = value

    @property
    def enabled(self):
        """Whether the Challenge is Enabled or not"""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    @property
    def challenge_type(self):
        """The type of Challenge"""
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, value):
        self._challenge_type = value

    @property
    def featured(self):
        """Whether the Challenge is Featured in MapRoulette. Only a superuser can set this."""
        return self._featured

    @featured.setter
    def featured(self, value):
        self._featured = value

    @property
    def default_priority(self):
        return self._default_priority

    @default_priority.setter
    def default_priority(self, value):
        self._default_priority = value

    @property
    def default_zoom(self):
        return self._default_zoom

    @default_zoom.setter
    def default_zoom(self, value):
        self._default_zoom = value

    @property
    def min_zoom(self):
        return self._min_zoom

    @min_zoom.setter
    def min_zoom(self, value):
        self._min_zoom = value

    @property
    def max_zoom(self):
        return self._max_zoom

    @max_zoom.setter
    def max_zoom(self, value):
        self._max_zoom = value

    def __init__(self, id=None):
        super(Challenge, self).__init__()
        self._id = id
        self._name = None
        self._description = None
        self._parent = None
        self._instruction = None
        self._difficulty = None
        self._blurb = None
        self._enabled = False
        self._challenge_type = None
        self._featured = None
        self._default_priority = None
        self._default_zoom = None
        self._min_zoom = None
        self._max_zoom = None

    def __str__(self):
        return json.dumps([{
            "id": self._id,
            "name": self._name,
            "description": self._description,
            "parent": self._parent,
            "instruction": self._instruction,
            "difficulty": self._difficulty,
            "blurb": self._blurb,
            "enabled": self._enabled,
            "challengeType": self._challenge_type,
            "featured": self._featured,
            "defaultPriority": self._default_priority,
            "defaultZoom": self._default_zoom,
            "minZoom": self._min_zoom,
            "maxZoom": self._max_zoom
        }])


class ChallengeCollection(object):
    """A collection of Challenges"""

    @property
    def challenges(self):
        return self._challenges

    @challenges.setter
    def challenges(self, value):
        self._challenges = value

    def add_challenge(self, challenge):
        self._challenges.append(challenge)

    def __init__(self):
        super(ChallengeCollection, self).__init__()
        self._challenges = []

    def __str__(self):
        return json.dumps(challenges)

    # TODO init with challenges JSON
