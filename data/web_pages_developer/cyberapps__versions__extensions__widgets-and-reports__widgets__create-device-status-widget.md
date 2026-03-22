---
title: "Creating a device status widget"
source: "https://developer.acronis.com/doc/cyberapps/versions/extensions/widgets-and-reports/widgets/create-device-status-widget.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:03:17.753303"
---

# Creating a device status widget

Creating a device status widget

To create a device status widget, the CyberApp must have at least one workload type with at least one attribute which defines a workload status. The attribute presentation must also be defined.
The following example is a device status widget for the workload type example provided at the end of the Creating a workload type section.


To create a device status widget

Open the Version.
Select Widgets and reports from the menu.
[If required] Click Enable to enable the extension point.
Click .
Select Device status in the Widget type dropdown.
Change the default Widget name.
[Optional] Change the widget CTI Identifier.

Note
For more information on CTI codes, see CTI.


Select a category from the Category dropdown.
Select a workload type from the Source (Workload type) dropdown.
Select an attribute from the Attribute dropdown.

Note

Not all attributes are available. To appear in the dropdown, attributes must be listed in the workload type’s attributes presentation list and be enum.
For more information, see steps 8 and 9 of Creating a workload type.



Select or clear the Display checkboxes to specify where the widget will be displayed by default.

Overview Dashboard (Management console)
Overview Dashboard (Protection console)


Note
By default, both are selected.


Click  to add a Legend entry for your widget.

Select an attribute value from the dropdown.
Select a color for the value from the color dropdown.
Repeat for all legend entries.


Click Save changes.



Example