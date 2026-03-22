# Configuring application-aware backup of virtual machines running Windows Server 2022 and later

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Application-aware backup > Configuring application-aware backup of virtual machines running Windows Server 2022 and later
Configuring application-aware backup of virtual machines running Windows Server 2022 and later

To perform application-aware backup on Hyper-V and VMware ESXi virtual machines that are running Windows Server 2022 or Windows Server 2025, you must use agent-based backup. For more information about the backup modes, see Agent-based and agentless backup.

Agent-based backup	Agentless backup
Application-aware backup	Supported	Not supported
Virtual machine icon in the Cyber Protect console

To configure application-aware backup in the agent-based mode

Install the protection agent (such as Agent for Windows, Agent for SQL, or Agent for Exchange) inside the guest operating system of the virtual machine.
In the Cyber Protect console, select the machine on which you installed the protection agent.
Configure the application-aware backup in a new protection plan.
Apply the protection plan to the virtual machine.
Run the protection plan.

As a result, a backup archive that contains the application-aware backup will be created.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.