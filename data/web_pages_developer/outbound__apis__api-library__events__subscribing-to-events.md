---
title: "Subscribing to the events"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/events/subscribing-to-events.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:06.516753"
---

# Subscribing to the events

Subscribing to the events

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/event_manager/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Before you start, fetch the list of event types by following the Fetching event topics and types procedure.
As a result, you should have the following variables available:
>>> topic_id # identifier of the topic to subscribe to
'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'
>>> event_types # list of event types to subscribe to
['cti.a.p.em.event.v1.0~a.p.tenant.barrier_updated.v1.0', 'cti.a.p.em.event.v1.0~a.p.tenant.created.v1.0']



Generate or use a previously generated UUID for the subscription ID:
# NOTE: this is a placeholder for the actual implementation
>>> subscription_id = get_subscription_id()
>>> subscription_id
'454e9a51-2207-4a2c-9db4-6ca168ac9597'



Important

If you are using a stateless consumer, you should keep the subscription ID in a persistent storage
to be able to manage the reading offset.
If you plan to read events using multiple instances, you must use the same subscription ID
for all instances that will be reading the events.



Define a variable named sub_data, and then assign with an object containing the information about the subscription to this variable:
>>> sub_data = {
...     "subscription_id": subscription_id,
...     "tenant_depth": "DIRECT", # or "ALL", or "CURRENT"
...     "auto_commit": false,
...     "types": event_types,
...     "topic_id": topic_id,
...     "session_timeout": "PT5M", # Optional. Session timeout in ISO 8601 duration format. Default is PT5M.
...     "tenant_id": "e34745c5-9c29-4a08-8936-870c12aab6df"
... }



Note

If you are using a stateless consumer, you may specify whether to auto-commit the offset or not.
The offset can be obtained by sending a GET request to /subscriptions/offset?subscription_id=<uuid>.
If you are using a stateful consumer, you should not auto-commit the offset and store it in a persistent storage instead.
If you are using multiple instances, the first instance that reads the event
will be able to continue reading the events within the specified session timeout.
Other instances will have to wait until the session timeout expires.
You may create and manage multiple subscriptions that specify different parameters and offsets if necessary.



[Optional] To filter events by specific content, you may use Common Expression Language (CEL).
Add the cel field to the sub_data object and specify CEL expression:
>>> sub_data['cel'] = 'event.client_id == "e34745c5-9c29-4a08-8936-870c12aab6df"'


Note that event object is addressed using the event keyword.

Convert the sub_data object to a JSON text:
>>> sub_data = json.dumps(sub_data, indent=4)



Send a POST request with the JSON text to the /subscriptions endpoint:
>>> response = requests.post(
...     f'{base_url}/subscriptions',
...     headers={'Content-Type': 'application/json', **auth},
...     data=sub_data,
... )



Check the status code of the response:
>>> response.status_code
201


Status code 201 means that the request was successful.
Also, the response body contains the subscription was created formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"subscription_id": "454e9a51-2207-4a2c-9db4-6ca168ac9597",
"topic_id": "cti.a.p.em.topic.v1.0~a.p.tenant.v1.0",
"types": [
"cti.a.p.em.event.v1.0~a.p.tenant.enabled.v1.0",
"cti.a.p.em.event.v1.0~a.p.tenant.disabled.v1.0"
],
"tenant_id": "e5afb5e8-84b6-415b-969d-bc10d19f3301",
"tenant_depth": "ALL",
"auto_commit": false,
"session_timeout": "PT5M"
}