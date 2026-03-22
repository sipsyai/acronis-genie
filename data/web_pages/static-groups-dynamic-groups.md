# Static groups and dynamic groups

Managing workloads in the Cyber Protect console > Device groups > Static groups and dynamic groups
Static groups and dynamic groups

You can create the following type of custom groups:

Static
Dynamic
Static groups

Static groups contain manually added workloads.

The content of a static group changes only when you explicitly add or remove a workload.

Example: You create a static group for the accounting department in your company, and then manually add the accountants' machines to this group. When you apply a group plan, the machines in that group become protected. If a new accountant is hired, you will have to add the accountant's machine to the static group manually.

Dynamic groups

Dynamic groups contain workloads that match specific criteria. You define these criteria in advance by creating a search query that includes attributes (for example, osType), their values (for example, Windows), and search operators (for example, IN).

Thus, you can create a dynamic group for all machines whose operating system is Windows or a dynamic group that contains all users in your Microsoft 365 organization whose email addresses begin with john.

All workloads that have the required attributes and values are automatically added to the group and any workload that loses a required attribute or value is automatically removed from the group.

Example 1: The host names of the machines that belong to the accounting department contain the word accounting. You search for the machines whose names contain accounting, and then you save the search results as a dynamic group. Then, you apply a protection plan to the group. If a new accountant is hired, the accountant's machine will have accounting in its name and will be automatically added to the dynamic group as soon as you register that machine in the Cyber Protect console.

Example 2: The accounting department forms a separate Active Directory organizational unit (OU). You specify the accounting OU as a required attribute, and then you save the search results as a dynamic group. Then, you apply a protection plan to the group. If a new accountant is hired, the accountant's machine will be added to the dynamic group as soon as it is added to the Active Directory OU and is registered in the Cyber Protect console (regardless of which comes first).

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.