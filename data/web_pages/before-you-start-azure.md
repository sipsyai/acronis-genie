# Before You Start Azure

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Azure > Before you start
Before you start
System requirements for the agent

By default, the virtual appliance is assigned the Standard_B2s size (4 GiB of RAM and 2 CPUs), which is optimal and sufficient for operations with up to ten virtual machines backed up in parallel. To improve the backup performance and avoid failures related to insufficient RAM memory, we recommend that you change the size of the virtual appliance (size in Azure) to get 4 vCPUs and 8 GB of RAM in more demanding cases. For example, increase the assigned resources when you back up more than ten virtual machines in parallel or if you back up simultaneously multiple virtual machines with large hard drives (500 GB or more).

For more information about this and other Azure virtual machine properties, see the Microsoft Azure documentation.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.