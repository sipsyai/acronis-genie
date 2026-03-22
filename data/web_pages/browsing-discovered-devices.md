# Viewing information about discovered devices

Installing and deploying Cyber Protection agents > Device discovery > Viewing information about discovered devices
Viewing information about discovered devices

You can use the filters that are incorporated on the Discovered devices page to quickly find specific devices in the list and view their details.

To find a discovered device and view its details

In the Protection console, click Discovered devices.

By default, the Devices without agent tab opens.

To search for devices from a specific category, click the corresponding tab.

Tab	Description
Devices without agent	This tab lists all discovered machines on which a protection agent can be installed, no matter what discovery method was used to discover them.
Active Directory	This tab lists the machines that were discovered by scanning the Active Directory.
Local network	This tab lists the devices (machines or other network devices) that were discovered by scanning the local corporate networks by using Device Sense ™.
Manual / From text file	This tab lists the machines that were discovered manually or from a text file.
Exclusions	This tab lists the devices that were excluded from discovery.

To search by device name, in the Search field, enter the device name.

The results in the list are filtered dynamically.

To search the results by using filters, click Filter, select one or several filters, and then click Apply.

Filter	Description
Device type

To search for one or several device types, click the field, and then select the relevant device types from the list.

This filter is not available on the Manual / From text file tab.


Discovery type

To filter the results based on the discovery method, click the field, and then select from the following methods.

Active Directory

Manual

Local network passive

Local network active

This filter is available on the Devices without agent tab only.


MAC address

To search for a device that has a specific MAC address, enter the MAC address in this field.

This filter is not available on the Manual / From text file tab.


IP address range	To filter the results based on the device IP address, enter the start IP address in the first field and the end IP address in the second field.
First discovered	To filter the results based on the date on which the device was initially discovered, click in the field, and then use a predefined or custom range.
Last discovered	To filter the results based on the date on which the device was last discovered, click in the field, and then use a predefined or custom range.
Organizational unit

The organizational unit in Active Directory to which the device belongs.

This filter is available on the Active Directory tab only.

Click the device, and then click Details.

In the Raw data pane, click the arrow icon.

To download the raw data in a JSON file, click Download.

The file is saved in the default download directory on the machine from which you are logged in to the Protection console.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.