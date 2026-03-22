# Firewall rules for cloud servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Firewall rules for cloud servers
Firewall rules for cloud servers

You can configure firewall rules to control the inbound and outbound traffic of the primary and recovery servers on your cloud site.

You can configure inbound rules after you provision a public IP address for the cloud server. By default, TCP port 443 is allowed, and all other inbound connections are denied. You can change the default firewall rules, and add or remove Inbound exceptions. If a public IP is not provisioned, you can only view the inbound rules, but cannot configure them.

You can configure outbound rules after when you provision Internet access for the cloud server. By default, TCP port 25 is denied, and all other outbound connections are allowed. You can change the default firewall rules, and add or remove outbound exceptions. If Internet access is not provisioned, you can only view the outbound rules, but cannot configure them.

For security reasons, there are predefined firewall rules that you cannot change.

For inbound and outbound connections:

Permit ping: ICMP echo-request (type 8, code 0) and ICMP echo-reply (type 0, code 0)

Permit ICMP need-to-frag (type 3, code 4)

Permit TTL exceeded (type 11, code 0)

For inbound connections only:

Non-configurable part: Deny all

For outbound connections only:

Non-configurable part: Reject all

Setting firewall rules for cloud servers

Checking the cloud firewall activities

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.