# Reviewing incidents

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Reviewing incidents
Reviewing incidents

Endpoint Detection and Response (EDR) provides an incident list that includes both prevention (or malware) and suspicious detections on a workload. The incident list gives you a quick-glance overview of any attacks or threats that are affecting your workloads, including threats that are yet to be mitigated.

From the incident list, you can quickly determine:

The security posture of an organization: how many incidents need to be investigated?
Which are the most critical incidents, and prioritize their investigation according to their severity.
Which incidents are new or ongoing.
When logged in as a partner administrator, you can view all EDR incidents in a single screen that consolidates incidents from all your customers, without the need to access each customer's individual incident view. An additional Customers column is displayed, which includes the customer name to which each incident belongs. In addition, the widgets shown on the Overview dashboard display metrics data aggregated across all customers.

The incident list, as shown below, is accessed from the Protection menu in the Cyber Protect console. For further information about reviewing the incidents in the incident list, see Prioritize which incidents need immediate attention To learn more about when an incident is created, see What exactly are incidents?.

If Managed Detection and Response (MDR) is enabled on your workloads, an additional MDR ticket column is displayed. This column display the ticket number provided by the MDR vendor.

The Cyber Protect console must be open in order for you to receive incident notifications.
What exactly are incidents?

Incidents, or security incidents, can be thought of as containers of at least one prevention or suspicious detection point (or a mix), and include all the related events and detections of a single attack. These security incidents can also include additional benign events that give further context into what happened.

This enables you to view attack events together in one single incident, and understand the logical steps that the attacker performed. In addition, it helps speed up the investigation time for an attack.

When EDR is enabled in the protection plan, security incidents are created when:

A prevention layer stops something: These incidents are automatically closed by the system, according to the protection plan settings. However, you can investigate what exactly the malware did before it was stopped. For example, ransomware is stopped when it starts to encrypt files, but prior to that it could have stolen credentials or installed a service.
Suspicious activity is detected by EDR: These are detections that should be investigated and remediated. By reviewing the visually enhanced cyber kill chain (for more information, see How to investigate incidents in the cyber kill chain), you can easily apply the relevant remediation actions.

Prioritize which incidents need immediate attention

Analyze incident details

Search for Indicators of Compromise (IoC) and suspicious activities

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.