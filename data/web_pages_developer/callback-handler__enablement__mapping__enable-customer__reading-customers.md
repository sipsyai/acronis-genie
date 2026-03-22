---
title: "Reading partner customers from your service"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/enable-customer/reading-customers.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:32.376973"
---

# Reading partner customers from your service

Reading partner customers from your service
When the partner administrator accesses the Acronis Management Portal for customer mapping, Acronis API Callback Gateway sends a POST request to your callback handler asking for the list of partner customers in your service.

Request
The callback request:

Specifies the cti.a.p.acgw.callback.v1.0~a.p.topology.read.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.topology.read.v1.0 callback request type.

This request can be represented with the following cURL command:
curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.topology.read.v1.0", "request_id": "<request_id>", "payload": {}, "created_at": "2023-04-10T15:33:01+00:00", "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.topology.read.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'


Response
The callback response code must be 200 and the response body must:

Specify the cti.a.p.acgw.response.v1.0~a.p.topology.read.ok.v1.0 response type.
Include the payload field with the list of partner’s customers in your service.

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.topology.read.ok.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>",
"payload": {
"items": [
{
"id": "<vendor_customer_organization_id>",
"name": "<vendor_customer_name>"
}
]
}
}