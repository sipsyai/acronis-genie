---
title: "Search attributes for cloud-to-cloud workloads"
section: "Managing workloads in the Cyber Protect console"
subsection: "Search attributes for cloud-to-cloud workloads"
page_range: "410-411"
tags: [search, cloud-to-cloud, Microsoft 365, Google Workspace, dynamic groups, query]
acronis_version: "26.02"
---

# Search attributes for cloud-to-cloud workloads

The following table summarizes the attributes that you can use in your search queries for Microsoft 365 and Google Workspace workloads. To see which attributes you can use in search queries for other types of workloads, see "Search attributes for non-cloud-to-cloud workloads."

| Attribute | Meaning | Can be used in | Search query examples | Supported for group creation |
|-----------|---------|----------------|----------------------|------------------------------|
| `name` | Display name of a Microsoft 365 or Google Workspace workload | All cloud-to-cloud resources | `name = 'My Name'`; `name LIKE '*nam*'` | Yes |
| `email` | Email address for a Microsoft 365 user or group, or a Google Workspace user | Microsoft 365 > Groups; Microsoft 365 > Users; Google Workspace > Users | `email = 'my_group_email@mycompany.com'`; `email LIKE '*@company*'`; `email NOT LIKE '*enterprise.com'` | Yes |
| `siteName` | Name of a site associated with a Microsoft 365 group | Microsoft 365 > Groups | `siteName = 'my_site'`; `siteName LIKE '*company.com*support*'` | Yes |
| `url` | Web address for a Microsoft 365 group or SharePoint site | Microsoft 365 > Groups; Microsoft 365 > Site collections | `url = 'https://www.mycompany.com/'`; `url LIKE '*www.mycompany.com*'` | Yes |
| `licensedByMsft` | Users who have a valid Microsoft 365 subscription. Licensed users can use Microsoft 365 services, such as Exchange Online and OneDrive. | Microsoft 365 > Users | `licensedByMsft = true`; `licensedByMsft = false` | Yes |
| `msftSignInBlocked` | Users who have been restricted from signing in to Microsoft 365. Blocked users cannot use Microsoft 365 services. | Microsoft 365 > Users | `msftSignInBlocked = true`; `msftSignInBlocked = false` | Yes |

## Search operators

The following operators can be used in search queries for all workloads (both cloud-to-cloud and non-cloud-to-cloud):

| Operator | Supported for | Meaning | Examples |
|----------|--------------|---------|----------|
| `AND` | All workloads | Logical conjunction operator | `name like 'en-00' AND tenant = 'Unit 1'` |
| `OR` | All workloads | Logical disjunction operator | `state = 'backup' OR state = 'interactionRequired'` |
| `NOT` | All workloads | Logical negation operator | `NOT(osProductType = 'workstation')` |
| `IN (<value1>,... <valueN>)` | All workloads | Checks if an expression matches any value in a list of values | `osType IN ('windows', 'linux')` |
| `NOT IN` | All workloads | The opposite of the IN operator | `NOT osType IN ('windows', 'linux')` |
| `LIKE 'wildcard pattern'` | All workloads | Checks if an expression matches the wildcard pattern. Wildcards: `*` or `%` represents zero, one, or multiple characters; `_` represents a single character | `name LIKE 'en-00'`; `name LIKE '*en-00'`; `name LIKE '*en-00*'`; `name LIKE 'en-00_'` |
| `NOT LIKE 'wildcard pattern'` | All workloads | The opposite of the LIKE operator | `NOT name LIKE 'en-00'` |
| `RANGE (<starting_value>, <ending_value>)` | All workloads | Checks if an expression is within a range of values (inclusive). Case-insensitive, uses ASCII sort order. | `ip RANGE('10.250.176.1','10.250.176.50')`; `name RANGE('a','d')` |
| `=` or `==` | All workloads | Equal to operator | `osProductType = 'server'` |
| `!=` or `<>` | All workloads | Not equal to operator | `id != '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` |
| `<` | Non-cloud-to-cloud workloads | Less than operator | `memorySize < 1024` |
| `>` | Non-cloud-to-cloud workloads | Greater than operator | `diskSize > 300GB` |
| `<=` | Non-cloud-to-cloud workloads | Less than or equal to operator | `lastBackupTime <= '2022-03-11 00:15'` |
| `>=` | Non-cloud-to-cloud workloads | Greater than or equal to operator | `nextBackupTime >= '2022-08-11'` |
