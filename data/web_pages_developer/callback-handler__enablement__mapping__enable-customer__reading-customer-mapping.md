---
title: "Reading the customer mapping from your service"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/enable-customer/reading-customer-mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:28.134290"
---

# Reading the customer mapping from your service

Reading the customer mapping from your service
After reading the partner’s customers from your service, the user interface for customer mapping
will send a POST request to your callback handler to check the mapping status of the received organizations for the partner.

Request
The callback request:

Specifies the cti.a.p.acgw.callback.v1.0~a.p.tenant_mapping.read.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.empty.v1.0 callback request type.
Omits the payload field.

This request can be represented with the following cURL command:
curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.empty.v1.0", "request_id": "<request_id>", "created_at": "2023-04-10T15:33:01+00:00", "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.tenant_mapping.read.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'


Response
The callback response code must be 200 and the response body must:

Specify the cti.a.p.acgw.response.v1.0~a.p.tenant_mapping.read.ok.v1.0 response type.
Include the payload field with a list of objects containing the partner’s customer organization IDs
and, if any, Acronis customer tenant IDs that were mapped to them.

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.tenant_mapping.read.ok.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>",
"payload": {
"items": [
{
"vendor_tenant_id": "<vendor_customer_organization_id>"
},
{
"vendor_tenant_id": "<vendor_customer_organization_id>",
"acronis_tenant_id": "<acronis_customer_tenant_id>"
}
]
}
}