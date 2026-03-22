# Acronis XDR Query Language (XQL)

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Reviewing incidents > Acronis XDR Query Language (XQL)
Acronis XDR Query Language (XQL)

Use XQL to search for Endpoint Detection and Response (EDR) events and then drill-down to the events you are looking for. This section lists the various elements of XQL you should be familiar with when searching for EDR events:

Syntax (including sample queries)
Event types and fields

For more information about using the Events search feature, see Search for Indicators of Compromise (IoC) and suspicious activities.

Syntax
Operation	Example


Selecting data source and columns

Selects the data source and columns for the query to operate on. This operator must be the first operator in the query.Queries for selecting data sources and columns are not case-sensitive.



eventType

eventType | where column = 'string'




Filtering data

Filters data based on conditions, and must start with a where keyword.

Note the following filtering options:

Strings can be enclosed with either single or double quotes.

Column searches are case sensitive by default. For equality checking, searches can be made case-insensitive with "~=":

eventType | where column = 'String' is case sensitive and will match only 'String'.

eventType | where column ~= 'String' is not case sensitive and will match all cases of 'string'.

Logical operators like AND and OR can be used to combine the filters.

key = value AND key < value OR key = value

Parentheses can be added around operators:

(key = value) AND (key < value OR key = value)

Use CONTAINS for partial string matching:

key CONTAINS 'value'

When searching across columns, CONTAINS can include single items or a list of items:

CONTAINS 'String'

CONTAINS ('String1', 'String2', 'String3')

Use ICONTAINS for case-insensitive partial string matching:

key ICONTAINS 'value'

Use IN for membership checking (case sensitive):

key IN ('value1', 'value2')

Use IIN for membership checking (not case sensitive):

key IIN ('value1', 'value2')

Use ago to filter dates. This syntax only accepts a numeric value followed by days(d), hours(h), minutes(m) or seconds(s):

column < ago(3d)

column < ago(3h)

column < ago(3m)

column < ago(30s)

Use regex matching according to the RE2 standard:

key MATCHES 'regex string'



eventType | where field == 'value'

eventType | where field != 'value'

eventType | where field > 'value'

eventType | where field < 'value'

eventType | where field >= 'value'

eventType | where field <= 'value'

eventType | where field CONTAINS 'substring'

eventType | where field NOT CONTAINS 'substring'

eventType | where field ICONTAINS 'substring'

eventType | where column ICONTAINS 'substring'

eventType | where field NOT ICONTAINS 'substring'

eventType | where column NOT ICONTAINS 'substring'

eventType | where field IN ('value1', 'value2')

eventType | where column IIN ('value1'. 'value2')

eventType | where field NOT IN ('value1', 'value2')

eventType | where field MATCHES 'value1*'

eventType | where field NOT MATCHES 'value1*'

eventType | where event_time > ago(5d)




Choosing fields

Specifies which fields to select and return from a query.

eventType | columns field1, field2, field3 ...


Sorting

Sorts the results of the query, which can be ascending or descending. If no order is specified, the default order is ascending.



eventType | order field1, field2, field3 ...

eventType | order field asc

eventType | order field desc




Searching across columns

Searches for a string across all columns in a table.

eventType | search 'query string'


Limit

Limits the result of the query.

eventType | limit 10

eventType | limit 1000 | group [field1, field2] | limit 10




Group operation

Performs a group operation on the data.

(Optional) You can specify aggregation functions to perform on the aggregated fields, or only specify aggregate functions without performing group operation on specific fields.



eventType | group [field]

eventType | group [field1, field2, field3, ...]

eventType | group with [max(field1), min(field2), avg(field3)]

eventType | group [field1, field2, field3, ...] with [max(field1), min(field2), avg(field3)]

eventType | group [field1, field2, field3, ...] with [max(field1) as max_field, min(field2), avg(field3) as avg_field]




Aggregation

Aggregates the results of the query to perform an operation.

These functions can only be used together with group operation (see above).



min(field)

max(field)

avg(field)

count()

count(field)

countdistinct(field)

Usually in program languages '==' is used to declare conditions, and '=' to assign values.

With Acronis XDR Query Language, you can only declare conditions and can use '=' and '==' interchangeably'.

Sample queries

This section includes a number of sample queries to illustrate how you can apply XQL syntax rules to your query.

Selecting fields from the WinProcCreate event type:

Copy
WinProcCreate | columns host_name, parent_start, parent_gpid, parent_pid, parent_user, proc_name

Filtering with conditions, before grouping the results by proc_name, and applying aggregate functions min() on parent_pid:

Copy
WinProcCreate | where host_name == 'BNi-Kub' AND parent_pid != -1 AND proc_name CONTAINS '1' AND host_name IN ('Computer1')  |  group [proc_name] with [min(parent_pid)]

Selecting data with filters, then counting the number of rows returned and ordering them:

Copy
WinProcCreate | where host_name == 'BNi-Kub' | group with [count() as new_count] | order new_count

Selecting data with regex filters:

Copy
WinProcCreate | where host_name matches 'BNi.*'

Selecting data with complex filters, and limiting the results:

Copy
WinProcCreate | where (host_name contains 'BNi-Kub') OR (host_name in ('Computer1', 'Computer2')) | limit 10

Selecting data with filters, then counting the distinct number of rows returned:

Copy
WinProcCreate | where host_name == 'BNi-Kub' | group with [countdistinct(*)]

Selecting data with filters, ordering by a field, and limiting the number of rows returned:

