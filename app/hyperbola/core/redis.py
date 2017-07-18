from urllib.parse import urlparse

from rediscluster import StrictRedisCluster


class ConnectionFactory(object):
    def __init__(self, server):
        self._server = server
        self._startup_nodes = self._parse_startup_nodes()

    @property
    def connection(self):
        return StrictRedisCluster(startup_nodes=self._startup_nodes, skip_full_coverage_check=True)

    def _parse_startup_nodes(self):
        return [
            {'host': url.hostname, 'port': int(url.port or 6379)}
            for url in map(urlparse, self._server)
            if url.hostname
        ]
