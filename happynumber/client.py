# !/usr/bin/env python
# coding=utf-8

import thriftpy
from thriftpy.rpc import make_client

HOST = "127.0.0.1"
PORT = 8001

if __name__ == "__main__":
    happynumber_thrift = thriftpy.load("happynumber.thrift", module_name="happynumber_thrift")
    client = make_client(happynumber_thrift.HappyNumber, HOST, PORT)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    happy_numbers = client.extract_happy_number(numbers)
    print happy_numbers
