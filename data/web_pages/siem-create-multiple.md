# Creating a SIEM forwarding plan for multiple customers

Working with plans > SIEM forwarding plans > Creating a SIEM forwarding plan for multiple customers
Creating a SIEM forwarding plan for multiple customers

To save time, you can create a single, generic SIEM forwarding plan and apply it for multiple customers. When you do this, you must choose an Acronis protected device for each participating customer to act as the writing device and data store.

To create a generic SIEM forwarding plan for multiple customers

Open your partner SIEM forwarding plan list.

Click Create.

Change the plan default name.

Click the pencil icon.

Edit the name.

Click the check mark to accept the changes.

Select Method for the SIEM forwarding plan:

Files

This method can use a Windows or a Linux device as the writer device.

Syslog server

This method can only use a Linux device as the writer device.

For more information, see SIEM forwarding plan methods.

Files method
Syslog server method

Click the Customer field.

A list of all your customers appears. Each customer has a corresponding dropdown list of all their Windows and Linux protected devices.

To appear in the dropdown list, a device must have the Acronis agent installed and must be online.

From the dropdown lists, select a writer device for each customer that you want to use the new SIEM forwarding plan.


The writer device must remain online at all times for the SIEM forwarding plan to function correctly.

Customers for which you do not specify a writer device will not use the new SIEM forwarding plan.

Click Done.

Click Specify to change the default File path values for the SIEM data stores on the writer devices, and then click Done.

If the specified directory is removed from any of the SIEM forwarding devices, then SIEM forwarding stops until you either restore the removed directory or modify File path to a valid directory.

Change the File format.

CEF (default)

Vendor-neutral, standardized format, designed for security events and detailed event analysis.

JSON

Highly flexible format, that allows custom, complex data. Best for modern log management platforms.

For more information, see SIEM data format and examples.

Select the Acronis data types to include in the SIEM forwarding plan.

By default, all available Acronis data types are included.

Click on the Data field.

Clear the checkboxes of the Acronis data types you do not want to include in the SIEM forwarding plan. The Acronis data types are:

Alerts

Updates of critical or error messages that require a rapid response.

Events

Event log data with insights into system performance and user interactions.

Activities

All success, informational, warning, critical, and error messages (e.g., DLP, URL filtering, backups).

Audit log

Internal security-relevant events that may impact the safety and integrity of the organization.

Audit log data can be stored for HIPAA compliance purposes if you use the Files method.

Click Done.

When finished, click Create.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.