# Configuring file filters

Managing the backup and recovery of workloads and files > Backup options > File filters (Inclusions/Exclusions) > Configuring file filters
Configuring file filters

You can configure the file filters in the protection plan.

To configure file filters

In a protection plan, expand the Backup module.
In Backup options, click Change.
Select File filters (Inclusions/Exclusions).

Configure the file filters.

You can configure one filter (inclusion or exclusion) or both filters. The exclusion filter takes precedence over the inclusion filter. For example, if you specify C:\File.exe in both filters, C:\File.exe will be skipped during a backup.

Using filters does not affect the selection of specific files in the backup scope (What to back up). For more information, see Filter examples.

If a name or path includes a comma or semicolon, replace them with the question mark (?) wildcard. The comma and the semicolon are interpreted as delimiters and will split the filter into two parts. For more information, see Wildcards.
Click Done.
Save the protection plan.

As a result, the file filters will be applied to the scope that is configured in the What to back up section of the protection plan.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.