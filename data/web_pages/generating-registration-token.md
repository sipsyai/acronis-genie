# Generating a registration token

Installing and deploying Cyber Protection agents > Registration of workloads > Registering workloads by using the graphical user interface > Generating a registration token
Generating a registration token

A registration token is a series of 12 characters, separated by hyphens in three segments. The registration token passes the identity of a user to the agent setup program, without storing the user credentials for the Cyber Protect console. This enables users to register workloads under their account or apply protection plans to workloads without logging in to the console.

Protection plans are not applied automatically during workload registration. Applying a protection plan is a separate task.

For security reasons, the tokens have limited lifetime, which you can adjust. The default lifetime is 3 days.

Administrators can generate registration tokens for all user accounts in the tenant that they manage. Users can generate registration tokens only for their own accounts.

To generate a registration token

As an administrator
As a user

Log in to the Cyber Protect console as an administrator.

If you are already signed in to Management Portal, you can go to the Cyber Protect console by navigating to Monitoring > Usage, and then, under the Protection tab, clicking Manage service.

[For partner administrators who manage customer tenants] In the Cyber Protect console, select the tenant with the user for whom you want to generate a token. You cannot generate a token on the All customers level.

Under Devices, click All devices > Add.

The Add devices pane opens on the right.

Scroll down to Registration token, and then click Generate.

Specify the token lifetime.
Select the user for whom you want to generate a token.
When you use the token, workloads will be registered under the user account that you select here.

[Optional] To enable the user of the token to apply and revoke a protection plan on the added workloads, select the plan from the drop-down list.

To apply or revoke the protection plan on the added workloads, you must run a script. For more information, see this knowledge base article.

Click Generate token.
Click Copy to copy the token to your device clipboard, or write the token down manually.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.