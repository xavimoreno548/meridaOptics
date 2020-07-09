import zerorpc
from API.api import Api


# TCPServer
class TCPServer(object):
    api = None

    def __init__(self):
        self.api = Api()

    def getAll(self):
        return self.api.get_all()

    def remove(self, id, stock):
        return self.api.remove(id, stock)

    def insert(self, id, stock):
        return self.api.insert(id, stock)


# MAIN
if __name__ == "__main__":
    server = zerorpc.Server(TCPServer(), name="TCPServer")
    server.bind("tcp://0.0.0.0:4242")
    server.run()
