# FIPS-compliant mode

Installing and deploying Cyber Protection agents > FIPS-compliant mode
FIPS-compliant mode

To meet compliance requirement, you can install and use protection agents in FIPS-compliant mode.

This mode uses only algorithms and cryptography libraries that are certified according to the Federal Information Processing Standards 140-2, as follows:

[Windows] FIPS-certified Microsoft Cryptography API: Next Generation (CNG).
[Linux] FIPS-certified BoringCrypto library.
[Windows and Linux] FIPS-certified OpenSSL 3 module.

The FIPS-compliant mode is supported by the following agents:

Agent for Windows (on 64-bit operating systems)

See the supported versions in Agent for Windows.

Agent for Windows (Legacy) does not support the FIPS-compliant mode.

Agent for Linux

See the supported versions in Agent for Linux.

Virtual appliances

Agent for VMware (Virtual Appliance)
Agent for Virtuozzo Hybrid Infrastructure
Agent for Scale Computing HC3
Agent for oVirt
Limitations

The following components or services are not FIPS-compliant:

File Sync & Share
Endpoint Detection and Response (EDR)
Disaster recovery
Data loss prevention (DLP)
Acronis Cyber Protect app (backup of mobile devices)
Physical data shipping
Web Restore console
Virtual appliances in FIPS-compliant mode do not support SMB shares.
Bootable media that is created by FIPS-compliant Agent for Windows or FIPS-compliant Agent for Linux does not support SMB shares.
You can select the FIPS mode for Agent for Windows and Agent for Linux only during the installation. To change the FIPS mode later, run the installation file again and modify the installation.

Installing Agent for Windows in FIPS-compliant mode

Installing Agent for Linux in FIPS-compliant mode

Enabling FIPS-compliant mode for a virtual appliance

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.