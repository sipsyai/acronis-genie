---
title: "API error codes"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/error-codes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:01.313709"
---

# API error codes

API error codes

You can inspect response codes via curl by adding the --include option.
For more information, see Inspecting API response codes.

The following table lists the description of error codes returned by the Account Management API in the error.code key:







Code
Description



4xx-5xx
HTTP error. See HTTP status codes.

1000
Internal system error

1001
Version mismatch

1002
Access denied

1003
Parent tenant is disabled

1004
Tenant name conflict

1005
Tenant not found

1006
Attempt to delete non-disabled tenant

1007
Attempt to move the tenant under child

1008
Moving within customer

1009
Attempt to remove storage in use

1010
Sync & Share email conflict

1011
Deprovisioning in progress

1012
Tenant is locked

1013
Attempt to move under disabled tenant

1014
Moving offering items is not available

1015
Infrastructure component conflict

1016
Attempt to turn off storage with child

1017
Attempt to turn off default storage

1018
The user is disabled

1019
Backup service is not available

1020
Attempt to register machine not by service user

1021
Offering item is not available

1022
Hard quota exceeded

1023
Offering items dependency error

1024
Address in forbidden list

1025
SMTP settings are incorrect

1026
Cannot enable service

1027
Does not satisfy business rules

1028
Guest user is already created

1029
Removing storage deprovisioning in progress

1030
Sync & Share users count quota exceeded

1031
Location conflict

1032
Target hierarchy devoid of locking tenant

1033
Invalid login

1034
Previous version of legal document is unpublished

1035
Moving offering items which are legally blocked