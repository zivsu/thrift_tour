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


class OperaterHandler(object):
    
    def add(self, a, b):
        return a + b


def run():
    # Make socket
    tsocket = TSocket.TServerSocket("localhost", 8001)
    # Make transport level obj
    tfactory = TTransport.TBufferedTransportFactory()
    # Wrap in a protocol
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # new server
    handler = OperaterHandler()
    processor = operater.Processor(handler)
    server = TServer.TSimpleServer(processor, tsocket, tfactory, pfactory)
    print "Starting thrift server..."
    server.serve()

if __name__ == "__main__":
    run()

