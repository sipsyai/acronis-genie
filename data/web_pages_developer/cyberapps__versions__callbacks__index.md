---
title: "Callbacks"
source: "https://developer.acronis.com/doc/cyberapps/versions/callbacks/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:00:28.097419"
---

# Callbacks

Callbacks

CyberApps exchange data between Acronis and the ISV cloud service using callbacks.
The callback handler receives callbacks and performs the appropriate corresponding actions on ISV cloud service data.
Callbacks include a request payload, which provides data to the callback handler, and/or one or more response payloads, which send data back to the CyberApp.

There are two callback types:



Pre-defined Acronis callbacks for CyberApp enablement.
Custom CyberApp callbacks for UI.



CyberApp users can trigger a custom callback in UI forms when the form is opened (these callbacks are called the data initializer callbacks), or when some user action occurs, such as clicking a button.
For example, you might create a data initializer callback to fetch a list from the ISV cloud platform, then display data from this list in a form table when the CyberApp user opens the form.
You might also create another custom callback to create a new list entry using data from input controls when a user clicks a button on the form.



In this section

Opening the callback list
Adding a callback
Working with callback payloads
Editing a callback
Deleting a callback