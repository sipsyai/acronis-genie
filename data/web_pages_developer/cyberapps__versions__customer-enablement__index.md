---
title: "Customer enablement form"
source: "https://developer.acronis.com/doc/cyberapps/versions/customer-enablement/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:01:29.058003"
---

# Customer enablement form

Customer enablement form
In the Customer enablement form menu item, you use the UI builder to
build an activation form which is presented to Acronis customer administrators as a pop-up when they click Activate on your CyberApp catalog card.

Important

Customer enablement form is not available if you set the CyberApp enablement method to mapping.
For more information, see Choosing and setting the CyberApp enablement method.


After a customer administrator activates your CyberApp, they can still access the form (to change or update credentials, for example) in the Settings tab of the CyberApp configuration UI.
They access the CyberApp configuration UI by clicking Manage on your CyberApp’s In use catalog card.

Note
Customer enablement form is a single form. You cannot create any dependent forms for it.

Acronis Cyber Protect Cloud displays the customer enablement form with:


The CyberApp name as the title of the form.
A Cancel button to close the form.
A Connect button to send the credentials and other user-supplied data, and activate the CyberApp.



Note
After activation, when the customer enablement form is displayed in the Settings tab, an additional button is included at the top of the form for the administrator to deactivate the CyberApp.


Example
A typical customer enablement form might also include:

A Text element to include connection instructions or information about the CyberApp.
An Input element to accept an identity registered on the ISV service (such as username, API client ID, etc.).
A Password element to accept a secret bound to the identity (such as a password, private key, etc.).



Note
See building the example for a step-by-step guide on how to build this form.


In this section

Creating the customer enablement form
Building the example