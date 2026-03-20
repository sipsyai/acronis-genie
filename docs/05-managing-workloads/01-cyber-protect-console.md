---
title: "The Cyber Protect console"
section: "Managing workloads in the Cyber Protect console"
subsection: null
page_range: "368-373"
tags: ["console", "overview", "administration-levels", "partner", "customer", "unit", "All-customers"]
acronis_version: "26.02"
---

# The Cyber Protect console

In the Cyber Protect console, you can manage workloads and plans, change the protection settings, configure reports, or check the backup storage.

The Cyber Protect console provides access to additional services or features, such as File Sync & Share or Antivirus and Antimalware protection and URL filtering, Patch management, Device control, and Vulnerability assessment. The type and number of these services and features vary according to your Cyber Protection license.

To check the dashboard with the most important information about your protection, go to **Monitoring** > **Overview**.

Depending on your access permissions, you can manage the protection for one or multiple customer tenants or units in a tenant. To switch the hierarchy level, use the dropdown list in the navigation menu. Only the levels to which you have access are shown. To go to Management Portal, click **Manage**.

The **Devices** section is available in simple and table view. The simple view shows only a few workloads. The table view is enabled automatically when the number of workloads becomes larger.

When a workload goes online or offline, it takes some time for its status to change in the Cyber Protect console. The workload status is checked every minute. If the agent installed on the corresponding machine is not transferring data, and there is no answer to five consecutive checks, the workload is shown as offline. The workload is shown as back online when it answers to a status check or starts transferring data.

## What's new in the Cyber Protect console

When new features of Cyber Protect Cloud are available, you see a pop-up window with a brief description of these features upon logging in to the Cyber Protect console. You can also view the description of the new features by clicking the **What's new** link in the bottom-left corner of the main Cyber Protect console window.

## Administration levels in the Cyber Protect console

Cyber Protect Cloud supports administration at the following levels:

- **Partner level (All customers)** — This level is only available for partner administrators who manage customer tenants.
- **Customer level** — This level is available for customer administrators and partner administrators who manage customer tenants.
- **Unit level** — This level is available for unit administrators, customer administrators from the parent tenant, and partner administrators who manage the parent customer tenant.

Administrators can manage objects, such as plans or workloads, in their own tenants and in their child tenants, with the following limitations:

- Customer tenants can restrict access for partner administrators.
- Units can always be accessed by customer administrators and partner administrators who manage the parent customer tenant.

Administrators cannot see or access objects at a level above their own tenant.

### Selecting an administration level

1. Log in to the Cyber Protect console as an administrator.
2. In the navigation menu on the left, click the arrow next to the tenant name.
3. Select one of the following options:
   - [For partner administrators] To work at the partner level, select **All customers**.
   - To work at the customer or unit level, select the name of a customer or unit.

## Using the Cyber Protect console at All customers level

Partner administrators can use the Cyber Protect console at the partner level (**All customers**).

At this level, partner administrators can perform actions with workloads from different customers. For example, a partner administrator can apply the same plan to multiple workloads from different customers.

At the partner level (**All customers**), the Cyber Protect console provides a customized view:

- **Alerts tab** — Partner administrators can see the alerts from all their managed customers, search the alerts, and filter them by Device, Customer, and Plan.
- **Activities tab** — Activities can be filtered by customer, status, time, and type. The following activity types are automatically pre-selected: Applying plan, Creating the protection plan, Protection plan, Revoking plan, Scripting.
- **Devices tab** — Partner administrators can see the workloads from all managed tenants, select workloads from different tenants, and create device groups.
- **Management tab** — Available plans are grouped by type. Partner administrators can see plans used in their managed customer tenants, and filter plans by status, customer, and creation date. They can create new plans on the partner level.
- **Software management tab** — If the software inventory scanning is enabled for customer workloads, you can see the software scanning results.

> **Important:** At the partner level (**All customers**), you might not be able to perform all operations that are available at the customer level. To perform an operation that is not supported at the partner level, go to the customer level.

### Viewing the workloads of specific customers

At the partner level, you can view the workloads with agents that belong to each managed customer tenant.

1. In the Cyber Protect console, go to **Devices** > **Machines with agents**.
2. In the tree, click **Machines with agents** to expand the list.
3. Click the name of the customer whose workloads you want to view and manage.

### Creating device groups at the partner level

You can create both static and dynamic device groups at the partner level (**All devices**).

### Performing autodiscovery of machines at the partner level

You can perform autodiscovery of machines at the partner level (**All customers**).

**Prerequisites:** There is at least one machine with an installed protection agent in your customer's local network or Active Directory domain.

> **Important:** Only agents that are installed on Windows machines can be discovery agents. Autodiscovery is not supported for adding Domain Controllers. Remote installation of agents is supported only for machines running Windows (Windows XP is not supported).

Discovery methods available at the partner level:
- **Search Active Directory** — discover machines via Active Directory using organizational unit list or LDAP dialect query
- **Scan local network** — active device discovery scan
- **Specify manually or import from file** — add machines by IPv4 address, hostname, or import a text file

### Creating a global antivirus and antimalware exclusions plan

The global exclusions plan enables partner administrators to create a list of trusted items (files, folders, processes, or hashes) at the partner level, add them to a single plan, and apply it to all customer workloads.

1. In Management Portal, go to **Monitoring** > **Usage**.
2. Under **Cyber Protect**, select **Protection**, and then click **Manage service**.
3. In the Cyber Protect console, go to **Management** > **Protection plans**.
4. Click **Create plan**.
5. Expand the **Global Antivirus & Antimalware protection exclusions** module.
6. Select the **Exclusions** option.
7. In the **Trusted items** section, click **Add** and select:
   - **File/folder/process** — specify the path and select whether to trust as file/folder or as process. Wildcards and local network paths are supported.
   - **Hash** — insert MD5 hashes to be included as trusted in the Protection exclusions list.
8. In the **Description** field, enter a short description for your exclusion.
9. Click **Add**, and then click **Done**.

> **Note:** You can create as many global exclusions plans as you need. Active plans are cumulatively applied. Duplicate items will not be duplicated. An item will always be trusted if it exists in the list of trusted items under a global exclusions plan and in the list of blocked items under the protection exclusions module.

## Using wildcards to define exclusions

The asterisk (*) substitutes for zero or more characters. The question mark (?) substitutes for zero or exactly one character. Environment variables cannot be used.

- Wildcards can be used in the middle or the end of a description (e.g., `C:\*.pdf`, `D:\folders\file.*`, `C:\Users\*\AppData\Roaming`).
- Wildcards cannot be used at the beginning of a description (e.g., `*.docx` and `*:\folder\` are not accepted).

## Using variables to define exclusions

You can also use variables to add items to the global exclusions list, with limitations:
- For Windows, only SYSTEM variables are supported (e.g., `%WINDIR%\Media`, `%public%`, `%CommonProgramFiles%\Acronis\`). User-specific variables like `%USERNAME%`, `%APPDATA%` are not supported.
- For macOS, environment variables are not supported.
- For Linux, environment variables are not supported.
