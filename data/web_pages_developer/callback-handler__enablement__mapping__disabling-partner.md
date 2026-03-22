---
title: "Disabling a mapped partner"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/disabling-partner.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:19.635118"
---

# Disabling a mapped partner

Disabling a mapped partner

The callback handler must support disabling of the CyberApp for a mapped partner.
If an Acronis partner requests to disable the CyberApp, Acronis Cyber Platform sends a callback request to your callback handler to remove the partner mapping in your cloud service.


Important
When a partner disables the CyberApp, the information about the customer mapping must be removed
for this partner.


Request
The disable callback request:


Specifies the cti.a.p.acgw.callback.v1.0~a.p.enablement.reset.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.empty.v1.0 callback request type.
Omits the payload field.


This callback request can be represented with the following cURL command:

curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.empty.v1.0", "request_id": "<request_id>", "created_at": "2023-04-10T15:33:01+00:00", "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.enablement.reset.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'



Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.0~a.p.success_no_content.v1.0 response type.
Omit the payload field.


HTTP/1.1 200 OK
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.success_no_content.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>"
}