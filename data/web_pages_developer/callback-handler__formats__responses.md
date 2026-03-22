---
title: "Callback response format"
source: "https://developer.acronis.com/doc/callback-handler/formats/responses.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:48.487307"
---

# Callback response format

Callback response format

Response body
Callback responses sent by your callback handler must include the following fields:







Field
Type
Description



type
string
The identifier of the callback response. The response identifier must match one of the identifiers defined for this callback. Example: cti.a.p.acgw.response.v1.0~vendor.app.read_users_ok.v1.0.

request_id
string
The UUID of the request that corresponds to this response.

response_id
string
The UUID of the response.

payload
object
An object containing the data structure configured for the callback response. This is optional.

err_message
string
A human-readable message that will be displayed if an error status code is returned. This is optional and only applicable for specific callbacks. See Callback error handling for details.



Example of successful response:
{
"type": "cti.a.p.acgw.response.v1.0~a.p.enablement.read.ok.v1.0",
"request_id": "eb768938-dbb6-4a5c-aae1-23cebfac7f26",
"response_id": "6eb3efde-8071-40ab-b820-6e749a2dafd6"
}


Example of enablement error response:
{
"request_id": "eb768938-dbb6-4a5c-aae1-23cebfac7f26",
"response_id": "6eb3efde-8071-40ab-b820-6e749a2dafd6",
"err_message": "You must sign a contract with Security Tool LLC to be able to map tenants."
}