# Preparing machines for remote installation by using a GPO

Installing and deploying Cyber Protection agents > Device discovery > Remote installation of agents > Preparing machines for remote installation by using a GPO
Preparing machines for remote installation by using a GPO

You can configure and apply an Active Directory Group Policy object (GPO) to prepare a set of machines that are members of the Active Directory for remote installation of the Protection agents.

Prerequisites

Your user is a member of the Domain Admins group or a domain administrator.
Group Policy Management Console (GPMC) is installed on the machine on which you are logged in to create the GPO.

To prepare machines for remote installation by using a GPO

To open GPMC, press Win + R, type gpmc.msc, and then press Enter.
In the console tree, right-click the domain or organizational unit (OU) to which you want to apply a GPO.
Click Create a GPO in this domain, and Link it here....
In the New GPO pop-up, enter a name for the GPO, and then click OK.
In the console tree, right-click the GPO that you created in the previous step, and then click Edit....

Disable Use Sharing Wizard, by following the steps below.

In the console tree, navigate to User Configuration > Preferences > Windows Settings > Registry.
Right-click Registry, and then click New > Registry Item.

In the New Registry Properties window, on the General tab, configure the registry item as follows.

Parameter	Value
Action	Update


Hive

HKEY_CURRENT_USER
Key Path

Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced


Value name

SharingWizardOn


Value type	REG_DWORD
Value data	0
Click Apply, and then click OK.

[For Windows Vista and later versions] Disable User Account Control (UAC) by following the steps below.

In the console tree, navigate to Computer Configuration > Preferences > Windows Settings > Registry.
Right-click Registry, and then click New > Registry Item.

In the New Registry Properties window, on the General tab, configure the registry item as follows.

Parameter	Value
Action	Update


Hive

HKEY_LOCAL_MACHINE
Key path

SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\


Value name

EnableLUA


Value type	REG_DWORD
Value Data	0
Click Apply, and then click OK.

[For Windows Vista and later versions] Disable User Account Control (UAC) Remote restrictions, by following the steps below.

In the console tree, navigate to Computer Configuration > Preferences > Windows Settings > Registry.
Right-click Registry, and then click New > Registry Item.

In the New Registry Properties window, on the General tab, configure the registry item as follows.

Parameter	Value
Action	Update


Hive

HKEY_LOCAL_MACHINE
Key path

SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System


Value name

LocalAccountTokenFilterPolicy


Value type	REG_DWORD
Value Data	1
Click Apply, and then click OK.

Enable File and Printer Sharing, by following the steps below.

In the console tree, navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Windows Defender Firewall with Advanced Security > Inbound Rules.
Right-click Inbound Rules, and then click New Rule.
In New Inbound Rule Wizard, configure the rule as follows.
On the Rule Type tab, select Predefined, select File and Printer Sharing, and then click Next.
On the Predefined Rules tab, click Next.
On the Action tab, select Allow the connection, and then click Finish.
In the console tree, navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Windows Defender Firewall with Advanced Security > Outbound Rules.
Right-click Outbound Rules, and then select New Rule.
In New Outbound Rule Wizard, configure the rule by performing the same actions as in steps d - f.

Link the GPO to the domain or OU, by following the steps below.

In the console tree, right-click the target domain or OU, and then click Link an Existing GPO....
On the Select GPO screen, select the GPO that you created, and then click OK.

On the target machines that you want to prepare for a remote agent installation, force the Group Policy Update, by following the steps below.

Run Command Prompt as an administrator.

Run the following command:

gpupdate /force

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.