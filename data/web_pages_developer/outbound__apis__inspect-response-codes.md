---
title: "Inspecting API response codes"
source: "https://developer.acronis.com/doc/outbound/apis/inspect-response-codes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:27:54.459688"
---

# Inspecting API response codes

Inspecting API response codes

API responses are assigned specific numeric codes, which let you quickly identify if a request to an endpoint has been successful or not; and if not, why.
The individual API chapters provide error codes and their detailed descriptions for each API endpoint.


To inspect response codes
All API responses are assigned specific numeric response codes that allow you to quickly identify if a request to an endpoint has been successful or, if not, why it was not successful.
You can inspect response codes via curl by adding the --include option:
curl -X POST -s <the Acronis data center URL>/<Acronis product API location>/status \
--header Authorization: Bearer <your token> \
--data "{...}"
--include

Success codes

The first line of the response output will contain the code.
For a successful request, the platform can also supply a JSON object in the response body, containing information about the operation.
For example:

HTTP/1.1 200 OK
<...>
{"created_by": "f90e086b...","last_access_at": "2020-05-22T10:13:28+00:00","tenant_id": "e5afb5e8...", ...}


Error codes
For an error code, the platform can respond with a JSON object in the response body, containing information about the specific error. These codes are specific to each API and endpoint.






Value
Description



error.code
A platform code or an HTTP code. Platform codes and descriptions are detailed in the individual API chapters.

error.message
A short descriptive message with the error reason.

error.details
An object with additional information on the error.

error.domain
A service or service component where the error has occurred.



For example:
HTTP/1.1 400 Bad Request
<...>

{"error":{"code":1006,"message":"It is prohibited to delete a non-disabled tenant.","details":{"info":"It is prohibited to delete a non-disabled tenant "1415032"","addition":[{"id":"1415032"}]},"context":{"id":"1415032"},"domain":"PlatformAccountServer"}}