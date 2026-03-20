---
title: "DLP Events, Dashboard Widgets, and Custom Sensitivity Categories"
section: "Data Loss Prevention"
subsection: "DLP Events and Monitoring"
page_range: "1471-1474"
tags: [dlp, events, dashboard, widgets, monitoring, custom-sensitivity, data-classifiers, audit-log]
acronis_version: "26.02"
---

# DLP Events, Dashboard Widgets, and Custom Sensitivity Categories

## Data Loss Prevention Events

Data Loss Prevention generates events in the DLP events view as follows:

- During observation mode, events are generated for all justified data transfers.
- During enforcement mode, events are generated based on the **Write in log** action configured for each policy rule that is triggered.

### Viewing Events for a Rule in the Data Flow Policy

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data flow policy**.
3. Locate the rule for which you want to view the events and click the ellipsis at the end of the rule line.
4. Select **View events**.

### Viewing Event Details in the DLP Events View

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **DLP events**.
3. Click an event in the list to view more details about it. The Event details pane expands to the right.
4. Scroll down and up in the Event details pane to view the available information. The details that are displayed depend on the type of rule and rule settings that triggered the event.

### Filtering Events in the DLP Events List

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **DLP events**.
3. In the upper left, click **Filter**.
4. Select sensitivity category, workload, action type, user, and channel from the drop-down menus. You can select more than one item in the drop-down menus. Filtering applies the logical operator OR between items in the same menu, but the logical operator AND is used between items from different menus. For example, if you select **PHI** and **PII** sensitivity category, the result will return all events that contain PHI or PII, or both. If you select sensitivity category **PHI** and action **Write access**, only events that match both categories will appear.
5. Click **Apply**.
6. To view all events again, click **Filter**, then **Reset to default**, and finally click **Apply**.

### Searching for Events in the DLP Events List

1. Navigate to **Protection** > **DLP events**.
2. From the drop-down list to the right of Filter, select a category in which you want to search: **Sender**, **Destination**, **Process**, **Message subject**, or **Reason**.
3. In the text box, enter the phrase you are interested in and confirm by pressing Enter on the keyboard. Only events matching the phrase you entered appear in the list.
4. To reset the list of events, click the **X** sign in the search text box and press Enter.

### Viewing Events Related to Specific Rules in the Data Flow Policy

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data flow policy**.
3. Select the check box in front of the name of the policy rule you are interested in. You can select multiple policy rules if needed.
4. Click **View events**. The view switches to **Protection** > **DLP events** and the events that are related to the policy rules that you selected appear in the list.

## Data Loss Prevention Widgets on the Overview Dashboard

The **Overview** dashboard provides a number of customizable widgets that give an overview of operations related to the Cyber Protection service, including Data Loss Prevention. You can find the following DLP widgets on the **Overview** dashboard under **Monitoring**:

- **Sensitive data transfers** -- Shows a total number of sensitive data transfer operations to internal and external recipients. The chart is divided by the type of permission: allowed, justified or blocked. Customizable by time range (1 day, 7 days, 30 days, or this month).

- **Outbound sensitive data categories** -- Shows a total number of sensitive data transfers to external recipients. The chart is divided by sensitive categories: PHI, PII, PCI DSS, and Marked as Confidential (Confidential).

- **Top senders of outbound sensitive data** -- Shows a total number of sensitive data transfers from the organization to external recipients and a list of the top five users with the largest number of transfers (along with these numbers). This statistic includes both allowed and justified transfers. Customizable by time range.

- **Top senders of blocked sensitive data transfers** -- Shows a total number of blocked sensitive data transfers and a list of the top five users with the largest number of attempted transfers (along with these numbers). Customizable by time range.

- **Recent DLP events** -- Shows details of recent Data Loss Prevention events for the selected time range. You can customize this widget using the following options:
  - **Range (date posted)** (1 day, 7 days, 30 days, or this month)
  - Name of the **workload**
  - **Operation status** (allowed, justified, or blocked)
  - **Sensitivity** (PHI, PII, Confidential, PCI DSS)
  - **Destination type** (external, internal)
  - **Grouping** (workload, user, channel, destination type)

The widgets are updated every five minutes. The widgets have clickable elements that enable you to investigate and troubleshoot issues. You can download the current state of the dashboard or send it via email in the .pdf or/and .xlsx format.

## Custom Sensitivity Categories

Custom sensitive data categories may help an organization to protect intellectual property and confidential data specific for that organization by expanding the DLP built-in catalog of regulatory-related content definitions for compliance.

### To Create a Custom Sensitive Category

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection** > **Data Loss Prevention** > **Data classifiers**.
3. Select **Sensitivity category**. The list of sensitivity categories is displayed.
4. Click **Add new** in the upper-right corner of the window.
5. In the window that opens, enter a name for the new sensitivity category and click **Create**. By default, newly-created or cloned categories are disabled. You can enable them once you configure all their parameters.
6. In the dropdown list to the right of the row, click **Edit**.
7. In the **Edit sensitivity** dialog, click **Add line** to expand the list of content detectors.
8. Select the content detectors to add:
   - To add existing content detectors, select the checkboxes next to their names, and then click **Add** in the lower-right corner.
   - To define a new content detector, click **Add new**, and configure the detector you need. Instead of starting from scratch, you can clone an existing content detector and edit it.
9. Verify that you added all content detectors that you need, and click **Done** in the lower-right corner.
10. Enable your custom sensitivity category.

Instead of creating a new sensitivity category from scratch, you can also clone one (either built-in or custom sensitivity) and adjust its parameters:

1. To clone an existing sensitivity, select **Clone** from the dropdown list at the end of its row.
2. Edit the cloned category to add or remove content detectors as needed, and click **Done** to save your changes.

> **Note:** Cloning a built-in sensitivity category inside one tenant creates a new sensitivity that contains the same detectors which become Custom once copied.
