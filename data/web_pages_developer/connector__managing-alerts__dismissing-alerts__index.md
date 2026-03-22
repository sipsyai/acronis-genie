---
title: "Dismissing alerts"
source: "https://developer.acronis.com/doc/connector/managing-alerts/dismissing-alerts/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:39.462986"
---

# Dismissing alerts

Dismissing alerts
You can dismiss alerts by sending a DELETE request to the /api/alert_manager/v1/alerts endpoint.

Request parameters







Parameter
Type
Description



id
string
Case-insensitive IDs of the alerts to delete.

type
array of strings
A filter by list of alert types.

category
array of strings
A filter by list of alert categories.

tenant
array of strings

Filter by one or more tenant IDs.
To filter by one tenant ID, specify a tenant ID: 2f4b84d8-6aad-487b-b0b1-40845bf72737.
To filter by multiple tenant IDs, specify tenants in the following format: or(2f4b84d8-6aad-487b-b0b1-40845bf72737,c70134c4-a244-4b22-99ad-e081301f7530).



severity
string


A filter by the alert severity. Available severities:


critical
error
warning
information



Available operators:



eq
Equal to the specified value. For example, eq(warning).



or
Equal to one of the specified values. For example, or(warning,critical).



lt
Less than the specified value. For example, lt(warning).



gt
Greater than the specified value. For example, gt(warning).



le
Less than or equals to the specified value. For example, le(warning).



ge
Greater than or equals to the specified value. For example, ge(warning).







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
Less than or equals to the specified value. For example, le(1439789551045000000).



ge
Greater than or equals to the specified value. For example, ge(1439789551045000000).







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
Less than or equals to the specified value. For example, le(1439789551045000000).



ge
Greater than or equals to the specified value. For example, ge(1439789551045000000).







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
Less than or equals to the specified value. For example, le(1439789551045000000).



ge
Greater than or equals to the specified value. For example, ge(1439789551045000000).







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
If the alerts were created successfully, the response returns status 204 without payload.

In this section

Step-by-step procedure