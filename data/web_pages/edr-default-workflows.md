# Endpoint Detection and Response (EDR) workflows

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Endpoint Detection and Response (EDR) workflows
Endpoint Detection and Response (EDR) workflows

There are six default EDR workflows that you can configure according to your requirements:

Quarantine threat (when an EDR incident is created)
Quarantine threat (when an EDR incident is updated)
Isolate workload (when an EDR incident is created)
Isolate workload (when an EDR incident is updated)
Malware incident requiring attention
Incident requiring attention

The following table describes the default triggers, conditions, and actions applicable to each workflow. For more information about modifying these conditions and actions, see Configuring an automated Endpoint Detection and Response (EDR) workflow.

Workflow	Trigger	Conditions	Actions
Quarantine threat	EDR incident is created

Threat status = "Not mitigated"

AND

Incident state = "Not started"

AND

Severity = "High"

AND

Incident type = "Process detected" OR "Malware detected"



Stop the process.

Quarantine the process.

Add a comment. The default comment text is "<Workflow name> - High severity threat quarantined".

Close the incident.


Quarantine threat	EDR incident is updated
Isolate workload	EDR incident is created

Threat status = "Not mitigated"

AND

Incident state = "Not started"

AND

Severity = "Critical"

AND

Verdict = "Malicious"

AND

Positivity Level > 9

AND

Incident type = "Process detected" OR "Malware detected"



Stop the process.

Quarantine the process.

Isolate the workload.

Add a comment. The default comment text is "<Workflow name> - Workload <Workload name> has been isolated after critical malware detection".

Send email to selected Cyber Protect console users.


Isolate workload	EDR incident is updated
Malware incident requiring attention	EDR incident is created

Threat status = "Not mitigated"

AND

Incident state = "Not started"

AND

Incident age > 8 hours

AND

Severity = "High" OR "Critical"

AND

Verdict = "Malicious"

AND

Incident type = "Malware detection"



Stop the process.

Quarantine the process.

Add a comment. The default comment text is "<Workflow name> - High/Critical severity threat quarantine due to no investigation for 8h".

Send email to selected Cyber Protect console users.


Incident requiring attention	EDR incident is created

Threat status = "Not mitigated"

AND

Incident state = "Not started"

AND

Incident age > 24 hours

AND

Severity = "High" OR "Critical"

AND

Verdict = "Malicious"



Stop the process.

Quarantine the process.

Add a comment. The default comment text is "<Workflow name> - High/Critical severity threat quarantine due to no investigation for 24h".

Send email to selected Cyber Protect console users.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.