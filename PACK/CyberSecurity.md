# Overview

Cyber security refers to the practice of protecting systems, networks, and programs from digital attacks.   
These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information, extorting money from users, or interrupting normal business processes.   
Effective cyber security measures include multiple layers of protection spread across computers, networks, and programs. To be successful, an organization’s people, processes, and technology must all complement one another to create an effective defense against cyber threats.

These topics are included here as well:
- ATA
    > https://learn.microsoft.com/en-us/advanced-threat-analytics/what-is-ata   
    https://learn.microsoft.com/en-us/advanced-threat-analytics/suspicious-activity-guide
    https://learn.microsoft.com/en-us/advanced-threat-analytics/ata-architecture   
    https://info.microsoft.com/rs/157-GQE-382/images/WE-SCRTY-CNTNT-FY17-03Mar-13-Advanced%20Threat%20Analytics-310193_content.pdf
- Password Hash
- Cyber security engineering
- Cloud security
- Endpoint security
- Server security
- Threat analytics
- Penetration test and vulnerability fix
- Security incidnet response
- MS products
    - Defender for endpoint
    - Windows defender anti-virus
    - Defender for cloud apps

## ATA Suspicious activity guide

Types: True positive, benign true positive, false positive

There are 22 suspicious activities mentioned in the guide. For each acitvity, you can read description, investigation and remediation, to learn:
- key factors to calssify whether a suspicious activity is type x
- general investigation steps after classification
- remediation steps to mitiate or resolve the issue.

### Suspicious activity

- Encryption downgrade activity
    - skeleton key
    - golden ticket
    - overpass the hash

- Identity theft using pass the hash or pass the ticket attack   
NTLM hash or kerberos tikcet is stolen and used. 

- Reconnaissance using
    - account enumeration
    - directory serivce queries
    - DNS