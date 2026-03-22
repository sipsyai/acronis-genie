# Installing agents remotely

Installing and deploying Cyber Protection agents > Device discovery > Remote installation of agents > Installing agents remotely
Installing agents remotely

Remote installation of agents is supported for Windows devices only.

Agent installation on multiple devices is only available for devices that are in the same network and discovered by the same discovery method.

You can remotely onboard multiple discovered devices at once. The onboarding process consists of agent installation, plans application, and device registration.

Complete automatic onboarding via Active Directory
Manual preconfiguration and automatic onboarding

Prerequisites

At least one domain controller on which a protection agent is installed must be available in the Active Directory.

To add multiple devices by using the complete automated onbording via Active Directory

In the Protection console, go to Devices > Discovered devices > Devices without agent.
Select the devices that you want to protect.
Click Install agent.
On the Select onboarding option tab, click Complete automatic onboarding via Active Directory.

In the Domain controller field, select the domain controller.

In the Domain administrator credentials field, click Select.

On the Credentials list screen, select the credentials of the administrator account of the domain controller, and then click Select credentials.

The domain controller scans the Active Directory for devices and displays them in a list. By default, all discovered devices are preselected, but you can clear the selection for the devices that you do not want to register and protect.

In the list of devices, ensure that the devices that you want to onboard are selected.

Click Next.

On the Select agent components tab, do the following:

To select the components that you want to install, click Components to install, and then select the components. For more information about the available components, see Agent components.

In the Settings pane, configure the installation options.

Option	Description
Service logon account

The account under which the services will run.
By default, Use Service User Accounts is selected. To change the default value, click Change.

For more information about all options, see Changing the logon account on Windows machines.


Restart the device when required	Select this option if you want the device to be restarted when the installation of a component requires it.
Do not restart the device if a user is logged in	Select this option if you do not want the device to be restarted when a user is logged in to it.

Select a user account under which you want to register the devices.

Click Next.

On the Select plans tab, to select plans that will be applied to the machines automatically, in the plan selection field of the corresponding plan type, click Change, select the plan, and then click Change again.

Plan selection is allowed only if two-factor authentication (2FA) is configured for the tenant. If 2FA is not configured, you must configure it first, and then log in to the Cyber Protect console and start this procedure from the beginning.

Click Next.

On the Review and register screen, check the required quotas, and then do one of the following:

To select different plans, go to the Select plans tab, follow the procedure in step 11, and then click Next until you return to the Review and register screen.

To register the workloads, click Register.

If you are logged in as a partner administrator, any required advanced packs will be automatically enabled for the tenant in which you register the workload.

If you are not logged in as a partner administrator, no required advanced packs will be automatically enabled. You can still apply the selected plans, but they might not work correctly. To resolve this issue, ask your partner administrator to enable the required advanced packs or change the preselected plans.

A file named RemoteInstallEntryPoint.bat is deployed to each registered workload on the network. This file installs the components required to deploy protection agents.

On rare occasions, security scans may flag this file as suspicious or malicious. If this happens, add it to the allowlist/whitelist so the installation can complete successfully.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.