from qbittorrent.base import Base


class File(Base):
    def __init__(self, url, session, client=None):
        super(File, self).__init__(url, session, client)

        self.name = None

        self.progress = None
        self.priority = None

        self.is_seed = None

    @classmethod
    def parse(cls, client, data):
        f = cls(client._url, client._session, client)
        f._fill(data)

        return f
