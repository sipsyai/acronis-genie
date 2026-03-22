---
title: "Reading the partner ID from your service"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/enable-partner/reading.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:49.249260"
---

# Reading the partner ID from your service

Reading the partner ID from your service
When an Acronis partner administrator enables the CyberApp, they open the CyberApp enablement form in the Acronis management portal.
The administrator enters the credentials for your cloud service. Acronis Cyber Platform securely stores the credentials and sends a POST request to your callback handler. The POST request asks for the organization ID that uses these credentials in your cloud service.

Request
The callback request will:

Specify the cti.a.p.acgw.callback.v1.0~a.p.enablement.read.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.0~a.p.empty.v1.0 callback request type.
Omit the payload field.

The request can be represented with the following cURL command:

curl -i -s -X POST <callback_handler_url> \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <jwt>' \
--header 'X-CyberApp-Auth: base64(<identity>:<secret>)' \
--header 'X-CyberApp-Extra: base64(<json_extra_data>)' \
--data '{"type": "cti.a.p.acgw.request.v1.0~a.p.empty.v1.0", "request_id": "<request_id>", "created_at": "2023-04-10T15:33:01+00:00", "context": {"callback_id": "cti.a.p.acgw.callback.v1.0~a.p.enablement.read.v1.0", "endpoint_id": "<endpoint_id>", "tenant_id": "<acronis_tenant_id>", "datacenter_url": "<acronis_datacenter_url>"}}'



Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.0~a.p.enablement.read.ok.v1.0 response type.
Include the payload field with the partner organization ID that corresponds to the credentials provided in the CyberApp enablement form and, if present, an Acronis tenant ID that was mapped to it.
If the CyberApp was:

Not previously enabled, the payload field must include only the partner ID:

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.enablement.read.ok.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>",
"payload": {
"vendor_tenant_id": "<vendor_msp_organization_id>"
}
}


If the CyberApp was previously enabled, the payload field must also include the mapped Acronis tenant ID for this organization ID:

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
<...>

{
"type": "cti.a.p.acgw.response.v1.0~a.p.enablement.read.ok.v1.0",
"request_id": "<request_id>",
"response_id": "<response_id>",
"payload": {
"vendor_tenant_id": "<vendor_msp_organization_id>",
"acronis_tenant_id": "<acronis_msp_tenant_id>"
}
}