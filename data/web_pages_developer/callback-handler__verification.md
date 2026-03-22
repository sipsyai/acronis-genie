---
title: "Callback handler verification"
source: "https://developer.acronis.com/doc/callback-handler/verification.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:53:05.432388"
---

# Callback handler verification

Callback handler verification
Acronis must verify your callback handler before you can deploy a CyberApp to any production data centers.

Note
Verification of custom callbacks is out of the callback handler verification scope.


Verification checks
For callback handler verification, the following checks are made:


Enablement and disablement works via UI
[For mapping enablement]




Enable CyberApp for a test partner.
Map a test customer.
Remove mapping.
Disable the CyberApp for the test partner.


Note
You must provide the name of the test partner account and the corresponding credentials for that test partner on the ISV system.






[For mirroring enablement]



Enable CyberApp for a test partner.
Enable the CyberApp for a test customer.
Disable the CyberApp for a test customer.
Disable the CyberApp for the test partner.


Note
You must provide the name of the test partner account.








Callback handler checks credentials
[For mapping enablement] Check that, at partner enablement, the callback handler does not accept a wrong user or password.
[For mirroring enablement] Not applicable.



Callback handler checks the presence of the Authorization header
[For both enablement methods] Check that callback handler does not accept requests without ‘Authorization: Bearer …’ header.



Callback handler verifies the content of the Authorization header
[For both enablement methods] Check that callback handler does not accept requests with an incorrect token in ‘Authorization: Bearer …’ header:



Corrupted token.
Valid, but issued for another CyberApp.






Verification preparation Postman collection
We provide a Postman collection that you can use to prepare for Acronis verification.
The collection includes tests for CyberApp enablement requests for both customer mapping and customer mirroring.
The requests include tests that verify whether the callback corresponds to the defined contract. The tests verify:


Response payload.
Received callback ID.
Response code.