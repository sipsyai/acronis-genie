# Viewing and understanding query results

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Reviewing incidents > Viewing and understanding query results
Viewing and understanding query results

When you have defined and executed your search query (see Searching for events), the results are displayed below the search query box in a table layout view. From this view, you can:

View all of the events for the selected period.

Click on an event row to view the details of an individual event.

Add or remove columns shown in the query results. See Adding or removing columns in the table layout view.

Switch to Data view, which displays all the event data in JSON format.

Hover over a column in the bar chart to view the date, timezone, count, and duration of events.

Adding or removing columns in the table layout view

In the table layout view, there are three ways you can add or remove the columns shown in the query results:

In the Field name pane, click  next to the relevant field name (in the Available fields section) to add that field as a column in the query results.

To remove a column, click  next to the relevant field name (in the Selected fields section).

Click on an event to display the Event details pane, and then click  or  to add or remove the relevant field from the search query results.

Hover over a column to display an X icon. Click the icon to remove the column.

If you include the Column operator in the query, only those fields specified by the Column operator are shown in the table layout view. You can still add or remove fields via the Fields panel.

If the query does not include the Column operator, the results are shown by default in the Data view layout (in JSON format). However, you can click Table view to switch views, or add fields via the Fields panel to automatically switch to Table view with only the fields you selected displayed.

For more information about the Column operator and other XQL elements, see Acronis XDR Query Language (XQL).

After adding or removing columns via the Event details pane or the Fields panel, the query is automatically run again.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.