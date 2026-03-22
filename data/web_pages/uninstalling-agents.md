# Uninstalling agents

Installing and deploying Cyber Protection agents > Installing protection agents by using the graphical user interface > Uninstalling agents
Uninstalling agents

When you uninstall an agent from a workload, the workload is automatically removed from the Cyber Protect console. If the workload is still shown after you uninstall the agent, for example, due to a network problem, manually remove this workload from the console. For more information about how to do it, refer to Removing workloads from the Cyber Protect console.

Uninstalling an agent does not delete any plans or backups.

To uninstall an agent

Windows
Linux
macOS
[For protection plans created after November 2024] The uninstallation and modification of the protection agents for Windows is prohibited by default. Agent for Windows can be modified only during a maintenance window or through the agent auto update functionality. For instructions on how to enable the one-time uninstallation or modification of an agent, see To allow the modification of an agent with uninstallation protection enabled. Do disable the agent uninstallation protection, see To disable agent uninstallation protection.
Sign in as an administrator to the machine with the agent .
In Control panel, go to Programs and Features (Add or Remove Programs in Windows XP).
Right-click Acronis Cyber Protect, and then select Uninstall.
[For password-protected agents] Specify the password that is required to uninstall the agent, and then click Next.

Select the Remove the logs and configuration settings check box.

If you are planning to install the agent again, keep this check box cleared. If you select the check box and then install the agent again, this workload might be duplicated in the Cyber Protect console and its old backups might not be associated with it.

Click Uninstall.

To uninstall components that are bundled with Agent for Windows

You can uninstall individual components that are bundled with Agent for Windows, such as Cyber Protect Monitor, Agent for Data Loss Prevention, or Bootable Media Builder, without uninstalling Agent for Windows.

Sign in as an administrator to the machine with the agent.
Run the setup program, and then click Modify installed components.
Clear the check boxes next to the components that you want to uninstall, and then click Done.

To remove Agent for VMware (Virtual appliance)

By using the vSphere Client, log in to vCenter Server.
[If the virtual appliance is powered on] Right-click the virtual appliance, and then click Power > Power Off. Confirm your decision.

[If the virtual appliance uses a locally attached storage on a virtual disk and you want to preserve data on that disk] Remove the virtual storage from the virtual appliance.

Right-click the virtual appliance, and then click Edit Settings.
Select the disk with the storage, and then click Remove.
Under Removal Options, click Remove from virtual machine.
Click OK.

As a result, the disk remains in the datastore. You can attach the disk to another virtual appliance.

Right-click the virtual appliance, and then click Delete from Disk. Confirm your decision.

[If you are not planning to use this appliance again] In the Cyber Protect console, go to Backup storage > Locations, and then delete the location corresponding to the locally attached storage.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.