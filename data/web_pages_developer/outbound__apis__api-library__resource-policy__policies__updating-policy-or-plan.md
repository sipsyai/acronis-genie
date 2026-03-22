---
title: "Updating a policy or protection plan"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/updating-policy-or-plan.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:16.890474"
---

# Updating a policy or protection plan

Updating a policy or protection plan

To update a policy or protection plan

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the protection policies as described in Fetching a list of policies and protection plans, then
define the policy_id variable and assign it with the ID of a protection policy. As an example,
the ID of the first policy will be taken:
>>> policy_id = policies[0]['id']
>>> policy_id
33965f81-7293-45d4-9f13-dc4281d7bdfd



Define a variable named policy_status, and then assign an object with the subject key containing a policy to this variable:
>>> policy_status = {
...     "subject": {
...         "policy": [
...             {
...                 "enabled": true
...             }
...         ]
...     }
... }



Note
For the list of available JSON parameters, see the Resource and Policy Management API reference.


Convert the policy_status object to a JSON text:
>>> policy_status = json.dumps(policy_status, indent=4)



Send a PATCH request with the JSON text to the /policy_management/v4/policies/{policy_id} endpoint:
>>> response = requests.patch(
...     f'{base_url}/policy_management/v4/policies/{policy_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=policy_status,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the plan has been updated successfully.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.