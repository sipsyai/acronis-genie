---
title: "Fetching the branding options of a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/branding/fetching-branding.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:44.468134"
---

# Fetching the branding options of a tenant

Fetching the branding options of a tenant

To fetch the branding options of a tenant

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the data center URL>/api/2'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id  # the UUID of the tenant to which the token provides access
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Assign either of the following values to the tenant_id variable – the UUID of a sub-tenant created via the API or a sub-tenant found by its name:
>>> tenant_id = created_tenant_id
>>> tenant_id
'0fcd4a69-8a40-4de8-b711-d9c83dc000f7'



Send a GET request to the /tenants/{tenant_id}/brand endpoint:
>>> response = requests.get(f'{base_url}/tenants/{tenant_id}/brand', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with branding options, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'account_server_url': 'mc.acronis.cloud',
'backup_console_url': 'mc.acronis.cloud/bc',
'color': 'FFFFFF',
'color_scheme': 'default',
'company_name': 'acronis',
'help_url': 'api/ams/links/help',
'hide_predefined': 1,
'home_url': 'www.acronis.com',
'knowledgebase_url': 'kb.acronis.com/errorcode/',
'logotype': '2f8ad2e2-28f2-11e7-aad1-5ffe2ad47151',
'mobile_app_android_download_url': 'www.mobile.com/download',
'mobile_app_ios_download_url': 'www.mobile.com/download',
'owns_custom_legal_docs': True,
'platform_terms_url': 'terms.acronis.com',
'privacy_policy_url': 'https://www.acronis.com/company/privacy.html',
'router_url': 'acronis.cloud',
'service_name': 'myservice',
'smtp_encryption': 'TLS',
'smtp_override': 1,
'smtp_password': '',
'smtp_port': 465,
'smtp_reply_address': 'noreply@mycompany.com',
'smtp_server': 'smtp.mycompany.com',
'smtp_user': 'smtpuser',
'support_phone': '+1 1111 1111111',
'support_url': 'support.acronis.com',
'terms_url': 'terms.acronis.com',
'upsell_url': 'www.partner.com/buy',
'user_guide_url': 'guide.acronis.com'}