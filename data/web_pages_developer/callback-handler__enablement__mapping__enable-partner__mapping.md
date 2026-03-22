---
title: "Mapping the partner ID to the Acronis tenant ID"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/enable-partner/mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:45.014921"
---

# Mapping the partner ID to the Acronis tenant ID

Mapping the partner ID to the Acronis tenant ID

When the CyberApp successfully reads the partner ID from your cloud service, it checks whether the partner ID is already mapped.

If the partner ID is not already mapped, the CyberApp sends a request to your callback handler containing the Acronis tenant ID and the partner ID on your service that need to be mapped by your cloud service.

Otherwise, the partner mapping will be denied and the callback will not be sent.


Request
The callback request:


Specifies the cti.a.p.acgw.callback.v1.0~a.p.enablement.write.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.enablement.write.v1.0 callback request type.
Contains the payload field with information about the mapping.


The request can be represented with the following cURL command:

curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.enablement.write.v1.0", "request_id": "<request_id>", "created_at": "2023-04-10T15:33:01+00:00", "payload": {"vendor_tenant_id": "<vendor_msp_organization_id>", "acronis_tenant_id": "<acronis_msp_tenant_id>"}, "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.enablement.write.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'



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