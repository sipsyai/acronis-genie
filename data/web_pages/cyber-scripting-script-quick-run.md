# Script quick run

Managing workloads in the Cyber Protect console > Cyber Scripting > Script quick run
Script quick run

You can run a script immediately, without including it in a scripting plan. You cannot use this operation on more than 150 workloads, on offline workloads, or on device groups.

The target workload must be assigned a service quota that supports the Script quick run functionality, and the RMM license (service-based licensing model) or Security and RMM (solution-based licensing mode) license must be enabled for its tenant. An appropriate service quota will be automatically assigned if it is available in the tenant.

You can only use your approved scripts from Script repository > My scripts. Only an administrator with the Cyber administrator role can use scripts in the Testing status. For more information about the roles, see User roles and Cyber Scripting rights.

You can start a quick run in the following ways:

From the Devices tab

Select one or more workloads, and then select which script to run on it.

From the Management > Scripting repository tab

Select a script, and then select one or more target workloads.

To run a script from the Devices tab

In the Cyber Protect console, go to Devices > All devices.
Select the workload on which you want to run the script, and then click Protect.
Click Script quick run.
Click Choose script, select the script that you want to use, and then click Done.

Choose under which account the script will run on the target workload. The following options are available:

System account (in macOS, this is the root account)

Currently logged-in account

Specify how long the script can run on the target workload.

If the script cannot finish running within the set time frame, the Cyber Script operation will fail.

You can use values between 1 and 1440 minutes.

[Only for PowerShell scripts] Configure the PowerShell execution policy.

For more information about this policy, see the Microsoft documentation.

Click Run now.

To run a script from the Scripting repository tab

In the Cyber Protect console, go to Management > Scripting repository.
Select the script that you want to run, and then click Script quick run.
Click Add workloads to select the target workloads, and then click Add.
Click Choose script, select the script that you want to use, and then click Done.

Choose under which account the script will run on the target workload. The following options are available:

System account (in macOS, this is the root account)

Currently logged-in account

Specify how long the script can run on the target workload.

If the script cannot finish running within the set time frame, the Cyber Script operation will fail.

You can use values between 1 and 1440 minutes.

[Only for PowerShell scripts] Configure the PowerShell execution policy.

For more information about this policy, see the Microsoft documentation.

Click Run now.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.