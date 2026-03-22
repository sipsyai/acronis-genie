# Prioritize which incidents need immediate attention

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Reviewing incidents > Prioritize which incidents need immediate attention
Prioritize which incidents need immediate attention

The Cyber Protect console incident list can be accessed at any time from the Protection menu in the Cyber Protect console. The incident list gives you a quick-glance overview of any attacks or threats, enabling you to prioritize incidents that require attention.

To ensure your workloads remain secure, always analyze and prioritize the incidents that are ongoing or not mitigated.
How to analyze which security incidents need immediate attention

The incident list enables you to analyze and prioritize the listed incidents that require attention. You can:

View which incidents are currently not mitigated: Quickly understand from the incident list if any attacks are currently in progress. Any incidents that are not mitigated, as indicated in the Threat status column, should be looked at immediately (by default, the incident list is filtered to display these incidents).
Understand the scope and impact of incidents: Based on your filtering of newly opened or ongoing attacks, understand the severity for the filtered incidents as well as the impact on your business.

Once you have a refined list of the most important incidents, you can then analyze incident details to get a better understanding of a specific incident , as well as the techniques used by the attacker to achieve their objective. For more information, see Analyze incident details.

By default, the incident list is sorted according to the Updated column, which details the date and time the incident was last updated with new detections recorded inside the incident. Note that any existing incident can be updated at any time, even if the incident was previously closed. You can also filter the list to show newly opened or ongoing attacks according to your requirements, as described in the procedure below.

To filter the incident list

At the top of the Incident list, click Filter to filter the displayed list of incidents. For example, if you select a start and end date in the Created field, the incident list and widgets display the relevant incidents created during the defined time period.

When done, click Apply.
Viewing which incidents are currently not mitigated

You can view the current threat status for incidents in the Threat status column, which shows if the incident is Mitigated or Not mitigated. The threat status is automatically defined by EDR; any incident that is not mitigated should be investigated as soon as possible.

You can then refine the displayed incident list further by applying filters. For example, if you want to filter the list according to threat status and a specific level of severity, select the relevant filter options. Once you have filtered the incidents that are of interest to you, you can then investigate them, as described in Investigating incidents.

You can also use the Threat status widget, as shown below, for a quick glance overview of the current threat status. Note that the data displayed in this widget reflects the filters you applied; see To filter the incident list.

Understanding the scope and impact of incidents

You can quickly understand the scope and impact of incidents by reviewing the Severity, Attack info, and Positivity level columns. As mentioned above, after you have determined which incidents are currently in progress you can then filter these additional columns to do the following:

Review which incidents are more critical in the Severity column. The severity of an incident can be one of Critical, High, or Medium.
Critical: There is a severe risk of malicious cyber activity with the risk of compromising critical hosts in your environment.
High: There is a high risk of malicious cyber activity with the risk of severe damage in your environment.
Medium: There is an increased risk of malicious cyber activity.

When determining the severity, the EDR algorithm takes into consideration the workload type as well as the scope of each step of the attack. For example, an incident which includes steps related to credential theft is set to Critical.

Understand why an incident was created in the Incident type column. The incident type can include any one or more of the following:
Ransomware detected
Malware detected
Suspicious process detected
Malicious process detected
Suspicious URL blocked
Malicious URL blocked
Determine which attack techniques are in use in the Attack info column, and understand if there is a common theme or pattern to the attacks.
Confirm how likely an incident is a true malicious attack; the Positivity level column includes a score of between 1-10 (the higher the score, the more likely the attack is a true malicious attack).

After you have found the incidents that need immediate attention, you can then investigate them, as described in Investigating incidents

You can also use the Severity history and Detection by tactics widgets for a quick glance overview of the severity and attack techniques.

The Detection by tactics widget displays the various attack techniques used, with values in green or red indicating the increase or decrease over the previous specified time range. This widget provides an aggregated view of all the objectives in the filtered incidents, giving you a quick overview of the impact on your customers.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.