# Applied and scheduled backup plans for Microsoft 365 workloads

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Applied and scheduled backup plans for Microsoft 365 workloads
Applied and scheduled backup plans for Microsoft 365 workloads

You can apply only one backup plan per service to an individual Microsoft 365 workload. For more information about the available services per workload, see Viewing the protection status of a Microsoft 365 workload per service.

For example, you can apply only one mailbox backup plan to a Microsoft 365 user. You can also apply the same type of plan (mailbox backup) to one or more dynamic or static groups that contain this workload. In this case, the user's mailbox can be backed up by more than one backup plan.

Only the plan that is applied first will automatically run as scheduled. Other plans will be successfully applied to the workload, but can only be run manually.

For example:

You apply Plan A (mailbox backup) to user John Doe. You cannot apply another mailbox backup plan (Plan B) to the same user because Plan A is already applied.
You apply Plan B (mailbox backup) to a dynamic or static group that contains John Doe. You cannot apply another mailbox plan (Plan C) to the same dynamic group because Plan B is already applied.
You apply Plan C (mailbox backup) to All groups, or a different dynamic or static group that contains John Doe.

As a result, Plan A, Plan B, and Plan C can back up John Doe's mailbox, but only Plan A will run as scheduled for this user because it was applied first. You can manually run Plan B and Plan C for John Doe. Plan B and Plan C will run as scheduled for users or groups on which each of these plans is the one applied first.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.