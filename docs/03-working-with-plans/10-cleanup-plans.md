---
title: "Cleanup plans"
section: "Working with plans"
subsection: "Cleanup"
page_range: "251-252"
tags: [cleanup, retention, backup management, off-host data processing]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#cleanup.html"
---

# Cleanup plans

Cleanup is an operation that deletes outdated backups according to the retention rules. This operation is only applicable to agents and workloads, and not cloud to cloud backups (which can only be manually deleted).

> **Note:** In service-based billing mode, this feature requires the **Servers** quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

## Supported locations

Cleanup plans support all backup locations, except for NFS folders and Secure Zone.

## Creating a cleanup plan

1. In the Cyber Protect console, click **Management** > **Cleanup**.
2. Click **Create plan**.
3. In **Agent**, select the agent that will perform the cleanup. You can select any agent that has access to the backup location.
4. In **Items to clean up**, select the archives or backup locations to clean up.
   - To switch between archives and locations, use the **Locations / Backups** switch in the upper-right corner.
   - If you select multiple encrypted archives, their encryption password must be the same. For archives that use different encryption passwords, create separate plans.
5. In **Schedule**, configure the cleanup schedule.
6. In **Retention rules**, specify the retention rules. The following options are available:
   - **By number of backups**
   - **By backup age** (separate settings for monthly, weekly, daily, and hourly backups)
   - **By total size of backups**
7. [If you selected encrypted archives in **Items to replicate**] Enable the **Backup password** switch, and then provide the encryption password.
8. [Optional] To modify the plan options, click the gear icon, and then configure the options as required.
9. Click **Create**.
