---
title: "SIEM JSON format examples and syslog configuration"
section: "Working with plans"
subsection: "SIEM forwarding plans"
page_range: "279-287"
tags: [SIEM, JSON, data format, alert examples, event examples, activity examples, audit log, syslog, rsyslog, Red Hat, Debian]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#siem-integration.html"
---

# JSON file format examples

The JSON (JavaScript Object Notation) file format provides a highly flexible structure that allows custom, complex data. It is best suited for modern log management platforms.

## JSON alert examples

```json
{"id":"A5BD4F48-6D24-4FF0-BD43-
FD7CE7367B0E","type":"EDRIncidentDetected","createdAt":"2025-10-
24T15:24:25.873371Z","severity":"warning","receivedAt":"2025-10-
24T15:24:26.63156432Z","updatedAt":"2025-10-24T15:24:26.63156432Z","tenant":
{"id":"102","uuid":"38c8ff04-99fb-446a-967d-
461a5e299814","locator":"/1/100/101/102/"},"category":"EDR","details":
{"changeId":"1","customerIncidentId":"1","customerName":"DemoCustomer","detectionTime":"2025-10-24T15:24:25.873371Z","edrAlertId":"637e4e23-bf95-4147-8fb8-
4b3664a7f51f","incidentCategories":"URL_BLOCKED","incidentId":"5894ce04-f94b-4cd3-
8685-f91efb3fd6a0","incidentTrigger":"no-ssl.acronis-detection-
test.com","isMalicious":"true","isMitigated":"true","mitigationState":"AUTO_
MITIGATED","osType":"WINDOWS","redirectLink":"https://eu-
cloud.acronis.com/ui/#/endpoint-detection/customer/101/incidents/5894ce04-f94b-4cd3-
8685-f91efb3fd6a0/investigation","resourceId":"292ab054-61b9-41ec-9416-
1f1b679a67a5","resourceName":"DESKTOP-VBTMUIG","verdict":"Malicious threat"}}
```

```json
{"id":"33A7E16F-9FE4-08BB-0EA1-
EF91855ACAFC","type":"BackupCanceled","createdAt":"2025-10-
24T15:19:15Z","severity":"warning","receivedAt":"2025-10-
24T15:04:08.316243862Z","updatedAt":"2025-10-24T15:19:15.216375706Z","tenant":
{"id":"104","uuid":"04cc830f-cc2d-4d85-bc0c-
154d3246ed55","locator":"/1/100/103/104/"},"category":"Backup","details":
{"activity":{"id":"EA9B4383-5B06-4F5C-8008-61D329714981"},"activityId":"EA9B4383-
5B06-4F5C-8008-61D329714981","backupLocations":
[{"name":"","type":"cloud"}],"backupSourcesType":"machines","finishTime":1761319155,
"planId":"A0210313-39A8-469F-AC1D-
D68B88923322","planName":"Linux","resourceId":"9386E27C-A64C-4E24-A2BC-
391A0DC8F9DE","resourceName":"syslog","startTime":1761319142}}
```

## JSON event examples

```json
{"id":"dc405251-539d-11cc-612f-86ebefff04bf","type":"cti.a.p.em.event.v1.0~a.active_
protection.agent.disabling_uninstall_protection_requested.v1.0","time":"2025-10-
10T17:24:19Z","ingest_time":"2025-10-10T17:24:19.619132791Z","source":"active-
protection-service","tenant_id":"ba959847-ca47-4a48-90a5-cb42789d5b34","client_
id":"c8d66ac4-0d5b-4ecb-b1b0-c3649df91231"}
```

```json
{"id":"29126f6f-218c-49d4-82a6-
3bbc5ef1e405","type":"cti.a.p.em.event.v1.0~a.p.agent.re_
registered.v1.0","time":"2025-10-10T17:25:08.517475067Z","ingest_time":"2025-10-
10T17:25:08.989631899Z","source":"agent-manager","subject":"c8d66ac4-0d5b-4ecb-b1b0-
c3649df91231","tenant_id":"ba959847-ca47-4a48-90a5-cb42789d5b34"}
```

```json
{"id":"1d21027d-5282-4e82-90a7-
de907a6b8808","type":"cti.a.p.em.event.v1.0~a.edr.incident.created.v1.0","time":"2025-10-24T15:25:54.348310092Z","ingest_time":"2025-10-
24T15:25:54.354555228Z","source":"edr-etlsvc/2509.1.0-394","subject":"5894ce04-f94b-
4cd3-8685-f91efb3fd6a0","tenant_id":"38c8ff04-99fb-446a-967d-461a5e299814"}
```

## JSON activity examples

```json
{"uuid":"0b013dcd-a606-4baf-80d9-
e209d74eb0f6","type":"policy.apply","queue":"legacySync","priority":"normal","tenant":{"id":"66","uuid":"07f6adf7-4665-4340-865d-
c4a4c66f4dcd","name":"DemoCustomer2","locator":"/1/66/"},"cancellable":true,"startedByUser":"DemoCustomer2","policy":{"id":"8cc61f3c-46b0-40a6-9d60-
7d72f68555db","type":"policy.protection.total","name":"XDR plan"},"resource":
{"id":"3b9187d6-0853-45ff-aab0-0c68cd643068","type":"machine","name":"WIN-
R1OR1V5M79O"},"context":{"IsProcessRoot":true,"Persistent":{"PlanID":"8cc61f3c-46b0-
40a6-9d60-7d72f68555db","PlanName":"XDR plan"},"PlanName":"XDR
plan","Specific":"Business","isLegacy":true,"title":"Applying plan 'XDR plan' with
ID '8cc61f3c-46b0-40a6-9d60-7d72f68555db' to resource 'WIN-R1OR1V5M79O' with ID
'3b9187d6-0853-45ff-aab0-
0c68cd643068'"},"id":163470203341038796,"idString":"1634702033410387968","state":"completed","issuer":{"id":"","clusterId":""},"enqueuedAt":"2025-10-
10T17:22:10.323642031Z","startedAt":"2025-10-
10T17:22:10.323642031Z","updatedAt":"2025-10-
10T17:22:10.350557478Z","completedAt":"2025-10-10T17:22:10.323642031Z","tenant":
{"id":"66","uuid":"07f6adf7-4665-4340-865d-
c4a4c66f4dcd","name":"DemoCustomer2","locator":"/1/66/"},"executor":
{"id":"","clusterId":""},"result":{"code":"ok"}}
```

