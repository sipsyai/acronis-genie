# Working with the Device control module

Managing workloads in the Cyber Protect console > Working with the Device control module
Working with the Device control module

A part of the Cyber Protection service protection plans, the device control module leverages a functional subset of the agent for Data Loss Prevention on each protected computer to detect and prevent unauthorized access and transmission of data over local computer channels. It provides fine-grained control over a wide range of data leakage pathways including data exchange using removable media, printers, virtual and redirected devices, and the Windows clipboard.

The module is available for Cyber Protect Essentials, Cyber Protect Standard, and Cyber Protect Advanced editions that are licensed per workload.

On Windows machines, the device control features require the installation of Agent for Data Loss Prevention. It will be installed automatically for protected workloads if the Device control module is enabled in their protection plans.

The device control module relies on the data loss prevention functions of the agent to enforce contextual control over data access and transfer operations on the protected computer. These include user access to peripheral devices and ports, document printing, clipboard copy / paste operations, media format and eject operations, as well as synchronizations with locally connected mobile devices. The agent for Data Loss Prevention includes a framework for all central management and administration components of the device control module, and therefore it must be installed on every computer to be protected with the device control module. The agent allows, restricts, or denies user actions based on the device control settings it receives from the protection plan that is applied to the protected computer.

The device control module controls access to various peripheral devices, whether used directly on protected computers or redirected in virtualization environments hosted on protected computers. It recognizes devices redirected in Microsoft Remote Desktop Server, Citrix XenDesktop / XenApp / XenServer, and VMware Horizon. It can also control data copy operations between the clipboard of the guest operating system running on VMware Workstation / Player, Oracle VM VirtualBox, or Windows Virtual PC, and the clipboard of the host operating system running on the protected computer.

The device control module can protect computers running the following operating systems:

Device control

Microsoft Windows 7 Service Pack 1 and later
Microsoft Windows Server 2008 R2 – Windows Server 2022
macOS 10.15 (Catalina)
macOS 11.2.3 (Big Sur)
macOS 12 (Monterey)
macOS 13 (Ventura)
macOS 14 (Sonoma)
macOS 15 (Sequoia)
Agent for Data Loss Prevention for macOS supports only x64 processors. Apple silicon ARM-based processors are not supported.

Data loss prevention

Microsoft Windows 7 Service Pack 1 and later
Microsoft Windows Server 2008 R2 – Windows Server 2022

Agent for Data Loss Prevention might be installed on unsupported macOS systems because it is an integral part of Agent for Mac. In this case, the Cyber Protect console will indicate that Agent for Data Loss Prevention is installed on the computer, but the device control and data loss prevention functionality will not work. Device control functionality will only work on macOS systems that are supported by Agent for Data Loss Prevention.

Limitation on the use of the agent for Data Loss Prevention with Hyper-V

Do not install Agent for Data Loss Prevention on Hyper-V hosts in Hyper-V clusters because it might cause BSOD issues, mainly in Hyper-V clusters with Clustered Shared Volumes (CSV).

If you use any of the following versions of Agent for Hyper-V, you need to manually remove Agent for Data Loss Prevention:

15.0.26473 (C21.02)

15.0.26570 (C21.02 HF1)

15.0.26653 (C21.03)

15.0.26692 (C21.03 HF1)

15.0.26822 (C21.04)

To remove Agent for Data Loss Prevention, on the Hyper-V host, run the installer manually and clear the Agent for Data Loss Prevention check box, or run the following command:

<installer_name> --remove-components=agentForDlp –quiet

You can enable and configure the device control module in the Device control section of your protection plan in the Cyber Protect console. For instructions, see steps to enable or disable device control.

The Device control section displays a summary of the module’s configuration:

Access settings - Shows a summary of device types and ports with restricted (denied or read-only) access, if any. Otherwise, indicates that all device types are allowed. Click this summary to view or change the access settings (see steps to view or change access settings).
Device types allowlist - Shows how many device subclasses are allowed by excluding from device access control, if any. Otherwise, indicates that the allowlist is empty. Click this summary to view or change the selection of allowed device subclasses (see steps to exclude device subclasses from access control).
USB devices allowlist - Shows how many USB devices/models are allowed by excluding from device access control, if any. Otherwise, indicates that the allowlist is empty. Click this summary to view or change the list of allowed USB devices/models (see steps to exclude individual USB devices from access control).
Exclusions - Shows how many access control exclusions have been set for Windows clipboard, screenshot capture, printers, and mobile devices.
See also
Enabling the use of the device control module on macOS

Using device control

Access settings

Device types allowlist

USB devices allowlist

Excluding processes from access control

Device control alerts

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.