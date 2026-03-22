# Changing the timeout for VM heartbeat and screenshot validation

Working with plans > Off-host data protection plans > Validation > Changing the timeout for VM heartbeat and screenshot validation
Changing the timeout for VM heartbeat and screenshot validation

When you validate a backup by running it as a virtual machine, you can configure the timeout between booting the virtual machine and sending the heartbeat request or taking a screenshot.

The default period is as follows:

One minute—For backups stored on a local folder or a network share.
Five minutes—For backups stored in the cloud storage.

To change the timeout

Open the configuration file of Agent for VMware or Agent for Hyper-V for editing.

The configuration file is available in the following locations:

[For Agent for VMware or Agent for Hyper-V running in Windows] C:\Program Files\BackupClient\BackupAndRecovery\settings.config

[For Agent for VMware (Virtual appliance)] /bin/mms_settings.config

For more information on how to access the configuration file on a virtual appliance, see SSH connections to a virtual appliance.

Go to <validation>, and then change the values for local backups and cloud backups as needed:

<validation>

<run_vm>

<initial_timeout_minutes>

<local_backups>1</local_backups>

<cloud_backups>5</cloud_backups>

</initial_timeout_minutes>

</run_vm>

</validation>

Save the configuration file.
Restart the agent.

[For Agent for VMware or Agent for Hyper-V running in Windows] Run the following commands at the command prompt:

net stop mms
net start mms
[For Agent for VMware (Virtual appliance)] Restart the virtual appliance.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.