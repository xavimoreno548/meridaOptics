import logging
import asyncio
from rpcudp.protocol import RPCProtocol


class ManageData:

    async def manage(self, protocol, address):
        result = await protocol.get_all(address)
        print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    listen = loop.create_datagram_endpoint(RPCProtocol, local_addr=('127.0.0.1', 4000))
    transport, protocol = loop.run_until_complete(listen)
    manage_data = ManageData()
    func = manage_data.manage(protocol, ('127.0.0.1', 3000))
    loop.run_until_complete(func)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    loop.close()
