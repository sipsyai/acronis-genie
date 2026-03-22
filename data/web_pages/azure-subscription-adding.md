# Adding access to a Microsoft Azure subscription

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Managing public cloud account access > Adding access to a Microsoft Azure subscription
Adding access to a Microsoft Azure subscription

By adding a Microsoft Azure subscription in the Cyber Protect console, Acronis can securely access your subscription and directly back up the relevant workloads to Microsoft Azure.

To add access to a Microsoft Azure subscription

In the Cyber Protect console, go to Infrastructure > Public clouds.
Click Add, and from the displayed list of options, select Microsoft Azure.

In the displayed dialog, click Sign in. You are redirected to the Microsoft login page.

You must be assigned with one of the following roles in Microsoft Azure AD in order to complete the connection to the subscription: Cloud Application Administrator, Application Administrator, or Global Administrator. You must also be assigned the Owner role for each selected subscription.

In the Microsoft login screen, enter your login credentials and accept the requested permissions. The connection process starts, and may take several minutes.

For more information about securely accessing your Microsoft Azure and subscription, see article Microsoft Azure connection security and audit (72684).

When the connection is complete, do the following:

In the Microsoft Azure subscription field, select the relevant subscription from the list.

In the Azure region field, select the region in which to deploy the system resources.

The system preselects the region in which most of the resource groups are located but you can change it depending on your preference.

Click Add subscription.

The subscription is added to the list of public clouds.

To renew the annual access certificate for the subscription, see Renewing access to a Microsoft Azure subscription.

To remove access to the subscription, see Removing access to a Microsoft Azure subscription.

If the Microsoft Azure account you are logged into includes access to multiple Microsoft Azure ADs, including ADs in which you were invited as a guest user, only the default user directory is selected. If you want to use a directory in which you are a guest user, you need to create a new user in that specific Microsoft Azure AD. You can then log in to that account and connect to the relevant subscription.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.