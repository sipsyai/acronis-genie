# Device discovery

Installing and deploying Cyber Protection agents > Device discovery
Device discovery

By using the device discovery functionality, you can:

Gain complete visibility of the network devices that are available in the organization's networks.
Use synchronization with Active Directory to reduce the efforts for provisioning resources and managing machines in a large Active Directory domain.
Automate the installation of protection agents and the registration of machines by detecting the machines in your Active Directory domain or local network.
Install protection agents on multiple workloads.

You can use one of the following methods to perform device discovery:

Active Directory discovery.

During an Active Directory discovery, the discovery agent collects information about the organizational unit (OU) of the machines and detailed information about their names and operating systems. However, the IP and MAC addresses are not collected.

Local network discovery by using Device Sense ™. For more information, see Device discovery by using Device Sense ™.

Manual discovery – By using a machine IP address or host name, or by importing a list of machines from a file.

During a manual discovery, the existing protection agents are updated and re-registered. If you perform the device discovery by using the same account under which an agent is registered, the agent will only be updated to the latest version. If you perform device discovery by using another account, the agent will be updated to the latest version and re-registered under the tenant to which the account belongs.

You can also configure passive device discovery by using Device Sense ™, and view detailed information about the devices that are available in the corporate local area networks in your organization. For more information, see Passive device discovery by using Device Sense ™.

Discovering multiple devices

Device discovery by using Device Sense ™

Viewing information about discovered devices

Remote installation of agents

Excluding devices from discovery

Connecting to discovered devices remotely

Troubleshooting device discovery

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.