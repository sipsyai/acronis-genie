# Configuring Point-to-site remote VPN access

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Connectivity and networks > Configuring Point-to-site remote VPN access
Configuring Point-to-site remote VPN access
The availability of this feature depends on the service quotas that are enabled for your account.

If you need to connect to your local site remotely, you can configure the Point-to-site connection to the local site. You can follow the procedure below or watch the video tutorial.

Prerequisites

Site-to-site Open VPN connectivity is configured.

The VPN appliance is installed on the local site.

To configure the Point-to-site connection to the local site

In the Cyber Protect console, go to Disaster Recovery > Connectivity.
Click Show properties.
Enable the VPN access to local site option.

Ensure that your user who needs to establish the Point-to-site connection to the local site has:

a user account in Cyber Protect Cloud. These credentials are used for authentication in the VPN client. Otherwise, create a user account in Cyber Protect Cloud.

a "Company Administrator" or "Cyber Protection" user role.

Configure the OpenVPN client:

Download the OpenVPN client version 2.4.0 or later from the following location https://openvpn.net/community-downloads/.

OpenVPN Connect client is not supported.

Install the OpenVPN client on the machine from which you want to connect to the local site.
Click Download configuration for OpenVPN. The configuration file is valid for users in your organization with the "Company Administrator" or "Cyber Protection" user role.
Import the downloaded configuration to the OpenVPN client.
Log in to the OpenVPN client with your Cyber Protect Cloud user credentials (see step 4 above).
[Optional] If two-factor authentication is enabled for your organization, then you should provide the one-time generated TOTP code.

If you enabled two-factor authentication for your account, you need to re-generate the configuration file and renew it for your existing OpenVPN clients. Users must re-log in to Cyber Protect Cloud to set up two-factor authentication for their accounts.

As a result, you will be able to connect to machines on the local site.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.