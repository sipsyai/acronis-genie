---
title: "Cyber Protection, Protection status, EDR, and Discovered devices widgets"
section: "Understanding your current level of protection"
subsection: "Monitoring"
page_range: "325-327"
tags: ["widgets", "cyber-protection", "protection-status", "EDR", "discovered-devices", "incidents", "threat-status"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#cyber-protection-getting-started.html"
---

# Cyber Protection widget

This widget shows the overall information about the size of backups, blocked malware, blocked URLs, found vulnerabilities, and installed patches.

The upper row shows the current statistics:

- **Backed up today** — the sum of recovery point sizes for the last 24 hours
- **Malware blocked** — the number of currently active alerts about malware blocked
- **URLs blocked** — the number of currently active alerts about URLs blocked
- **Existing vulnerabilities** — the number of currently existing vulnerabilities
- **Patches ready to install** — the number of currently available patches to be installed

The lower row shows the overall statistics:

- The compressed size of all backups
- The accumulated number of blocked malware across all machines
- The accumulated number of blocked URLs across all machines
- The accumulated number of discovered vulnerabilities across all machines
- The accumulated number of installed updates/patches across all machines

> **Important:** The values of storage usage displayed in the product UI are in binary byte units — mebibytes (MiB), gibibytes (GiB), and tebibytes (TiB) — even though the labels show MB, GB, and TB respectively.

---

# Protection status widget

This widget shows the current protection status for all machines.

A machine can be in one of the following statuses:

- **Protected** — machines with applied protection plan.
- **Unprotected** — machines without applied protection plan. These include both discovered machines and managed machines with no protection plan applied.
- **Managed** — machines with installed protection agent.
- **Discovered** — machines without installed protection agent.

If you click on the machine status, you will be redirected to the list of machines with this status for more details.

---

# Discovered devices widget

This widget shows detailed information about the devices that were discovered in the organization's networks, including device name, type, operating system, manufacturer, model, IP address, MAC address, organization, first/last discovered timestamps, and discovery type.

---

# Endpoint Detection and Response (EDR) widgets

Endpoint Detection and Response (EDR) includes seven widgets, all of which can be accessed from the **Overview** dashboard; three of these widgets are also displayed by default within the EDR functionality.

The seven widgets available are:

1. **Top incident distribution per workload** — Displays the top five workloads with the most incidents. Hover over a workload row to view a breakdown of the current investigation state for the incidents; the investigation states are **Not started**, **Investigating**, **Closed**, and **False positive**. Click on the workload to analyze further.

2. **Threat status** — Displays the current threat status for all workloads, highlighting the current number of incidents that are not mitigated and that need investigating. The widget also indicates the number of incidents that were mitigated (manually and/or automatically by the system).

3. **Incident severity history** — A bar chart showing the distribution of incidents by severity level (Critical, High, Medium, Low) over a configurable time range. You can click on any bar to drill down into the incident list.

4. **Security incident MTTR** — Shows the Mean Time To Remediate for security incidents over the selected time range. This helps measure how quickly your team responds to and resolves security threats.

5. **Security incident burndown** — A chart showing the trend of open vs resolved security incidents over time. Helps visualize whether your team is keeping up with incoming incidents.

6. **Detection by tactics** — Displayed in EDR. Shows the distribution of detections mapped to MITRE ATT&CK tactics, helping identify the most common attack patterns in your environment.

7. **Workload network status** — Shows the current network isolation status of workloads, indicating which workloads are isolated from the network and which are connected.
