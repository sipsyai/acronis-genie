---
title: "Deleting a protection plan"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/deleting-plan.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:30.563950"
---

# Deleting a protection plan

Deleting a protection plan

To delete a protection plan

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the protection plans as described in Fetching a list of policies and protection plans, then
define the policy_id variable and assign it with the ID of a protection plan. As an example,
the ID of the first protection plan will be taken:
>>> policy_id = protection_plans[0]['id']
>>> policy_id
5b15f6e1-88ec-4dce-b523-0e8394c0bc19



Send a DELETE request to the /policy_management/v4/policies/{policy_id} endpoint:
>>> response = requests.delete(f'{base_url}/policy_management/v4/policies/{policy_id}', headers=auth)



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the protection plan has been successfully deleted.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.