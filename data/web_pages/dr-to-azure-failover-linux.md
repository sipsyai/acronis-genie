# Requirements and limitations for failover of Linux VMs to Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure > Requirements and limitations for failover of Linux VMs to Microsoft Azure
Requirements and limitations for failover of Linux VMs to Microsoft Azure

This section outlines key requirements and limitations for failing over Linux workloads to Microsoft Azure, especially in environments without Internet access.

Requirements
Azure VM Agent installation with Internet access

The Azure VM Agent is automatically installed during test and production failover.

The required Linux tools (for example, cloud-init, network drivers) are fetched from public repositories (for example, archive.ubuntu.com or mirror.centos.org).

For security, you can allow outbound https only to specific repositories.

Azure VM Agent installation without Internet access

You must manually install the Azure VM Agent on the source Linux machine before failover.

Without the agent, the failover may fail or result in limited VM functionality.

Limitations
Internet dependency

No Internet access on the target Azure VM will require an Azure agent to be preinstalled on the original workload, which adds configuration overhead.

No access to Internet might prevent post-failover updates (for example, networking or backup tools).

Recommendations
Allow Internet access for production and test VNet before a failover. This is a default setup.
Restrict outbound access to only specific Linux repositories if you know them before a failover.
Restrict access to specific production services during test failovers.
You can use internal mirrors or VPN to minimize Internet reliance.
Run regular test failovers to ensure environment readiness.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.