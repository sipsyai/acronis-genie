---
title: "Backup scanning plans and cloud application backups"
section: "Working with plans"
subsection: "Backup scanning and cloud applications"
page_range: "260-261"
tags: [backup scanning, malware, ransomware, cloud applications, Microsoft 365, Google Workspace, collaboration apps]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#backup-scanning-plans.html"
---

# Backup scanning plans

To scan backups for malware (including ransomware), create a backup scanning plan.

> **Important:** Backup scanning plans are not supported for all workloads and backup storages. For more details, see "Limitations" (p. 1111).

## Creating a backup scanning plan

1. In the Cyber Protect console, go to **Management** > **Backup scanning**.
2. In the **Actions** pane, click **Create plan**.
3. [Optional] Change the default plan name.
4. In **Backups to scan**, click **Specify**.
   a. [Optional] To add a new location, click **Add**, select the location, and then click **Done**.
   b. Click **Locations** or **Backups** to select the scope for the plan.
   c. Select entire location or individual archives in a location. You can select one or more items.
   d. Click **Done**.
5. [If the selected archives are encrypted] In **Encryption**, enable the toggle, and then enter the encryption password. The password you specified will be used for the scanning of all backups in the plan, so all selected archives must use the same encryption password. For archives that use different encryption passwords, create separate plans.
6. Click **Create**.

As a result, a backup scanning plan is created. The cloud agent will automatically scan the selected archives once an hour. You cannot change the plan schedule or the period between two consecutive scans.

# Backup plans for cloud applications

The **Management** > **Cloud applications backup** tab shows cloud-to-cloud backup plans. These plans back up applications running in the cloud by means of agents that run in the cloud and use the cloud storage as a backup location.

In this section, you can perform the following operations:
- Create, view, run, stop, edit, and delete a backup plan
- View activities related to each backup plan
- View alerts related to each backup plan

For more information about cloud applications backup, refer to:
- Protecting Microsoft 365 data
- Protecting Google Workspace data

## Running cloud-to-cloud backups manually

To prevent disrupting the Cyber Protection service, the number of manual cloud-to-cloud backup runs is limited to 10 runs per Microsoft 365 or Google Workspace organization during an hour. After this number has been reached, the number of runs allowed is reset to one per hour, and then an additional run becomes available each hour thereafter (e.g. hour 1, 10 runs; hour 2, 1 run; hour 3, 2 runs) until a total of 10 runs per hour is reached.

Backup plans applied to groups of devices (mailboxes, drives, sites) or containing more than 10 devices cannot be run manually.

# Protection of collaboration and communication applications

Zoom, Cisco Webex Meetings, Citrix Workspace, and Microsoft Teams are now widely used for video/web conferencing and communications. The Cyber Protection service allows you to protect your collaboration tools.

> **Note:** The availability of this feature depends on the service quotas that are enabled for your account.

The protection configuration for Zoom, Cisco Webex Meetings, Citrix Workspace, and Microsoft Teams is similar. The example below covers the configuration for Zoom.

## Setting up Zoom protection

1. Install the protection agent on the machine where the collaboration application is installed.
2. Log in to the Cyber Protect console and apply a protection plan that has one of the following modules enabled:
   - **Antivirus and Antimalware protection** (with the **Self-Protection** and **Active Protection** settings enabled) -- if you have one of the Cyber Protect editions.
   - **Active Protection** (with the **Self-Protection** setting enabled) -- if you have one of the Cyber Backup editions.
3. [Optional] For automatic update installation, configure the **Patch management** module in the protection plan.

As a result, your Zoom application will be under protection that includes the following activities:
- Installing Zoom client updates automatically
- Protecting Zoom processes from code injections
- Preventing suspicious operations by Zoom processes
- Protecting the "hosts" file from adding the domains related to Zoom
