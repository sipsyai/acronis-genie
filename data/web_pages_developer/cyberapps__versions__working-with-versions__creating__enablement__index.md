---
title: "CyberApp enablement combinations"
source: "https://developer.acronis.com/doc/cyberapps/versions/working-with-versions/creating/enablement/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:09:18.543508"
---

# CyberApp enablement combinations

CyberApp enablement combinations
There are eight possible CyberApp enablement combinations.

Note
For callback handler details for each method, see Enabling the CyberApp in the callback handler chapter.


Mapped partner and customer enablement

Mapped enablement creates a connection between existing accounts on your cloud service and the Acronis partners and their customers who enable the CyberApp.
To set CyberApp enablement to this method, see Setting mapped partner and customer enablement.



Mapped partner and mirrored customer enablement

Mapped partner enablement creates a connection between existing accounts on your cloud service and the Acronis partners.
When the partner administrator enables the CyberApp for their customers, you must create an account for each customer on your cloud service.
To set CyberApp enablement to this method, see Setting mapped partner and customer enablement.



Mapped partner and explicit customer enablement

Mapped partner enablement creates a connection between existing accounts on your cloud service and the Acronis partners.
The Acronis customers are not required to have an account on your cloud service.
To set CyberApp enablement to this method, see Setting mapped partner and customer enablement.



Mirrored partner and mapped customer enablement

Mirrored partner enablement creates new accounts on your cloud service for Acronis partners who enable the CyberApp.
Mapped customer enablement creates a connection between existing accounts on your cloud service and the Acronis customers who enable the CyberApp.
To set CyberApp enablement to this method, see Setting mirrored partner and mapped customer enablement.



Mirrored partner and customer enablement

Mirrored partner and customer enablement creates new accounts on your cloud service for Acronis partners who enable the CyberApp and their customers.
The Acronis partner and their customers are not required to have an account on your cloud service.
To set CyberApp enablement to this method, see Setting mirrored partner and customer enablement.



Mirrored partner and explicit customer enablement

Mirrored partner and explicit customer enablement creates accounts on your cloud service for Acronis partners who enable the CyberApp. Customers work with Acronis data only.
The Acronis partner and their customers are not required to have an account on your cloud service.
To set CyberApp enablement to this method, see Setting mirrored partner and explicit customer enablement.



Explicit partner and mirrored customer enablement

With this enablement method, when the partner administrator enables the CyberApp, no account is required or created on your cloud service for the partner.
However, when the partner administrator enables the CyberApp for their customers, you must create an account for each customer on your cloud service.
To set CyberApp enablement to this method, see Setting explicit partner and mirrored customer enablement.



Explicit partner and customer enablement

Explicit enablement for partners and customers means both partners and their customers are enabled with Acronis data only. No information is sent to the vendor cloud service.
There is no communication with your cloud service when the partner administrator enables the CyberApp, and there is no communication with your cloud service when the partner administrator enables the CyberApp for a customer.



Important

If you use this enablement method, you do not need a callback handler for CyberApp enablement purposes.
However, if the CyberApp functionality uses callbacks, you must create a callback handler and provide the URL when setting this enablement method.



To set CyberApp enablement to this method, see Setting explicit partner and customer enablement.

In this section

Setting mapped partner and customer enablement
Setting mapped partner and mirrored customer enablement
Setting mapped partner and explicit customer enablement
Setting mirrored partner and mapped customer enablement
Setting mirrored partner and customer enablement
Setting mirrored partner and explicit customer enablement
Setting explicit partner and mirrored customer enablement
Setting explicit partner and customer enablement