import logging
import asyncio
from rpcudp.protocol import RPCProtocol


async def manage(protocol, address):
    # call rpc that returns immediately
    #result = await protocol.get_all(address)
    #print(result)

    result = await protocol.remove(address, 1, 1)
    print(result)


loop = asyncio.get_event_loop()
loop.set_debug(True)

# Start local UDP server to be able to handle responses
listen = loop.create_datagram_endpoint(RPCProtocol, local_addr=('127.0.0.1', 4000))
transport, protocol = loop.run_until_complete(listen)

# Call remote UDP server to say hi
func = manage(protocol, ('127.0.0.1', 3000))
loop.run_until_complete(func)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()