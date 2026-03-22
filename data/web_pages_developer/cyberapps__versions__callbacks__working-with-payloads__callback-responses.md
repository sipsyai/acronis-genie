---
title: "Adding a response payload"
source: "https://developer.acronis.com/doc/cyberapps/versions/callbacks/working-with-payloads/callback-responses.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:00:40.893607"
---

# Adding a response payload

Adding a response payload

Note

If the Version is in the Draft state, and you have the appropriate Vendor Portal account type, you can open and edit the Version.
Otherwise, you can only view the Version details.
For more information on Version states, see Version approval process.



To add a response payload

Open the callback.
Select the RESPONSES tab.


Click Add response.



Specify a unique Identifier.
You will need the CTI to use in the callback handler.



[Optional] Enter a Response name.
This helps you identify responses if the callback has multiple.


Enter a unique HTTP code.
Compose the JSON schema for the payload.

Important
If you leave the payload structure empty, the response will not include the payload field.


[Optional] Repeat the steps for each required response.
[Optional] To delete a response, click the response’s  button.
Click Save changes.