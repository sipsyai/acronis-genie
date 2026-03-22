---
title: "The callback handler"
source: "https://developer.acronis.com/doc/callback-handler/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:57.026732"
---

# The callback handler

The callback handler
To manage communication and data exchange between the Acronis platform and your cloud service, you must create a callback handler.
A callback handler is an API endpoint that accepts HTTP requests (called callbacks) from the Acronis Cyber Platform’s API Callback Gateway, processes them according to
the specified format, sends the corresponding action to be executed by your service, and returns the operation result.

The Acronis Cyber Platform’s API Callback Gateway receives an HTTP request from a user and sends it to your callback handler URL.
Your callback handler receives the HTTP request from Acronis API Callback Gateway and responds in a specific format.


Note
For more information on callbacks, see the callbacks chapter.


Simplified flow




In this section

Basic requirements
Callback formats
Verifying callback requests
Enabling the CyberApp
Custom callbacks
Callback error handling
Callback handler verification
Sample code in GitHub