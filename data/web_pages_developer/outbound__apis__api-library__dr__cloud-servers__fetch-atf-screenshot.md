---
title: "Fetch automated test failover screenshot"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/dr/cloud-servers/fetch-atf-screenshot.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:59.104262"
---

# Fetch automated test failover screenshot

Fetch automated test failover screenshot

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/dr/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Obtain scoped access token for the customer tenant.
As a result, the following variables should be available:
>>> scoped_auth # the 'Authorization' header value with the scoped access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the information about the recovery server by its ID and store the information in the recovery_server variable.
>>> recovery_server = response.json()



In the automated_test_failover field:

Check the screenshot_link link for full-size of the automated test failover result:
>>> screenshot_link = recovery_server['automated_test_failover']['screenshot_link']



Check the screenshot_preview_link for a preview of the automated test failover result:
>>> screenshot_link = recovery_server['automated_test_failover']['screenshot_preview_link']





If the screenshot_link is not None, you can use it to download and view the automated test failover result, or open in a web browser.
>>> if screenshot_link is not None:
...     print(f"Full-size screenshot: {screenshot_link}")
... else:
...     print("No screenshot available.")