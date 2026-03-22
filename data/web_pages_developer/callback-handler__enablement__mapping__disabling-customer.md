---
title: "Disabling a mapped customer"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/disabling-customer.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:15.412493"
---

# Disabling a mapped customer

Disabling a mapped customer

Note

This is the same process as Writing the customer mapping to your service.
By writing customer mapping you can either enable or disable the customer.



When customer mapping is applied or removed for the selected tenants in the user interface, Acronis API Callback Gateway will send a POST request to your callback handler to write the mapping data.
Your service must store the received mapping and Acronis Cyber Platform will also store the mapping in case the request was successful.


Request
The callback request:

Specifies the cti.a.p.acgw.callback.v1.0~a.p.tenant_mapping.write.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.tenant_mapping.write.v1.0 callback request type.
Contains the payload field with the information about the mapped customers.

This request can be represented with the following cURL command:
curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.tenant_mapping.write.v1.0", "request_id": "<request_id>", "created_at": "2023-04-10T15:33:01+00:00", "payload": {"modified": [{"vendor_tenant_id": "<vendor_customer_organization_id>", "acronis_tenant_id": "<acronis_customer_tenant_id>"}]}, "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.tenant_mapping.write.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'


Response
The callback response code must be 200 and the response body must:

Specify the cti.a.p.acgw.response.v1.0~a.p.success_no_content.v1.0 response type.
Omit the payload field.

HTTP/1.1 200 OK
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.success_no_content.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>"
}