---
title: "New tab UI element"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/layout-management/tabs-container.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:05.889566"
---

# New tab UI element

Tabs container

This element appears as a tab folder containing multiple forms.
Tabs containers let the user tab between forms.
The forms included in a tabs container act as separate entities, with no data connection between them.

See examples

Properties



ID
Element identifier.


Width (see examples)


Default
This is for backward compatibility purposes only.



Fit
Sets the width of the tab container according to the width of the largest form assigned to a tab. See the Tabs section, described below.



Fill
Uses all of the available width.
For more information, see Element distribution.





Title
Text displayed in the upper-left corner of the tabs container.
The text is converted to all ALL CAPS and is displayed in bold.



Direction (see examples)
The tabs can be displayed in Horizontal or Vertical mode.



Tabs
In this section, you define the tabs to include in the tabs container.
For more information, see Populating a tab container.






Populating a tab container

To populate a tab container

Click .

From the Form name dropdown, select a form.
You can select any form in the form group with the exception of the root form.


[Optional] Enter a Title for the tab. If you do not supply a title, the form name is used.
[Optional] Select an icon from the Icon name dropdown. The icon is displayed to the left of the title.
[Optional] Select a color for the icon from the Icon color dropdown.

Note
This option is only available if you selected a monochrome icon on the previous step.


Repeat steps 1 to 5 for each form you want to include in the tabs container.
[Optional] Click the  and  to reorder the tab list.
[Optional] Click  to delete a tab.



Example

Note
The following example was created prior to the Width property being introduced.





Examples

Width examples
In these examples, Tab 1 and Tab 2 both contain forms with elements which have Width properties of Fit. Therefore, when the tab container Width property is also set to Fit, the tab container is sized to accomodate the widest of the two forms. In this case, the width required to accomodate the tab container elements (the title and the 2 tabs) is more than that of either form.



Direction examples
In these examples, the tab containers are identical appart from the Direction property.
The tab containers are Width: Fit and both tabs 1 and 2 contain forms with only Width: Fit elements.
Therefore, both tab containers are sized to accomodate the widest of the two forms, or the combiation of the tab container elements (whichever is longer).
Since the DIRECTION: VERTICAL tab container does not need to accomodate the tab titles and icons in its width, it is not as wide as the DIRECTION: HORIZONTAL tab container.