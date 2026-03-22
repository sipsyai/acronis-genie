# Search operators

Managing workloads in the Cyber Protect console > Device groups > Creating a dynamic group > Search operators
Search operators

The following table summarizes the operators that you can use for your search queries.

You can use more than one operator in a single query.

Operator	Supported for	Meaning	Examples


AND



All workloads

Logical conjunction operator

name like 'en-00' AND tenant = 'Unit 1'




OR

All workloads	Logical disjunction operator

state = 'backup' OR state = 'interactionRequired'




NOT

All workloads	Logical negation operator

NOT(osProductType = 'workstation')


IN (<value1>,... <valueN>)	All workloads	This operator checks if an expression matches any value in a list of values.	osType IN ('windows', 'linux')


NOT IN

All workloads

This operator is the opposite of the IN operator.



NOT osType IN ('windows', 'linux')




LIKE 'wildcard pattern'

All workloads

This operator checks if an expression matches the wildcard pattern.

You can use the following wildcard operators:

* or % The asterisk and the percent sign represent zero, one, or multiple characters
_ The underscore represents a single character


name LIKE 'en-00'

name LIKE '*en-00'

name LIKE '*en-00*'

name LIKE 'en-00_'




NOT LIKE 'wildcard pattern'

All workloads

This operator is the opposite of the LIKE operator.

You can use the following wildcard operators:

* or % The asterisk and the percent sign represent zero, one, or multiple characters
_ The underscore represents a single character


NOT name LIKE 'en-00'

NOT name LIKE '*en-00'

NOT name LIKE '*en-00*'

NOT name LIKE 'en-00_'




RANGE(<starting_value>, <ending_value>)

All workloads

This operator checks if an expression is within a range of values (inclusive).

Search queries with alphanumeric strings use the ASCII sort order but are case-insensitive.



ip RANGE('10.250.176.1','10.250.176.50')

name RANGE('a','d')

With this query, you can filter all names that begin with A, B, and C, such as Alice, Bob, Claire. However, only the single letter D meets the requirements, so names with more letters, such as Diana or Don will not be included.

To achieve the same result, you can also use the following query:

name >= 'a' AND name <= 'd'


= or ==	All workloads	Equal to operator	osProductType = 'server'
!= or <>	All workloads	Not equal to operator	id != '4B2A7A93-A44F-4155-BDE3-A023C57C9431'
<	Non-cloud-to-cloud workloads	Less than operator	memorySize < 1024
>	Non-cloud-to-cloud workloads	Greater than operator.	diskSize > 300GB
<=	Non-cloud-to-cloud workloads	Less than or equal to operator	lastBackupTime <= '2022-03-11 00:15'
>=	Non-cloud-to-cloud workloads	Greater than or equal to operator	nextBackupTime >= '2022-08-11'
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.