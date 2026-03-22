---
title: "Fetching workloads"
source: "https://developer.acronis.com/doc/connector/managing-workloads/fetching-workloads/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:54:17.484933"
---

# Fetching workloads

Fetching workloads
You can obtain a list of workloads that are present in Acronis Cyber Protect Cloud by sending a GET request to the /api/workload_management/v5/workloads endpoint.

Request structure







Parameter
Type
Description



tenant_id
string

Filter by one or more tenant IDs. Maximum 100 items.
To filter by one tenant ID, specify a tenant ID: 2f4b84d8-6aad-487b-b0b1-40845bf72737.
To filter by multiple tenant IDs, specify tenants in the following format: or(2f4b84d8-6aad-487b-b0b1-40845bf72737,c70134c4-a244-4b22-99ad-e081301f7530).



type
string

Filter by one or more workload types. Maximum 10 items.
To filter by one workload type, specify the workload type identifier: cti.a.p.wm.workload_aspect.v1.0~a.p.machine.v1.0.
To filter by multiple workload types, specify the workload type identifiers in the following format: or(cti.a.p.wm.workload_aspect.v1.0~a.p.machine.v1.0,cti.a.p.wm.workload_aspect.v1.0~a.p.mobile.v1.0).



workload_id
string

Filter by one or more workload IDs. Maximum 100 items.
To filter by one workload ID, specify a workload ID: 2f4b84d8-6aad-487b-b0b1-40845bf72737.
To filter by multiple workload IDs, specify workloads in the following format: or(2f4b84d8-6aad-487b-b0b1-40845bf72737,c70134c4-a244-4b22-99ad-e081301f7530).



search
string

Search for workloads by type and tags using an SQL-like syntax.
For more information on the syntax and available attributes,
see https://www.acronis.com/support/documentation/CyberProtectionService/index.html#operators-dynamic-groups.html.



updated_at
string

Filter by the date and time when the workload was updated in RFC3339 format.
Supports the following formats:
To filter by the specific date and time, specify the exact date and time: 2009-11-10T23:00:00Z.
To filter by specific conditions, use one of the following operators:

ge() - returns the workloads whose dates are greater than or equal (>=) to the specified date. For example, ge(2009-11-10T23:00:00Z).
gt() - returns the workloads whose dates are greater than (>) the specified date. For example, gt(2009-11-10T23:00:00Z).
le() - returns the workloads whose dates are less than or equal (<=) the specified date. For example, le(2009-11-10T23:00:00Z).
lt() - returns the workloads whose dates are less than (<>) the specified date. For example, lt(2009-11-10T23:00:00Z).
range() - returns the workloads whose dates are within the specified range including the specified dates. For example, range(2009-11-10T23:00:00Z,2009-11-11T23:00:00Z).
xrange() - returns the workloads whose dates are within the specified range excluding the specified dates. For example, xrange(2009-11-10T23:00:00Z,2009-11-11T23:00:00Z).




include_status
boolean
If true, includes workload statuses in the response. Does not include workload statuses otherwise.

include_all_attributes
boolean
If true, includes all workload attributes in the response. Does not include workload attributes otherwise. Mutually exclusive with the include_attributes.

include_attributes
array of string
Includes the specified workload attributes (if present) by their names in the response. Mutually exclusive with the include_attributes.

include_allowed_actions
boolean
If true, includes allowed actions for the workload in the response. Does not include workload actions otherwise.

include_aggregated_aspects
boolean
If true, includes aspects that were aggregated into the workload.

order
string

Sorts workloads by orderable fields. Only one field can be specified in the request.
Fields that can be used for ordering:

is_group
updated_at

To sort by a specific field, specify the field: updated_at. The results will be ordered in ascending order.
To specify the order, use one of the following operators:

asc() - returns the workloads ordered by the field in ascending order. For example, asc(updated_at).
desc() - returns the workloads ordered by the field in ascending order. For example, desc(updated_at).




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



items
array of object
A list of workloads.

items[*].id
string
The UUID of the workload.

items[*].type
string
The identifier of the workload type.

items[*].name
string
A name of the workload.

items[*].attributes
object
A key-value map of workload attributes. Allowed values are defined by the attributes schema specified in the Vendor Portal.

items[*].client_id
string
An identifier of the API client that created the workload. Must be the client ID of your application.

items[*].allowed_actions
array of string
A list of workload action identifiers that are allowed for this workload.

items[*].tenant_id
string
The identifier of the tenant where the workload was created.

items[*].external_id
string
The identifier that is used in the external system where the workload is originated from. Equal to the id field in case it was not specified.

items[*].agent_id
string
UUID of the agent that manages the workload. Only applicable to Acronis workloads.

items[*].created_at
string
RFC3339 date and time in UTC timezone when the workload was created.

items[*].updated_at
string
RFC3339 date and time in UTC timezone when the workload was updated.

items[*].aggregates_detection_query
object
Parameters of any use cases when workload group is automatically created.

items[*].parent_child_relationship_query
array of objects
Parameters of any use cases when the parent-child relationship is set automatically.

items[*].is_auto_created
boolean
True if the workload was created due to merge and cluster-like use case. False otherwise.

items[*].aggregation_status
string

Status of the workload aggregation. Can be one of the following:

NOT_AGGREGATED - workload was not aggregated.
MERGED_AUTOMATICALLY - workload was merged automatically.
MERGED_MANUALLY - workload was merged manually.
SPLIT_MANUALLY - workload was split manually.




items[*].enabled
boolean
Status of the workload. True if enabled, false otherwise.

paging
object
An object containing the information about the pagination.

paging.cursors
object
An object containing the information about the cursors to the pages.

paging.cursors.before
string
Cursor to the next page.

paging.cursors.after
string
Cursor to the previous page.

_links
array of object
A list of links related to the requested resource.




In this section

Step-by-step procedure