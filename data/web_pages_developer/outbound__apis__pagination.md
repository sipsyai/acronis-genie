---
title: "Pagination"
source: "https://developer.acronis.com/doc/outbound/apis/pagination.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:08.670439"
---

# Pagination

Pagination

Some endpoints may return a large amount of results that generate an excessive amount of internet traffic and server load.
In order to reduce the number of results, these endpoints use a paging mechanism, allowing them to return the results over multiple pages.
The size of the page is defined by the limit query string parameter.
If this parameter is not explicitly set, the endpoint will return a default number of results that is specified for the limit query string parameter in the API reference.
For example, if there are 99 results, and the limit query string parameter is set to 50 results, the API will split the results over two pages, returning the first page with 50 results and with a paging cursor that leads to the second page of the remaining 49 results.

An example of such a request performed via cURL:

curl -isX GET -G <the Acronis data center URL>/<Acronis product API location>/<endpoint> \
--data "limit=50" \
-H Authorization: Bearer <your token>
When the next or previous page is available, the payload will include a page token. The page token is a string that encodes the query parameters of the request
and allows you to navigate to the next or previous page of the results.

Note
Some endpoints may support only forward navigation, while others may support both forward and backward navigation.

When the next page with the results is available, the response will contain the after page token:
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json
<other headers...>

{"items":[...],"paging":{"cursors":{"after":"0A8AAAAAAAAAAA=="}}, ...}
In order to navigate to the next page, the endpoints may accept the after query string parameter that must be used together with the limit
query string parameter. Note that the after page token must be URL encoded:
curl -isX GET -G <the Acronis data center URL>/<Acronis product API location>/<endpoint> \
--data "limit=50" \
--data-urlencode "after=0A8AAAAAAAAAAA==" \
-H Authorization: Bearer <your token>
When you navigate to the next page of the results, the response will also contain the before page token, which allows you to return to the previous page:
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json
<other headers...>

{"items":[...],"paging":{"cursors":{"before":"AAAAAAAAAAAAAA=="}}, ...}
In order to navigate to the previous page, the endpoints may accept the before query string parameter that must be used together with the limit
query string parameter. Note that the before page token must be URL encoded:
curl -isX GET -G <the Acronis data center URL>/<Acronis product API location>/<endpoint> \
--data "limit=50" \
--data-urlencode "before=AAAAAAAAAAAAAA==" \
-H Authorization: Bearer <your token>