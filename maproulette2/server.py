#!/usr/bin/env python

import requests

class Server(object):

    base_url = "http://maproulette.org/api/v2"
    api_key = None

    def __init__(self, api_key):
        self.api_key = api_key

    def post(self, payload):
        pass

    def get(self):
        pass

    def put(self, payload):
        pass

    def delete(self):
        pass
