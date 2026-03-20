---
title: "SIEM data format and CEF examples"
section: "Working with plans"
subsection: "SIEM forwarding plans"
page_range: "273-279"
tags: [SIEM, CEF, data format, alert examples, event examples, activity examples, audit log examples]
acronis_version: "26.02"
---

# SIEM data format and examples

Acronis SIEM forwarding plans can send data for Acronis alerts, events, activities, tasks, and audit log entries, with one of two file formats: JSON and CEF.

SIEM files include different data with distinct structures, depending on data type and the forwarding plan file format. This section provides examples of data for all four data types in both formats.

## CEF file format

The CEF (Common Event Format) file format contains:
- Alert examples
- Event examples
- Activity examples
- Audit log examples

## CEF alert examples

```
Oct 15 14:45:01 WIN-R1OR1V5M79O siem_log_forwarder[8608]:
CEF:0|Acronis|DemoCustomer|1.0|BackupStatusUnknown|BackupStatusUnknown|5|cs1=
{"agentId":"c8d66ac4-0d5b-4ecb-b1b0-c3649df91231","backupLocations":
[{"type":"cloud"}],"backupSourcesType":"files","errorMessage":{"kbLink":
{"serCode":"BackupStatusUnknown"}},"planId":"a92799fc-f657-4a10-b6ed-
16975c4d0ef0","planName":"Protect Win","resourceId":"3b9187d6-0853-45ff-aab0-
0c68cd643068","resourceName":"WIN-R1OR1V5M79O"} cs1Label=alertdetails
deviceExternalId=3b9187d6-0853-45ff-aab0-0c68cd643068 dvchost=WIN-R1OR1V5M79O
```

