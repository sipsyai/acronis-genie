# Server-side protection

Configuring your antivirus and antimalware protection > Antivirus and antimalware protection > Antivirus and antimalware protection settings > Server-side protection
Server-side protection

This feature defines whether Active Protection protects network folders that are shared by you from the external incoming connections from other servers in the network that may potentially bring threats.

The availability of this feature depends on the service quotas that are enabled for your account.

Default setting: Off.

The availability of this feature depends on the license that you have.
Server-side protection is not supported for Linux.

To set trusted connections

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Server-side protection.
Use the Server-side protection toggle to enable it.
Select the Trusted tab.
In the Trusted connections field, click Add to define connections that will be allowed to modify data.
In the ComputerName/Account field, type the name of the computer and the account of the machine where the protection agent is installed. For example, MyComputer\TestUser.
In the Host name field, type the host name of the machine that is allowed to connect to the machine using the protection agent.

Click the check mark to the right to save the connection definition.

Click Done.

To set blocked connections

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Server-side protection.
Use the Server-side protection toggle to enable it.
Select the Blocked tab.
In the Blocked connections field, click Add to define connections that will not be allowed to modify data.
In the ComputerName/Account field, type the name of the computer and the account of the machine where the protection agent is installed. For example, MyComputer\TestUser.
In the Host name field, type the host name of the machine that is allowed to connect to the machine using the protection agent.

Select the check box to the right to save the connection definition.

Click Done.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.