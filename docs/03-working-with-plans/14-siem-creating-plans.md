---
title: "Creating SIEM forwarding plans"
section: "Working with plans"
subsection: "SIEM forwarding plans"
page_range: "267-271"
tags: [SIEM, forwarding plan, multiple customers, individual customer, create, rename, edit, delete]
acronis_version: "26.02"
---

# Creating a SIEM forwarding plan for multiple customers

To save time, you can create a single, generic SIEM forwarding plan and apply it for multiple customers. When you do this, you must choose an Acronis protected device for each participating customer to act as the writing device and data store.

## To create a generic SIEM forwarding plan for multiple customers

1. Open your partner SIEM forwarding plan list.
2. Click **Create**.
3. [Optional] Change the plan default name.
   a. Click the pencil icon.
   b. Edit the name.
   c. Click the check mark to accept the changes.
4. Select **Method** for the SIEM forwarding plan:
   - **Files** -- This method can use a Windows or a Linux device as the writer device.
   - **Syslog server** -- This method can only use a Linux device as the writer device.
5. **Files method:**
   a. Click the **Customer** field. A list of all your customers appears. Each customer has a corresponding dropdown list of all their Windows and Linux protected devices. To appear in the dropdown list, a device must have the Acronis agent installed and must be online.
   b. From the dropdown lists, select a writer device for each customer that you want to use the new SIEM forwarding plan.
   > **Important:** The writer device must remain online at all times for the SIEM forwarding plan to function correctly.

   Customers for which you do not specify a writer device will not use the new SIEM forwarding plan.
   c. Click **Done**.
   d. [Optional] Click **Specify** to change the default **File path** values for the SIEM data stores on the writer devices, and then click **Done**.
   > **Important:** If the specified directory is removed from any of the SIEM forwarding devices, then SIEM forwarding stops until you either restore the removed directory or modify **File path** to a valid directory.

   **Syslog server method:**
   a. Click the **Customer** field. A list of all your customers appears. Each customer has a corresponding dropdown list of all their Linux protected devices. To appear in the dropdown list, a device must have the Acronis agent installed and must be online.
   b. From the dropdown lists, select a writer device for each customer that you want to use the new SIEM forwarding plan.
   > **Important:** The writer device must remain online at all times for the SIEM forwarding plan to function correctly.

   Customers for which you do not specify a writer device will not use the new SIEM forwarding plan.
   c. Click **Done**.
6. [Optional] Change the **File format**.
   - **CEF** (default) -- Vendor-neutral, standardized format, designed for security events and detailed event analysis.
   - **JSON** -- Highly flexible format, that allows custom, complex data. Best for modern log management platforms.
7. [Optional] Select the Acronis data types to include in the SIEM forwarding plan. By default, all available Acronis data types are included.
   a. Click on the **Data** field.
   b. Clear the checkboxes of the Acronis data types you do not want to include in the SIEM forwarding plan. The Acronis data types are:
      - **Alerts** -- Updates of critical or error messages that require a rapid response.
      - **Events** -- Event log data with insights into system performance and user interactions.
      - **Activities** -- All success, informational, warning, critical, and error messages (e.g., DLP, URL filtering, backups).
      - **Audit log** -- Internal security-relevant events that may impact the safety and integrity of the organization.
      > **Note:** Audit log data can be stored for HIPAA compliance purposes if you use the **Files** method.
   c. Click **Done**.
8. When finished, click **Create**.

# Creating a SIEM plan for an individual customer

## To create a plan for an individual customer

1. Open the Acronis Protection console for the customer.
2. Select **Management** from the main menu.
3. Select **SIEM forwarding plans**.
4. Click **Create**.
5. [Optional] Change the plan default name.
   a. Click the pencil icon.
   b. Edit the name.
   c. Click the check mark to accept the changes.
6. Select **Method** for the SIEM forwarding plan:
   - **Files** -- This method can use a Windows or a Linux device as the writer device.
   - **Syslog server** -- This method can only use a Linux device as the writer device.
7. **Files method:**
   a. Click **Specify** to select the **Writer device** from the list of available protected Windows and Linux devices, and then click **Done**.
   > **Important:** The SIEM forwarding device must remain online at all times for the SIEM forwarding plan to function correctly.
   b. [Optional] Click **Specify** to change the default **File path** for the SIEM data store on the writer device, and then click **Done**.
   > **Important:** If the specified directory is removed, SIEM forwarding stops until you either restore the removed directory or modify **File path** to a valid directory.

   **Syslog server method:**
   a. Click **Specify** to select the **Writer device** from the list of available, protected Linux devices, and then click **Done**.
   > **Important:** The writer device must remain online at all times for the SIEM forwarding plan to function correctly.
   b. Click **Done**.
8. [Optional] Change the **File format**.
   - **CEF** (default) -- Vendor-neutral, standardized format, designed for security events and detailed event analysis.
   - **JSON** -- Highly flexible format, that allows custom, complex data. Best for modern log management platforms.
9. [Optional] Select the Acronis data types to include in the SIEM forwarding plan. By default, all available Acronis data types are included.
   a. Click on the **Data** field.
   b. Clear the checkboxes of the Acronis data types you do not want to include. The Acronis data types are:
      - **Alerts** -- Updates of critical or error messages that require a rapid response.
      - **Events** -- Event log data with insights into system performance and user interactions.
      - **Activities** -- All success, informational, warning, critical, and error messages (e.g., DLP, URL filtering, backups).
      - **Audit log** -- Internal security-relevant events that may impact the safety and integrity of the organization.
      > **Note:** Audit log data can be stored for HIPAA compliance purposes.
   c. Click **Done**.
10. Click **Create**.

# Renaming a SIEM forwarding plan

1. Open your partner SIEM forwarding plan list or the customer-specific list.
2. Click on the plan you want to rename. The details and actions sidebar opens.
3. Click **Rename**.
4. Edit the plan name.
5. Click **Rename**.

# Editing a SIEM forwarding plan

> **Note:** You cannot change the **Method**. To change it, you must delete the SIEM forwarding plan and create a new one.

1. Open your partner SIEM forwarding plan list or the customer-specific list.
2. Click on the plan you want to edit. The details and actions sidebar opens.
3. Click **Edit**.
4. Make your changes and click **Confirm**.

# Deleting a SIEM forwarding plan

> **Note:** When you delete a SIEM forwarding plan, data forwarding ceases, but the data which has already been forwarded is not deleted.

1. Open your partner SIEM forwarding plan list or the customer-specific list.
2. Click on the plan you want to delete. The details and actions sidebar opens.
3. Click **Delete**.
4. Select the confirmation checkbox to enable the **Confirm** button.
5. Click **Confirm**.
