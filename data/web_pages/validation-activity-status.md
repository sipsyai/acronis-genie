# Validation activity status

Working with plans > Off-host data protection plans > Validation > Validation activity status
Validation activity status

A validation plan might include multiple backups. All backups are processed sequentially, one by one, in a single validation activity.

A protection agent can run only one validation activity at a time. For example, two simultaneous validation activities require two agents and three simultaneous activities require three agents.

The following table summarizes the possible statuses of a validation activity.

Activity result	Plan with one backup	Plan with multiple backups
Success	All validation methods succeeded	All validation methods succeeded in all backups
Success with warnings	N/A	At least one validation method failed in at least one backup
Fail	At least one validation method failed	At least one validation method failed in all backups



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.