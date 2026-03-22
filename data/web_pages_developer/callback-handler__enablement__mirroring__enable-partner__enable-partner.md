---
title: "Enabling a partner using mirroring"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/enable-partner/enable-partner.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:18.699929"
---

# Enabling a partner using mirroring

Enabling a partner using mirroring

To enable a partner using mirroring

Request

When the state of partner enablement is checked, a callback request to enable the CyberApp will be sent.
Your callback handler must take the tenant ID from context.tenant_id and pass it to your service.
Your service must create a new record in the database (or update an existing DB record) for this partner_tenant_id.

The callback request will:


Specify the cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.enable.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.enable.v1.0 request type.
The payload field will include acronis_tenant_id and acronis_tenant_name of the partner that is being enabled.


Example
{
"request_id": "76c9fb58-58d9-4264-96a7-1d0b479b2ba7",
"type": "cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.enable.v1.0",
"payload": {
"acronis_tenant_id": "999d63d2-831e-40b9-aaab-16f919a483d0",
"acronis_tenant_name": "yury_partner11_864"
},
"context": {
"callback_id": "cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.enable.v1.0",
"endpoint_id": "cti.a.p.acgw.endpoint.v1.1~yury_partner1_864.mirroring_test.endpoint.v1.1",
"tenant_id": "999d63d2-831e-40b9-aaab-16f919a483d0",
"datacenter_url": "https://eu8.acronis.cloud"
},
"created_at": "0001-01-01T00:00:00Z"
}




Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.enable.ok.v1.0 response type.
Include the payload field with:


state set to ENABLED
vendor_tenant_id set to the identifier of the tenant created for the partner in your system.
acronis_tenant_id set to the UUID of the partner’s tenant that enabled the CyberApp.





Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.enable.ok.v1.0",
"request_id": "8636ef5c-abec-4218-8b77-8b3b2ddf06ac",
"response_id": "9bffdbe7-1d32-42fc-8a37-4531c77a677e",
"payload": {
"state": "ENABLED",
"vendor_tenant_id": "1",
"acronis_tenant_id": "9ae2aada-2342-4fc0-8d92-007b597a7d9c"
}
}