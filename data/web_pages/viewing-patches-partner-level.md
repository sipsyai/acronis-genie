# Viewing patches at the partner level

RMM > Managing software > Assessing vulnerabilities and managing patches > Viewing patches at the partner level
Viewing patches at the partner level

After a vulnerability assessment scan completes, you can view information about the available patches for the vulnerabilities that were found on your customers' devices.

To view details about a patch

Log in to the Cyber Protect console at the partner level (All customers), and then go to Software management > Patches.

The following table describes the information for the patches that you can view on the screen.

Column	Description
Name

Name of the patch




Severity



Severity of the patch: Critical, High, Medium, Low, or None.


Stability

Stability score of the patch that indicates if it is safe to install the patch. You can use this information to estimate the potential impact of a patch before you install it - if a patch is stable or can expose the organization to vulnerabilities. A patch can have one of the following stability scores:

Stable - Indicates that the patch has no reported issues or concerns based on sentiment analysis and other data sources, and that the patch is known (there is enough data about this particular patch). You can confidently install this patch without significant risk.

Minor issues - Suggests that the patch has some reported issues, such as issues in product functionality or UI, but they are minor, non-critical, or have clear workarounds. Usually, you can proceed with the patch installation in most environments, but you should review the issues first.

Caution - Highlights that the patch has significant or widespread issues reported, such as causing system instability, breaking functionality, or introducing security vulnerabilities. In this case, you should delay the patch installation, test it thoroughly in a controlled environment, or wait for vendor updates.

Critical issues - Indicates that the patch has severe, high-impact issues that could cause major disruptions, such as system crashes, data loss, or critical application failures. You must avoid installing this patch until the vendor releases a fix or guidance.

When you click the values in this column, you can see the following additional information about the patch: patch overview, potential risks, statistics and metrics, specific configurations, insights and recommendations, and user experience.

The Stability information is gathered from diverse external sources by using AI search engines.




Affected product

Product for which the patch is applicable
Customers	Number of customers that have devices on which the patch can be installed. If you click the number, the Affected tenants tab opens, where you can see a list of the affected customers.
Devices	Number of devices on which the patch can be installed. If you click the number, the Patchable devices tab opens, where you can see more information about the devices, such as name, customer account under which the device is registered, and MAC address.


Approval status



Approval status of the patch - mainly needed for automatic approval scenarios.

Approved – the patch was installed on at least one machine and validated as OK.
Declined – the patch is not safe, and might corrupt a machine system.
Pending approval – the patch status is unclear, and should be validated.

If you configured automatic patch approval settings with propagation to your customers, but a customer manually changed the approval status of a patch to another value, you will see a conflict warning.

To see a list of the tenants and the approval status for each tenant, click the conflict warning icon.

For more information about configuring patch settings at partner level, see Configuring patch settings at partner level.


Approval statistics

Color bar that visualizes the approval status of the patches. The colors represent the following statuses:

Red - Declined
Green - Approved
Blue - Pending approval



Installed versions

Product versions that are already installed
Patch version	Version of the patch
Last reported	Date that the patch was last reported


Vendor

Vendor of the patch


Category



Category to which the patch belongs:

Critical update – broadly released fixes for specific problems addressing critical, non-security related bugs.
Security update – broadly released fixes for specific products addressing security issues.
Definition update – updates to virus or other definition files.
Update rollup – cumulative set of hotfixes, security updates, critical updates, and updates packaged together for easy deployment. A rollup generally targets a specific area, such as security, or a specific component, such as Internet Information Services (IIS).
Service pack – cumulative sets of all hotfixes, security updates, critical updates, and updates created since the release of the product. Service packs might also contain a limited number of customer-requested design changes or features.
Tool – utilities or features that aid in accomplishing a task or set of tasks.
Feature pack – new feature releases, usually rolled into products at the next release.
Update – broadly released fixes for specific problems addressing non-critical, non-security related bugs.
Application – patches for an application.



Microsoft KB

If the patch is for a Microsoft product, the field shows the KB article ID


Release date

Date when the patch was released
First installed

Date of the first successful installation of the patch on a machine


Patch ID	ID of the patch


License agreement



Acceptance status of the license agreement of the patch. The license agreement can be in one of the following statuses:

Agreed - License agreement is accepted.
Pending - Initial state of the license agreement, when no decision has been made yet.
Declined - If you decline the license agreement, the patch status becomes Declined and it will not be installed.

To view details about a specific patch in the list of patches, click the corresponding patch.

A new pane opens with information for the specific patch. You can see the following additional details about the patch.

Tab	Description
Details	On this tab, you can review the details of the patch, such as license agreement, size, language, vendor site, and number of patchable devices and affected tenants.
Affected tenants	On this tab, you can see a list of all customers and units that have patchable devices (devices on which the patch can be installed) and the number of patchable devices per tenant.
Patchable devices	On this tab, you can see a list of all your customers' devices on which the patch can be installed.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.