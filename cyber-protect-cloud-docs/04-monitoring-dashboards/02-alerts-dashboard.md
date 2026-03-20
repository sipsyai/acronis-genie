---
title: "The Alerts dashboard"
section: "Understanding your current level of protection"
subsection: "Monitoring"
page_range: "290-294"
tags: ["alerts", "dashboard", "filtering", "sorting", "service-desk", "ticket", "customization"]
acronis_version: "26.02"
---

# The Alerts dashboard

The **Monitoring** > **Alerts** dashboard displays the current alerts for the tenants that you manage. The alerts are shown for all customer tenants or a specific customer tenant, according to the selected level in the drop-down list in the navigation menu.

The drop-down list is not available if you manage only one tenant.

Each alert contains general information about its cause or troubleshooting advice. For further assistance in resolving the underlying issue, click **Get support** under each alert. Depending on your role and the services that are enabled in your tenant, you can search for solution in the knowledge base or submit a support ticket.

## Customizing the Alerts dashboard

The **Alerts** dashboard supports simple view and table view. The simple view shows a scrollable list of the current alerts, while the table view shows more alerts on one screen and additional information about these alerts.

### Switch between views

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. To switch to table view, click the table view icon.
3. To switch to simple view, click the simple view icon.

### Add or remove columns

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. [If you use the simple view] Click the table view icon.
3. Click the gear icon in the upper-right corner, and then select the columns that you want to be visible.

The following columns are available:

| Column | Description |
|--------|-------------|
| **Severity** (always available) | Importance level of the alert. Severity can be: Critical, Error, Warning, Informational. |
| **Alert type** | Alert summary. See "Alert types and categories" (p. 295). |
| **Message** (always available) | Alert details. |
| **Monitoring type** | Monitoring type — threshold-based or anomaly-based. |
| **Workload** | Workload for which the alert is generated. |
| **Date and time** | Timestamp of the alert. |
| **Plan** | Plan related to the alert (if applicable). |
| **Alert category** | Alert group by functional area. |
| **Source** | Origin of the alert — System or an integration app. |

> **Note:** If multiple columns are selected, you might need to scroll the screen horizontally to view all available information.

### Hide quick filter

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. Click the icon on top of the quick filter section.

## Filtering alerts

You can use the quick filter or the main filter.

### Quick filter

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. In the **View** drop-down list, select the filtering criteria.
3. [Optional] [If you selected **Alert category**] Select a specific alert category.
4. [Optional] Select a specific alert type.

### Main filter

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. Click **Filter**.
3. Configure the filter criteria, and then click **Apply**.

> **Note:** The available filter criteria depend on the quick filter settings that you might already have configured.

## Sorting alerts

When using the table view, you can sort the alerts in descending or ascending order.

1. In the Cyber Protect console, go to **Monitoring** > **Alerts**.
2. [If you use simple view] Click the table view icon.
3. Click the name of the column in which you want to sort the alerts.

> **Note:** You cannot sort the alerts by clicking the **Message** column.

## Creating a service desk ticket from an alert

If the PSA service is enabled for your account, you can create a new service desk ticket directly from the alert.

### To create a service desk ticket

1. In the relevant alert, click **Create a new ticket**. Alternatively, when working in the table view mode, select an alert, and then select **Create a new ticket** in the right pane.
2. Define the following:
   - In the header section, select the **Billable** check box if you want the time recorded on the ticket to be billed to the customer. In addition, select the **Email the customer** check box if you want to send ticket updates to the customer.
   - In the **General information** section, define a ticket title. This field is pre-filled with an alert summary but can be edited.
   - In the **Customer information** section, the fields are pre-filled with the relevant information from the alert.
   - In the **Configuration item or service** section, the fields are pre-filled with the device linked to the alert. You can reassign a device, as required.
   - In the **Support agent** section, the fields are pre-filled with the default support agent, category, and support group. You can reassign a different agent, as required.
   - In the **Ticket update** section, the fields are pre-filled with the alert description and details. The **Status** field is set as **New** by default, and can be changed.
   - In the **Attachments**, **Billable items**, and **Internal notes** sections, add the relevant items as required.
3. Click **Done**.

When the ticket is created, a link to the ticket is added to the alert. If an alert is closed, the related ticket is also automatically closed.

> **Note:** You can only create one ticket per alert.
