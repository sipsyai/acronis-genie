---
title: "Applying a protection plan to resources"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/applying-plan-to-resources.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:22.135576"
---

# Applying a protection plan to resources

Applying a protection plan to resources

To apply a protection plan to resources

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



Define a variable named application_data, and then assign an object containing the policy_id key with the ID of protection plan, and the context object with the items key containing a list of resource IDs to this variable:
>>> application_data = {
...     'policy_id': policy_id,
...     'context': {
...         'items': [
...             resource_id
...         ]
...     }
... }



Convert the application_data object to a JSON text:
>>> application_data = json.dumps(application_data, indent=4)



Send a POST request with the JSON text to the /policy_management/v4/applications endpoint:
>>> response = requests.post(
...     f'{base_url}/policy_management/v4/applications',
...     headers={'Content-Type': 'application/json', **auth},
...     data=application_data,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the protection plan has been applied to provided resources.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the issues key, containing an empty array, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'issues': []}