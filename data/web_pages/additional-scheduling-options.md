# Additional scheduling options

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Additional scheduling options
Additional scheduling options

You can configure the backups to run only if specific conditions are met, to run only during a specified period, or to run with a delay compared to the schedule.

To configure start conditions

In the protection plan, expand the Backup module.
Click Schedule.

On the Schedule pane, click Show more.

Select the check boxes next to the start conditions that you want to include, and then click Done.

For more information about the available start conditions and how to configure them, see Start conditions.

Save the protection plan.

To configure a time range

In the protection plan, expand the Backup module.
Click Schedule.
Select the Run the plan within a date range check box.
Specify the period according to your needs, and then click Done.
Save the protection plan.

As a result, the backups will run only during the specified period.

To configure a delay

To avoid excessive network load when you back up multiple workloads to a network location, a small random delay is configured as a backup option. You can disable it or change its setting.

In the protection plan, expand the Backup module.

Click Backup options, and then select Scheduling.

The delay value for each workload is selected randomly between zero and the maximum value you specify. By default, the maximum value is 30 minutes.

For more information about this backup option, see Scheduling

The delay value for each workload is calculated when you apply the protection plan to that workload, and remains the same until you edit the maximum delay value.

Specify the period according to your needs, and then click Done.
Save the protection plan.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.