---
title: "Tracking the execution progress of a policy"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/tracking-policy-progress.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:26:12.688710"
---

# Tracking the execution progress of a policy

Tracking the execution progress of a policy

To track the execution progress of a policy

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



[Optional] To get a unique result, fetch the resources as described in Fetching a list of all resources,
then define the agent_id variable and assign it with the ID of the agent of a resource. As an example, the
agent ID of the first resource will be taken:
>>> agent_id = resources[0]['agent_id']
>>> agent_id
'23effcf6-2798-4631-9a52-5785bf3af657'



Define a variable named filters, and then assign an object containing the ID of the policy in the policy_id key and ID of the agent in the agent_id key to this variable:
>>> filters = {
...     'policy_id': policy_id,
...     'agent_id': agent_id
... }



Note
For the list of available query string parameters, see the Resource and Policy Management API reference.


Send a GET request to the /policy_management/v4/applications endpoint:
>>> response = requests.get(
...     f'{base_url}/policy_management/v4/applications',
...     headers=auth,
...     params=filters,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with the items key containing an array with application objects as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'items': [{...
'agent_id': '23effcf6-2798-4631-9a52-5785bf3af657',
'context': {'id': '5c350066-2ba6-4eeb-aa91-1213dd35f033',
'type': 'resource.machine'},
'context_tenant_id': '17',
'id': 'e8987b4d-d191-4751-baae-1aae6d4f36c1',
'last_activity': 'policy.security.patch_management',
'last_runtime': '2020-10-08T15:04:43.2648116Z',
'next_activity': 'policy.security.patch_management',
'next_run_time': '2020-10-12T12:10:00Z',
'origin_contexts': ['5c350066-2ba6-4eeb-aa91-1213dd35f033'],
'policy': {'id': '33965f81-7293-45d4-9f13-dc4281d7bdfd',
'name': '',
'type': 'policy.security.patch_management'},
'running': {'progress': '0', 'state': 'running'},
'status': 'running',
'tenant_id': '16'},
...]}



Iterate over the items array and check the status in the status field and the value of the progress
field in the running object of the application(s):
>>> for application in applications:
...     print(f'Status of the {application['policy']['type'] policy is {application['status']}}')
...     if application['status'] == 'running':
...         print(f'Current progress is {application['running']['progress']}%')