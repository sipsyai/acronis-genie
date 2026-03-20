---
title: "Workflow Components and Templates"
section: "Managing and assigning automation workflows"
subsection: "Workflow triggers, actions, and templates"
page_range: "1122-1124"
tags: [workflow-triggers, workflow-actions, workflow-templates, EDR, alerts, devices, tenants, users, notifications, automation]
acronis_version: "26.02"
---

# Workflow Components and Templates

This topic outlines the supported components that partner tenants can use to initiate workflows and define corresponding response actions or operations within the system. The table at the end lists the available workflow templates that you can use as examples when creating your own workflows.

## Workflow Triggers

The following triggers can be used to automate the execution of workflows:

| Category | Trigger Name | Description |
|---|---|---|
| **EDR** | EDR incident created | Triggered automatically when a new incident is created in the system. |
| | EDR incident updated | Triggered whenever an existing incident is updated. |
| **Devices** | Device registered | Triggered when a new device is successfully registered. |
| **Alert** | Alert created | Triggered when any monitored service or system component generates a new alert. |
| **Tenants** | Tenant created | Triggered when a new tenant is created. |
| | Tenant enabled | Triggered when a disabled tenant is re-enabled. |
| **Users** | User created | Triggered when a new user is created for the tenant. |
| | User deleted | Triggered when a user is deleted. |
| | User disabled | Triggered when a user is disabled. |
| | User enabled | Triggered when a disabled user is re-enabled. |

## Workflow Actions

The following action components can be included in workflows to automate the execution of their corresponding actions:

### EDR Actions

| Action Name | Description |
|---|---|
| Assign incident | Assigns the EDR incident to a specified user. |
| Change state | Updates the state of the EDR incident. |
| Quarantine | Quarantines the detected file or object. |
| Stop process | Terminates a specified process on the workload. |
| Add comment | Adds a comment to an EDR incident. |
| Isolate device | Isolates the workload from the network. |

### Devices Actions

| Action Name | Description |
|---|---|
| Apply protection plan | Applies a protection plan to the workload (taken from the existing list). |
| Revoke protection plan | Revokes the applied protection plan from the workload. |
| Get backup status | Retrieves the current backup status of the workload. |
| Run patch management | Initiates the patch management process on the device. |
| Run script | Executes a script on the device (taken from the existing list). |
| Get security status | Retrieves the current security status of the workload. |
| Run backup | Starts a backup task on the selected device. |
| Get patch management status | Retrieves the patch management status of the device. |
| Run vulnerability assessment | Runs a vulnerability assessment on the device. |
| Run malware scan | Executes a malware scan on the device. |

### Alert Actions

| Action Name | Description |
|---|---|
| Get tenant from alert | Retrieves the tenant associated with the alert. |
| Get workload from alert | Retrieves the workload associated with the alert. |
| Dismiss alert | Dismisses the alert. |

### Notifications Actions

| Action Name | Description |
|---|---|
| Send email to tenant admins | Sends an email notification to tenant administrators. |

### Users Actions

| Action Name | Description |
|---|---|
| Create user | Creates a new user under the specified tenant. |
| Configure notifications | Configures user notification settings. |
| Manage user roles | Assigns or modifies user roles and permissions. |

### General Actions

| Action Name | Description |
|---|---|
| Wait | Delays workflow execution for a specified duration. |

## Workflow Templates

The following workflow templates can be used as predefined examples for automation:

| Template Name | Category |
|---|---|
| Client Backup Routine Workflow | Alert |
| Blocked URL Alert Handler | Alert |
| Server Backup Failure Workflow | Alert |
| Quarantine Threat Workflow | EDR |
| Isolate Workload Workflow | EDR |
| Malware incident requiring attention | EDR |
| Incident requiring attention | EDR |
| Automatic assignment of incident | EDR |
