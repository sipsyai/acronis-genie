# Viewing the list of available patches

RMM > Managing software > Assessing vulnerabilities and managing patches > Viewing the list of available patches
Viewing the list of available patches

After a vulnerability assessment scan completes, you can view information about the available patches in Software management > Patches.

To view details about a specific patch, in the list of patches, click the corresponding patch.

The following table describes the information for the patch that you can view on the screen.

Column	Description


Approval status



The approval status is mainly needed for automatic approval scenarios.

You can define one of the following statuses for a patch:

Approved – the patch was installed on at least one machine and validated as ok
Declined – the patch is not safe and may corrupt a machine system
Pending approval – the patch status is unclear and should be validated



License agreement


Agreed
Disagreed. If you disagree with the license agreement, then the patch status becomes Declined and it will not be installed



Severity



The severity of the patch:

Critical
High
Medium
Low
None



Vendor

The vendor of the patch


Affected product

Product for which the patch is applicable


Installed versions

Product versions that are already installed


Version

Version of the patch
Stability

Stability score of the patch that indicates if it is safe to install the patch. You can use this information to estimate the potential impact of a patch before its installation, and whether a patch is stable or can expose the organization to vulnerabilities. A patch can have one of the following stability scores:

Stable - Indicates that the patch has no reported issues or concerns based on sentiment analysis and other data sources, and that the patch is known (there is enough data about this particular patch). You can confidently install this patch without significant risk.

Minor issues - Suggests that the patch has some reported issues, such as issues in product functionality or UI, but they are minor, non-critical, or have clear workarounds. Usually, you can proceed with the patch installation in most environments, but you should review the issues first.

Caution - Highlights that the patch has significant or widespread issues reported, such as causing system instability, breaking functionality, or introducing security vulnerabilities. In this case, you should delay the patch installation, test it thoroughly in a controlled environment, or wait for vendor updates.

Critical issues - Indicates that the patch has severe, high-impact issues that could cause major disruptions, such as system crashes, data loss, or critical application failures. You must avoid installing this patch until the vendor releases a fix or guidance.

When you click the values in this column, you can see the following additional information about the patch: patch overview, potential risks, statistics and metrics, specific configurations, insights and recommendations, and user experience.

The Stability information is gathered from diverse external sources by using AI search engines.




Category



The category to which the patch belongs:

Critical update – broadly released fixes for specific problems addressing critical, non-security related bugs.
Security update – broadly released fixes for specific products addressing security issues.
Definition update – updates to virus or other definition files.
Update rollup – cumulative set of hotfixes, security updates, critical updates, and updates packaged together for easy deployment. A rollup generally targets a specific area, such as security, or a specific component, such as Internet Information Services (IIS).
Service pack – cumulative sets of all hotfixes, security updates, critical updates, and updates created since the release of the product. Service packs might also contain a limited number of customer-requested design changes or features.
Tool – utilities or features that aid in accomplishing a task or set of tasks.
Feature pack – new feature releases, usually rolled into products at the next release.
Update – broadly released fixes for specific problems addressing non-critical, non-security related bugs.
Application – patches for an application.



Release date

The date when the patch was released
Last reported	The date of the last time when the patch was reported
First installed

The date of the first successful installation of the patch on a machine




Microsoft KB

If the patch is for a Microsoft product, the field shows the KB article ID


Machines

Number of affected machines


Vulnerabilities

The number of vulnerabilities. If you click on it, you will be redirected to the list of vulnerabilities.


Size

The average size of the patch


Language

The language which is supported by the patch


Vendor site

The official site of the vendor

Configuring the patch lifetime in the list

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.