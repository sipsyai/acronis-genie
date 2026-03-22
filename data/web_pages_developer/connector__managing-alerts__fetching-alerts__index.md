---
title: "Fetching alerts"
source: "https://developer.acronis.com/doc/connector/managing-alerts/fetching-alerts/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:47.861545"
---

# Fetching alerts

Fetching alerts
You can obtain a list of alerts by sending a GET request to the /api/alert_manager/v1/alerts endpoint.

Request parameters







Parameter
Type
Description



id
string
Case-insensitive IDs of the alerts to return.

type
array of strings
A filter by list of alert types.

category
array of strings
A filter by list of alert categories.

tenant
array of strings


Filter by one or more tenant IDs.
To filter by one tenant ID, specify a tenant ID. For example: 2f4b84d8-6aad-487b-b0b1-40845bf72737.
To filter by multiple tenant IDs, specify tenants in the following format: or(2f4b84d8-6aad-487b-b0b1-40845bf72737,c70134c4-a244-4b22-99ad-e081301f7530).




skip
string
Case-insensitive IDs of the alerts to exclude.

severity
string


A filter by the alert severity.
Available operators:




eq
Equal to the specified value. For example: eq(warning).



or
Equal to one of the specified values. For example, or(warning,critical).



lt
Less than the specified value. For example, lt(warning).



gt
Greater than the specified value. For example, gt(warning).



le
Less than or equal to the specified value. For example, le(warning).



ge
Greater than or equal to the specified value. For example, ge(warning).







show_deleted
boolean
If true, dismissed alerts will be included in the response.

show_deleted_only
boolean
If true, only dismissed alerts will be included in the response.

updated_at
string


A filter by date in the UNIX nanoseconds timestamp format when the alert was created or dismissed.
Available operators:




eq
Equal to the specified value. For example, eq(1439789551045000000).



lt
Less than the specified value. For example, lt(1439789551045000000).



gt
Greater than the specified value. For example, gt(1439789551045000000).



le
Less than or equal to the specified value. For example, le(1439789551045000000).



ge
Greater than or equal to the specified value. For example, ge(1439789551045000000).







created_at
string


A filter by date in the UNIX nanoseconds timestamp format when the alert was created.
Available operators:




eq
Equal to the specified value. For example, eq(1439789551045000000).



lt
Less than the specified value. For example, lt(1439789551045000000).



gt
Greater than the specified value. For example, gt(1439789551045000000).



le
Less than or equal to the specified value. For example, le(1439789551045000000).



ge
Greater than or equal to the specified value. For example, ge(1439789551045000000).







deleted_at
string


A filter by date in the UNIX nanoseconds timestamp format when the alert was dismissed.
Available operators:




eq
Equal to the specified value. For example, eq(1439789551045000000).



lt
Less than the specified value. For example, lt(1439789551045000000).



gt
Greater than the specified value. For example, gt(1439789551045000000).



le
Less than or equal to the specified value. For example, le(1439789551045000000).



ge
Greater than or equal to the specified value. For example, ge(1439789551045000000).







order
string


An ordering filter that orders the results by parameter value. If no operator provided, the results will be ordered in ascending order.
The following parameters can be used:



created_at
type
severity
source
source_time_stamp
updated_at
deleted_at
category
planId
planName
resourceId
resourceName



Available operators:




asc
Ascending.



desc
Descending.







limit
integer
Number of the results returned in the response.

before
string
Cursor to the previous results page.

after
string
Cursor to the next results page.





Response structure
If the workloads were fetched successfully, the response returns status 200, with the payload in the following structure:







Parameter
Type
Description



type
string
The identifier of the alert type.

category
string
The identifier of the alert category.

details
object
An object that contains the information about the alert.

details.title
string
A human-readable title of the alert.

details.category
string
A human-readable alert category name.

details.description
string
A human-readable description of the alert.

details.fields
object

An object with arbitrary keys and values where each key-value pair represents a table row.
Key is the first column, value is the second column of the row.


Note

If the object includes a key-value of the type url: http://some_url, the URL is displayed as an active link.
If the URL is too long to fit on a single line in the alert, it is truncated and the suppressed characters are replaced with an ellipsis.






tenantID
string
The identifier of the tenant where the alert was triggered.




In this section

Step-by-step procedure