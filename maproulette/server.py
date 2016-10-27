#!/usr/bin/env python

import os
import json
import requests


class Server(object):
    """MapRoulette server instance"""

    def __init__(self, api_key, project_id, base_url="http://maproulette.org/api/v2"):
        super(Server, self).__init__()
        self.base_url = base_url
        self.project_id = project_id
        self.headers = {"apiKey": api_key}

    def get(self, path, use_api_key):
        if use_api_key:
            response = requests.get(
                os.path.join(self.base_url, path),
                headers=self.headers)
        else:
            response = requests.get(os.path.join(self.base_url, path))
        if response.status_code == 200:
            return response.json()
        raise MaprouletteException()

    def post(self, path, payload):
        response = requests.post(
            os.path.join(self.base_url, path),
            data=payload,
            headers=self.headers)
        return response.json()

    def put(self, path, payload):
        response = requests.put(
            os.path.join(self.base_url, path),
            data=payload,
            headers=self.headers)
        return response.json()

    def delete(self, path):
        response = requests.delete(
            os.path.join(self.base_url, path),
            headers=self.headers)
        return response.json()

    def my_challenges(self):
        response = requests.get(
            os.path.join(
                self.base_url,
                "project",
                self.project_id,
                "challenges"),
            headers=self.headers
        )
        return response.json()
