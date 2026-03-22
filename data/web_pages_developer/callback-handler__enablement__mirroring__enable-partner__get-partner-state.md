---
title: "Getting partner enablement state"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/enable-partner/get-partner-state.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:22.919629"
---

# Getting partner enablement state

Getting partner enablement state

To get partner enablement state

Request

When the CyberApp is enabled by an partner, the UI sends a callback request to check the state of the partner enablement.
Your callback handler must take the tenant ID from context.tenant_id and pass it to your service to check whether it is currently enabled.

The callback request will:


Specify the cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.get_state.v1.0 callback identifier.
Specify the cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.get_state.v1.0 request type.
Omit the payload field.


Example
{
"type": "cti.a.p.acgw.request.v1.1~a.p.partner.mirroring.get_state.v1.0",
"request_id": "14ba57f7-b28c-4e5f-b1ae-55eba40a8502",
"created_at": "2024-05-17T13:46:29.362Z",
"context": {
"callback_id": "cti.a.p.acgw.callback.v2.0~a.p.partner.mirroring.get_state.v1.0",
"endpoint_id": "cti.a.p.acgw.endpoint.v1.0~wasabi_technologies.wasabi_qa.endpoint.v1.0",
"tenant_id": "9ae2aada-2342-4fc0-8d92-007b597a7d9c",
"datacenter_url": "https://eu8.acronis.cloud"
},
"payload": {}
}




Response
The callback response code must be 200, and the response body must:


Specify the cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.get_state.ok.v1.0 response type.
Include the payload field with the state field set to the corresponding enablement status.


If the CyberApp was not previously enabled, the payload field must include the state field set to DISABLED.
Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.get_state.ok.v1.0",
"request_id": "14ba57f7-b28c-4e5f-b1ae-55eba40a8502",
"response_id": "cd03f831-8437-44eb-adea-094749e24f5f",
"payload": {
"state": "DISABLED"
}
}


If the CyberApp was already enabled, the payload field must include the state field set to ENABLED.
Example
{
"type": "cti.a.p.acgw.response.v1.1~a.p.partner.mirroring.get_state.ok.v1.0",
"request_id": "14ba57f7-b28c-4e5f-b1ae-55eba40a8502",
"response_id": "cd03f831-8437-44eb-adea-094749e24f5f",
"payload": {
"state": "ENABLED"
}
}