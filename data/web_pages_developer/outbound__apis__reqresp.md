---
title: "Requests and responses"
source: "https://developer.acronis.com/doc/outbound/apis/reqresp.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:12.869531"
---

# Requests and responses

Requests and responses

Communication with the endpoints is done via textual HTTP messages, the bodies of which may be empty or have a specific format.
The format is indicated in a Content-Type header of a message.


Request message type


Empty message body
Example


GET /.well-known/openid-configuration HTTP/1.1
Host: https://eu2.acronis.cloud:433
<empty line>



JSON (mostly) message body
Example


POST /api/2/clients HTTP/1.1
Host: https://eu2.acronis.cloud:443
Content-Type: application/json
Authorization: Bearer dXNlcjpwYXNz

{
"type": "api_client",
"tenant_id": "e5afb5e8-84b6-415b-969d-bc10d19f3301",
"token_endpoint_auth_method": "client_secret_basic",
"data": {"client_name": "MyApp"}
...
}



HTML form message body
Example


POST /api/2/idp/token HTTP/1.1
Host: https://eu2.acronis.cloud:443
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer dXNlcjpwYXNz

grant_type=client_credentials&scope=offline_access





Response message type


Empty message body
Example


HTTP/1.1 204 No Content
<other headers...>
<empty line>



JSON (mostly) message body
Example


HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: no-store
Pragma: no-cache
<other headers...>

{
"refresh_token":"NvLK6BAGJuNZEuQaiclVBg",
"expires_on":1560523337,
"token_type":"bearer",
"access_token":"encoded.jwt.struct",
"id_token":"identity.jwt.struct"
}



HTML form message body
Example


HTTP/1.1 200 OK
Content-Type: text/html
<other headers...>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<h5>Please wait...</h5>
</body>
</html>



In some cases, endpoint URLs may be complemented with query parameters.
Developers rarely craft HTTP messages themselves: software, a web browser, proxy, or web server, perform this action.
Good tools for working with these messages are curl, PowerShell, or Postman.
For example, to fetch the information about a client from the /clients/{client_id} endpoint via curl, use the following command:
curl -isX GET https://eu2.acronis.cloud/api/2/clients/<your client ID> \
-H "Authorization: Bearer <your token>"
For the descriptions of the curl options used in this example, see the curl man page.
The response output may be as follows:
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 17 Jun 2019 06:55:25 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 573
<other headers...>

{"created_by": "f90e086b...","last_access_at": "2020-05-22T10:13:28+00:00","tenant_id": "e5afb5e8...", ...}
The full collection of endpoints, their descriptions, HTTP methods they support, request data they accept, and responses they generate is available in the individual API reference documents.