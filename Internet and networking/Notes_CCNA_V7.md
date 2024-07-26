Notes about the CCNA book Chinese version 7. To learn networking systematically.

online book:   
https://res.frytea.com/Ebooks/CCNA%E5%AD%A6%E4%B9%A0%E6%8C%87%E5%8D%97%E4%B8%AD%E6%96%87%E7%AC%AC%E4%B8%83%E7%89%88.pdf#google_vignette

## Chapter 1

devices, collision domain, broadcast domain

## Chap 2

- OSI, 7 layers network model in details.
- 以太网
- 数据封装   
    用户信息 -> 数据 -> 数据段 -> 分组、数据报 -> 帧 -> 比特

## Chap 3

- DoD 四层网络模型，及各层中协议，如FTP, http, SMTP, IMAP等
- TCP UDP
- IP

## Chap 5

本章和第四章有有关子网的内容略过，更适用于IT dept.

- TCP/IP 故障排除
    - ping 12.0.0.1 巡回地址 loopback address, localhost
    - ping local IP address
    - ping the router IP
    - ping the remote server IP, 如果是远程网络故障，对服务器端按上述步骤排查
    - check if DNS works

## Chap 8 IP路由

分组、数据帧的区别：是两种在OSI网络模型不同层中传输的数据单元（protocol data unit）
- 网络层 - 分组
- 数据链路层 - 数据帧