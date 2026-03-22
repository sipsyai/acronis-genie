# Combining data flow policy rules

Data Loss Prevention > Creating the data flow policy and policy rules > Combining data flow policy rules
Combining data flow policy rules

When a data transfer matches more than one rule, the permissions and actions configured for all rules are combined and applied as follows.

Permissions

If a data transfer matches more than one rule and these rules have different permissions for the same data category, the overriding rule is the one with higher priority permission, according to the following permission priority list (in descending order):

Exception with the Prioritized flag
Allow with the Prioritized flag
Deny
Exception
Allow

If a data transfer matches more than one rule and these rules have different permissions for different data categories, the following logic is applied for the override:

The most restrictive rule permission is defined for each of the sensitivity categories that the data transfer matches.
The most restrictive of the rule permissions defined in point 1 is enforced.

Example

A file transfer matches three rules in different sensitivity categories as follows:

Sensitivity category	Permission
PII	Allow - Prioritized
PHI	Exception - Prioritized
PCI	Deny

The permission that will be applied is Deny.

Actions

If a data transfer matches more than one rule and these rules have different options configured in the Action field, all configured actions in all triggered rules are performed.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.