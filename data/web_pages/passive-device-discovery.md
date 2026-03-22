# Configuring passive device discovery

Installing and deploying Cyber Protection agents > Device discovery > Device discovery by using Device Sense ™ > Configuring passive device discovery
Configuring passive device discovery

Passive device discovery continuously scans the corporate networks for devices. By using passive device discovery:

Partners can gain a visibility of the customers' networks and the number and type of devices that are available in these networks.
Customers can gain visibility of their organization's networks and the number and type of devices that are available in these networks.

To configure the passive device discovery settings

In the Cyber Protect console, go to Settings > Management.
Click the Passive device discovery tab.

Ensure that the Enable passive device discovery switch is enabled.

The system automatically assigns Windows agents as discovery agents.

Change the default settings.

Setting	Description
Smart auto-selection of discovery agents	Number of agents that will be automatically selected to perform passive device discovery in the local network. The default value is 1.* The maximum value is 3.
Prevent device discovery in non-corporate networks	Minimum number of agents that must be present in a network to classify it as a corporate environment and enable its scan. The default value is 3.* The maximum value is 1000.
Enhanced identification of devices in a network	Enable or disable the use of multicast signals for more precise identification of device types joining the local network. By default, the switch is disabled.*

* The default value might differ, depending on the configuration of an upper-level tenant. Default values are inherited and are the same as the ones that are set for the upper-level tenant. However, you can change the default values according to your organization's needs.

Click Save.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.