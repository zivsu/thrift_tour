# !/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import sys
sys.path.append('gen-py.tornado')

from thrift import TTornado
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from tornado import ioloop
import requests

from ipinfo import IPInfo

"https://github.com/apache/thrift/pull/654/commits/54b475ab746adfb07c5df3a3a243ec9297ddf9f5"

class IPHandler(object):

    def __init__(self):
        self.dest_url = "http://ip.taobao.com/service/getIpInfo.php"
    
    def get_ip_info(self, ip):
        payload = {"ip": ip}
        r = requests.get(self.dest_url, params=payload)
        print r.url
        try:
            json_data = r.json()
            code = json_data["code"]
            if code == 0:
                ipinfo = json_data["data"]
                ip_location = "{}{}{}".format(ipinfo["country"], ipinfo["area"], ipinfo["city"]).encode("utf-8")
            else:
                ip_location = None
        except Exception as e:
            print e
            ip_location = None 
        return ip_location

def make_server():
    handler = IPHandler()
    processor = IPInfo.Processor(handler)
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TTornado.TTornadoServer(processor, pfactory)
    return server

if __name__ == "__main__":
    server = make_server()
    print "Starting the server..."
    server.bind(8001)
    server.start(1)
    ioloop.IOLoop.instance().start()

