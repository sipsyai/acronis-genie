# Acronis Cyber Protect Cloud - RAG-Ready Documentation

This repository contains chunked, RAG-ready markdown files extracted from the **Acronis Cyber Protect Cloud Console User Guide (v26.02)**.

## Purpose

These markdown documents are designed for use in a Retrieval-Augmented Generation (RAG) system, enabling AI-powered question answering about Acronis Cyber Protect Cloud.

## Source

- **Document:** CyberProtectionService_userguide_en-US.pdf
- **Version:** 26.02
- **Total Pages:** 1,542
- **Language:** English

## Structure

Each chapter is organized into its own directory with numbered markdown files:

```
cyber-protect-cloud-docs/
├── README.md                          # This file
├── 01-getting-started/                # Chapter 1: Getting Started (p. 21-35)
├── 02-installing-deploying-agents/    # Chapter 2: Installing and Deploying Agents (p. 36-207)
├── 03-working-with-plans/             # Chapter 3: Working with Plans (p. 208-247+)
├── 04-monitoring-dashboards/          # Chapter 4: Monitoring and Dashboards (p. 288-327+)
├── 05-managing-workloads/             # Chapter 5: Managing Workloads (p. 368-407+)
├── 06-backup-and-recovery/            # Chapter 6: Backup and Recovery (p. 484-503+)
├── 07-disaster-recovery/              # Chapter 7 (planned)
├── 08-antivirus-antimalware/          # Chapter 8 (planned)
└── 09-genai-protection/               # Chapter 9 (planned)
```

## Chunk Format

Each markdown file follows this format:

```yaml
---
title: "Topic title"
section: "Parent section name"
subsection: "Sub-section name (if applicable)"
page_range: "21-23"
tags: ["relevant", "search", "tags"]
acronis_version: "26.02"
---
```

### Chunk Rules

1. **Self-contained:** Each chunk can be read independently and makes sense on its own
2. **Tables preserved:** All tables are kept in markdown table format
3. **Lists maintained:** Numbered steps and bullet lists are preserved
4. **Image references:** Noted as `[Image: description]`
5. **Cross-references:** Noted as `See: [topic-name]` with relative links
6. **Target size:** 500-1500 words per chunk (tables excluded from count)
7. **Large sections split:** Feature tables are split by category (10a, 10b, etc.)

## Completed Chapters

- [x] **01-getting-started** - Getting Started with Cyber Protection (p. 21-35)
  - Account activation, password requirements, 2FA setup
  - Privacy settings, accessing the service, supported browsers
  - My Inbox (overview, notifications, search)
  - Supported protection features by OS (7 sub-files by category)
  - Supported operating systems and versions

- [x] **02-installing-deploying-agents** - Installing and Deploying Cyber Protection Agents (p. 36-107, partial)
  - Preparation, ports, firewall requirements
  - Agent-based vs agentless backup, which agent to choose
  - System requirements, downloading agents
  - Linux packages required, proxy server settings
  - Dynamic installation of components, macOS permissions
  - FIPS-compliant mode (Windows, Linux, virtual appliances)
  - Installing agents via GUI (Windows, Linux, macOS)
  - Uninstalling agents (all platforms + VMware VA)
  - Installing agents via CLI (Windows, Linux, macOS with full parameters)
  - Registration of workloads (console, credentials, tokens)
  - *Remaining sections (p. 108-207): Registration CLI, updating agents, Group Policy deployment, virtual appliances, device discovery, protection settings — to be completed*

- [x] **03-working-with-plans** - Working with Plans (p. 208-247, partial)
  - Understanding plans: plan types and availability by admin level
  - Built-in plans (Essential, Extended, Complete protection + monitoring + remote management)
  - Default plans, Favorite plans, Preselected plans
  - Plans at different administration levels (Partner/Customer/Unit access matrix)
  - Protection plans and modules (all 13 modules described)
  - Actions with protection plans (apply, edit, export/import, revoke, enable/disable, delete, clone)
  - Compatibility issues and resolution procedures
  - Off-host data protection plans and backup replication
  - Validation methods (VM heartbeat, screenshot validation, checksum verification)
  - *Remaining sections (p. 248+): Cleanup, Conversion to VM, Backup scanning, Cloud applications, additional plan types — to be completed*

- [x] **04-monitoring-dashboards** - Monitoring and Dashboards (p. 288-327, partial)
  - Monitoring overview: Overview and Activities dashboards
  - Alerts dashboard: customization, filtering, sorting, service desk tickets
  - Alert types - Backup alerts (12 types with resolution)
  - Alert types - Disaster recovery alerts (30+ types with resolution)
  - Alert types - Antimalware, URL Filtering, Licensing, EDR, Device Control alerts
  - Alert types - System, Public Clouds, Software deployment, Management, Search, Monitoring alerts
  - Widgets: Cyber Protection, Protection status, EDR (7 widgets), Discovered devices
  - *Remaining sections (p. 328-367): CyberFit Score, Disk health, GenAI, Data protection map, Vulnerability/Patch widgets, Activities tab, Cyber Protect Monitor, Reports — to be completed*

## Planned Chapters

- [ ] 04-monitoring-dashboards (remaining widgets)
- [x] 05-managing-workloads (p. 368-407, partial) — Console overview, admin levels, partner-level features, global exclusions, wildcards/variables; Workloads types/adding/removing; Device groups (built-in, custom, static, dynamic, cloud-to-cloud, search operators)
- [x] 06-backup-and-recovery (p. 484-503, partial) — Supported OS: Windows (Agent for Windows, Legacy, SQL/AD/Exchange, DLP), Linux (30+ distros, kernel 2.6.9-6.15), macOS (High Sierra-Tahoe 26); All agent types with supported versions; Virtualization platforms (VMware, Hyper-V, Scale Computing, Proxmox, Citrix, oVirt/KVM, Azure, EC2) with limitations; Application versions (SQL Server, Exchange, SharePoint, Oracle, SAP HANA, MySQL, MariaDB)
- [ ] 07-disaster-recovery
- [ ] 08-antivirus-antimalware
- [ ] 09-genai-protection
