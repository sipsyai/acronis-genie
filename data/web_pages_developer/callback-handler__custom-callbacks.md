---
title: "Custom callbacks"
source: "https://developer.acronis.com/doc/callback-handler/custom-callbacks.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:51:02.433680"
---

# Custom callbacks

Custom callbacks

To support data interaction with your cloud service (for example, creating a new user), you can create custom callbacks, and programmatically support them in your callback handler.
For example, CyberApp UI forms can have:



Data initializer callbacks.
The callback response of this custom callback provides data from your cloud service to the form when a user opens it.
For more information, see Mapping a data initializer callback.



On click callbacks for buttons.
These allow the user to manage data on a form, to submit form data to your cloud service, etc.




Important
As with standard callbacks, before processing a custom callback request from the CyberApp, your callback handler must verify the origin of the request.


Note

All callback requests include Acronis tenant ID in the context.tenant_id field. See Callback request format for more information.
The callback handler must verify that the mapping is present for the tenant and, if necessary, limit the operation/returned data to that tenant.



Example
Consider the following main menu item in Acronis Management menu:




In this form, the specified data initializer callback request is sent to the callback handler when the page is loading, and a table is populated with data received in the data initializer callback response.
There are two action buttons:



The Create user button opens a dependent form.
The user enters data in the dependent form, which is sent to your cloud service in an On click callback request when the user clicks the appropriate button on the dependent form.



The Re-invite user button sends an On click callback request when the user clicks it.
The callback handler receives the callback request and acts accordingly.


Note

In the screenshot, this button is not enabled. It is enabled when the user selects at least one row. For more information, see Building element visibility logic.




Additionally, if a button’s On click callback request results in updated data on the cloud service, and this updated data should be reflected on the form, the On click callback response might include the updated data, which will refresh data displayed to the user on the form.


Note
For more information, see the Mapping and Callbacks sections.