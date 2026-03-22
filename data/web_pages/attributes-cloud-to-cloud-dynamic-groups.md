# Search attributes for cloud-to-cloud workloads

Managing workloads in the Cyber Protect console > Device groups > Creating a dynamic group > Search attributes for cloud-to-cloud workloads
Search attributes for cloud-to-cloud workloads

The following table summarizes the attributes that you can use in your search queries for Microsoft 365 and Google Workspace workloads.

To see which attributes you can use in search queries for other types of workloads, see Search attributes for non-cloud-to-cloud workloads.

Attribute	Meaning	Can be used in	Search query examples	Supported for group creation
name	Display name of a Microsoft 365 or Google Workspace workload	All cloud-to-cloud resources

name = 'My Name'

name LIKE '*nam*'

Yes
email	Email address for a Microsoft 365 user or group, or a Google Workspace user

Microsoft 365 > Groups

Microsoft 365 > Users

Google Workspace > Users



email = 'my_group_email@mycompany.com'

email LIKE '*@company*'

email NOT LIKE '*enterprise.com'

Yes
siteName	Name of a site that is associated with a Microsoft 365 group	Microsoft 365 > Groups

siteName = 'my_site'

siteName LIKE '*company.com*support*'

Yes
url	Web address for a Microsoft 365 group or SharePoint site

Microsoft 365 > Groups

Microsoft 365 > Site collections



url = 'https://www.mycompany.com/'

url LIKE '*www.mycompany.com*'

Yes
licensedByMsft	Users who have a valid Microsoft 365 subscription. Licensed users can use Microsoft 365 services, such as Exchange Online and OneDrive.	Microsoft 365 > Users

licensedByMsft = true

licensedByMsft = false

Yes
msftSignInBlocked	Users who have been restricted from signing in to Microsoft 365. Blocked users cannot use Microsoft 365 services.	Microsoft 365 > Users

msftSignInBlocked = true

msftSignInBlocked = false

Yes
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.