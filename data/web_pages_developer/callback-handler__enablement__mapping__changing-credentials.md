---
title: "Changing CyberApp credentials"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mapping/changing-credentials.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:11.182136"
---

# Changing CyberApp credentials

Changing CyberApp credentials

Note
This procedure uses the same cti.a.p.acgw.callback.v1.0~a.p.enablement.write.v1.0 callback as described in Mapping the partner ID to the Acronis tenant ID.

A partner can change the credentials that were used to enable the CyberApp. When the partner
sends a request to change the credentials, your callback handler will receive a request containing:

An X-CyberApp-Auth header with updated credentials.
A payload that:


Specifies the cti.a.p.acgw.callback.v1.0~a.p.enablement.write.v1.0 callback identifier.
Specifies the cti.a.p.acgw.request.v1.0~a.p.enablement.write.v1.0 callback request type.
Contains the payload field with information about the mapping.




{
"type": "cti.a.p.acgw.request.v1.0~a.p.enablement.write.v1.0",
"request_id": "<request_id>",
"created_at": "2023-04-10T15:33:01+00:00",
"context": { ... },
"payload": {
"vendor_tenant_id": "<vendor_msp_organization_id>",
"acronis_tenant_id": "<acronis_msp_tenant_id>"
}
}


The callback handler must ensure that the credentials belong to the same partner ID. The request must be denied
in case the credentials belong to a different partner ID.