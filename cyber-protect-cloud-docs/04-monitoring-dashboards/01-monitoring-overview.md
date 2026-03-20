---
title: "Monitoring - Overview and Activities dashboards"
section: "Understanding your current level of protection"
subsection: "Monitoring"
page_range: "288-290"
tags: ["monitoring", "dashboard", "overview", "activities", "widgets", "customization"]
acronis_version: "26.02"
---

# Monitoring

The **Monitoring** tab provides important information about your current level of protection, and includes the following dashboards:

- **Overview**
- **Activities**
- **Alerts**
- **Threat feed** (for more information, see "Threat feed" (p. 348))

## The Overview dashboard

The **Overview** dashboard provides a number of customizable widgets that give an overview of operations related to the Cyber Protection service. Widgets for other services will be available in future releases.

The widgets are updated every five minutes. The widgets have clickable elements that enable you to investigate and troubleshoot issues. You can download the current state of the dashboard or send it via email in the .pdf or/and .xlsx format.

You can choose from a variety of widgets, presented as tables, pie charts, bar charts, lists, and tree maps. You can add multiple widgets of the same type with different filters.

The buttons **Download** and **Send** in **Monitoring** > **Overview** are not available in the Standard editions of the Cyber Protection service.

> **Important:** The values of storage usage displayed in the product UI are in binary byte units — mebibytes (MiB), gibibytes (GiB), and tebibytes (TiB) — even though the labels show MB, GB, and TB respectively.

### To rearrange the widgets on the dashboard

Drag and drop the widgets by clicking on their names.

### To edit a widget

Click the pencil icon next to the widget name. Editing a widget enables you to rename it, change the time range, set filters, and group rows.

### To add a widget

Click **Add widget**, and then do one of the following:

- Click the widget that you want to add. The widget will be added with the default settings.
- To edit the widget before adding it, click Customize when the widget is selected. After editing the widget, click **Done**.

### To remove a widget

Click the X sign next to the widget name.

---

## The Activities dashboard

The **Activities** dashboard provides an overview of the current and past activities on protected workloads. The retention period is 90 days. This period might be shorter if the number of activities is too large or due to data center maintenance.

Dates and times are shown according to the time zone settings of the machine that you use to access the Cyber Protect console.

To customize the view of the **Activities** dashboard, click the gear icon, and then select the columns that you want to see.

To see the activity progress in real time, select the **Refresh automatically** check box. However, frequent updating of multiple activities degrades the performance of the management server.

### Searching activities

You can search the listed activities by the following criteria:

- **Device name** — This is the machine on which the activity is carried out.
- **Started by** — This is the account who started the activity.

### Filtering activities

You can also filter the activities by the following properties:

- **Status** — For example, succeeded, failed, in progress, canceled.
- **Type** — For example, applying plan, deleting backups, installing software updates.
- **Time** — For example, the most recent activities, the activities from the past 24 hours, or the activities during a specific period within the default retention period.

To see more details about an activity, select this activity from the list, and then, in the **Activity details** panel, click **All properties**.
