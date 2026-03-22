---
title: "Mirrored enablement"
source: "https://developer.acronis.com/doc/callback-handler/enablement/mirroring/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:31.520067"
---

# Mirrored enablement

Mirrored enablement
With partner and/or customer mirroring, neither the partner nor their customers have an account on your cloud service.
Instead, you mirror their accounts on your service, with a direct relationship between the Acronis tenant and the new tenant on your system.


Verifying callback requests
Since they do not have any credentials on your service, you must identify and verify the requests coming from Acronis.

Important
Your callback handler must verify every callback request.

When the callback request is successfully verified, you can fetch the Acronis tenant ID from context.tenant_id and check your data against this tenant ID.

In this section

Mirrored partner enablement
Mirrored customer enablement
Disabling a mirrored partner
Disabling mirrored customers