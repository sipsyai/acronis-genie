# Scheduling

Managing the backup and recovery of workloads and files > Backup options > Scheduling
Scheduling

This option defines whether backups start exactly as scheduled or with a delay, and how many virtual machines are backed up simultaneously.

For more information about how to configure the backup schedule, see Running a backup on a schedule.

The preset is: Distribute backup start times within a time window. Maximum delay: 30 minutes.

You can select one of the following:

Start all backups exactly as scheduled

Backups of physical machines will start exactly as scheduled. Virtual machines will be backed up one by one.

Distribute start times within a time window

Backups of physical machines will start with a delay from the scheduled time. The delay value for each machine is selected randomly and ranges from zero to the maximum value you specify. You may want to use this setting when backing up multiple machines to a network location, to avoid excessive network load. The delay value for each machine is determined when the protection plan is applied to the machine and remains the same until you edit the protection plan and change the maximum delay value.

Virtual machines will be backed up one by one.

Limit the number of simultaneously running backups by

Use this option to manage the parallel backup of virtual machines that are backed up on the hypervisor level (agentless backup).

Protection plans in which this option is selected can run together with other protection plans that are operated by the same agent at the same time. When you select this option, you must specify the number of parallel backups per plan. The total number of machines that are backed up simultaneously by all plans is limited to 10 per agent. To learn how to change the default limit, see Limiting the total number of simultaneously backed-up virtual machines.

Protection plans in which this option is not selected run the backup operations sequentially, one virtual machine after another.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.