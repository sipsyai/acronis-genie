---
title: "Disabling a mirrored partner"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/disable-partner.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:01.877641"
---

# Disabling a mirrored partner

Disabling a mirrored partner

To disable a mirrored partner

Request

If a partner disables the CyberApp, the UI sends a callback request to disable the partner tenant.
Your callback handler must take the tenant ID from context.tenant_id and pass it to your service.
Your service must find the record associated with the Acronis tenant ID and set its status to DISABLED.


Important
Additionally, your service must disable all customers related to that partner.

The callback request will:


Specify the cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.reset.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.reset.v1.0 request type.
Omit the payload field.


Example
{
"request_id": "474ee7c0-e058-42bc-95ce-e7c0e12550cb",
"type": "cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.reset.v1.0",
"context": {
"callback_id": "cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.reset.v1.0",
"endpoint_id": "cti.a.p.acgw.endpoint.v1.1~yury_partner1_864.mirroring_test.endpoint.v1.1",
"tenant_id": "999d63d2-831e-40b9-aaab-16f919a483d0",
"datacenter_url": "https://eu8.acronis.cloud"
},
"created_at": "0001-01-01T00:00:00Z"
}




Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.reset.ok.v1.0 response type.
Omit the payload field.


Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.reset.ok.v1.0",
"request_id": "a123053b-f91b-43cd-b08a-d9f80c355f65",
"response_id": "db3c7133-d4a5-47f1-8b2a-c2e32b7eaf00"
}