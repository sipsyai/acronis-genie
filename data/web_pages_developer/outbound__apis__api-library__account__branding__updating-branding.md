---
title: "Updating branding options for a tenant"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/branding/updating-branding.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:52.880233"
---

# Updating branding options for a tenant

Updating branding options for a tenant

To update branding options for a tenant

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



Obtain the number of the latest tenant revision.
You will have to specify this number in a subsequent request to the tenant.
This is required to manage concurrent tenant modifications.

Fetch the tenant information as described in steps 3-5 of Fetching information about an individual tenant.
As the result, you should have a tenant variable with the tenant object.
Define a variable named tenant_version, and then assign the value of the version key from the tenant object to this variable:
>>> tenant_version = tenant['version']
>>> tenant_version
3





Define a variable named params, and then assign an object with the version key containing version of the tenant to this variable:
>>> params = {
...     'version': tenant_version
... }



Define a variable named branding_options, and then assign an object with branding options to this variable:
>>> branding_options = {
...     'company_name': 'FooBar',
...     'color_scheme': 'orange'
... }



Note

You can fetch the list of available color schemes by sending a GET request to the /logic/color_schemes endpoint.
For more information on available branding options, see the API reference.



Convert the branding_options object to a JSON text:
>>> branding_options = json.dumps(branding_options, indent=4)
>>> print(branding_options)
{
"company_name": "FooBar",
"color_scheme": "orange"
}



Send a PUT request to the /tenants/{tenant_id}/brand endpoint:
>>> response = requests.put(
...     f'{base_url}/tenants/{tenant_id}/brand',
...     headers={'Content-Type': 'application/json', **auth},
...     data=branding_options,
...     params=params,
... )



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that branding options have been updated. Version number of the tenant will be also increased by 1.

Note
A different status code means that an error has occurred. For details of the error, see HTTP status response codes and API error codes.

Also, the response body contains an object with branding options, formatted as a JSON text. When converted to an object, it will look like this:
>>> pprint.pprint(response.json())
{'account_server_url': 'mc.acronis.cloud',
'backup_console_url': 'mc.acronis.cloud/bc',
'color': '000000',
'color_scheme': 'default',
'company_name': 'FooBar',
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



[Optional] Increase the value of the tenant_version variable by 1:
>>> tenant_version = tenant_version + 1