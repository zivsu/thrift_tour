###1. OS X Install Thrift
[install guide](https://thrift.apache.org/docs/install/os_x)


### 2. Unofficial Guide Document
[thrift-missing-guide](http://diwakergupta.github.io/thrift-missing-guide/)


### 3. py+tornado+thrift 实现异步调用
在OS X平台下，thrift版本是0.9.3，如果是安装此版本，对于里面源码的tutorial的py.tornado例子，Tornado 版本应该是2.4.0。需要注意下版本的问题。如果是从[github thrift](https://github.com/apache/thrift)里面的[例子](https://github.com/apache/thrift/tree/master/tutorial/py.tornado)，则可以兼容到tornado最新版本4.3.0。虽然可以执行，但是会在server会throw connection closed exception,需要根据[pull request](https://github.com/apache/thrift/pull/654/commits/54b475ab746adfb07c5df3a3a243ec9297ddf9f5)对源码进行更改。


