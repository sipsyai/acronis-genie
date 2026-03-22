---
title: "Listening for the events"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/events/listening-for-events.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:22:02.311847"
---

# Listening for the events

Listening for the events

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/event_manager/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Before you start, fetch the subscription ID by following the Subscribing to the events procedure.
As a result, you should have the following variable available:
>>> topic_id
'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'
>>> subscription_id
'454e9a51-2207-4a2c-9db4-6ca168ac9597'



Generate or use a previously generated UUID for the consumer ID:
# NOTE: this is a placeholder for the actual implementation
>>> consumer_id = get_consumer_id()
>>> consumer_id
'5d0805ff-fa52-4175-abb1-c10061da437d'



Important
If you plan to read events using multiple instances, you must use different consumer ID
for each instance that will be reading the events. Only one instance will be able to receive
the events simultaneously within the session timeout specified in the subscription.


Specify an offset from which you will be listening the events. There are the following options:

To read the events starting from a specific position in history,
fetch a specific offset position to read the topics from:

Define a variable named params, and then assign with the ID of the topic to get the offset for to this variable:
>>> params = {
...     "topic_id": topic_id,
...     "position": "EARLIEST"
... }



Send a GET request to the /topics/{topic_id}/offsets endpoint:
>>> response = requests.get(f'{base_url}/topics/{topic_id}/offsets', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the earliest offset for the topic formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'offset': 0, 'topic_id': 'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'}



Store the offset in a variable for further use:
>>> offset = response.json()['offset']
>>> offset
0





If you are using a stateless consumer and want to continue reading from a previous known offset:

Define a variable named params, and then assign with the ID of the subscription to this variable:
>>> params = {
...     "subscription_id": subscription_id
... }



Send a GET request to the /subscriptions/offset endpoint:
>>> response = requests.get(f'{base_url}/subscriptions/offset', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains the current stored offset for the subscription formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'offset': 0, 'subscription_id': 'fd02a25c-fcb0-42a0-a5ce-56c1131db356'}



Store the offset in a variable for further use:
>>> offset = response.json()['offset']
>>> offset
0





If you are using a stateful consumer and want to continue reading from a previous known offset,
specify the offset that is stored in your persistent storage:
1# NOTE: this is a placeholder for the actual implementation
2offset = get_offset(consumer_id)





Define a variable named params, and then assign an object with the parameters for events listening to this variable:
>>> params = {
...     "subscription_id": subscription_id,
...     "consumer_id": consumer_id,
...     "offset": offset,
...     # "timeout": "PT30S", # Optional. The maximum time to wait for events in ISO 8601 duration format. Default is 30 seconds.
... }



Send a GET request to the /events endpoint.
The request will keep the connection open either until the events are received or the timeout is reached:
>>> response = requests.get(f'{base_url}/events', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful and events have been received.
Also, the response body contains an object containing the list of events formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{'events': [{'id': '9251fdc0-eb78-49b6-acaa-ed258074e4f5',
'ingest_time': '2024-10-01T11:01:16.070777369Z',
'previous': 93376477,
'sequence': 93376478,
'source': 'account-server',
'subject': '692ff7d2-8505-44ed-82b0-e82ee8d42ef2',
'tenant_id': '692ff7d2-8505-44ed-82b0-e82ee8d42ef2',
'time': '2024-10-01T11:01:16.03094914Z',
'type': 'cti.a.p.em.event.v1.0~a.p.tenant.disabled.v1.0'}],
'offset': 93376478}



In case you receive code 202, that means that there are no new events yet. You can retry the request after a period in seconds specified in the Retry-After header.
After you finished processing the events, you should store the offset for the next request:

If you are using a stateful consumer, store the offset in the persistent storage.
If you are using a stateless consumer without auto-commit, commit the offset by sending a POST request to /subscriptions/offset.
If you are using a stateless consumer with auto-commit, the offset is committed automatically.