#!/usr/bin/env python


class MapRouletteObject(object):
    """Abstract MapRoulette base class"""

    # TODO use ABC?

    @property
    def path(self):
        raise NotImplementedError()

    def get(self, server, use_api_key=False):
        return server.get(self.path, use_api_key)

    def post(self, server):
        return server.post(self.path, self.__str__())

    def put(self, server):
        return server.put(self.path, self.__str__())

    def delete(self, server):
        return server.delete()
