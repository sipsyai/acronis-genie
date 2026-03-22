# Remediating user risks

RMM > Managing and monitoring the Microsoft 365 environment > Managing Microsoft 365 users > Remediating user risks
Remediating user risks

You can remediate a number of security risks related to a specific user's Microsoft 365 account. Note that you can only remediate one user risk at a time.

The risks that you can remediate include:

Administrator accounts with a mailbox - remove administrator privileges from accounts where the mailbox is required, and create a new separate administrator account for the user.
Dormant guest, user, and administrator accounts - identify ex-employees or other unused accounts, and remove administrator and other accounts that are no longer required.
Accounts with MFA disabled or not enrolled - evaluate which user accounts are at risk according to the required MFA settings and baselines.
Anonymous administrator accounts - determine if users who require administrator privileges should be given a separate administrator account (without a mailbox).
Accounts with incorrectly configured shared mailboxes - identify the relevant users who need to “Send as” or have “Full access” to the shared account.

In service-based licensing, this functionality requires the RMM > Microsoft 365 seats service quota to be applied to all the customer's Microsoft 365 seats.

In solution-based licensing, the functionality is enabled with either Security and RMM or Ultimate Protection license.

To remediate user risks

In the Cyber Protect console, go to Microsoft 365 management > Users.

Select the checkbox in the relevant user row, and then click Remediate user.

From the Risk dropdown, select the risk you want to remediate, and then click Remediate.

The following table lists the risks and the remediation steps that are applied when you click Remediate.

Risk	Remediation steps
MFA is disabled or user not enrolled	MFA is enabled for the user.
Dormant accounts	Stops any new sign-ins for the selected dormant user or administrator account. If the user or administrator is signed in, they are automatically signed out from all Microsoft services within 60 minutes.
Dormant admins
Admin mailboxes

Removes administrator privileges from the selected account and creates a new, separate administrator account (unlicensed) for the user. The system also automatically generates a CSV file that lists the created administrator accounts and their one-time passwords.


Anonymous admins	Deletes the anonymous administrator account.
Shared mailboxes	Converts the user account to a shared mailbox. You can then delegate "Send as" or "Full access" to the relevant users.
Guests	Deletes the dormant guest user account.
In the confirmation dialog, click Confirm. Then click Close.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.