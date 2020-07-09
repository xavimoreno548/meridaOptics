import asyncio
from rpcudp.protocol import RPCProtocol
from API.api import Api


class RPCServer(RPCProtocol):

    api = None

    def __init__(self):
        super().__init__()
        self.api = Api()

    def rpc_get_all(self, sender):
        return self.api.get_all()

    def rpc_remove(self, sender, id: int, stock: int):
        return self.api.remove(id, stock)

    def rpc_insert(self,sender, id: int, stock: int):
        return self.api.insert(id, stock)


loop = asyncio.get_event_loop()
loop.set_debug(True)

# listen for requests
listen = loop.create_datagram_endpoint(RPCServer, local_addr=('127.0.0.1', 3000))
transport, protocol = loop.run_until_complete(listen)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()
