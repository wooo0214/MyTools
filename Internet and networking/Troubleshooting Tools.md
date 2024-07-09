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

### Senarios

1. Service Startup 

    Suppose you are getting error like "Windows could not start a service, the system cannot find the path specified".
    Use ProcMon to trace both File and Registry information simultaneously: The problem is that we are getting an “ACCESS DENIED” message when we try to read the service information from the HKLM\System\CurrentControlSet\Services\APC UPS Service registry key.  I checked the permissions on this registry key, and discovered that the Local Admin group had Deny access.  Once this was corrected - the service started up just fine.

