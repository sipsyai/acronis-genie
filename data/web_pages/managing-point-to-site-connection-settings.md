# Managing point-to-site connection settings

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Managing point-to-site connection settings
Managing point-to-site connection settings
The availability of this feature depends on the service quotas that are enabled for your account.

In the Cyber Protect console, go to Disaster Recovery > Connectivity and then click Show properties in the upper right corner.

VPN access to local site

This option is used for managing VPN access to the local site. By default it is enabled. If it is disabled, then the Point-to-site access to the local site will be not allowed.

Download configuration for OpenVPN

This will download the configuration file for the OpenVPN client. The file is required to establish a Point-to-site connection to the cloud site.

Re-generate configuration

You can re-generate the configuration file for the OpenVPN client.

This is required in the following cases:

If you suspect that the configuration file is compromised.
If two-factor authentication was enabled for your account.

As soon as the configuration file is updated, connecting by means of the old configuration file becomes not possible. Make sure to distribute the new file among the users who are allowed to use the Point-to-site connection.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.