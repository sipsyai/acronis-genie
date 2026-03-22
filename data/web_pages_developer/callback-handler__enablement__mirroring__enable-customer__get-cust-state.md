---
title: "Getting customer enablement status"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/enable-customer/get-cust-state.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:10.276182"
---

# Getting customer enablement status

Getting customer enablement status

To get customer enablement status

Request
When a partner opens the Customer Management tab in the CyberApp, the UI sends a callback request to load the information about the enablement status of its customers.
The callback request will:


Specify the cti.a.p.acgw.callback.v2.0~a.p.customer.mirroring.get_state.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.1~a.p.customer.mirroring.get_state.v1.0 request type.
Omit the payload field.


Example
{
"type": "cti.a.p.acgw.request.v1.1~a.p.customer.mirroring.get_state.v1.0",
"request_id": "ff2a71a4-ae4d-48a9-879a-35cab62d50be",
"created_at": "0001-01-01T00:00:00Z",
"context": {
"callback_id": "cti.a.p.acgw.callback.v2.0~a.p.customer.mirroring.get_state.v1.0",
"endpoint_id": "cti.a.p.acgw.endpoint.v1.0~yury_partner1_864.mirroring_test.endpoint.v1.0",
"tenant_id": "9ae2aada-2342-4fc0-8d92-007b597a7d9c",
"datacenter_url": "https://eu8.acronis.cloud"
}
}




Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.1~a.p.customer.mirroring.get_state.ok.v1.0 response type.

Include the payload field with the list of customers that have the CyberApp enabled.
The enablement information must include:




vendor_tenant_id
Vendor tenant ID that corresponds to this customer.



acronis_tenant_id
Acronis tenant ID that corresponds to this customer.



[If applicable] settings
Settings that were used to enable the customer.







Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.customer.mirroring.get_state.ok.v1.0",
"request_id": "dd7b46a3-9bdc-462a-ae0e-1019a4874d8a",
"response_id": "1ca896a3-7c1b-42d2-a828-dbea6c64dfcb",
"payload": [
{
"vendor_tenant_id": "2",
"acronis_tenant_id": "5a19bda3-c964-4e92-87ad-55c21df1285c",
"settings": {}
}
]
}