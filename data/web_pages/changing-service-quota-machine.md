# Changing the service quota of workloads

Installing and deploying Cyber Protection agents > Changing the service quota of workloads
Changing the service quota of workloads

A service quota is automatically assigned when a protection plan is applied to a workload for the first time.

The most appropriate quota is assigned, depending on the type of the protected workload, its operating system, required level of protection, and the quota availability. If the most appropriate quota is not available in your organization, the second-best quota is assigned. For example, if the most appropriate quota is Web Hosting Servers but it is not available, the Servers quota is assigned.

Examples of quota assignment:

A physical machine that runs a Windows Server or a Linux operating system is assigned the Servers quota.
A physical machine that runs a Windows desktop operating system is assigned the Workstations quota.
A physical machine that runs Windows 10 with enabled Hyper-V role is assigned the Workstations quota.
A desktop machine that runs on a virtual desktop infrastructure and the protection agent of which is installed inside the guest operating system (for example, Agent for Windows), is assigned the Virtual machines quota. This type of machine can also use the Workstations quota when the Virtual machines quota is not available.
A desktop machine that runs on a virtual desktop infrastructure and which is backed up in the agentless mode (for example, by Agent for VMware or Agent for Hyper-V), is assigned the Virtual machines quota.
A Hyper-V or vSphere server is assigned the Servers quota.
A server with cPanel or Plesk is assigned the Web Hosting Servers quota. It can also use the Virtual machines or the Servers quota, depending on the type of machine on which the web server runs, if the Web Hosting Servers quota is not available.
The application-aware backup requires the Servers quota, even for a workstation.

You can manually change the original assignment later. For example, to apply a more advanced protection plan to the same workload, you might need to upgrade the workload's service quota. If the features required by this protection plan are not supported by the currently assigned service quota, the protection plan will fail.

Alternatively, you can change the service quota if you purchase a more appropriate quota after the original one is assigned. For example, the Workstations quota is assigned to a virtual machine. After you purchase a Virtual machines quota, you can manually assign this quota to the workload, instead of the original Workstations quota.

You can also release the currently assigned service quota, and then assign this quota to another workload.

You can change the service quota of an individual workload or for a group of workload.

To change the service quota of an individual workload

In the Cyber Protect console, go to Devices.
Select a workload, and then click Details.
In the Service quota section, click Change.
In the Change quota window, select the service quota or No quota, and then click Change.

To change the service quota for a group of workloads

In the Cyber Protect console, go to Devices.
Select more than one workloads, and then click Assign quota.
In the Change quota window, select the service quota or No quota, and then click Change.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.