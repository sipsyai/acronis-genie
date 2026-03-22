# Searching for events

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Reviewing incidents > Searching for events
Searching for events

You can search for Endpoint Detection and Response (EDR) events across all workloads protected by EDR.

You can search for events only within a selected customer.

If you use the Cyber Protect console on the partner tenant level (when All customers is selected), you cannot search for events from all your managed customers.

To search for events

In the Cyber Protect console, go to Protection > Events search.

Enter your search query using Acronis XDR Query Language (XQL), and define a time range.

Note that XQL uses autocomplete to assist you in building a query. For more information about the syntax and query options available, see Acronis XDR Query Language (XQL).

When building the query, the following keyboard operations are also available:

Press Enter to send the cursor to the next line. The "|" character is also added at the start of the new line (which helps when writing multi-stage queries).

Press Shift+Enter to send the cursor to the next line.

To use one of the last ten executed queries, click History, and then select the relevant query. The search query field is automatically filled with the query. For more information, see Working with saved queries.

Click Run to execute the query.

You can also press Ctrl+Enter to execute the query.

The query results are displayed. For more information, see Viewing and understanding query results.

Refine your search query as required. For example, select to display specific fields or events that contain a certain file name.

To save the current query, click Save as. For more information, see Working with saved queries.

Disabling event search

Searching for events requires storing and processing event data in an external third-party cloud data warehouse system. If you do not want event data stored outside your data center, you can disable event search for EDR events.

To disable event search

In the Cyber Protect console, go to Protection > Events search.

Above the list of search queries, click Settings.

Turn off the Event Search toggle, and then click Apply.

The Events search is disabled message remains on the screen.

To re-enable event search

Click Enable.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.