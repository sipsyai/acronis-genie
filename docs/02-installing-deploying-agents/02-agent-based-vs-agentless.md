---
title: "Agent-based and agentless backup"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "39"
tags: ["agent-based", "agentless", "backup", "virtual-machines", "virtual-appliance"]
acronis_version: "26.02"
---

# Agent-based and agentless backup

Agent-based backup requires that a protection agent is installed on each protected machine. Agent-based backup is supported on all physical and virtual machines. For more information about which agent you need and where to install it, see [Which agent do I need?](./03-which-agent-do-i-need.md).

Agentless backup is supported by some virtualization platforms and it is not available for physical machines. Agentless backup requires only one protection agent, which is installed on a dedicated machine in the virtual environment. This agent backs up all other virtual machines in this environment. For more information about the supported backup types per virtualization platform, see "Supported virtualization platforms" (p. 495).

For some virtualization platforms, virtual appliances are available. A virtual appliance (VA) is a ready-made virtual machine that contains a protection agent. The virtual appliances are available in hypervisor-specific formats, such as .ovf, .ova, or .qcow.

## Which backup type do I need?

**We recommend the agent-based backup if you need the following:**

- Additional protection functionality, such as antivirus and antimalware, patch management, or remote desktop connection. See [Supported protection features by operating system](../01-getting-started/10a-supported-features-protection-plans-and-backup.md).
- Separate virtual machines at the tenant level. For example, because you want to provide the users in the tenant with access only to their own backups.
- File-level backups that you can recover to the guest operating systems.

**We recommend the agentless backup if you need the following:**

- Only backup, without any additional protection features.
- Simplified management — you can back up multiple virtual machines by installing and configuring only one agent.
- Minimal resource usage — one dedicated agent uses less CPU and RAM than multiple agents installed on each virtual machine in your environment.
- Specific backup setups, such as LAN-free backup. For more information about this feature, see "Agent for VMware - LAN-free backup" (p. 887).
- Less configuration overhead. The dedicated agent backs up the virtual machines on the hypervisor level, regardless of guest operating systems.
