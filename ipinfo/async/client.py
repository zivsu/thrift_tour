#!/usr/bin/env python
import logging
import sys

sys.path.append('gen-py.tornado')

from thrift import TTornado
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from tornado import gen
from tornado import ioloop

from ipinfo import IPInfo


@gen.coroutine
def communicate():
    # create client
    transport = TTornado.TTornadoStreamTransport('localhost', 8001)
    # open the transport, bail on error
    try:
        yield transport.open()
        print('Transport is opened')
    except TTransport.TTransportException as ex:
        logging.error(ex)
        raise gen.Return()

    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    client = IPInfo.Client(transport, pfactory)

    ip_location = yield client.get_ip_info("27.42.14.179")
    print ip_location

    # close the transport
    client._transport.close()
    raise gen.Return()

if __name__ == "__main__":
    # create an ioloop, do the above, then stop
   io_loop =  ioloop.IOLoop.current()
   for _ in range(10):
        io_loop.run_sync(communicate)
