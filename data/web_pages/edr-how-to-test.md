# How to test if Endpoint Detection and Response (EDR) is working correctly

Endpoint Detection and Response (EDR) > How to test if Endpoint Detection and Response (EDR) is working correctly
How to test if Endpoint Detection and Response (EDR) is working correctly

To ensure EDR is deployed and working, you can run a number of commands that trigger EDR detections.

When EDR is deployed, you should see incidents immediately if any suspicious activity occurs. The steps below enable you to check if EDR is working if no new incidents were triggered for several days.

To test if EDR is deployed and working correctly

Login to the relevant domain-joined Active Directory user account.

Run the following two commands in Windows PowerShell:

net group "Domain Computers" /domain

net user administrator /domain

In the Cyber Protect console, go to Protection > Incidents to view the generated incident.

You can also click on the triggered Medium severity type incident to display it in the EDR cyber kill chain and confirm the PowerShell commands you executed in the previous step, as shown in the example below.

Run the following commands in Windows PowerShell:

c:\>whoami

c:\>net localgroup

c:\>net localgroup administrators

c:\>powershell -command start-process cmd -verb runas

c:\WINDOWS\system32>net user administrator /active:yes

c:\>powershell -command Get-Hotfix

In the EDR cyber kill chain, click on the executable nodes (for example, net.exe or whoami.exe) to display the exact PowerShell commands executed on the command line. These commands are shown in the Details section of the Overview tab in the example below.

After you have confirmed that an EDR incident was generated, manually set the Threat status for the incident to Mitigated and the Investigation state to Closed. For more information, see How to investigate incidents in the cyber kill chain. You can also enter a comment for the incident to indicate that this was a test incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.