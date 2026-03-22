# Changing the logon account on Windows machines

Installing and deploying Cyber Protection agents > Installing protection agents by using the graphical user interface > Installing protection agents in Windows > Changing the logon account on Windows machines
Changing the logon account on Windows machines

On the Select agent components tab, define the account under which the services will run by specifying Logon account for the agent service. You can select one of the following:

Use Service User Accounts (default for the agent service)

Service User Accounts are Windows system accounts that are used to run services. The advantage of this setting is that the domain security policies do not affect these accounts' user rights. By default, the agent runs under the Local System account.

Create a new account

The account name will be Agent User for the agent.

Use the following account

If you install the agent on a domain controller, the system prompts you to specify existing accounts (or the same account) for the agent. For security reasons, the system does not automatically create new accounts on a domain controller.

The user account that you specify when the setup program runs on a domain controller must be granted the Log on as a service right. This account must have already been used on the domain controller, in order for its profile folder to be created on that machine.

See also Using gMSA accounts with the Cyber Protection agent.

For more information about installing the agent on a read-only domain controller, see this knowledge base article.

If you chose the Create a new account or Use the following account option, ensure that the domain security policies do not affect the related accounts' rights. If an account is deprived of the user rights assigned during the installation, the component may work incorrectly or not work.
Note that we do not recommend changing the logon accounts manually after the installation is completed.
Privileges required for the logon account

The Cyber Protection agent for Windows is run as a Managed Machine Service (MMS) on protected Windows machines. The account under which the agent will run must have specific rights for the agent to work correctly. The MMS user account should be configured as follows:

Included in the Backup Operators and Administrators groups. On a Domain Controller, the user must be included in the group Domain Admins.

Granted the Full Control permission on the folder %PROGRAMDATA%\Acronis and on its subfolders.

For Windows XP and Server 2003, permissions should be granted on folder %ALLUSERSPROFILE%\Application Data\Acronis and its subfolders.

Granted the Full Control permission on certain registry keys in the following key: HKEY_LOCAL_MACHINE\SOFTWARE\Acronis.

Assigned the following user rights:

Log on as a service
Adjust memory quotas for a process
Replace a process level token
Modify firmware environment values
How to assign the user rights

Follow the instructions below to assign the user rights (this example uses the Log on as service user right, the steps are the same for other user rights):

Log on to the computer by using an account with administrative privileges.
From Windows Control Panel, open Administrative Tools, and then open Local Security Policy.
Expand Local Policies and click User Rights Assignment.
In the right-hand pane, right-click Log on as a service, and select Properties.
Click the Add User or Group… button to add a new user.
In the Select Users, Computers, Service Accounts, or Groups window, find the account to which you want to assign this privilege, and then click OK.
In the Log on as a service Properties, click OK to save the changes.

Ensure that the user which you have added to the Log on as service user right is not listed in the Deny log on as a service policy in Local Security Policy.

Using gMSA accounts with the Cyber Protection agent

Group Managed Service Accounts (gMSA) can be used to run services on multiple servers without having to manage the password.

The following procedure is applicable if you want to change the user account used by the Acronis Cyber Protection agent after the installation, so that the agent can use a gMSA.

All protection plans previously assigned to the machine on which you are changing the logon account will stop working and you will have to revoke and re-apply them after having changed the account.

To enable the use of a gMSA for the Cyber Protection agent

Create a gMSA following the standard procedure documented in the Microsoft knowledge base.
Configure the gMSA as described in section Privileges required for the logon account.
Assign the gMSA as the logon account for the MMS service on the machine where the agent runs.

Open the Windows Start menu, and enter services.msc to open the list of local services.

Right-click the Acronis Managed Machine Service and click Properties.

On the Log On tab, select This account and then click Browse to find the gMSA that you want to use.

Click OK.

Apply protection plans as needed.
If you had protection plans applied to the machine prior to changing the logon account, revoke those plans and re-apply them.
If you didn't have protection plans applied to the machine, create new ones or select existing plans and apply them.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.