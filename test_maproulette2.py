#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from maproulette2 import *

import unittest


class TestApi(unittest.TestCase):
    """Unit tests for the Maproulette 2 API wrapper"""

    def setUp(self):
        api_key = os.environ["MR_API_KEY"]
        self.server = Server(api_key)

    def tearDown(self):
        self.server = None

    def test_createProject(self):
        """Test creation of a project locally"""
        p = Project()
        self.assertIsInstance(p, Project)
        p = Project(1234)
        self.assertEqual(p.id, 1234)
        self.assertIsNone(p.name)
        self.assertIsNone(p.description)

    def test_modifyProjectName(self):
        p = Project()
        p.name = "New Project Name"
        self.assertEqual(p.name, "New Project Name")

    def test_modifyProjectId(self):
        """Tests trying to change the Project ID, which should not be possible as it is set by MapRoulette"""
        p = Project(1234)
        with self.assertRaises(Exception):
            p.id = 12345

    def test_retrieveProject(self):
        """Test retrieving a project from the server"""
        p = Project(1)
        p.get(self.server)
        self.assertIn('"id": 1', p.__str__())

if __name__ == '__main__':
    if os.environ.get("MR_API_KEY"):
        unittest.main()
    else:
        print("Please set your MapRoulette API key in environment variable MR_API_KEY first.")
