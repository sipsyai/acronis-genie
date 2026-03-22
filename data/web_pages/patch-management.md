# Patch management

RMM > Managing software > Assessing vulnerabilities and managing patches > Patch management
Patch management
The availability of this feature depends on the service quotas that are enabled for your account.
To enable the Patch management module in the protection plan, the Vulnerability assessment module must be enabled.

For more information about the supported third-party products for Windows OS, see List of third-party products supported by Patch Management (62853).

Use the patch management functionality to:

install OS-level and application-level updates
approve patches manually or automatically
install patches on-demand or according to a schedule
precisely define which patches to install by different criteria: severity, category, and approval status
perform pre-update backup to prevent possible unsuccessful updates
define the reboot action after patch installation

To work with Windows updates, the patch management feature requires that Windows updates are enabled on the workload. The patch management feature relies on the Windows update service which detects which updates are missing and proposes them based on the existing running OS version.

The patch management feature supports upgrades to Windows 11. However, you must verify that the Windows 10 workloads that you are planning to upgrade are properly prepared for it. See this Microsoft article for details.

For updates of third-party products for Windows, Cyber Protection uses peer-to-peer technology to minimize network bandwidth traffic. You can choose one or more dedicated agents that will download updates from the Internet and distribute them among other agents in the network. All agents will also share updates with each other as peer-to-peer agents.

The patch management workflow

Patch management settings in the protection plan

Viewing the list of available patches

Automatic patch approval

Approving patches manually

Installing patches on demand

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.