```
Oct 15 14:42:46 WIN-R1OR1V5M79O siem_log_forwarder[8608]:
CEF:0|Acronis|DemoCustomer|1.0|BackupFailed|BackupFailed|10|cs1={"activity":
{"id":"FE0B2835-3C9D-4D5A-9D02-FD0CBE5042B8","type":"8F01AC13-F59E-4851-9204-
DE1FD77E36B4"},"activityId":"FE0B2835-3C9D-4D5A-9D02-
FD0CBE5042B8","backupLocations":
[{"name":"","type":"cloud"}],"backupSourcesType":"machines","error":
{"code":20250646,"fields":{"$module":"service_process_vsa64_41100","AgentName":"WIN-
R1OR1V5M79O","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"},"src":
{"file":"c:\\\\b\\\\1223\\\\enterprise\\\\common\\\\tol\\\\command\\\\command.cpp",
"func":"Tol::`anonymous-
namespace'::MakeFailResultWithName","line":503,"tag":"0x8d165e86fb8195c5"},...}
cs1Label=alertdetails deviceExternalId=3b9187d6-0853-45ff-aab0-0c68cd643068
dvchost=WIN-R1OR1V5M79O
```

```
Oct 24 15:15:00 syslog siem_log_forwarder[2622955]:
CEF:0|Acronis|DemoCustomer2|1.0|BackupCanceled|BackupCanceled|5|cs1={"activity":
{"id":"4084E850-0F4A-448A-AF1A-D7B5A49567D2"},"activityId":"4084E850-0F4A-448A-AF1A-
D7B5A49567D2","backupLocations":
[{"name":"","type":"cloud"}],"backupSourcesType":"machines","finishTime":1761318832,
"planId":"A0210313-39A8-469F-AC1D-
D68B88923322","planName":"Linux","resourceId":"9386E27C-A64C-4E24-A2BC-
391A0DC8F9DE","resourceName":"syslog","startTime":1761318829} cs1Label=alertdetails
deviceExternalId=9386E27C-A64C-4E24-A2BC-391A0DC8F9DE dvchost=syslog
```

```
Oct 24 09:00:03 DESKTOP-VBTMUIG siem_log_forwarder[776]:
CEF:0|Acronis|DemoCustomer3|1.0|EDRIncidentDetected|EDRIncidentDetected|10|cs1=
{"changeId":"2","customerIncidentId":"2","customerName":"CustomerA","detectionTime":
"2025-10-24T15:49:25.717247Z","edrAlertId":"c60abcd5-ffd5-4bdb-8c2c-
23aa275ae0b5","incidentCategories":"MALWARE_DETECTED","incidentId":"a999c62b-9b1e-
4d3a-85d9-d54743107b22","incidentTrigger":"New Text
Document.txt","isMalicious":"true","isMitigated":"false","mitigationState":"NOT_
MITIGATED","osType":"WINDOWS","redirectLink":"https://eu-
cloud.acronis.com/ui/#/endpoint-detection/customer/101/incidents/a999c62b-9b1e-4d3a-
85d9-d54743107b22/investigation","resourceId":"292ab054-61b9-41ec-9416-
1f1b679a67a5","resourceName":"DESKTOP-VBTMUIG","verdict":"Malicious threat"}
cs1Label=alertdetails deviceExternalId=292ab054-61b9-41ec-9416-1f1b679a67a5
dvchost=DESKTOP-VBTMUIG
```

## CEF event examples

```
Oct 10 20:14:15 WIN-R1OR1V5M79O siem_log_forwarder[8088]:
CEF:0|Acronis|DemoCustomer2|1.0|cti.a.p.em.event.v1.0~a.p.agent.re_
registered.v1.0|cti.a.p.em.event.v1.0~a.p.agent.re_registered.v1.0|1|cs1=
{"id":"380b8b6f-e4cb-4d36-84a2-
2894a7e298b3","type":"cti.a.p.em.event.v1.0~a.p.agent.re_
registered.v1.0","time":"2025-10-10T17:01:32.232185894Z","ingest_time":"2025-10-
10T17:01:32.266874946Z","source":"agent-manager","subject":"c8d66ac4-0d5b-4ecb-b1b0-
c3649df91231","tenant_id":"ba959847-ca47-4a48-90a5-cb42789d5b34"}
cs1Label=eventdetails
```

```
Oct 10 20:14:15 WIN-R1OR1V5M79O siem_log_forwarder[8088]:
CEF:0|Acronis|DemoCustomer2|1.0|cti.a.p.em.event.v1.0~a.active_
protection.agent.disabling_uninstall_protection_
requested.v1.0|...|1|cs1={"id":"4b6b4e57-a679-0d94-2175-
2a015cdfa9f6","type":"cti.a.p.em.event.v1.0~a.active_protection.agent.disabling_
uninstall_protection_requested.v1.0","time":"2025-10-10T17:00:51Z","ingest_
time":"2025-10-10T17:00:51.247926345Z","source":"active-protection-service","tenant_
id":"ba959847-ca47-4a48-90a5-cb42789d5b34","client_id":"c8d66ac4-0d5b-4ecb-b1b0-
c3649df91231"} cs1Label=eventdetails
```

## CEF activity examples

```
Oct 10 20:14:15 WIN-R1OR1V5M79O siem_log_forwarder[8088]:
CEF:0|Acronis|DemoCustomer2|1.0|agent.add|agent.add|1|cs1=
{"IsProcessRoot":true,"Persistent":{"ID":"c8d66ac4-0d5b-4ecb-b1b0-
c3649df91231","Name":"WIN-
R1OR1V5M79O","OwnerID":"67"},"Specific":"Business","UserName":"WIN-
R1OR1V5M79O\\\\AMS User","isLegacy":true,"title":"Adding agent 'WIN-R1OR1V5M79O' to
the management server"} cs1Label=taskcontext cs2={"code":"ok"} cs2Label=taskresult
cs3={"uuid":"ee54f502-4a06-498c-8b00-22824ba40231","type":"A59E8BF2-39C3-42C4-B667-
CB672381A214","queue":"legacySync","priority":"normal","tenant":
{"id":"67","uuid":"ba959847-ca47-4a48-90a5-cb42789d5b34","name":"Demo Customer2
(DemoCustomer2)","locator":"/1/66/67/"},"cancellable":true,"startedByUser":"WIN-
R1OR1V5M79O\\\\AMS User",...} cs3Label=taskdetails dvchost=
suser= deviceExternalId=
```

## CEF audit log examples

```
Oct 15 14:42:46 WIN-R1OR1V5M79O siem_log_forwarder[8608]: CEF:0|Acronis
audit|DemoCustomer|1.0|user.login|user.login|2|cs1={"created_at":"2025-10-
15T11:36:34.623186Z","id":"9281f317-2d71-4741-ac85-d085c94e95b6","date":"2025-10-
15T11:36:28Z","event_type":"user.login","request_type":"ui","initiator_
ip":"10.136.42.69","initiator_tenant_name":"DemoCustomer","initiator_tenant_
uuid":"882d7a61-7124-433d-88fd-215399399838","initiator_user_
name":"DemoCustomer","initiator_user_uuid":"f0c90ee2-b350-47be-a6d8-
ce2e178bb937","object_name":"Demo Customer (DemoCustomer)","object_tenant_
name":"DemoCustomer","object_tenant_uuid":"882d7a61-7124-433d-88fd-
215399399838","object_user_name":"DemoCustomer","object_user_uuid":"f0c90ee2-b350-
47be-a6d8-ce2e178bb937","original_event_uuid":"1e179947-6608-49cb-b733-
d744c4bbc90e","severity_int":6,"severity_name":"info","tag":"all","topic":"audit_
event_retention"} cs1Label=eventdetails
```

```
Oct 15 14:42:46 WIN-R1OR1V5M79O siem_log_forwarder[8608]: CEF:0|Acronis
audit|DemoCustomer|1.0|settings_service.audit.setting.value.update|settings_
service.audit.setting.value.update|2|cs1={"created_at":"2025-10-
15T11:42:14.614182Z","id":"101f7fb1-dd59-424a-b016-8986691f139f","date":"2025-10-
15T11:42:11Z","event_type":"settings_service.audit.setting.value.update","request_
type":"api","initiator_ip":"10.233.95.53","initiator_tenant_name":"/","initiator_
tenant_uuid":"0e467be0-d567-4427-9dce-e7a2a16f9ada","object_name":"uninstall_
protection","object_tenant_name":"Demo Customer (DemoCustomer)",...,
"severity_name":"info","tag":"all","topic":"audit_event_retention"}
cs1Label=eventdetails
```
