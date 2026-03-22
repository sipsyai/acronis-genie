---
title: "Enabling the CyberApp"
source: "https://developer.acronis.com/doc/callback-handler/enablement/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:06.635029"
---

# Enabling the CyberApp

Enabling the CyberApp
The callback handler must be able to manage predefined callback requests sent from Acronis API Callback Gateway when an Acronis partner enables the CyberApp for their organization and/or for their customers from an Acronis integration catalog.

Note

The callbacks depend on the enablement method the CyberApp uses.
You specify the CyberApp enablement method when you create a CyberApp Version.
If you decide to change the enablement method, you can do so in the General Settings section when you edit a CyberApp Version.



Enablement methods
There are eight enablement methods you can use for the CyberApp. This section examines these methods, and provides technical details of the callbacks involved.

Mapped partner and customer enablement

Mapped enablement creates a connection between existing accounts on your cloud service and the Acronis partners and their customers who enable the CyberApp.

The Acronis partner has a pre-existing account on your service. When the partner administrator enables the CyberApp, they must provide credentials for this account.
The account on your cloud service and Acronis platform are then mapped.
For details, see Mapped partner enablement.

If the partner administrator enables the CyberApp for their customers, the customers must have accounts on your cloud service also.
The customer accounts on your cloud service and the customer accounts on Acronis platform are then mapped.
For details, see Mapped customers enablement.



Mapped partner and mirrored customer enablement

Mapped partner enablement creates a connection between existing accounts on your cloud service and the Acronis partners who enable the CyberApp.

The Acronis partner has a pre-existing account on your service. When the partner administrator enables the CyberApp, they must provide credentials for this account.
The account on your cloud service and Acronis platform are then mapped.
For details, see Mapped partner enablement.

Mirrored customer enablement creates new accounts on your cloud service for the Acronis partner customers.
The Acronis partner customers are not required to have an account on your cloud service.

When the partner administrator enables the CyberApp for their customers, you must create an account on your cloud service for each customer.
There is a direct relationship between the Acronis partner customers and the new accounts on your system.
For details, see Mirrored customer enablement.



Mapped partner and explicit customer enablement

Mapped partner enablement creates a connection between existing accounts on your cloud service and the Acronis partners who enable the CyberApp.

The Acronis partner has a pre-existing account on your service. When the partner administrator enables the CyberApp, they must provide credentials for this account.
The account on your cloud service and Acronis platform are then mapped.
For details, see Mapped partner enablement.

When the partner administrator enables the CyberApp for their customers, no account is required or created on your cloud service for the customer.
No callback request is sent to your callback handler at this time, and no action is required on your cloud service.



Mirrored partner and mapped customer enablement

Mirrored partner enablement creates new accounts on your cloud service for Acronis partners who enable the CyberApp.
The Acronis partner is not required to have an account on your cloud service.

When the partner administrator enables the CyberApp, you must create an account on your cloud service for the partner.
There is a direct relationship between the Acronis partner and the new account on your system.
For details, see Mirrored partner enablement.

If the partner administrator enables the CyberApp for their customers, the customers must have accounts on your cloud service also.
The customer accounts on your cloud service and the customer accounts on Acronis platform are then mapped.
For details, see Mapped customers enablement.



Mirrored partner and customer enablement

Mirrored partner and customer enablement creates new accounts on your cloud service for Acronis partners who enable the CyberApp and their customers.
The Acronis partner and their customers are not required to have an account on your cloud service.

When the partner administrator enables the CyberApp, you must create an account on your cloud service for the partner.
There is a direct relationship between the Acronis partner and the new account on your system.
For details, see Mirrored partner enablement.

When the partner administrator enables the CyberApp for their customers, you must create an account on your cloud service for each customer.
There is a direct relationship between the Acronis partner customers and the new accounts on your system.
For details, see Mirrored customer enablement.



Mirrored partner and explicit customer enablement

Mirrored partner and explicit customer enablement creates accounts on your cloud service for Acronis partners who enable the CyberApp. Customers work with Acronis data only.
The Acronis partner and their customers are not required to have an account on your cloud service.

When the partner administrator enables the CyberApp, you must create an account on your cloud service for the partner.
There is a direct relationship between the Acronis partner and the new account on your system.
For details, see Mirrored partner enablement.

When the partner administrator enables the CyberApp for their customers, no account is required or created on your cloud service for the customer.
No callback request is sent to your callback handler at this time, and no action is required on your cloud service.



Explicit partner and mirrored customer enablement

With this enablement option combination, when the partner administrator enables the CyberApp, no account is required or created on your cloud service for the partner.
No partner enablement callback request is sent to your callback handler, and no action is required on your cloud service at that time.

However, when the partner administrator enables the CyberApp for their customers, you must create an account for each customer on your cloud service.
There is a direct relationship between the Acronis partner customers and the new accounts on your system.
For details, see Mirrored customer enablement.



Explicit partner and customer enablement

Explicit enablement for partners and customers means both partners and their customers are enabled with Acronis data only. No information is sent to the vendor cloud service.
There is no communication with your cloud service when the partner administrator enables the CyberApp, and there is no communication with your cloud service when the partner administrator enables the CyberApp for a customer.
Therefore, you do not need a callback handler for enablement purposes.


Important
If you want to use custom callbacks for CyberApp functionality, you must create a callback handler to manage those callback requests.


In this section

Mapped enablement
Mirrored enablement