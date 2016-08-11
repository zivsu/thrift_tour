# !/usr/bin/env python
# coding=utf-8
import sys

sys.path.append("./gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from operater import operater
from operater.ttypes import *


def run():
    # Make socket
    tsocket = TSocket.TSocket("localhost", 8001)
    # Make transport level obj
    transport = TTransport.TBufferedTransport(tsocket)
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # new client
    client = operater.Client(protocol)
    transport.open()
    sum  = client.add(12, 30)
    print "12+30={}".format(sum)
    transport.close()
    
if __name__ == "__main__":
    run()

