---
title: "Acronis XDR Query Language (XQL) and Sample Queries"
section: "Endpoint Detection and Response (EDR)"
subsection: "XQL Query Language"
page_range: "1151-1154"
tags: [edr, xql, query-language, syntax, sample-queries, filtering, aggregation]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#edr-search-query-language.html"
---

# Acronis XDR Query Language (XQL)

Use XQL to search for Endpoint Detection and Response (EDR) events and then drill-down to the events you are looking for. This section lists the various elements of XQL you should be familiar with when searching for EDR events.

## Syntax

### Selecting Data Source and Columns

Selects the data source and columns for the query to operate on. This operator must be the first operator in the query. Queries for selecting data sources and columns are not case-sensitive.

```
eventType
eventType | where column = 'string'
```

### Filtering Data

Filters data based on conditions, and must start with a `where` keyword. Filtering options include:

| Operator | Example |
|----------|---------|
| Equals | `eventType \| where field == 'value'` |
| Not equals | `eventType \| where field != 'value'` |
| Greater than | `eventType \| where field > 'value'` |
| Less than | `eventType \| where field < 'value'` |
| Greater or equal | `eventType \| where field >= 'value'` |
| Less or equal | `eventType \| where field <= 'value'` |
| Contains (case-sensitive) | `eventType \| where field CONTAINS 'substring'` |
| Not contains | `eventType \| where field NOT CONTAINS 'substring'` |
| Contains (case-insensitive) | `eventType \| where field ICONTAINS 'substring'` |
| Not icontains | `eventType \| where column ICONTAINS 'substring'` |

Additional filtering options:

- **Parentheses** can be added around operators: `(key = value) AND (key < value OR key = value)`
- **CONTAINS** for partial string matching: `key CONTAINS 'value'`. When searching across columns, CONTAINS can include single items or a list: `CONTAINS ('String1', 'String2', 'String3')`
- **ICONTAINS** for case-insensitive partial string matching: `key ICONTAINS 'value'`
- **IN** for membership checking (case sensitive): `key IN ('value1', 'value2')`
- **IIN** for membership checking (not case sensitive): `key IIN ('value1', 'value2')`
- **ago** to filter dates: accepts numeric value followed by days(d), hours(h), minutes(m) or seconds(s): `column < ago(3d)`, `column < ago(3h)`, `column < ago(3m)`, `column < ago(30s)`
- **MATCHES** for regex matching (RE2 standard): `key MATCHES 'regex string'`
- **NOT IN**: `eventType \| where field NOT IN ('value1', 'value2')`
- **NOT MATCHES**: `eventType \| where field NOT MATCHES 'value1*'`

Logical operators **AND** and **OR** can be used to combine filters: `key = value AND key < value OR key = value`

Column searches are case sensitive by default. For equality checking, searches can be made case-insensitive with `~=`: `eventType | where column ~= 'String'` will match all cases of 'string'.

With Acronis XDR Query Language, you can only declare conditions and can use `=` and `==` interchangeably.

### Choosing Fields

Specifies which fields to select and return from a query:

```
eventType | columns field1, field2, field3 ...
```

### Sorting

Sorts the results of the query (ascending or descending). If no order is specified, the default order is ascending:

```
eventType | order field1, field2, field3 ...
eventType | order field asc
eventType | order field desc
```

### Searching Across Columns

Searches for a string across all columns in a table:

```
eventType | search 'query string'
```

### Limit

Limits the result of the query:

```
eventType | limit 10
eventType | limit 1000 | group [field1, field2] | limit 10
```

### Group Operation

Performs a `group` operation on the data. Optionally specify aggregation functions on the aggregated fields:

```
eventType | group [field]
eventType | group [field1, field2, field3, ...]
eventType | group with [max(field1), min(field2), avg(field3)]
eventType | group [field1, field2, field3, ...] with [max(field1), min(field2), avg(field3)]
eventType | group [field1, field2, field3, ...] with [max(field1) as max_field, min(field2), avg(field3) as avg_field]
```

### Aggregation Functions

Aggregation functions can only be used together with `group` operation:

- `min(field)` - Minimum value
- `max(field)` - Maximum value
- `avg(field)` - Average value
- `count()` - Count all rows
- `count(field)` - Count non-null values
- `countdistinct(field)` - Count distinct values

## Sample Queries

### Selecting fields from WinProcCreate event type

```
WinProcCreate | columns host_name, parent_start, parent_gpid, parent_pid, parent_user, proc_name
```

### Filtering with conditions and applying aggregate functions

```
WinProcCreate | where host_name == 'BNi-Kub' AND parent_pid != -1 AND proc_name
CONTAINS '1' AND host_name IN ('Computer1')  |  group [proc_name] with [min(parent_pid)]
```

### Selecting data with filters, counting and ordering

```
WinProcCreate | where host_name == 'BNi-Kub' | group with [count() as new_count] | order new_count
```

### Selecting data with regex filters

```
WinProcCreate | where host_name matches 'BNi.*'
```

### Selecting data with complex filters and limiting results

```
WinProcCreate | where (host_name contains 'BNi-Kub') OR (host_name in ('Computer1', 'Computer2')) | limit 10
```

### Counting distinct rows

```
WinProcCreate | where host_name == 'BNi-Kub' | group with [countdistinct(*)]
```

### Ordering and limiting

```
WinProcCreate | where host_name == 'BNi-Kub' | order host_name | limit 10
```
