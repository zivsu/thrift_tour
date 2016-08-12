package main

import (
    "os"
    "fmt"
    "net"
    "git.apache.org/thrift.git/lib/go/thrift"
    "fibonacci"
)

const (
    HOST = "127.0.0.1"
    PORT = "8001"
)


func main() {
    transportFactory := thrift.NewTTransportFactory()
    protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
    
    tsocket, err := thrift.NewTSocket(net.JoinHostPort(HOST, PORT))
    if err != nil {
        fmt.Println("error resolving address:", err)
        os.Exit(1)
    }

    transport := transportFactory.GetTransport(tsocket)
    if err := transport.Open(); err != nil {
        fmt.Println("Error opening socket to "+ HOST + ":" + PORT)
        os.Exit(1)
    }
    defer transport.Close()
    client := fibonacci.NewFibonacciClientFactory(transport, protocolFactory)
    f, err := client.Fib(10)
    fmt.Println(f)
}
