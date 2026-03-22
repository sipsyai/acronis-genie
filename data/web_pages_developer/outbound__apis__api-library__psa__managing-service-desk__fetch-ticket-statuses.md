---
title: "Fetch ticket statuses"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/psa/managing-service-desk/fetch-ticket-statuses.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:25:01.078260"
---

# Fetch ticket statuses

Fetch ticket statuses

Authenticate to the cloud platform via the Python shell.
The following variables should be available now:
>>> base_url  # the base URL of the API
'<the Acronis data center URL>/api/advanced-automation/v1'
>>> auth  # the 'Authorization' header value with the access token
{'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImMwMD...'}
>>> tenant_id # the ID of the partner tenant that can be accessed with the token
'ede9f834-70b3-476c-83d9-736f9f8c7dae'



Send a GET request to the /Statuses endpoint:
>>> response = requests.get(f'{base_url}/Statuses', headers=auth)



Check the status code of the response:
>>> response.status_code
200


Status code 200 means that the request was successful.
Also, the response body contains a list of statuses that can be assigned to a ticket formatted as a JSON text.
When converted to an object, it will look as follows:
>>> pprint.pprint(response.json())
{
"statuses": [
{
"Id": "a83d4718-7709-4dec-9c94-074f361f3897",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "ActionPlannedInSite",
"IsStatusForClosedCall": false,
"Sequence": 180,
"RequirePlanning": true,
"ClassName": "actionplannedinsite",
"Translation": "Onsite work scheduled",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "3994de1d-c657-45d2-aac5-087e8648912d",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Incident",
"IsStatusForClosedCall": false,
"Sequence": 999920,
"RequirePlanning": false,
"ClassName": null,
"Translation": "Incident",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "2a078177-466a-4b55-aae1-20fe2de2e4e3",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "IssueQuote",
"IsStatusForClosedCall": false,
"Sequence": 300,
"RequirePlanning": false,
"ClassName": "issuequote",
"Translation": "Outstanding quote",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "dd1327f0-b338-467b-aaab-21a9b57cea63",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Completed",
"IsStatusForClosedCall": true,
"Sequence": 999,
"RequirePlanning": false,
"ClassName": "completed",
"Translation": "Solved",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "dd2a6b5c-61ee-46c2-8134-2e289356f160",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "WaitingApproval",
"IsStatusForClosedCall": false,
"Sequence": 400,
"RequirePlanning": false,
"ClassName": "waitingapproval",
"Translation": "Waiting for approval",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "5816e519-1017-4e3b-bb9f-2e31af53ce0e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "New",
"IsStatusForClosedCall": false,
"Sequence": 111,
"RequirePlanning": false,
"ClassName": "new",
"Translation": "New",
"Active": true,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "3ddae1c5-2c32-446f-bf91-370214799f80",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "CallActionPlaned",
"IsStatusForClosedCall": false,
"Sequence": 160,
"RequirePlanning": true,
"ClassName": "callactionplaned",
"Translation": "Activities scheduled",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "725ad85e-d7cd-44ea-bb9c-5d433329dc8a",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Change",
"IsStatusForClosedCall": false,
"Sequence": 503,
"RequirePlanning": false,
"ClassName": "change",
"Translation": "Change",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "18fbc8c9-eb73-4378-989a-5dfc25e535fc",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "InProgress",
"IsStatusForClosedCall": false,
"Sequence": 113,
"RequirePlanning": false,
"ClassName": "callinprogress",
"Translation": "In progress",
"Active": true,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "4ec40767-1ad3-493c-b481-5ef2ade372be",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Delayed",
"IsStatusForClosedCall": false,
"Sequence": 114,
"RequirePlanning": false,
"ClassName": "delayed",
"Translation": "Delayed",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "6e717073-d6a4-4047-ad0a-6a42d353cf01",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "ClientUpdate",
"IsStatusForClosedCall": false,
"Sequence": 220,
"RequirePlanning": false,
"ClassName": "clientupdate",
"Translation": "Updated by employee",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "9091bc00-b55a-4836-8cb7-7d633d5a076e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "ClientUpdateReceive",
"IsStatusForClosedCall": false,
"Sequence": 500,
"RequirePlanning": false,
"ClassName": "updatevanklantontvangen",
"Translation": "Client update received",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "df794744-91b8-42ef-a79b-8448ba342293",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "WorkPlans",
"IsStatusForClosedCall": false,
"Sequence": 502,
"RequirePlanning": false,
"ClassName": "workplans",
"Translation": "Schedule activities",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "4feaaa86-8757-44d6-a8d6-99fdf9f8ce4d",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "New",
"IsStatusForClosedCall": false,
"Sequence": 1,
"RequirePlanning": false,
"ClassName": "new",
"Translation": "New",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "db4e4023-82a7-4112-8d36-acf4238773f7",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "WorkOnSitePlans",
"IsStatusForClosedCall": false,
"Sequence": 150,
"RequirePlanning": false,
"ClassName": "callactionplaned",
"Translation": "Schedule onsite activities",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "c9e91523-522f-4517-b388-ae492e965bd2",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "SupplierUpdate",
"IsStatusForClosedCall": false,
"Sequence": 230,
"RequirePlanning": false,
"ClassName": "supplierupdate",
"Translation": "Updated by supplier",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "0a83b991-15a6-4e8e-b99f-b079a29f5c1e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "CallClosed",
"IsStatusForClosedCall": true,
"Sequence": 9999,
"RequirePlanning": false,
"ClassName": "callclosed",
"Translation": "Closed",
"Active": true,
"AllowInactive": true,
"NextStatus": "9958d2d5-b7ac-452b-bc31-f87739958bff",
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "98c2b674-ad5d-4895-8160-b188b1d82996",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Solved",
"IsStatusForClosedCall": true,
"Sequence": 116,
"RequirePlanning": false,
"ClassName": "completed",
"Translation": "Solved",
"Active": true,
"AllowInactive": false,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "52d6d4a2-9ae4-48e5-b351-b409398b1d2e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "PendingStart",
"IsStatusForClosedCall": false,
"Sequence": 112,
"RequirePlanning": false,
"ClassName": "new",
"Translation": "Pending start",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "b838914b-476b-445b-be8c-c62adefe018e",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "PendingAtSupplier",
"IsStatusForClosedCall": false,
"Sequence": 130,
"RequirePlanning": false,
"ClassName": "pendingatsupplier",
"Translation": "Pending vendor/supplier",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "0b8497d4-e867-47de-9c9a-cc51b6e97668",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "OnHold",
"IsStatusForClosedCall": false,
"Sequence": 115,
"RequirePlanning": false,
"ClassName": "onhold",
"Translation": "On hold",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 2,
"LastChangeDate": null
},
{
"Id": "f2ad73d8-19cd-4d47-8884-d08c57aa1320",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "AnalysisSecondLineManagement",
"IsStatusForClosedCall": false,
"Sequence": 99991,
"RequirePlanning": false,
"ClassName": null,
"Translation": "On hold",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "15887a59-097b-457e-b39a-e5d330b370cc",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "CallInProgress",
"IsStatusForClosedCall": false,
"Sequence": 120,
"RequirePlanning": false,
"ClassName": "callinprogress",
"Translation": "In progress",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "ef76bdb4-4884-4330-b09f-f064b841d10d",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "WaitingForClient",
"IsStatusForClosedCall": false,
"Sequence": 140,
"RequirePlanning": false,
"ClassName": "waitingforclient",
"Translation": "Waiting for response",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "9958d2d5-b7ac-452b-bc31-f87739958b00",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "OutSLA",
"IsStatusForClosedCall": false,
"Sequence": 10000,
"RequirePlanning": false,
"ClassName": "outOfSLA",
"Translation": "SLA breach",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
},
{
"Id": "9958d2d5-b7ac-452b-bc31-f87739958bff",
"Tenant": "8dcdc278-e900-458a-b245-eaca02c05939",
"Name": "Reopened",
"IsStatusForClosedCall": false,
"Sequence": 110,
"RequirePlanning": false,
"ClassName": "reopened",
"Translation": "Reopened",
"Active": true,
"AllowInactive": true,
"NextStatus": null,
"StatusType": 0,
"LastChangeDate": null
}
]
}