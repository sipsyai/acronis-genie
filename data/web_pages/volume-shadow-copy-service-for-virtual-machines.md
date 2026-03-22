# Volume Shadow Copy Service (VSS) for virtual machines

Managing the backup and recovery of workloads and files > Backup options > Volume Shadow Copy Service (VSS) for virtual machines
Volume Shadow Copy Service (VSS) for virtual machines

This option controls the creation of quiesced snapshots for protected virtual machines.

The preset is: Enabled.

When this option is enabled, the transactions of all VSS-aware applications running in the virtual machine are completed before taking a quiesced snapshot.

If a quiesced snapshot cannot be taken for some reason, the outcome of the backup operation depends on the application backup settings as follows.

If application backup is set to Enabled and a quiesced snapshot cannot be taken after the number of re-attempts specified in the Error handling option, the backup fails.

If application backup is set to Disabled and a quiesced snapshot cannot be taken after the number of re-attempts specified in the Error handling option, a crash-consistent backup is created.

To make the backup fail instead of creating a crash-consistent backup, select the Fail backup if taking a quiesced snapshot is not possible check box.

When this option is disabled, a non-quiesced snapshot is taken. The virtual machine will be backed up in a crash-consistent state.

The following table summarizes the available settings and their results.

Settings	Quiesced snapshot was taken successfully	Quiesced snapshot was not taken
Application backup enabled	Application backup disabled	Application backup enabled	Application backup disabled


Volume Shadow Copy Service (VSS) for virtual machines enabled

Fail backup if taking a quiesced snapshot is not possible not selected

Quiesced snapshot is taken. Application-consistent backup is created.	Quiesced snapshot is taken. Application-consistent backup is created.	Backup fails.	Non-quiesced snapshot is taken. Crash-consistent backup is created.
Volume Shadow Copy Service (VSS) for virtual machines enabled

Fail backup if taking a quiesced snapshot is not possible selected

Quiesced snapshot is taken. Application-consistent backup is created.	Quiesced snapshot is taken. Application-consistent backup is created.	Backup fails.	Backup fails.
Volume Shadow Copy Service (VSS) for virtual machines disabled	Non-quiesced snapshot is taken. Crash-consistent backup is created.	Non-quiesced snapshot is taken. Crash-consistent backup is created.	Non-quiesced snapshot is taken. Crash-consistent backup is created.	Non-quiesced snapshot is taken. Crash-consistent backup is created.

Enabling Volume Shadow Copy Service (VSS) for virtual machines also triggers the pre‐freeze and post‐thaw scripts that you might have on the backed-up virtual machine. For more information on these scripts, see Running pre‐freeze and post‐thaw scripts automatically.

To take a quiesced snapshot, the backup software applies VSS inside a virtual machine by using VMware Tools, Hyper-V Integration Services, Virtuozzo Guest Tools, Red Hat Virtualization Guest Tools, or QEMU Guest Tools, respectively.

For Red Hat Virtualization (oVirt) virtual machines, we recommend that you install QEMU Guest Tools instead of Red Hat Virtualization Guest Tools. Some versions of Red Hat Virtualization Guest Tools do not support application-consistent snapshots.

This option does not affect Scale Computing HC3 virtual machines. For them, quiescing depends on whether Scale Tools are installed on the virtual machine.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.