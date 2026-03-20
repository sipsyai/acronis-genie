---
title: "Events Search and Saved Queries"
section: "Endpoint Detection and Response (EDR)"
subsection: "Events Search"
page_range: "1145-1152"
tags: [edr, events-search, ioc, indicators-of-compromise, xql, saved-queries, query-results]
acronis_version: "26.02"
---

# Search for Indicators of Compromise (IoC) and Suspicious Activities

To detect and mitigate threats before they escalate into high impact incidents, use the **Events search** feature. This search feature enables hunting for IoCs and suspicious activities across all workloads enabled with Endpoint Detection and Response (EDR).

## Events Search Capabilities

Use the **Events search** feature to:

- Run custom queries on event data collected from all workloads to search for hashes. Alternatively, obtain metrics to answer certain questions (for example, show workloads with an unusually high number of processes).
- Filter queries using attributes provided by EDR endpoints and data from other integrations, such as operating system activities, user activities, and network activities.
- View an intuitive summary of the data based on queries to help in incident investigation or the hunting of threats.
- Save and share queries with users within the same organization.

The **Events search** feature is accessed from the **Protection** menu in the Cyber Protect console. The default retention period for EDR events search results is seven days.

## Searching for Events

You can search for EDR events across all workloads protected by EDR. Events can only be searched within a selected customer (not across all managed customers at the partner tenant level).

### Steps to Search for Events

1. In the Cyber Protect console, go to **Protection > Events search**.
2. Enter your search query using Acronis XDR Query Language (XQL), and define a time range. XQL uses autocomplete to assist in building queries.
   - Press **Enter** to send the cursor to the next line. The "|" character is also added at the start of the new line (useful for multi-stage queries).
   - Press **Shift+Enter** to send the cursor to the next line without adding the pipe character.
   - To reuse one of the last ten executed queries, click **History** and select the relevant query.
3. Click **Run** to execute the query (or press **Ctrl+Enter**).
4. Refine the search query as required. For example, select to display specific fields or events that contain a certain file name.
5. (Optional) To save the current query, click **Save as**.

## Disabling Event Search

Searching for events requires storing and processing event data in an external third-party cloud data warehouse system. If you do not want event data stored outside your data center, you can disable event search for EDR events.

### Steps to Disable Event Search

1. In the Cyber Protect console, go to **Protection > Events search**.
2. Above the list of search queries, click **Settings**.
3. Turn off the **Event Search** toggle, and then click **Apply**.

The **Events search is disabled** message remains on the screen. To re-enable event search, click **Enable**.

## Viewing and Understanding Query Results

When a search query is defined and executed, the results are displayed below the search query box in a table layout view. From this view, you can:

- View all of the events for the selected period.
- Click on an event row to view the details of an individual event.
- Add or remove columns shown in the query results.
- Switch to **Data view**, which displays all the event data in JSON format.
- Hover over a column in the bar chart to view the date, timezone, count, and duration of events.

### Adding or Removing Columns in the Table Layout View

There are three ways to add or remove columns shown in the query results:

1. In the **Field name** pane, click the add button next to the relevant field name (in the **Available fields** section) to add that field as a column. To remove a column, click the remove button next to the relevant field name (in the **Selected fields** section).
2. Click on an event to display the **Event details** pane, and then click the add or remove buttons to add or remove the relevant field from the search query results.
3. Hover over a column to display an X icon. Click the icon to remove the column.

If you include the `Column` operator in the query, only those fields specified by the `Column` operator are shown in the table layout view. You can still add or remove fields via the **Fields** panel.

If the query does not include the `Column` operator, the results are shown by default in the **Data view** layout (JSON format). Click **Table view** to switch views, or add fields via the **Fields** panel to automatically switch to **Table view**.

After adding or removing columns via the **Event details** pane or the **Fields** panel, the query is automatically run again.

## Working with Saved Queries

The **Events search** feature enables saving, reusing, and updating queries.

### Save a New Query

1. In the Cyber Protect console, go to **Protection > Events search**.
2. Define your query in the search query box.
3. Click **Save as**.
4. In the **Save new query** dialog, define the following:
   - Enter a unique query name, and (optionally) add a description.
   - Select the **Save time filter** checkbox to ensure the defined time filter is included in the query.
   - Select the **Allow others to use this query** checkbox to ensure other users within the same customer tenant can use the query. If not selected, only the administrator, company administrator, and user who created the query can use it.
5. Click **Save**. When saving, only the text part of the query and the selected time range are saved.

A maximum of 300 queries can be saved per customer tenant account. When this limit is reached, you are prompted to delete a saved query before saving the new query.

### Run a Previously Saved Query

1. In the search query box, click **Saved queries**.
2. In the displayed list, click on the relevant query. The query is added to the search query box and automatically run.

### Update a Saved Query

1. In the search query box, click **Saved queries**.
2. Hover over the query you want to update and click the pencil icon.
3. Make the required changes to the query and click **Save**.
4. (Optional) Click the saved query to run it.

### Delete a Query

1. In the search query box, click **Saved queries**.
2. In the list of saved queries, hover over the query you want to delete and click the trash can icon.
3. In the confirmation dialog, click **Delete**.
