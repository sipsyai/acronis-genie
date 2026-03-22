---
title: "Log in using service user account"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/appmgr/service-user-login.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:20:50.551256"
---

# Log in using service user account

Log in using service user account

Important
This endpoint is available only for CyberApps with “Access to Acronis EDR incidents” set to “Read-only” or “Read and write”.

This endpoint allows MDR to log in to Acronis Cyber Protect Cloud on behalf of the end customer using a service user account.

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'https://eu2.acronis.cloud/api/application_manager/v2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}



Fetch an ID of the tenant where you want your security analyst to log in on behalf of the end customer.
>>> target_tenant_id = '00000000-0000-0000-0000-000000000000'



Define a variable named vendor_app_code, and then assign a code of your CyberApp to this variable:
>>> vendor_app_code = 'vendor.app'



Define a variable named external_id, and then assign an ID that will be assigned to the service user to this variable:
>>> external_id = 'service_user_1'



Define a variable named params, and then assign service user login parameters to this variable:
>>> params = {
...     'tenant_id': target_tenant_id,
...     'purpose': 'login',
...     'external_id': external_id,
... }



Send a GET request to the /application/{vendor_app_code}/service_user:login endpoint with the following parameters:
>>> response = requests.get(
...     f'{base_url}/application/{vendor_app_code}/service_user:login',
...     headers=auth,
...     params=params,
...     allow_redirects=False,
... )



Check the status code of the response:
>>> response.status_code
301


Status code 301 means that the request was successful and the response contains a redirect link with the one-time token (OTT) in the Location header.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes.