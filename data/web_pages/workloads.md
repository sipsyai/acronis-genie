# Workloads

Managing workloads in the Cyber Protect console > Workloads
Workloads

A workload is any type of protected resource − for example, a physical machine, a virtual machine, a mailbox, or a database instance. In the Cyber Protect console, the workload is shown as an object to which you can apply a plan (protection plan, backup plan, or scripting plan).

Some workloads require installing a protection agent or deploying a virtual appliance. You can install agents by using the graphical user interface or by using the command-line interface (unattended installation). You can use the unattended installation to automate the installation procedure. For more information about how to install protection agents, see Installing and deploying Cyber Protection agents.

A virtual appliance (VA) is a ready-made virtual machine that contains a protection agent. With a virtual appliance, you can back up other virtual machines in the same environment without installing a protection agent on them (agentless backup). The virtual appliances are available in hypervisor-specific formats, such as .ovf, .ova, or .qcow. For more information about which virtualization platforms support agentless backup, see Supported virtualization platforms.

Agents must be online at least once every 30 days. Otherwise, their plans will be revoked and the workloads will become unprotected.

The table below summarizes the workload types and their respective agents.

Workload type	Agent

Examples

(non-exhaustive list)


Physical machines	A protection agent is installed on every protected machine.

Workstation

Laptop

Server


Virtual machines

Depending on the virtualization platform, the following backup methods might be available:

Agent-based backup − A protection agent is installed on every protected machine.

Agentless backup − A protection agent is installed only on the hypervisor host, on a dedicated virtual machine, or is deployed as a virtual appliance. This agent backs up all virtual machines in the environment.



VMware virtual machine

Hyper-V virtual machine

Kernel-based virtual machine (KVM) managed by oVirt

VMware Cloud Director (vCD) virtual machines*




Microsoft 365 Business workloads

Google Workspace workloads



These workloads are backed up by a cloud agent for which no installation is required.

To use the cloud agent, you need to add your Microsoft 365 or Google Workspace organization to the Cyber Protect console.

Additionally, a local Agent for Office 365 is available. It requires installation and can only be used to back up Exchange Online mailboxes. For more information about the differences between the local and the cloud agent, see Protecting Microsoft 365 data.



Microsoft 365 mailbox

Microsoft 365 OneDrive

Microsoft Teams

SharePoint site

Google mailbox

Google Drive


Applications

The data of specific applications is backed up by dedicated agents, such as Agent for SQL, Agent for Exchange, Agent for MySQL/MariaDB, or Agent for Active Directory.



SQL Server databases

MySQL/MariaDB databases

Oracle databases

Active Directory


Mobile devices	A mobile app is installed on the protected devices.	Android or iOS devices
Websites	The websites are backed up by a cloud agent for which no installation is required.	Websites accessed via the SFTP or SSH protocols

For more information about which agent you need and where to install it, see Which agent do I need?

* For more information about integrating VMware Cloud Director with Cyber Protect Cloud, see the Partner Administrator guide.

Adding workloads to the Cyber Protect console

Removing workloads from the Cyber Protect console

Asset types

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.