Copy
WinProcCreate | where host_name == 'BNi-Kub' | order host_name | limit 10
Event types and fields

This section includes:

Event types
Sample data types
Event fields
Event types
Name	Description	Type


WinProcCreate

For more information about the available fields, see WinProcCreate.

Windows process creation events	Events


WinProcTerminate

For more information about the available fields, see WinProcTerminate.

Windows process termination events	Events


WinNetAccess

For more information about the available fields, see WinNetAccess.

Windows network access events	Events


WinRegAccess

For more information about the available fields, see WinRegAccess.

Windows registry access events	Events


WinScriptExec

For more information about the available fields, see WinScriptExec.

Windows script execution events (including PowerShell, VBS, etc)	Events


WinFileAccess

For more information about the available fields, see WinFileAccess.

Windows file access events (read/write)	Events


WinLogin

For more information about the available fields, see WinLogin.

Windows user login events	Events


WinLogout

For more information about the available fields, see WinLogout.

Windows user logout events	Events


WinAgentDetection

For more information about the available fields, see WinAgentDetection.

Windows detection events	Detections
Sample data types
Data type	Sample	Description
String

WinProcCreate | where host_name == 'BNi-Kub'

WinProcCreate | where host_name == "BNi-Kub"

Strings must be surrounded by single quotes or double quotes.
UUID

WinProcCreate | where agent_id == '61f0c404-5cb3-11e7-907b-a6006ad3dba0'

WinProcCreate | where agent_id == "61f0c404-5cb3-11e7-907b-a6006ad3dba0"



UUIDs are string values, and must be surrounded by single quotes or double quotes.

UUID values must be in an 8-4-4-4-12 sequence.


DateTime

WinProcCreate | where event_time < '2022-11-01'

WinProcCreate | where event_time < "2022-11-01"



DateTime is a string value, and must be surrounded by single quotes or double quotes.

DateTime must be in a YYYY-MM-DD format.


Bool

WinLogin | where is_admin == 1

WinLogin | where is_admin == 0

WinLogin | where is_admin == true

WinLogin | where is_admin == false

Boolean values can be represented by 1, 0, true or false.
Integer	WinLogin | where proc_pid > 25	An integer value.
Event fields
Event type	Field (Data type)
WinProcCreate

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_prod (String)

proc_prod_desc (String)

proc_sha1 (String)

proc_sha256 (String)

proc_signatures (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

timestamp (DateTime)


WinProcTerminate

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

owner (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

term_args (String)

term_gpid (UUID)

term_integrity_level (String)

term_md5 (String)

term_name (String)

term_oname (String)

term_path (String)

term_pid (Int)

term_sha1 (String)

term_sha256 (String)

term_start (DateTime)

term_upn (String)

term_user (String)

term_user_domain (String)

timestamp (DateTime)


WinNetAccess

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

net_dst_ip (String)

net_dst_port (Int)

net_host (String)

net_http_method (String)

net_http_url (String)

net_protocol (String)

net_src_ip (String)

net_src_port (Int)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

timestamp (DateTime)


WinRegAccess

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

reg_key (String)

reg_operation (String)

reg_original_key (String)

reg_original_value_data (String)

reg_value_data (String)

reg_value_name (String)

reg_value_type (String)

resource_id (UUID)

timestamp (DateTime)


WinScriptExec

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

script_data (String)

script_fragment (Bool)

script_size (Int)

script_type (String)

timestamp (DateTime)


WinFileAccess

agent_id (UUID)

customer (String)

event_time (DateTime)

file_md5 (String)

file_name (String)

file_op (String)

file_path (String)

file_sha1 (String)

file_sha256 (String)

host_name (String)

id (UUID)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

timestamp (DateTime)


WinLogin

agent_id (UUID)

customer (String)

domain (String)

event_time (DateTime)

host_name (String)

id (UUID)

is_admin (Bool)

login_time (DateTime)

name (String)

owner (String)

resource_id (UUID)

security_id (String)

timestamp (DateTime)

type (String)


WinLogout

agent_id (UUID)

customer (String)

event_time (DateTime)

host_name (String)

id (UUID)

logout_time (DateTime)

resource_id (UUID)

security_id (String)

timestamp (DateTime)


WinAgentDetection

agent_id (UUID)

customer (String)

detection_type (String)

event_time (DateTime)

file_md5 (String)

file_name (String)

file_path (String)

file_sha1 (String)

file_sha256 (String)

host_name (String)

id (UUID)

mitre_stid (Int)

mitre_tactics (Int)

mitre_tid (Int)

owner (String)

parent_args (String)

parent_gpid (UUID)

parent_integrity_level (String)

parent_md5 (String)

parent_name (String)

parent_oname (String)

parent_path (String)

parent_pid (Int)

parent_sha1 (String)

parent_sha256 (String)

parent_start (DateTime)

parent_upn (String)

parent_user (String)

parent_user_domain (String)

proc_args (String)

proc_gpid (UUID)

proc_integrity_level (String)

proc_md5 (String)

proc_name (String)

proc_oname (String)

proc_path (String)

proc_pid (Int)

proc_sha1 (String)

proc_sha256 (String)

proc_start (DateTime)

proc_upn (String)

proc_user (String)

proc_user_domain (String)

resource_id (UUID)

severity (String)

threat_name (String)

timestamp (DateTime)

url (String)

url_blocked (Bool)

url_cat (Array(String))

url_list (String)

url_md5 (String)

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.