# Overview

This topic is about troubleshooting tools for network issues.

## Wireshark

- filter protocol
- filter IP
    - ip.src==IP && ip.dst == IP, not ip.addr == IP
- filter port
    - tcp.port eq 443, udp.port eq 53
- filter tcp steam
    - tcp.stream eq  $streamindex
- filter rst
    - tcp.flags.reset == 1 and tcp.ack == 0
- fuzzy match/wildcard
    - http.request.uri contains "string"

## Fiddler

## Process Monitor

- filter