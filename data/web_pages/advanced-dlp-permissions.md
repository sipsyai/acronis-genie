# Adjusting the permissions in data flow policy rules

Data Loss Prevention > Creating the data flow policy and policy rules > Adjusting the permissions in data flow policy rules
Adjusting the permissions in data flow policy rules

Data Loss Prevention supports three types of permissions in data flow policy rules. The permissions are configured individually in each rule of the policy.

Allow

(permissive)

Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are allowed.
Exception

(prohibitive)



Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are not allowed, but the sender can submit an exception to the rule to allow a specific transfer.

All subsequent data transfers between this sender and recipient for this sensitivity category will be allowed for five minutes after the exception is submitted.

Deny

(prohibitive)



Data transfers that match the combination of sensitivity category, sender, and recipient defined in the rule are not allowed, and the sender does not have the option to submit an exception.

In addition, a priority flag can be assigned to the Allow and Exception permissions to increase the policy management flexibility. With this setting, you can override the permissions set for specific groups in other data flow rules in the policy. You can use it to apply a group data flow rule only to some of its members. To achieve this, you must create a data flow rule for specific users that you want to exclude from the group rules, and then prioritize their permissions over the data flow restrictions configured in the rules for the group to which these users belong. For information on permission priorities when combining rules, see Combining data flow policy rules.

Before switching a company or unit policy from Observation to Enforcement mode, it is crucial to adjust the default rules for each sensitive data category from the permissive to a prohibitive state. Default rules are marked with an asterisk (*) in the Data flow policy view. Read more about the types of policy rules in the Fundamentals guide.

To edit permissions in policy rules

Log in to the Cyber Protect console as an administrator.
Navigate to Protection > Data flow policy.
Select the policy rule that you wish to edit and click Edit above the rules list.
The Edit data flow rule window opens.
In the Permission section, select Allow, Exception, or Deny.
(Optional) To prioritize the Allow or Exception permission of this rule over the permissions in other rules, select the Prioritize check box.

You do not need to use this check box to prioritize a data flow rule over the default Any > Other rule, because it has the lowest priority in the policy by default.

For information on permission priorities when combining rules, see Combining data flow policy rules.

(Optional) Select an action to be executed when the rule is triggered.
Save the changes to the policy rule.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.