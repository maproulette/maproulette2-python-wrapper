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
        pass

    def test_createProject(self):
        """Test creation of a project locally"""
        p = Project()
        self.assertIsInstance(p, Project)

    def test_retrieveProject(self):
        """Test retrieving a project from the server"""
        p = Project(1)
        p.get(self.server)
        self.assertIn('"id": 1,', p.__str__())

if __name__ == '__main__':
    unittest.main()
