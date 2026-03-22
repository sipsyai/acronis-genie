# JSON alert examples

Working with plans > SIEM forwarding plans > SIEM data format and examples > JSON alert examples
JSON alert examples
Copy
{"id":"A5BD4F48-6D24-4FF0-BD43-FD7CE7367B0E","type":"EDRIncidentDetected","createdAt":"2025-10-24T15:24:25.873371Z","severity":"warning","receivedAt":"2025-10-24T15:24:26.63156432Z","updatedAt":"2025-10-24T15:24:26.63156432Z","tenant":{"id":"102","uuid":"38c8ff04-99fb-446a-967d-461a5e299814","locator":"/1/100/101/102/"},"category":"EDR","details":{"changeId":"1","customerIncidentId":"1","customerName":"DemoCustomer","detectionTime":"2025-10-24T15:24:25.873371Z","edrAlertId":"637e4e23-bf95-4147-8fb8-4b3664a7f51f","incidentCategories":"URL_BLOCKED","incidentId":"5894ce04-f94b-4cd3-8685-f91efb3fd6a0","incidentTrigger":"no-ssl.acronis-detection-test.com","isMalicious":"true","isMitigated":"true","mitigationState":"AUTO_MITIGATED","osType":"WINDOWS","redirectLink":"https://eu-cloud.acronis.com/ui/#/endpoint-detection/customer/101/incidents/5894ce04-f94b-4cd3-8685-f91efb3fd6a0/investigation","resourceId":"292ab054-61b9-41ec-9416-1f1b679a67a5","resourceName":"DESKTOP-VBTMUIG","verdict":"Malicious threat"}}
{"id":"33A7E16F-9FE4-08BB-0EA1-EF91855ACAFC","type":"BackupCanceled","createdAt":"2025-10-24T15:19:15Z","severity":"warning","receivedAt":"2025-10-24T15:04:08.316243862Z","updatedAt":"2025-10-24T15:19:15.216375706Z","tenant":{"id":"104","uuid":"04cc830f-cc2d-4d85-bc0c-154d3246ed55","locator":"/1/100/103/104/"},"category":"Backup","details":{"activity":{"id":"EA9B4383-5B06-4F5C-8008-61D329714981"},"activityId":"EA9B4383-5B06-4F5C-8008-61D329714981","backupLocations":[{"name":"","type":"cloud"}],"backupSourcesType":"machines","finishTime":1761319155,"planId":"A0210313-39A8-469F-AC1D-D68B88923322","planName":"Linux","resourceId":"9386E27C-A64C-4E24-A2BC-391A0DC8F9DE","resourceName":"syslog","startTime":1761319142}}



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.