---
title: "Fetching event topics and types"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/events/fetching-topics-events.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:21:53.902291"
---

# Fetching event topics and types

Fetching event topics and types

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/event_manager/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Define a variable named topic_id, and then assign with the ID of the topic to get the event types for to this variable:
>>> topic_id = 'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'



Send a GET request to the /topics endpoint:
>>> response = requests.get(f'{base_url}/topics', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of available event topics formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
[{'archive_consolidation': 'NONE',
'description': "Task manager's events topic",
'id': 'cti.a.p.em.topic.v1.0~a.p.task.v1.0',
'ordering': 'EVENTMANAGER',
'persistency': True,
'producer_consolidation': 'NONE',
'retention': 'P7D'},
{'archive_consolidation': 'TTS',
'description': "Account Server's tenant topic",
'id': 'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0',
'ordering': 'PRODUCER',
'persistency': True,
'producer_consolidation': 'TTS',
'retention': 'P180D'}]



Check if the topic you are interested in is in the list of available topics:
>>> topics = response.json()
>>> any(topic_id == topic['id'] for topic in topics)
>>> True


If topic is not in the list, you may need to check the permissions or the topic ID you are using.

Define a variable named params, and then assign with the ID of the topic which event types to get to this variable:
>>> params = {
...     "topic_id": topic_id
... }



Send a GET request to the /types endpoint:
>>> response = requests.get(f'{base_url}/types', headers=auth, params=params)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of event types for the request topic formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
[{'description': 'Tenant barrier attribute updated event',
'id': 'cti.a.p.em.event.v1.0~a.p.tenant.barrier_updated.v1.0',
'topic_id': 'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'},
{'description': 'Tenant created event',
'id': 'cti.a.p.em.event.v1.0~a.p.tenant.created.v1.0',
'topic_id': 'cti.a.p.em.topic.v1.0~a.p.tenant.v1.0'}]



Collect the list of event types that you would like to subscribe to and listen for
and store them in the event_types variable:
>>> events = response.json()
# A set of event types to listen for
>>> requested_events = {
...     'cti.a.p.em.event.v1.0~a.p.tenant.enabled.v1.0',
...     'cti.a.p.em.event.v1.0~a.p.tenant.disabled.v1.0',
... }
>>> event_types = [event['id'] for event in events if event['id'] in requested_events]
>>> event_types
['cti.a.p.em.event.v1.0~a.p.tenant.barrier_updated.v1.0', 'cti.a.p.em.event.v1.0~a.p.tenant.created.v1.0']



Note
The list of event_types may be empty if requested events are not listed in the response.