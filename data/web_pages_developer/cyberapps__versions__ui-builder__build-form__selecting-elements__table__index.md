---
title: "TABLE"
source: "https://developer.acronis.com/doc/cyberapps/versions/ui-builder/build-form/selecting-elements/table/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:06:18.894797"
---

# TABLE

TABLE

Note
This element is not available in the CyberApp enablement form.

Tables are generally used to display an array of data. For more information, see Populating a table with data.

You can drop elements onto table columns to display data graphically, and to allow users to edit data.
To send user-modified table data for your service to update centrally, you must either:



Define an Action button and map a callback.
Define an On row click action and map a callback.
Add a button to the container form and map a callback.



Note

You can drop a Button element onto a column, and define a Callback On click action for it, which can map the model of the selected row.
This has the same functionality to a table action button which has the Availability parameter set to If one row is selected.



PROPERTIES



ID
Element identifier.


Width


Default
This is for backward compatibility purposes only.



Fit
Sets the width according to the combined widths of the columns.



Fill
Uses all of the available width.
For more information, see Element distribution.





Row key
The ID of one of the table columns, which can be used to uniquely identify table rows.
If not set, the default row key is ‘id’.



Note
Table rows cannot be selected if the row key is not present in the callback response.




Searchable column ID
The ID of one of the columns, used to search the table.



Note

The search field is only displayed if you specify a value.
If you use a paginated callback to populate the table, this property is not available. If you want to allow a search, you can use an input element, and map it to the callback request.






The table PROPERTIES folder also includes sections to control:

General table style.
The list and order of columns, and their individual properties.
Row click actions.
Action buttons.


In this section

Populating a table with data
Dynamic icons in a table
Style
Table columns
On row click action
Table action buttons