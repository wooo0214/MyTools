
## Overview

This page will talk about:

1. What is a server?
1. What is a client?
1. How internet works?
1. Protocols

### Reference

https://res.frytea.com/Ebooks/CCNA%E5%AD%A6%E4%B9%A0%E6%8C%87%E5%8D%97%E4%B8%AD%E6%96%87%E7%AC%AC%E4%B8%83%E7%89%88.pdf


## Client vs Server

从连接操作看，发起连接的是客户端，接受连接的是服务器。

https://blog.csdn.net/ck784101777/article/details/103985933

A server is a computer that is always on and running in an endless loop, just waiting for someone to send it a request.

A client is a computer making the request. In this example, our laptop's browser where we typed "github.com". It sends requests via HTTP to server's address - "GET /"

When the server receives a request a request from the client, it looks up the resource that iis being requested. Then it sends a file back. Usually on the internet, the file is a HTML file.

## Internet

> How do two computers talk to each other and send messages?

https://www.youtube.com/watch?v=BBBOPAU0FuQ

The internet is a set of rules for connecting computers and passing messages or files between them. All computers connected to the internet use the same rules when they talk to each other, and they will receive their own IP addresses.

DNS (Domain Name System) allows your computer to lookup computer names (like github.com) and get back the correct IP address.

The internet is a bunch of computers sending files (images, music, docs, raw data, and those files can be linked together and full of rich media) to one another. The protocol for sending these rich files is called HyperText Transfer Protocol (HTTP).

> How webpages appear on the browser?

A browser is a piece of software that renders web pages. It receives and reads HTML files, and renders the HTML files and all the files that it links to, it renders the elements in the file on the screen.

### Collision Domain and Broadcast domain

CD: domain that only one device can send information at a time.
BD: domain that devices can recieve the broadcast sent from a site.

## Protocols

Protocols are rules that computers need to follow when commnicating over the network.

https://www.cnblogs.com/fzz9/p/8964513.html

For example,
- TCP
- IP
- UDP
- HTTP