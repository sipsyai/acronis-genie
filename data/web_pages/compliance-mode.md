# Compliance mode

Additional Cyber Protection tools > Compliance mode
Compliance mode

The Compliance mode is designed for clients with higher security demands. This mode requires mandatory encryption for all backups and allows only locally set encryption passwords.

With the Compliance mode, all backups created in a customer tenant and its units are automatically encrypted with the AES algorithm and a 256-bit key. Users can set the encryption passwords only on the protected devices, and cannot set them in the protection plans.

The Compliance mode cannot be disabled.
Limitations
The Compliance mode is compatible only with agents version 15.0.26390 or higher.
The Compliance mode is not available for devices running Red Hat Enterprise Linux 4.x or 5.x, and their derivatives.
Cloud services cannot access encryption passwords. Due to this limitation, some features are not available for tenants in Compliance mode.
Unsupported features

The following features are not available for tenants in Compliance mode:

Recovery through the Cyber Protect console
File-level browsing of backups through the Cyber Protect console
Access to the Web Restore console
Cloud-to-cloud backup
Website backup
Application backup
Backup of mobile devices
Antimalware scan of backups
Safe recovery
Automatic creation of corporate allowlists
Data protection map
Disaster recovery
Reports and dashboards related to the unavailable features

Setting the encryption password

Changing the encryption password

Recovering backups in tenants in Compliance mode

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.