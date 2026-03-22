---
title: "Enabling customers using mirroring"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/enable-customer/enable-customer.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:06.075822"
---

# Enabling customers using mirroring

Enabling customers using mirroring

To enable partner customers using mirroring

Request
When an Acronis partner selects a customer and enables the CyberApp for them on the Customer Management tab, the UI sends a callback request to write the information about the customer enablement status.
The callback request will:


Specify the cti.a.p.acgw.callback.v2.0~a.p.customer.mirroring.set_state.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.1~a.p.customer.mirroring.set_state.v1.0 request type.


If the partner enables customers, the payload will include the enabled field with a list of customer tenant IDs in Acronis.
Example
{
"request_id": "ff2a71a4-ae4d-48a9-879a-35cab62d50be",
"type": "cti.a.p.acgw.request.v1.1~a.p.customer.mirroring.set_state.v1.0",
"payload": {
"partner_tenant_id": "999d63d2-831e-40b9-aaab-16f919a483d0",
"partner_tenant_name": "yury_partner11_864",
"enabled": [
{
"acronis_tenant_id": "18a55fe8-7275-478c-a54e-af2ed53b6a20",
"acronis_tenant_name": "yury_customer11_864"
}
]
},
"context": {
"callback_id": "cti.a.p.acgw.callback.v2.0~a.p.customer.mirroring.set_state.v1.0",
"endpoint_id": "cti.a.p.acgw.endpoint.v1.1~yury_partner1_864.mirroring_test.endpoint.v1.1",
"tenant_id": "999d63d2-831e-40b9-aaab-16f919a483d0",
"datacenter_url": "https://eu8.acronis.cloud"
},
"created_at": "0001-01-01T00:00:00Z"
}




Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.1~a.p.customer.mirroring.set_state.ok.v1.0 response type.
Omit the payload field.


Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.customer.mirroring.set_state.ok.v1.0",
"request_id": "eb768938-dbb6-4a5c-aae1-23cebfac7f26",
"response_id": "6eb3efde-8071-40ab-b820-6e749a2dafd6"
}