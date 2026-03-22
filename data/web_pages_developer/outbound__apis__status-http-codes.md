---
title: "HTTP status response codes"
source: "https://developer.acronis.com/doc/outbound/apis/status-http-codes.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:17.076001"
---

# HTTP status response codes

HTTP status response codes
The following is a summary of the HTTP response codes returned by the API, and a description of each.
The API-specific reference documentation provides a list of API error codes and descriptions for each endpoint.






Code
Description



20x
A request to an endpoint has been successful and the response body may contain a JSON object with the results.

400
A request to an endpoint has failed and the response body contains a JSON object with the error details.

401
Cannot process a request to an endpoint because the token specified in the Authorization header is expired or invalid.

403
Cannot process a request to an endpoint because your account has no right to access this endpoint.

404
A request to a non-existing endpoint or no requested data is found in the service.

405
A request uses a method that is not supported by the endpoint.

409
Another object of the same type already exists.

415
A request uses a format that is not supported by the endpoint. This problem might occur when an incorrect or no Content-Type header was provided in a request.

50x
A service operation issue. We recommend retrying the request twice, with a 1-2 second interval. If the error continues, contact the company administrator or try again later.