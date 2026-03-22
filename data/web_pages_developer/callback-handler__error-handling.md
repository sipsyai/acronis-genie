---
title: "Callback error handling"
source: "https://developer.acronis.com/doc/callback-handler/error-handling.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:52:35.889189"
---

# Callback error handling

Callback error handling
Callbacks can define their own error responses, but the Acronis API Callback Gateway provides default handling for specific HTTP error response codes and communication errors.

Default error response codes

These HTTP status codes do not need to be specified in callbacks. The Acronis API Callback Gateway will process them.
A corresponding error message will also be rendered in the user interface for partners and customers.









Status code
Reason
UI message



401 Unauthorized
The callback handler rejected the unauthorized request.
Connection to <cyberapp_name> service could not be established due to invalid credentials.

403 Forbidden
The callback handler rejected the request due to invalid credentials.
Connection to <cyberapp_name> service could not be established due to invalid credentials.

410 Gone
The callback handler is no longer available at the provided URL.
Response from to <cyberapp_name> service cannot be processed due to invalid format.

429 Too Many Requests
The callback handler rejected the request due to too many requests. The request can be retried by API Callback Gateway.
None

500-599
The callback handler responded with an error that indicates a server error.
Connection to <cyberapp_name> service could not be established.





Enablement error messages
A callback handler can include a human-readable error message in the err_message field of the response body.
An error message may indicate a precondition that must be met before enabling the CyberApp for a partner or customer.
For example, a Managed Security Service Provider (MSSP) may need to sign a contract before enabling the CyberApp
for their customers and return an appropriate error message that will appear as follows:

This message can be displayed in the user interface when attempting to enable the CyberApp in the following scenarios:

Mapping the partner ID to the Acronis tenant ID
Writing the customer mapping to your service
Enabling a partner using mirroring
Enabling customers using mirroring



Communication errors

The following communication errors will be handled by the Acronis API Callback Gateway.
A corresponding error message will be rendered in the user interface for MSPs and customers.









Error
Reason
UI message



TLS handshake failed
Acronis API Callback Gateway was unable to negotiate the secure protocol with the callback handler.
Connection to <cyberapp_name> service could not be established.

Invalid SSL certificate
Acronis API Callback Gateway was unable to verify the SSL certificate of the callback handler domain name.
Connection to <cyberapp_name> service could not be established due to invalid certificate.

Server is unreachable
Acronis API Callback Gateway was unable to find a route to the callback handler. The request can be retried by API Callback Gateway.
Connection to <cyberapp_name> service could not be established.

Connection timed out
Acronis API Callback Gateway was able to establish the connection but did not receive a response within the specific time. The request can be retried by API Callback Gateway.
Connection to <cyberapp_name> service could not be established.

Unexpected 2xx-3xx response
Callback handler responded with a response within the 200-399 range that does not match any code defined for this callback.
Response from to <cyberapp_name> service cannot be processed due to invalid format.

Unexpected 4xx response
Callback handler responded with a response within the 400-499 range that does not match any code defined for this callback or in the Status codes table.
Response from to <cyberapp_name> service cannot be processed due to invalid format.

Response schema error
Callback handler responded with a structure that does not match the schema defined for this callback.
Response from to <cyberapp_name> service cannot be processed due to invalid format.

Request schema error
Callback handler received a request from the user interface which structure does not match the schema defined for this callback.
Request to <cyberapp_name> was not sent due to invalid format.