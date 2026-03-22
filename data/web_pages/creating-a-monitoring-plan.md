# Creating a monitoring plan

RMM > Monitoring the health and performance of workloads > Monitoring plans > Creating a monitoring plan
Creating a monitoring plan

You can create a monitoring plan, and then add workloads to it to configure the monitoring functionality on the managed workloads.

Prerequisites

The version of the agent that is installed on the workload supports the monitoring functionality.

To create a monitoring plan

From Monitoring plans
From All devices
In the Protection console, go to Management > Monitoring plans.

Create a monitoring plan by using one of the two options.

If there are no monitoring plans in the list, click Create.
If there are monitoring plans in the list, click Create plan.

In the Create monitoring plan window, depending on the license of your tenant, do the following:

If your tenant is using Standard protection (service-based licensing mode), the following four monitors are automatically added to the monitoring plan: Disk space, Hardware changes, Last system restart, and Files and folders size.

If the RMM pack is enabled for your tenant (service-based licensing mode) or you are using Security and RMM (solution-based licensing more), select one of the template options, and then click Next.

Option	Description
Recommended	Select this option to create a monitoring plan with the default monitoring configuration.
Custom	Use this option to create a monitoring plan from scratch.

To change the default name of the plan, click the pencil icon, enter the name of the plan, and then click OK.

To add a monitor to the plan, click Add monitor, click the monitor in the list, and then click Add.

The settings of the monitor will be populated automatically with the default values.
You can add up to 30 monitors to a monitoring plan.

In the monitor parameters screen, change the default settings of the monitor and alerts, and then click Done.

You can configure different settings for each monitor. For more information, see Configurable monitors and Configuring monitoring alerts.

To delete a monitor, click the bin icon, and then click Delete.

[Optional] To add workloads to the plan:

Click Add workloads.
Select the workloads, and then click Add.
If there are compatibility issues that you want to resolve, follow the procedure as described in Resolving compatibility issues.
Click Create.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.