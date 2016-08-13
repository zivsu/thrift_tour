# !/usr/bin/env python
# coding=utf-8

import thriftpy
from thriftpy.rpc import make_server

HOST = "127.0.0.1"
PORT = 8001

class Dispatcher(object):

    def is_happy_number(self, number):
        seen = []    
        while 1:
            sum_digits = sum(int(digit) ** 2  for digit in str(number))
            if sum_digits == 1:
                return True
            elif sum_digits in seen:
                return False
            else:
                number = sum_digits
                seen.append(number)

    def extract_happy_number(self, numbers):
        new = []
        for number in numbers:
            if self.is_happy_number(number):
                new.append(number)
        return new

def new_server():
    happynumber_thrift = thriftpy.load("happynumber.thrift", module_name="happynumber_thrift")    
    return make_server(happynumber_thrift.HappyNumber, Dispatcher(), HOST, PORT)

if __name__ == "__main__":
    server = new_server()
    print "Starting thrift server..."
    server.serve()
