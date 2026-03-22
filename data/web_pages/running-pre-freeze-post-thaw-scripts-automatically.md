# Running pre‐freeze and post‐thaw scripts automatically

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Running pre‐freeze and post‐thaw scripts automatically
Running pre‐freeze and post‐thaw scripts automatically

With VMware Tools, you can automatically run custom pre‐freeze and post‐thaw scripts on virtual machines that you back up in the agentless mode. Thus, for example, you can run custom quiescing scripts and create application‐consistent backups for virtual machines running applications that are not VSS-aware.

Prerequisites

The pre‐freeze and post‐thaw scripts must be located in a specific folder on the virtual machine.

For Windows virtual machines, the location of this folder depends on the ESXi version of the host.

For example, for virtual machines running on an ESXi 6.5 host, this folder is C:\Program Files\VMware\VMware Tools\backupScripts.d\. You must create the backupScritps.d folder manually. Do not store other types of files in this folder because this may cause VMware Tools to become unstable.

For more information about the location of the pre‐freeze and post‐thaw scripts for other ESXi versions, refer to the VMware documentation.

For Linux virtual machines, copy your scripts to the /usr/sbin/pre-freeze-script and /usr/sbin/post-thaw-script directories, respectively. The scripts in /usr/sbin/pre-freeze-script are run when you create a snapshot and those in /usr/sbin/post-thaw-script are run when the snapshot is finalized. The scripts must be executable by the VMware Tools user.

To run pre‐freeze and post‐thaw scripts automatically

Ensure that VMware Tools are installed on the virtual machine.
On the virtual machine, put your custom scripts in the required folder.

In the protection plan for this machine, enable the Volume Shadow Copy Service (VSS) for virtual machines option.

This creates a VMware snapshot with the Quiesce guest file system option enabled, which in turn triggers the pre-freeze and post-thaw scripts inside the virtual machine.

You do not need to run custom quiescing scripts on virtual machines running VSS-aware applications, such as Microsoft SQL Server or Microsoft Exchange. To create an application-consistent backup for such machines, enable the Volume Shadow Copy Service (VSS) for virtual machines option in the protection plan.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.