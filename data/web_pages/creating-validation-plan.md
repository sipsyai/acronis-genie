# Creating a validation plan

Working with plans > Off-host data protection plans > Validation > Creating a validation plan
Creating a validation plan

To validate a backup archive as an off-host data processing operation, you must create a validation plan.

A validation plan might include multiple backups and one backup can be validated by multiple validation plans.

To create a validation plan

In the Cyber Protect console, go to Management > Validation.

Click Create plan.

To modify the plan name, click the default name, and then specify a new name.

In Agent, select the agent that will perform the validation, and then click OK.

If you want to perform validation by running a virtual machine from a backup, select a machine with Agent for VMware or Agent for Hyper-V.
If you do not want to perform validation by running a virtual machine from a backup, select any machine that has access to the backup location.

In Items to validate, select the backup archives that you want to validate.

Select the validation scope—Backup archives or backup locations, by clicking Backups or Locations in the upper-right corner.

If the selected archives are encrypted, all of them must use the same encryption password. For archives that use different encryption passwords, create separate plans.

Click Add.

Depending on the validation scope, select one or more locations, or a location and one or more backup archives, and then click Done.

Click Done.

In What to validate, select which backups (also known as recovery points) within the selected archives to validate. The following options are available:

All backups

Only the last backup

In How to validate, select the validation method.

You can select one or both of the following options:

Checksum verification

Run as a virtual machine

The Run as a virtual machine option provides the VM heartbeat and Screenshot validation methods. For more information, see Validation methods.

[If you selected Checksum verification] Click Done.

[If you selected Run as a virtual machine] Configure the settings for this option.

In Target machine, select the virtual machine type (ESXi or Hyper-V), the host, and the machine name template, and then click OK.

The default name is [Machine Name]_validate.

In Datastore (for ESXi) or Path (for Hyper-V), select the datastore for the virtual machine.
Select one or both validation methods:
VM heartbeat
Screenshot validation

Click VM settings to change the memory size and network connections of the virtual machine.

By default, the virtual machine is not connected to a network and the virtual machine memory size equals that of the original machine.

Click Done.

In the validation plan, click Schedule, and then configure the schedule.

[If the archives selected in Items to validate are encrypted] Enable the Backup password switch, and then provide the encryption password.

To modify the plan options, click the gear icon.

Click Create.

As a result, the validation plan is created and will run according to the schedule that you configured. To run the plan immediately, select it in Management > Validation, and then click Run now. After the validation starts, you can check the running activity and drill down to its details in Cyber Protect console, under Monitoring > Activities.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.