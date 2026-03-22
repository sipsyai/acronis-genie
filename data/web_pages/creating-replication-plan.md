# Creating a replication plan

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Creating a replication plan
Creating a replication plan

A replication plan must be created for each machine individually. It is not possible to apply an existing plan to other machines.

To create a replication plan

Select a virtual machine to replicate.

Click Replication.

The software displays a new replication plan template.

To modify the replication plan name, click the default name.

Click Target machine, and then do the following:

Select whether to create a new replica or use an existing replica of the original machine.

Select the ESXi host and specify the new replica name, or select an existing replica.

The default name of a new replica is [Original Machine Name]_replica.

Click OK.
[Only when replicating to a new machine] Click Datastore, and then select the datastore for the virtual machine.

Click Schedule to change the replication schedule.

By default, replication is performed on a daily basis, Monday to Friday. You can select the time to run the replication.

If you want to change the replication frequency, move the slider, and then specify the schedule.

You can also do the following:

Set a date range for when the schedule is effective. Select the Run the plan within a date range check box, and then specify the date range.
Disable the schedule. In this case, replication can be started manually.

Click the gear icon to modify the replication options.

Click Apply.

To run the plan manually, click Run now on the plan panel.

As a result of running a replication plan, the virtual machine replica appears in the All devices list with the following icon:

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.