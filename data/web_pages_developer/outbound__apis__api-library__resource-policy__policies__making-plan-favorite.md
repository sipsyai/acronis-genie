---
title: "Making a protection plan a favorite"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/resource-policy/policies/making-plan-favorite.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:55.831420"
---

# Making a protection plan a favorite

Making a protection plan a favorite

Note
To find out more about favorite plans, see the Favorite plans chapter of the Acronis Cyber Protection User Guide.


Note

Only 10 plans may be configured as favorites.
To add multiple plans to favorites in one request, see the PATCH /policy_management/v4/policies/favorite endpoint in the Resource and Policy Management API reference.



To make a protection plan a favorite

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch the plan as described in Fetching a list of policies and protection plans, then
define the policy_id variable and assign it with the ID of the plan. As an example,
the ID of the first policy will be taken:
>>> policy_id = policies[0]['id']
>>> policy_id
33965f81-7293-45d4-9f13-dc4281d7bdfd



Define a variable named policy_favorite, and then assign an object with the subject key containing a policy to this variable:
>>> policy_favorite = {
...     "subject": {
...         "policy": [
...             {
...                 "default": true,
...                 "favorite": true,
...                 "favorite_order": 1
...             }
...         ]
...     }
... }



Note
For the list of available JSON parameters, see the Resource and Policy Management API reference.


Convert the policy_favorite object to a JSON text:
>>> policy_favorite = json.dumps(policy_favorite, indent=4)



Send a PATCH request with the JSON text to the /policy_management/v4/policies/{policy_id} endpoint:
>>> response = requests.patch(
...     f'{base_url}/policy_management/v4/policies/{policy_id}',
...     headers={'Content-Type': 'application/json', **auth},
...     data=policy_favorite,
... )



Check the status code of the response:
>>> response.status_code
204


Status code 204 means that the plan has been updated successfully.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.