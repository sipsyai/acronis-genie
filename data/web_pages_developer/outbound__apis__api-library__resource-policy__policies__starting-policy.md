---
title: "Start execution of a policy"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/starting-policy.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:08.471274"
---

# Start execution of a policy

Start execution of a policy

To start execution of a policy

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



Note
Execution of the policy.protection.total policy will start execution of its enabled children policies.


[Optional] Fetch the resources as described in Fetching a list of all resources, then define the
resource_id variable and assign it with the ID of a resource. As an example, the ID of the
first resource will be taken:
>>> resource_id = resources[0]['id']
>>> resource_id
'5c350066-2ba6-4eeb-aa91-1213dd35f033'



Note
If resources are not specified in the request, the policy will be executed on all resources to which it is applied.


Define a variable named policy_exec_data, and then assign an object containing the following JSON parameters to this variable:
>>> policy_exec_data = {
...     'state': 'running',
...     'policy_id': policy_id,
...     'context_ids': [resource_id]
... }



Note
For the list of available JSON parameters, see the Resource and Policy Management API reference.


Convert the policy_exec_data object to a JSON text:
>>> policy_exec_data = json.dumps(policy_exec_data, indent=4)



Send a PUT request with the JSON text to the /policy_management/v4/applications/run endpoint:
>>> response = requests.put(
...     f'{base_url}/policy_management/v4/applications/run',
...     headers={'Content-Type': 'application/json', **auth},
...     data=policy_exec_data,
... )



Check the status code of the response:
>>> response.status_code
202


Status code 202 means that the request was successful.
#.  Check the status code of the response:

>>> response.status_code
202



Status code 202 means that the request was successful.
If you received error code 422 and RunNowRespBody contains a message related to application status or licensing, ensure that the provided policy is enabled and the resource has correct service quota assigned.



Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.