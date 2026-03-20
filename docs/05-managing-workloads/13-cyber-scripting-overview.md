---
title: "Cyber Scripting overview, prerequisites, and user roles"
section: "Managing workloads in the Cyber Protect console"
subsection: "Cyber Scripting"
page_range: "463-466"
tags: [cyber scripting, automation, scripts, PowerShell, Bash, user roles, permissions, prerequisites]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#cyber-scripting.html"
---

# Cyber Scripting

With Cyber Scripting, you can use scripts to automate routine operations on Windows and macOS machines in your environment, such as installing software, modifying configurations, starting or stopping services, and creating accounts. Thus, you can decrease the time that you spend on such operations and reduce the risk of error when performing them manually.

Cyber Scripting is available for administrators and users at the customer level, and to partner administrators (service providers). The scripts that you can use must be approved in advance. Only the administrators with the **Cyber administrator** role can approve and test new scripts.

Depending on your user role, you can perform different operations with scripts and scripting plans.

## Prerequisites

- The Cyber Scripting functionality requires the RMM (service-based licensing mode) or Security and RMM (solution-based licensing mode) license.
- To use all the features of Cyber Scripting such as script editing, script run, creation of scripting plans, and so on, you must enable two-factor authentication for your account.

## Limitations

- The following scripting languages are supported:
  - PowerShell
  - Bash
- Cyber Scripting operations can only run on target machines that have an installed protection agent.

## Supported platforms

Cyber Scripting is available for Windows and macOS workloads.

| Operating system | Version |
|-----------------|---------|
| Windows | Windows 7 SP1 and later -- all editions |
| | Windows 8/8.1 -- all editions (x86, x64), except for the Windows RT editions |
| | Windows 10 -- Home, Pro, Education, Enterprise, IoT Enterprise editions |
| | Windows 11 |
| | Windows Server 2008 R2 SP1 and later -- Standard, Enterprise, Datacenter, Foundation, and Web editions |
| | Windows Server 2012/2012 R2 -- all editions |
| | Windows Server 2016 |
| | Windows Server 2019 |
| | Windows Server 2022 |
| | Windows Storage Server (2008 R2, 2012, 2012 R2, 2016) |
| macOS | macOS Mojave 10.14 |
| | macOS Catalina 10.15 |
| | macOS Big Sur 11 |
| | macOS Monterey 12 |

## User roles and Cyber Scripting rights

The available actions with scripts and scripting plans depend on the script status and your user role. Administrators can manage objects, such as plans or workloads, in their own tenants and in their child tenants, with the following limitations:

- Customer tenants can restrict access for partner administrators.
- Units can always be accessed by customer administrators and partner administrators who manage the parent customer tenant.
- Administrators cannot see or access objects at a level above their own tenant.
- Lower-level administrators have only read-only access to the scripting plans applied to their workloads by an upper-level administrator.

### Role descriptions

- **Company administrator** -- Full administrator rights in all services. With regard to Cyber Scripting, same rights as the Cyber administrator role.
- **Cyber administrator** -- Full permissions, including approval of scripts that can be used in the tenant, and the ability to run scripts with the **Testing** status.
- **Administrator** -- Partial permissions: ability to run approved scripts as well as create and run scripting plans that use approved scripts.
- **Read-only administrator** -- Limited permissions: ability to view scripts and protection plans that are used in the tenant.
- **User** -- Partial permissions: ability to run approved scripts as well as create and run scripting plans that use approved scripts, but only on the user's own machine.

### Permissions matrix

| Role | Object | Draft | Testing | Approved |
|------|--------|-------|---------|----------|
| **Cyber administrator / Company administrator** | Scripting plan | Edit, Delete, Revoke, Disable, Stop | Create, Edit, Apply, Enable, Run, Delete, Revoke, Disable, Stop | Create, Edit, Apply, Enable, Run, Delete, Revoke, Disable, Stop |
| | Script | Create, Edit, Change status, Clone, Delete, Cancel running | Create, Edit, Change status, Run, Clone, Delete, Cancel running | Create, Edit, Change status, Run, Clone, Delete, Cancel running |
| **Administrator** | Scripting plan | View | View, Cancel run | Edit, Apply, Enable, Run, Delete, Revoke, Disable, Stop |
| | Script | Create, Edit, Clone, Delete, Cancel running | View, Clone, Cancel running | Run, Clone, Cancel running |
| **User** (for their own workloads) | Scripting plan | Edit, Revoke, Disable, Stop | Cancel run | Edit, Apply, Enable, Run, Delete, Revoke, Disable, Stop |
| | Script | Create, Edit, Clone, Delete, Cancel running | View, Clone, Cancel running | Run, Clone, Cancel running |
| **Read-only administrator** | Scripting plan | View | View | View |
| | Script | View | View | View |
