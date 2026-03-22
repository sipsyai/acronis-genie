# Deploying the OVF template

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for VMware (Virtual Appliance) > Deploying the OVF template
Deploying the OVF template

Click All devices > Add > Broadcom (VMware) ESXi > Virtual Appliance (OVF).

The .zip archive is downloaded to your machine.

Unpack the .zip archive. The folder contains one .ovf file and three .vmdk files.
Ensure that these files can be accessed from the machine running vSphere Client.
Start vSphere Client and log on to the vCenter Server.

Deploy the OVF template.

When configuring storage, select the shared datastore, if it exists. Thick or thin disk format does not matter, as it does not affect the appliance performance.
When configuring network connections, be sure to select a network that allows an Internet connection, so that the agent can properly register itself in the cloud.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.