# Creating a scripting plan

Managing workloads in the Cyber Protect console > Cyber Scripting > Scripting plans > Creating a scripting plan
Creating a scripting plan

You can create a scripting plan in the following ways:

On the Devices tab

Select workloads, and then create a scripting plan for them.

On the Management > Scripting plans tab

Create a scripting plan, and then select the workloads to which to apply the plan.

To create a scripting plan on the Devices tab

In the Cyber Protect console, go to Devices > Machine with agents.
Select the workloads or the device groups to which you want to apply a scripting plan, and then click Protect or Protect group, respectively.
[If there are already applied plans] Click Add plan.

Click Create plan > Scripting plan.

A template for the scripting plan opens.

To modify the scripting plan name, click the pencil icon.

Click Choose script, select the script that you want to use, and then click Done.

You can only use your approved scripts from Script repository > My scripts. Only an administrator with the Cyber administrator role can use scripts in the Testing status. For more information about the roles, see User roles and Cyber Scripting rights.

Configure the schedule and the start conditions for the scripting plan.

Choose under which account the script will run on the target workload. The following options are available:

System account (in macOS, this is the root account)

Currently logged-in account

Specify how long the script can run on the target workload.

If the script cannot finish running within the set time frame, the Cyber Scripting operation will fail.

The minimum value that you can specify is one minute and the maximum is 1440 minutes.

[Only for PowerShell scripts] Configure the PowerShell execution policy.

For more information about this policy, see the Microsoft documentation.

Click Create.

To create a scripting plan on the Scripting plans tab

In the Cyber Protect console, go to Management > Scripting plans.

Click Create plan.

A template for the scripting plan opens.

To select the workloads or the device groups to which you want to apply the new plan, click Add workloads.

Click Machines with agents to expand the list, and then select the desired workloads or device groups.

Click Add.

For more information about how to create device groups at the partner level, see Creating a static device group at the partner level and Creating a dynamic device group at the partner level.

You can also select workloads or device groups after you create the plan.

To modify the scripting plan name, click the pencil icon.

Click Choose script, select the script that you want to use, and then click Done.

You can only use your approved scripts from Script repository > My scripts. Only an administrator with the Cyber administrator role can use scripts in the Testing status. For more information about the roles, see User roles and Cyber Scripting rights.

Configure the schedule and the start conditions for the scripting plan.

Choose under which account the script will run on the target workload. The following options are available:

System account (in macOS, this is the root account)

Currently logged-in account

Specify how long the script can run on the target workload.

If the script cannot finish running within the set time frame, the Cyber Scripting operation will fail.

The minimum value that you can specify is one minute and the maximum is 1440 minutes.

[Only for PowerShell scripts] Configure the PowerShell execution policy.

For more information about this policy, see the Microsoft documentation.

Click Create.

See also
Schedule and start conditions
Managing the target workloads for a plan
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.