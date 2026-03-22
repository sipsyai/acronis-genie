---
title: "Revoking protection plans from resources"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/revoking-plan-from-resources.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:04.262498"
---

# Revoking protection plans from resources

Revoking protection plans from resources

To revoke protection plans from resources

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



Fetch the resources as described in Fetching a list of all resources, then define the
resource_id variable and assign it with the ID of a resource. As an example, the ID of the
first resource will be taken:
>>> resource_id = resources[0]['id']
>>> resource_id
'5c350066-2ba6-4eeb-aa91-1213dd35f033'



Define a variable named filters, and then assign an object with the policy_id key containing the ID of the policy, and the context key containing the ID of the resource to this variable:
>>> filters = {
...     'policy_id': policy_id,
...     'context_id': resource_id
... }


For the list of available query string parameters, see the Resource and Policy Management API reference.

Note
To revoke plans from multiple resources, provide the values in the following format:
or(33965f81-7293-45d4-9f13-dc4281d7bdfd,c70134c4-a244-4b22-99ad-e081301f7530)


Send a DELETE request to the /policy_management/v4/applications endpoint:
>>> response = requests.delete(
...     f'{base_url}/policy_management/v4/applications',
...     headers=auth,
...     params=filters,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the protections plans has been revoked from provided resources.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.