# Review and mitigate IOCs on affected workloads

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Investigating incidents > Review and mitigate IOCs on affected workloads
Review and mitigate IOCs on affected workloads

When Endpoint Detection and Response (EDR) is enabled in a protection plan, you can view any known threats that are affecting workloads in the protection plan. You can also mitigate any remaining indicators of compromise (IOCs) that were not automatically mitigated. For information on how to automatically mitigate IOCs, see Define threat feed settings.

To review and mitigate affected workloads

In the Cyber Protect console, go to Monitoring > Threat feed.
Click on a thread to display the details for that threat.
In the Indicators of compromise (IOCs) prevalence section, click the n workloads link to view the workloads with unmitigated IOCs.

In the displayed Workloads page, click on the relevant workload and review its details. You can run specific functionality on the workload, including defining additional URLs to filter (see URL filtering), and blocking malicious processes (refer to the Exclusions section in Antivirus and antimalware protection settings).

For example, if a threat feed indicates that a workload has been affected by an IOC, first locate and analyze the IOC, as described in Review and analyze discovered IOCs. Then go to the protection plan for the workload and define additional protection, such as blocking malicious file hashes or processes.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.