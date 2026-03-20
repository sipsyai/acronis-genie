---
title: "Wiping data, RMM integrations, CyberApp workloads, and linking workloads"
section: "Managing workloads in the Cyber Protect console"
subsection: "Workload management operations"
page_range: "451-456"
tags: [remote wipe, RMM, CyberApp, aggregated workloads, linking users, last logged-in user]
acronis_version: "26.02"
---

# Wiping data from a managed workload

> **Note:** Remote wipe is available with the Advanced Security pack.

Remote wipe allows a Cyber Protection administrator and a machine owner to delete the data on a managed machine -- for example, if it gets lost or stolen. Thus, any unauthorized access to sensitive information will be prevented.

Remote wipe is only available for machines running Windows versions 10 and later. By default, the `doWipeProtected` function is used. If it is not available, the `doWipe` function is used.

To receive the wipe command, the machine must be turned on and connected to the Internet.

## To wipe data from a machine

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the machine whose data you want to wipe.

   > **Note:** You can wipe data from one machine at a time.

3. Click **Details**, and then click **Wipe data**. If the machine that you selected is offline, the **Wipe data** option is inaccessible.
4. Confirm your choice.
5. Enter the credentials of this machine's local administrator, and then click **Wipe data**.

> **Note:** You can check the details about the wiping process and who started it in **Monitoring** > **Activities**.

# Viewing workloads managed by RMM integrations

> **Note:** This feature is only available if the PSA service is enabled.

When you integrate an RMM platform as part of the PSA service, you can view and monitor information from devices that are managed by the RMM platform. This information is available in the Cyber Protect console, by navigating to **Devices**.

## To view workloads managed by RMM integrations

1. Go to **Devices** > **All devices**.
2. Sort the **RMM integration** column to locate the relevant integrations.
3. Select the relevant workload.
4. In the **Actions** pane, select **Details**.
5. In the displayed pane, one of three options is displayed, according to your configured workload:
   - **Acronis services only:** If the workload is configured to work only with Acronis services, no RMM integration information is displayed.
   - **Both Acronis and RMM:** The Acronis services and RMM integration details are located in two tabs, **Overview** and **RMM integration**. Click **RMM integration** to view the integration details, including the workload name and type (provided by the RMM platform), description and location. In addition, any installed and enabled RMM agent add-ons are also shown.
   - **RMM only:** The RMM integration details are displayed, including the workload name and type (provided by the RMM platform), description and location. In addition, any installed and enabled RMM agent add-ons are also shown.

> **Note:** When the workload is configured with RMM integration (either in tandem with Acronis services or with an RMM integration only), you can:
> - Initiate a remote connection (available for Datto RMM, N-able N-central, N-able RMM integrations).
> - Review installed add-ons on the third party RMM device (available for N-able RMM only).
> - Directly access the third party RMM device's details (available for Datto RMM, N-able N-central, NinjaOne).

# CyberApp workloads

CyberApp workloads are created by ISVs (Independent software vendors) and appear in the Cyber Protect console after you enable a CyberApp integration. The following conditions must be met:

- The **Workloads and actions** extension point must be enabled in the CyberApp.
- At least one **Workload type** must be defined in the CyberApp.
- The connector service hosted by the ISV must ensure that the CyberApp workloads are added and updated to the Acronis platform.

## Aggregated workloads

A physical workload may have Cyber Protect agent and one or several CyberApp agents installed at the same time. In this case, the same workload will have more than one representation on the **All Devices** screen -- a separate record will be shown for the Acronis workload, and for each CyberApp workload. If the automatic merging of workloads is enabled and configured from Vendor Portal or from the Cyber Protect console, the system will compare the host addresses and the MAC addresses of the Acronis workloads and the CyberApp workloads, and will merge all representations into a single aggregated workload. You can also manually merge and unmerge workloads in the Cyber Protect console.

## Working with CyberApp workloads

### Merge

**Prerequisites:** Workloads from different sources are available for the tenant.

1. In the **All devices** screen, select the workloads that you want to merge.

   > **Note:** The merge action is displayed if you select workloads from different sources, such as an Acronis workload and a CyberApp workload.

2. Click **Merge workloads**.

### Perform custom actions

**Prerequisites:** A CyberApp integration that has **Workload actions** defined is enabled for the tenant.

1. In the **All devices** screen, click the workload.
2. Click **Integrated App actions**.
3. Click the action.

### Working with aggregated workloads

- **View details:** Click the aggregated workload, then click **Details**. The details are separated into tabs, each tab showing the details for each workload representation.
- **Unmerge:** Click the aggregated workload, click **Unmerge source workloads**, then confirm. You will see a separate entry for each source workload.
- **Perform custom actions:** Click the workload, click **Integrated App actions**, and depending on the number of CyberApp workloads, click the action directly or first select the CyberApp.

# Linking workloads to specific users

> **Note:** This feature is only available if the PSA service is enabled.

By linking a workload to a specific user, you can automatically link the workload to new service desk tickets created by or assigned to the user.

## To link a workload to a user

1. Go to **Devices** > **All devices**, and then select the relevant workload.
2. In the **Actions** pane, select **Link to a user**.
3. Select the relevant user. You can also change the selected user for existing linked workloads.
4. Click **Done**. The selected user is now displayed in the **Linked user** column.

## To unlink a workload from a user

1. Go to **Devices** > **All devices**, and then select the relevant workload.
2. In the **Actions** pane, select **Link to a user**.
3. Click **Unlink user**.
4. Click **Done**.

# Viewing the last logged-in user

If you enable the **Show last logged-in** setting in the remote management plan that is applied to a workload, the system will record information about the users who log in to the device. You can view this information in the Dashboard or in the workload's details.

## To view the user who last logged in to a device

1. Click **Devices**. The **All devices** screen opens. In the **Last login** column, you can see the name of the user who logged in last on each device. In the **Last login time** column, check the time when the user logged in last on each device.
2. Click a device for which you want to check the details.
3. Click the **Details** icon.
4. In the **Last users logged in** section, check the name of the user who logged in to the device last and the date and time of the last login.

> **Note:** The system lists up to 5 different users who logged in to the device last.