## JSON audit log example

```json
{"created_at":"2025-10-10T17:24:27.614209Z","id":"40731c13-d69d-4557-a20a-
9009addfd65b","date":"2025-10-10T17:24:23Z","event_type":"settings_
service.audit.value.update","request_type":"api","initiator_
ip":"10.233.95.90","initiator_tenant_name":"/","initiator_tenant_uuid":"ea80595e-
d07e-402a-b5bf-cb854cf6a437","object_name":"uninstall_protection","object_tenant_
name":"Demo Customer2 (DemoCustomer2)","object_tenant_uuid":"ba959847-ca47-4a48-
90a5-cb42789d5b34","original_event_uuid":"bf70ee8e-3c55-49ed-98ca-
b089490a4758","severity_int":6,"severity_name":"info","tag":"all","topic":"audit_
event_retention"}
```

# Red Hat content example

The following is an example of Red Hat-based (Rocky Linux) SIEM content. This content is found in the `/etc/rsyslog.conf` file.

```conf
# rsyslog configuration file

# For more information see /usr/share/doc/rsyslog-*/rsyslog_conf.html
# or latest version online at http://www.rsyslog.com/doc/rsyslog_conf.html
# If you experience problems, see http://www.rsyslog.com/doc/troubleshoot.html

#### GLOBAL DIRECTIVES ####

# Where to place auxiliary files
global(workDirectory="/var/lib/rsyslog")

# Use default timestamp format
module(load="builtin:omfile" Template="RSYSLOG_TraditionalFileFormat")

#### MODULES ####

module(load="imuxsock"    # provides support for local system logging (e.g. via
logger command)
    SysSock.Use="off") # Turn off message reception via local log socket;
                        # local messages are retrieved through imjournal now.
module(load="imjournal"             # provides access to the systemd journal
    UsePid="system" # PID number is retrieved as the ID of the process the
journal entry originates from
    FileCreateMode="0644" # Set the access permissions for the state file
    StateFile="imjournal.state") # File to store the position in the journal

# Include all config files in /etc/rsyslog.d/
include(file="/etc/rsyslog.d/*.conf" mode="optional")

#### RULES ####

# Log anything (except mail) of level info or higher.
# Don't log private authentication messages!
*.info;mail.none;authpriv.none;cron.none      /var/log/messages

# The authpriv file has restricted access.
authpriv.*                                    /var/log/secure

# Log all the mail messages in one place.
mail.*                                        -/var/log/maillog

# Log cron stuff
cron.*                                        /var/log/cron

# Everybody gets emergency messages
*.emerg                                       :omusrmsg:*

# Save news errors of level crit and higher in a special file.
uucp,news.crit                                /var/log/spooler

# Save boot messages also to boot.log
local7.*                                      /var/log/boot.log

# ### sample forwarding rule ###
#action(type="omfwd"
# # An on-disk queue is created for this action. If the remote host is
# # down, messages are spooled to disk and sent when it is up again.
#queue.filename="fwdRule1"       # unique name prefix for spool files
#queue.maxdiskspace="1g"         # 1gb space limit (use as much as possible)
#queue.saveonshutdown="on"       # save messages to disk on shutdown
#queue.type="LinkedList"         # run asynchronously
#action.resumeRetryCount="-1"    # infinite retries if host is down
# # Remote Logging (we use TCP for reliable delivery)
# # remote_host is: name/ip, e.g. 192.168.0.1, port optional e.g. 10514
#Target="remote_host" Port="XXX" Protocol="tcp")
```

# Debian content example

The following is an example of Debian-based (Ubuntu Linux) SIEM content. This content is found in the `/etc/rsyslog.conf` file.

```conf
# /etc/rsyslog.conf configuration file for rsyslog
#
# For more information install rsyslog-doc and see
# /usr/share/doc/rsyslog-doc/html/configuration/index.html
#
# Default logging rules can be found in /etc/rsyslog.d/50-default.conf

#################
#### MODULES ####
#################

module(load="imuxsock") # provides support for local system logging
#module(load="immark")  # provides --MARK-- message capability

# provides UDP syslog reception
#module(load="imudp")
#input(type="imudp" port="514")

# provides TCP syslog reception
#module(load="imtcp")
#input(type="imtcp" port="514")

# provides kernel logging support and enable non-kernel klog messages
module(load="imklog" permitnonkernelfacility="on")

###########################
#### GLOBAL DIRECTIVES ####
###########################

#
# Use traditional timestamp format.
# To enable high precision timestamps, comment out the following line.
#
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

# Filter duplicated messages
$RepeatedMsgReduction on

#
# Set the default permissions for all log files.
#
```
