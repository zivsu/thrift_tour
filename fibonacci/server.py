# !/usr/bin/env python
# coding=utf-8
import sys

sys.path.append("./gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from fibonacci import fibonacci
from fibonacci.ttypes import *

class SeqHandler(object):

    def fib(self, n):
        f1, f2 = 0, 1
        for _ in range(n):
            f1, f2 = f2, f1+f2
        return f1

def new_server():
    # Make socket
    tsocket = TSocket.TServerSocket("127.0.0.1", 8001)
    # Make transport level obj
    tfactory = TTransport.TBufferedTransportFactory()
    # Wrap in a protocol
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # new server
    handler = SeqHandler()
    processor = fibonacci.Processor(handler)
    server = TServer.TSimpleServer(processor, tsocket, tfactory, pfactory)
    return server

if __name__ == "__main__":
    server = new_server()
    print "Starting thrift server..."
    server.serve()
    
