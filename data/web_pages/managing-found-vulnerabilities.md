# Managing found vulnerabilities

RMM > Managing software > Assessing vulnerabilities and managing patches > Managing found vulnerabilities
Managing found vulnerabilities

If the vulnerability assessment was performed at least once and some vulnerabilities were found, you can see them in Software management > Vulnerabilities. The list of vulnerabilities shows both vulnerabilities that have patches to be installed, and those that do not have suggested patches. You can use the filter to show only vulnerabilities with patches.

Name	Description


Name

The name of vulnerability.


Affected products

Software products for which the vulnerabilities were found.


Machines

The number of affected machines.


Severity



The severity of found vulnerability. The following levels can be assigned according to the Common Vulnerability Scoring System (CVSS):

Critical: 9 - 10 CVSS
High: 7 - 9 CVSS
Medium: 3 - 7 CVSS
Low: 0 - 3 CVSS
None



Patches

The number of appropriate patches.


Published

The date and time when the vulnerability was published in Common Vulnerabilities and Exposures (CVE).


Detected

The first date when an existing vulnerability was detected on machines.

You can find the description of found vulnerability by clicking its name in the list.

To start the vulnerability remediation process

In the Cyber Protect console, go to Software management > Vulnerabilities.
Select the vulnerability in the list, and then click Install patches. The vulnerability remediation wizard will open.
Select the patches to be installed on the selected machines, and then click Next.
Select the machines on which you want to install the patches.

Select the restart options.

The following table provides more information about the restart options.

Option	Description
Restart if required	If you want the workload to be restarted after the software is installed or uninstalled only if the software requires it, select this checkbox.
Always restart

If you want the workload to always be restarted after the software is installed or uninstalled, select this checkbox.


Do not restart

If you do not want the workload to be restarted after the software is installed or uninstalled, select this checkbox.


Schedule automatic restart

This option is available if you selected Restart if required or Always restart.

The option enables automatic restart of the workload.


If a user is logged on to the device, the device will be automatically restarted after:

This option is available if you selected Schedule automatic restart.

Select the period after which the workload will be restarted automatically. The user who is logged in to the workload will be notified about a pending automatic restart and the time when it will happen. Thus, users can save their work and prepare for the restart.


Additional notifications

This option is available if you selected Schedule automatic restart.

Select this option if you want the user who is logged in to the workload to be reminded repeatedly about a pending restart before the selected period passes.

The timing of notifications depends on the selected period and transitions into a countdown as the restart time nears. This ensures that users stay informed and prepared for the restart. Notifications are triggered by a successful software update or deployment and are sent at the following times.

The timing of the first notification coincides with the selected period.

24 h before the automatic restart.
8 h before the automatic restart.
4 h before the automatic restart.
1 h before the automatic restart.
30 min before restart.
15 min before restart.
5 min before the automatic restart. The last user notification cannot be closed or dismissed.

If no user is logged on to the device, restart it immediately

This option is available if you selected Schedule automatic restart.

If you select this option and no user is logged in to the workload, the workload will be restarted immediately, without waiting for the selected period before automatic restart to pass.

Click Install patches.

As a result, the selected patches are installed on the selected machines.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.