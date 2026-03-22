---
title: "Fetch service desk configuration"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-service-desk-configuration.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:24:40.074641"
---

# Fetch service desk configuration

Fetch service desk configuration

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /StaticFormData endpoint:
>>> response = requests.get(f'{base_url}/StaticFormData', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains an object with the current service desk configuration formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"TenantKey": "8dcdc278-e900-458a-b245-eaca02c05939",
"Priorities": {
"683a47ec-e57c-43a5-ba10-2ccdc03fd331": "Default Priority"
},
"Categories": [
{
"Id": "b378c809-840e-4888-9d72-2b5a9ded3642",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "BUDR",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "1c26dabc-8b41-4cb1-9d43-3f1ffa62d7a9",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "BUDR",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "7f8320eb-d653-40ae-9d57-1257bead1a28",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "00000000-0000-0000-0000-000000000000",
"Name": "Default Category",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "7f8320eb-d653-40ae-9d57-1257bead1a29",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "7f8320eb-d653-40ae-9d57-1257bead1a28",
"Name": "Default Sub-category",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "07a686b8-ff78-4283-a057-50820be22602",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "File backup/restore",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "decbb4a0-4342-42b5-8be0-2dc7180306de",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "File backup/restore",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "618ab86f-9bdf-4022-96af-1cfaeb9994de",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "00000000-0000-0000-0000-000000000000",
"Name": "General",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "7dd37156-a0d2-4fd3-82aa-607a58f6cbc6",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Name": "General question",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "07754fdc-2862-480a-83ce-903d6a67edea",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "General question",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "030825fd-478d-4800-b952-e6827f6ba2ed",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "General question",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "a385737a-b62d-4efb-82e7-a8ae7de3b853",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Name": "Hardware issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "7c283c7f-f024-428f-a22c-6609acf4fd88",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "Hardware issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "a44668b0-e771-483c-9f74-c3422621137a",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "Hardware issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "00000000-0000-0000-0000-000000000000",
"Name": "Mobile device",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "d5f438df-7ec1-4ccc-a53f-eb5bb1949faa",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "618ab86f-9bdf-4022-96af-1cfaeb9994de",
"Name": "New ticket",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "fbf5e448-6491-4bcb-970f-727a3d3f5633",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Name": "Other",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "cd66a17f-a765-4a78-af20-1f7a05bc20d2",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "Other",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "a6f2e522-d49f-4b13-a97b-6b6773446f9e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "Other",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "1cde0a27-f301-41b3-975e-27a53368d4be",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "618ab86f-9bdf-4022-96af-1cfaeb9994de",
"Name": "Purchase order",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "c646df04-a238-4195-9f19-52d47a180451",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Name": "Security and Antivirus",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "79056ead-d0ae-4e93-a371-67e3af62107f",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "Security and Antivirus",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "04897470-9550-4826-80c5-5d4fa542dfc8",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "Security and Antivirus",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "db544760-a975-49b8-b4fb-33afc534e508",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "00000000-0000-0000-0000-000000000000",
"Name": "Server",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "fd78846f-6858-4628-88dd-c1692a00e7db",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "1cd185fb-a10d-4430-b4b6-29b85523dae9",
"Name": "Software issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "5c555670-fec4-4d18-9dbc-6f72b31da8e8",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "db544760-a975-49b8-b4fb-33afc534e508",
"Name": "Software issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "1c6a363c-775e-4db4-bf55-30c478d47b13",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Name": "Software issue",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
},
{
"Id": "b9f81977-1932-410d-8bb7-ec24bc4cc395",
"Tenant": "00000000-0000-0000-0000-000000000000",
"ParentId": "00000000-0000-0000-0000-000000000000",
"Name": "Workstation",
"Active": false,
"InUse": false,
"IsDefault": false,
"HasActiveSubcategories": false,
"CategoryHasSubcategoryAsDefault": false,
"LastChangeDate": null
}
],
"ServiceLevelAgreements": {
"63b75905-10d4-44e9-ba1e-7aa2eff4100b": {
"Id": "63b75905-10d4-44e9-ba1e-7aa2eff4100b",
"Name": "Default SLA",
"ServiceStartMinutes": 480,
"ServiceStopMinutes": 1080,
"ResponseTimeInMinutes": 4800,
"FeedbackIntervalInMinutes": 24000,
"InWeekends": false,
"ApplyOnHolydays": false
},
"d154891a-87a4-48e2-8742-f685199baabe": {
"Id": "d154891a-87a4-48e2-8742-f685199baabe",
"Name": "Fixed Price 24/7",
"ServiceStartMinutes": 0,
"ServiceStopMinutes": 1439,
"ResponseTimeInMinutes": 480,
"FeedbackIntervalInMinutes": 2880,
"InWeekends": false,
"ApplyOnHolydays": false
},
"7364885a-bbc4-4566-92a5-6bee29bc1ac4": {
"Id": "7364885a-bbc4-4566-92a5-6bee29bc1ac4",
"Name": "Fixed Price Office hours",
"ServiceStartMinutes": 540,
"ServiceStopMinutes": 1080,
"ResponseTimeInMinutes": 480,
"FeedbackIntervalInMinutes": 2880,
"InWeekends": false,
"ApplyOnHolydays": false
},
"43dceee4-e778-45b9-96e2-7cac9ed2578a": {
"Id": "43dceee4-e778-45b9-96e2-7cac9ed2578a",
"Name": "Time and materials",
"ServiceStartMinutes": 540,
"ServiceStopMinutes": 1080,
"ResponseTimeInMinutes": 480,
"FeedbackIntervalInMinutes": 5760,
"InWeekends": false,
"ApplyOnHolydays": false
}
},
"BusinessUnits": {
"6fd181cf-10e7-4a99-a56f-cd143e50e368": "cstmr_001Group",
"ed43a6d8-05d2-4a51-aa22-049a808714dd": "cyber_prtnr_0810_1009am Group",
"730a3b95-36a4-41d1-9b12-66f220eec23e": "SofiaBusinessSchoolGroup",
"aa8623e5-e765-4663-967d-2cb6a209f8e1": "Support group"
},
"Statusses": {
"4feaaa86-8757-44d6-a8d6-99fdf9f8ce4d": {
"Id": "4feaaa86-8757-44d6-a8d6-99fdf9f8ce4d",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "New",
"IsStatusForClosedCall": false,
"Sequence": 1,
"RequirePlanning": false,
"ClassName": "new",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"9958d2d5-b7ac-452b-bc31-f87739958bff": {
"Id": "9958d2d5-b7ac-452b-bc31-f87739958bff",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Reopened",
"IsStatusForClosedCall": false,
"Sequence": 110,
"RequirePlanning": false,
"ClassName": "reopened",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"5816e519-1017-4e3b-bb9f-2e31af53ce0e": {
"Id": "5816e519-1017-4e3b-bb9f-2e31af53ce0e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "New",
"IsStatusForClosedCall": false,
"Sequence": 111,
"RequirePlanning": false,
"ClassName": "new",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"52d6d4a2-9ae4-48e5-b351-b409398b1d2e": {
"Id": "52d6d4a2-9ae4-48e5-b351-b409398b1d2e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Pending start",
"IsStatusForClosedCall": false,
"Sequence": 112,
"RequirePlanning": false,
"ClassName": "new",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"18fbc8c9-eb73-4378-989a-5dfc25e535fc": {
"Id": "18fbc8c9-eb73-4378-989a-5dfc25e535fc",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "In progress",
"IsStatusForClosedCall": false,
"Sequence": 113,
"RequirePlanning": false,
"ClassName": "callinprogress",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"4ec40767-1ad3-493c-b481-5ef2ade372be": {
"Id": "4ec40767-1ad3-493c-b481-5ef2ade372be",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Delayed",
"IsStatusForClosedCall": false,
"Sequence": 114,
"RequirePlanning": false,
"ClassName": "delayed",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"0b8497d4-e867-47de-9c9a-cc51b6e97668": {
"Id": "0b8497d4-e867-47de-9c9a-cc51b6e97668",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "On hold",
"IsStatusForClosedCall": false,
"Sequence": 115,
"RequirePlanning": false,
"ClassName": "onhold",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"98c2b674-ad5d-4895-8160-b188b1d82996": {
"Id": "98c2b674-ad5d-4895-8160-b188b1d82996",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Solved",
"IsStatusForClosedCall": true,
"Sequence": 116,
"RequirePlanning": false,
"ClassName": "completed",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
"15887a59-097b-457e-b39a-e5d330b370cc": {
"Id": "15887a59-097b-457e-b39a-e5d330b370cc",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "In progress",
"IsStatusForClosedCall": false,
"Sequence": 120,
"RequirePlanning": false,
"ClassName": "callinprogress",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"b838914b-476b-445b-be8c-c62adefe018e": {
"Id": "b838914b-476b-445b-be8c-c62adefe018e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Pending vendor/supplier",
"IsStatusForClosedCall": false,
"Sequence": 130,
"RequirePlanning": false,
"ClassName": "pendingatsupplier",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"ef76bdb4-4884-4330-b09f-f064b841d10d": {
"Id": "ef76bdb4-4884-4330-b09f-f064b841d10d",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Waiting for response",
"IsStatusForClosedCall": false,
"Sequence": 140,
"RequirePlanning": false,
"ClassName": "waitingforclient",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"db4e4023-82a7-4112-8d36-acf4238773f7": {
"Id": "db4e4023-82a7-4112-8d36-acf4238773f7",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Schedule onsite activities",
"IsStatusForClosedCall": false,
"Sequence": 150,
"RequirePlanning": false,
"ClassName": "callactionplaned",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"3ddae1c5-2c32-446f-bf91-370214799f80": {
"Id": "3ddae1c5-2c32-446f-bf91-370214799f80",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Activities scheduled",
"IsStatusForClosedCall": false,
"Sequence": 160,
"RequirePlanning": true,
"ClassName": "callactionplaned",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"a83d4718-7709-4dec-9c94-074f361f3897": {
"Id": "a83d4718-7709-4dec-9c94-074f361f3897",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Onsite work scheduled",
"IsStatusForClosedCall": false,
"Sequence": 180,
"RequirePlanning": true,
"ClassName": "actionplannedinsite",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"6e717073-d6a4-4047-ad0a-6a42d353cf01": {
"Id": "6e717073-d6a4-4047-ad0a-6a42d353cf01",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Updated by employee",
"IsStatusForClosedCall": false,
"Sequence": 220,
"RequirePlanning": false,
"ClassName": "clientupdate",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"c9e91523-522f-4517-b388-ae492e965bd2": {
"Id": "c9e91523-522f-4517-b388-ae492e965bd2",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Updated by supplier",
"IsStatusForClosedCall": false,
"Sequence": 230,
"RequirePlanning": false,
"ClassName": "supplierupdate",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"2a078177-466a-4b55-aae1-20fe2de2e4e3": {
"Id": "2a078177-466a-4b55-aae1-20fe2de2e4e3",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Outstanding quote",
"IsStatusForClosedCall": false,
"Sequence": 300,
"RequirePlanning": false,
"ClassName": "issuequote",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"dd2a6b5c-61ee-46c2-8134-2e289356f160": {
"Id": "dd2a6b5c-61ee-46c2-8134-2e289356f160",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Waiting for approval",
"IsStatusForClosedCall": false,
"Sequence": 400,
"RequirePlanning": false,
"ClassName": "waitingapproval",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"9091bc00-b55a-4836-8cb7-7d633d5a076e": {
"Id": "9091bc00-b55a-4836-8cb7-7d633d5a076e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Client update received",
"IsStatusForClosedCall": false,
"Sequence": 500,
"RequirePlanning": false,
"ClassName": "updatevanklantontvangen",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"df794744-91b8-42ef-a79b-8448ba342293": {
"Id": "df794744-91b8-42ef-a79b-8448ba342293",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Schedule activities",
"IsStatusForClosedCall": false,
"Sequence": 502,
"RequirePlanning": false,
"ClassName": "workplans",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"725ad85e-d7cd-44ea-bb9c-5d433329dc8a": {
"Id": "725ad85e-d7cd-44ea-bb9c-5d433329dc8a",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Change",
"IsStatusForClosedCall": false,
"Sequence": 503,
"RequirePlanning": false,
"ClassName": "change",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"dd1327f0-b338-467b-aaab-21a9b57cea63": {
"Id": "dd1327f0-b338-467b-aaab-21a9b57cea63",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Solved",
"IsStatusForClosedCall": true,
"Sequence": 999,
"RequirePlanning": false,
"ClassName": "completed",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"0a83b991-15a6-4e8e-b99f-b079a29f5c1e": {
"Id": "0a83b991-15a6-4e8e-b99f-b079a29f5c1e",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Closed",
"IsStatusForClosedCall": true,
"Sequence": 9999,
"RequirePlanning": false,
"ClassName": "callclosed",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": "9958d2d5-b7ac-452b-bc31-f87739958bff",
"StatusType": 0,
"LastChangeDate": null
},
"9958d2d5-b7ac-452b-bc31-f87739958b00": {
"Id": "9958d2d5-b7ac-452b-bc31-f87739958b00",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "SLA breach",
"IsStatusForClosedCall": false,
"Sequence": 10000,
"RequirePlanning": false,
"ClassName": "outOfSLA",
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"f2ad73d8-19cd-4d47-8884-d08c57aa1320": {
"Id": "f2ad73d8-19cd-4d47-8884-d08c57aa1320",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "On hold",
"IsStatusForClosedCall": false,
"Sequence": 99991,
"RequirePlanning": false,
"ClassName": null,
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
"3994de1d-c657-45d2-aac5-087e8648912d": {
"Id": "3994de1d-c657-45d2-aac5-087e8648912d",
"Tenant": "00000000-0000-0000-0000-000000000000",
"Name": "Incident",
"IsStatusForClosedCall": false,
"Sequence": 999920,
"RequirePlanning": false,
"ClassName": null,
"Translation": null,
"Active": false,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
}
},
"CurrentSupportUserId": "83bab5c4-ded7-4a6b-a249-591e15286361",
"CurrentSupportUser": {
"TendantId": "00000000-0000-0000-0000-000000000000",
"AspnetProviderUserKey": "00000000-0000-0000-0000-000000000000",
"ComputicateUserId": "83bab5c4-ded7-4a6b-a249-591e15286361",
"UserName": "Partner Administrator",
"Firstname": null,
"SurnamePrefix": null,
"Surname": null,
"LogOnUsername": "prtnr_usr_0810_1009am",
"BusinessUnitId": "aa8623e5-e765-4663-967d-2cb6a209f8e1",
"Manager": "83bab5c4-ded7-4a6b-a249-591e15286361",
"CountryId": "d46c54bd-1704-4a55-bb76-fc03073669a0",
"AcceptedToS": null,
"Filter": null,
"FilterId": "00000000-0000-0000-0000-000000000000",
"ProfilePictureSrc": null,
"UserTierType": 3,
"Deleted": null
},
"Tier": 3,
"UserTier": 3,
"GroupsManaged": [
"ed43a6d8-05d2-4a51-aa22-049a808714dd",
"aa8623e5-e765-4663-967d-2cb6a209f8e1"
],
"Templates": [
{
"Id": "2f0586b5-efde-4655-a962-213130e1edac",
"Name": "Please call me back",
"Text": "I have tried to call you but could not reach you. Can you please call me back?",
"Language": "00000000-0000-0000-0000-000000000000",
"Active": false
},
{
"Id": "1c22c534-e96e-473a-9f29-28320a79dcd5",
"Name": "Account created",
"Text": "<p>A user account was created for [ENDUSER].</p><p>Their credentials are:</p><p>User name: (username)</p><p>Password: (password)</p>",
"Language": "00000000-0000-0000-0000-000000000000",
"Active": false
}
],
"Languages": [
{
"Id": "2fdb8928-7c05-4e31-a690-135c5be79ffb",
"Country": "3bfba166-1862-4db0-ab3e-d3c4340ba53c",
"Name": "한국어",
"Active": false
},
{
"Id": "6c42b4f2-34b7-4010-b07a-271bebb55c09",
"Country": "bcb337b5-9d64-4bf5-b32f-740fb08f4070",
"Name": "Polski",
"Active": false
},
{
"Id": "23adaa14-fe07-48e3-9a45-3573425a721d",
"Country": "3ae0ca0c-70de-42a1-ac99-40fd3e94d22d",
"Name": "Español",
"Active": false
},
{
"Id": "aec96754-aeb3-44bb-9140-4cde9c8802a7",
"Country": "eb9711e2-2f13-4721-8a2e-aff92331f579",
"Name": "Français",
"Active": false
},
{
"Id": "5647c235-e255-42ad-b844-54281dccbb93",
"Country": "4a01049b-bcb7-414d-a1cf-5c133f2956d6",
"Name": "Português",
"Active": false
},
{
"Id": "c3fa37e8-eb26-4e26-9b4c-5463a0b64653",
"Country": "52f55d7f-3d34-4893-88db-e5793986cffd",
"Name": "Svenska",
"Active": false
},
{
"Id": "87036a71-d718-4975-9296-6e6d50a43473",
"Country": "e297b0aa-9a9f-4196-920d-6e4edb3ee945",
"Name": "Čeština",
"Active": false
},
{
"Id": "8c3e2b9b-a485-4252-93fe-73f8182ef817",
"Country": "248da49e-506e-4bef-888d-c72738224101",
"Name": "Deutsch",
"Active": false
},
{
"Id": "66f82b19-0fc8-491d-9492-7a466d7839d7",
"Country": "f569a08d-fb9e-4ec5-ab93-ac3e9b4e3db1",
"Name": "Italiano",
"Active": false
},
{
"Id": "cd739ab1-4c5f-4cb2-a42e-8ea37c10feb7",
"Country": "37599bef-7321-4694-8e1d-3e309f1fb050",
"Name": "Dansk",
"Active": false
},
{
"Id": "5a6955f9-8994-42bc-a768-9fa147e7b478",
"Country": "b3b06e77-6ef1-46cf-931f-f09e1cc19fc5",
"Name": "Malayu",
"Active": false
},
{
"Id": "48d06c90-f8a4-4726-a83c-a47dbb709f25",
"Country": "d46c54bd-1704-4a55-bb76-fc03073669a0",
"Name": "English",
"Active": true
},
{
"Id": "4babc61b-add5-4978-9c0a-aeb510557f98",
"Country": "34be9ad9-c4c4-4435-adde-37a8536d849e",
"Name": "Türkçe",
"Active": false
},
{
"Id": "8d7f07d4-c819-4e51-b90e-bd9cc7f0ea11",
"Country": "46fab221-1f60-4d79-949f-a2b8f89e7284",
"Name": "日本語",
"Active": false
},
{
"Id": "ec53e4b8-21c2-4ac7-839b-c0b26e9ac362",
"Country": "0309138b-473b-4656-9e6a-1cbf0a62a127",
"Name": "Português (Brasil)",
"Active": false
},
{
"Id": "3e91f259-0f8e-42ef-ac47-ed43726a2f79",
"Country": "111d7f43-c756-406a-8dff-b00c16c43316",
"Name": "Suomi",
"Active": false
},
{
"Id": "6288c6db-5bb7-4346-9add-fd362c8fbcce",
"Country": "124ea0e3-abfd-450a-b9ed-f14fcd39acf7",
"Name": "Nederlands",
"Active": false
}
],
"LegalForms": [
"-",
"UNKNOWN"
],
"Countries": {
"e7f12dd9-f940-4edc-8247-a7a194d572a7": "Afghanistan",
"f274c9e9-2a42-4d01-9b86-4e9ac371bb5a": "Albania",
"8b807e32-a9c5-46ef-b835-4945739cf52e": "Algeria",
"d24370e6-5a5c-4e5d-86b2-9cb5e3f2e9a7": "Argentina",
"6a7c5b86-95a2-4001-9c48-7e93523ad330": "Armenia",
"c3572b7c-33aa-43e8-9e0f-1e4e3b93f7e3": "Australia",
"a35e3180-5a58-452e-8130-39becb076b84": "Austria",
"3a15a5b1-7be7-446f-8cb4-ef09697eeb0f": "Azerbaijan",
"a3cad84e-0939-4350-a15f-d6ef82388f08": "Bangladesh",
"5d10790d-4b73-4e60-912a-11a00b5e7e9e": "Belarus",
"a1a2081f-fce7-469e-82aa-502cb9796ce0": "Belgium",
"475d56a5-d144-48f8-850a-7029af52cb85": "Belize",
"3c0e3299-8cd5-4d66-bd91-1522d547ad6d": "Bolivia",
"26a5dccb-fb13-4fe8-a156-85149f8eea52": "Bosnia and Herzegovina",
"0309138b-473b-4656-9e6a-1cbf0a62a127": "Brazil",
"b28c162b-007a-42a1-ba97-d798e9e26909": "Bulgaria",
"a8e81812-6c34-4435-9574-e8ae1cc9af0e": "Cambodia",
"ab5063ed-f900-4c0f-b7d7-a24aeb76ae2d": "Canada",
"40f7eeae-acc9-4bad-a1a0-5a9f622a4915": "Chile",
"923057e6-ca45-441a-812d-b8bf02f88f88": "China",
"f326e326-7738-4bfa-b03e-b15cc57a14ae": "Colombia",
"fc0108ff-ab8c-4cd7-8b42-3f2b3276e716": "Croatia",
"e297b0aa-9a9f-4196-920d-6e4edb3ee945": "Czech Republic",
"37599bef-7321-4694-8e1d-3e309f1fb050": "Denmark",
"b3cd5b81-e6ae-4909-b99f-f5488a89dd5a": "Ecuador",
"074d91cf-9f30-4aba-908a-0b503a3c2b6b": "Egypt",
"a7b9f58a-99d9-4579-ac14-74c205d32ae3": "Estonia",
"d0e4d953-4485-4acd-b795-e94d8df0d4d1": "Ethiopia",
"18f20fe7-9b8d-42dc-a32d-0445c1ebb263": "Faroe Islands",
"111d7f43-c756-406a-8dff-b00c16c43316": "Finland",
"eb9711e2-2f13-4721-8a2e-aff92331f579": "France",
"124ac24c-7493-42a1-af06-ba5b850950cb": "Georgia",
"248da49e-506e-4bef-888d-c72738224101": "Germany",
"9b644c06-71a4-4fae-a1aa-3dfbd0a9546f": "Ghana",
"b41236b8-f464-4ea9-bc91-5b7e71662308": "Greece",
"c75716e5-bbbe-41c9-90c1-14b0bd35465b": "Greenland",
"0335e28f-abd1-4b8f-b3c8-4e6a846f1530": "Guatemala",
"d310902a-c193-4a43-b295-4bdb4eeecdca": "Hong Kong",
"a812c85b-dddf-443d-84d7-0e9c8276417b": "Hungary",
"d5090641-f223-445e-b77a-e8929f4251a0": "Iceland",
"734c7b09-e003-4569-9a02-378f8c63b72a": "India",
"39fdf642-9804-48b2-9327-abdd4c972ce7": "Indonesia",
"deef6ded-c0c5-4fd5-8761-c19ae097b4cb": "Iran",
"91897ea7-5388-47a6-82e8-d86d2cfb0522": "Iraq",
"40fb3507-34f7-4b06-9920-24477559fb3a": "Ireland",
"f4feb010-a1c6-4c3e-9f37-a2494d5aa0a6": "Israel",
"f569a08d-fb9e-4ec5-ab93-ac3e9b4e3db1": "Italy",
"6db30587-e4a1-46e5-a348-0eef866e0fb2": "Jamaica",
"46fab221-1f60-4d79-949f-a2b8f89e7284": "Japan",
"a454bbd4-88d4-42f8-a541-d2c433604ff6": "Jordan",
"4d9f6a4e-66d8-48f3-8026-8f9f6845f4cc": "Kazakhstan",
"07658c65-ff7d-41cb-b9f6-3c7ad60205a7": "Kenya",
"f767fe86-01b1-4a17-8b99-23c35395700d": "Kuwait",
"4e7011ad-9dde-4909-ad06-140e21533ec7": "Latvia",
"619063a6-b93a-4cc6-a072-c9686cd12cd8": "Lebanon",
"b73c8439-d218-4fb3-adc6-f3ea2afc1616": "Libya",
"c4d47f16-15b9-4a6d-90b3-8ca2f1ad3bdf": "Liechtenstein",
"3cc35f7c-7c34-4edf-baaa-684a53ef93be": "Lithuania",
"bd3216f0-22f0-481b-8a9e-d97a17137cb9": "Luxembourg",
"17208fca-0029-4f7e-9ec9-9508a2e9f84d": "Macedonia",
"b3b06e77-6ef1-46cf-931f-f09e1cc19fc5": "Malaysia",
"013da874-95c7-4903-93f5-f918a531a3a9": "Maldives",
"c99bb641-cdf1-4f44-8ed9-0876101ce863": "Malta",
"4a254e4c-84b1-4254-adaa-69b67d79b113": "Mexico",
"7ae9535f-fc57-4fa4-84c5-67b5dcca24b3": "Monaco",
"dc70480d-b90b-4dad-b991-c052fbfe9ad4": "Mongolia",
"5a18588a-03d3-4b34-b4bc-5dc97a821a24": "Montenegro",
"c151f959-4439-4e74-913e-ec3055c39655": "Morocco",
"ab1e3edd-ffc4-44de-9527-2189cad7501d": "Nepal",
"124ea0e3-abfd-450a-b9ed-f14fcd39acf7": "Netherlands",
"536a7ea0-9988-4024-8085-52f4e26daa19": "New Zealand",
"6e540384-b423-4b11-87fd-4acc88f39d21": "Nicaragua",
"279f419f-43b0-4e23-894c-7a5bf6369a2e": "Niger",
"3385f804-69b5-43d8-afe3-fbe8009f248c": "Nigeria",
"b4387244-2d83-4b7d-91a6-0232d11095f1": "North Korea",
"fcbb0e43-666c-4b84-b8dd-d878c4887a5b": "Norway",
"4ce62ea6-8da1-4f4c-a567-9df21230edcb": "Pakistan",
"5b833c0f-a201-4c1b-a970-1034eb25f04a": "Panama",
"92794f7d-1006-4395-8605-46c15c90f0f1": "Paraguay",
"0e5e5031-5eb7-409c-9353-27a861d812d8": "Peru",
"7ef23649-1ada-43c5-b018-4e9d2a58e9a9": "Philippines",
"bcb337b5-9d64-4bf5-b32f-740fb08f4070": "Poland",
"4a01049b-bcb7-414d-a1cf-5c133f2956d6": "Portugal",
"20ad6bf0-0404-4298-8db2-8004e84f602c": "Puerto Rico",
"09ac4cd9-2ab7-4357-b278-e232b0e6d706": "Qatar",
"f0e794e1-a061-4ec4-b13c-7431ed6a76c1": "Romania",
"20909e21-5628-412c-b933-2f2ac939b296": "Russia",
"ada1ac81-5f4d-4e3c-90c3-7b53d91576ee": "Saudi Arabia",
"1ab10a25-46e5-4f6e-9b8e-f3183023145f": "Senegal",
"cfeba81a-3fb1-401c-bf03-5cf5e4dd28d4": "Serbia",
"c2e9cd38-f887-405d-a7d6-5a6665780df8": "Singapore",
"86281947-bfaa-4b0e-a34a-8b7bb25208d2": "Slovakia",
"6b16d403-0ae3-48f9-8f02-4cf1eab4c91e": "Slovenia",
"f963bac3-0012-4dd7-8b93-825e0306b3fa": "South Africa",
"3bfba166-1862-4db0-ab3e-d3c4340ba53c": "South Korea",
"3ae0ca0c-70de-42a1-ac99-40fd3e94d22d": "Spain",
"e80a3ac8-e60e-400a-aded-6993ba36c5ef": "Sri Lanka",
"52f55d7f-3d34-4893-88db-e5793986cffd": "Sweden",
"2e570121-9be8-4626-b738-e27c7777683f": "Switzerland",
"6697db21-3808-4a7b-9a28-8d5b91ada8bb": "Syria",
"460edb86-6473-4fa5-bc81-1c7000c96f66": "Taiwan",
"ebcc441d-194e-47c3-96a4-75675597d722": "Tajikistan",
"b4610267-1159-4458-a58e-ce5862c47628": "Thailand",
"d7c67f5d-9d11-44cb-b653-57c79a7f6942": "Tunisia",
"34be9ad9-c4c4-4435-adde-37a8536d849e": "Turkey",
"33aefb90-fbec-4bfe-ab93-02b303d1062e": "Turkmenistan",
"b67e36bf-723d-4ea5-90ca-c56e1ba230c4": "Ukraine",
"e80b6cee-b7fb-4b70-92f4-d771bfb485b6": "United Arab Emirates",
"cd7b9e82-ebd2-41be-be76-84a97b453b4c": "United Kingdom",
"d46c54bd-1704-4a55-bb76-fc03073669a0": "United States",
"c85178f2-0078-47c1-bc48-afd27c0a984e": "Uruguay",
"098dbdc6-3597-403a-a68c-98f3ddb606f1": "Uzbekistan",
"7f7d3b67-9e5b-4260-821f-e06e94802c61": "Venezuela",
"a72c16e7-aa0b-443b-8f36-dc5a9db44ff5": "Vietnam",
"db21c3b1-1758-42cc-a66b-96d01a30bacd": "Yemen - Republic of Yemen"
},
"ContractPartTypes": {
"99bac074-0e2d-4565-bf90-cf7655d2b500": "Default type",
"99bac074-0e2d-4565-bf90-cf7655d2b501": "Managed Service",
"99bac074-0e2d-4565-bf90-cf7655d2b502": "ICT Service"
},
"ClosedStatusses": [
"98c2b674-ad5d-4895-8160-b188b1d82996",
"dd1327f0-b338-467b-aaab-21a9b57cea63",
"0a83b991-15a6-4e8e-b99f-b079a29f5c1e"
],
"InProgressOrNewStatusses": [
"4feaaa86-8757-44d6-a8d6-99fdf9f8ce4d",
"9958d2d5-b7ac-452b-bc31-f87739958bff",
"5816e519-1017-4e3b-bb9f-2e31af53ce0e",
"52d6d4a2-9ae4-48e5-b351-b409398b1d2e",
"18fbc8c9-eb73-4378-989a-5dfc25e535fc",
"4ec40767-1ad3-493c-b481-5ef2ade372be",
"0b8497d4-e867-47de-9c9a-cc51b6e97668",
"15887a59-097b-457e-b39a-e5d330b370cc",
"b838914b-476b-445b-be8c-c62adefe018e",
"ef76bdb4-4884-4330-b09f-f064b841d10d",
"db4e4023-82a7-4112-8d36-acf4238773f7",
"3ddae1c5-2c32-446f-bf91-370214799f80",
"a83d4718-7709-4dec-9c94-074f361f3897",
"6e717073-d6a4-4047-ad0a-6a42d353cf01",
"c9e91523-522f-4517-b388-ae492e965bd2",
"2a078177-466a-4b55-aae1-20fe2de2e4e3",
"dd2a6b5c-61ee-46c2-8134-2e289356f160",
"9091bc00-b55a-4836-8cb7-7d633d5a076e",
"df794744-91b8-42ef-a79b-8448ba342293",
"725ad85e-d7cd-44ea-bb9c-5d433329dc8a",
"9958d2d5-b7ac-452b-bc31-f87739958b00",
"f2ad73d8-19cd-4d47-8884-d08c57aa1320",
"3994de1d-c657-45d2-aac5-087e8648912d"
],
"Aliases": [
{
"FieldToMap": "ed43a6d8-05d2-4a51-aa22-049a808714dd",
"ActualName": "cyber_prtnr_0810_1009am Group",
"Alias": "",
"Type": 3
},
{
"FieldToMap": "aa8623e5-e765-4663-967d-2cb6a209f8e1",
"ActualName": "Support group",
"Alias": "",
"Type": 3
}
]
}