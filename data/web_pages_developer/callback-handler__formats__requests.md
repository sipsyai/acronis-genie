---
title: "Callback request format"
source: "https://developer.acronis.com/doc/callback-handler/formats/requests.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:44.292169"
---

# Callback request format

Callback request format

Request header
To successfully process requests coming from Acronis API Callback Gateway, your callback handler must check the following headers, which are sent with each request:



Authorization
An authorization header containing a JWT (JSON Web Token) signed by Acronis. The value format is Bearer <jwt>, where <jwt> is the JWT.
See Request verification for more details.



X-CyberApp-Auth
An authentication header containing the base64-encoded credentials from your cloud.
The credentials format is <identity>:<secrets>, where <identity> is an identity registered in your service (such as a username, API client ID, etc.) in plain text format and <secrets> is a JSON text (such as {\"<model_property>\": <value>}) containing secrets (such as passwords, private keys, etc.) that are used to authenticate the identity.
See UI builder for more details.



Note

To parse X-CyberApp-Auth correctly, your callback handler must implement a function that splits the credentials into two parts at the first colon (:). The left part must be interpreted as plain text and the right part as JSON.
You can use the following Python script as a reference:

from base64 import b64decode
import json
# Decode the request header
credentials = b64decode(request.headers['X-CyberApp-Auth']).decode()
# Find the first colon position
sep_pos = credentials.index(':')
# Collect the <identity> part as plain text
identity = credentials[:sep_pos]
# Collect the <secrets> part and load as JSON
secrets = json.loads(credentials[sep_pos + 1:])


For more details on authentication handling, see our callback handler example here.




X-CyberApp-Extra
A header containing extra data specified by you.
The data is formatted as a base64-encoded JSON text.
For example, if extra data was not provided, the header will contain the e30= base64-encoded string, which is decoded to the {} JSON string and can be parsed with a JSON parser.






Request body
Callback requests sent by Acronis API Callback Gateway include the following fields, which the callback handler must process:







Field
Type
Description



type
string
The callback request identifier. The callback handler can verify whether this identifier matches the one defined for this callback. Example: cti.a.p.acgw.request.v1.0~vendor.app.read_users.v1.0.

request_id
string
The request UUID.

created_at
string
The date the request was made, in RFC3339 format.

context
object
Contains information about the context of the request.

context.callback_id
string
The callback identifier. The callback handler must use this identifier to identify which action needs to be done and which responses can be provided. Example: cti.a.p.acgw.callback.v1.0~vendor.app.read_users.v1.0.

context.endpoint_id
string
The endpoint identifier. The callback handler can use this identifier to verify whether the request was intended for the endpoint where it is located.

context.tenant_id
string
An identifier of the Acronis tenant ID from which the request was made. The callback handler may use this tenant ID to perform actions or return the data in the scope of the provided tenant ID.

context.datacenter_url
string
The URL of the Acronis data center from which the request was made.

payload
object
An object containing the data structure specified for the callback request. This is optional.