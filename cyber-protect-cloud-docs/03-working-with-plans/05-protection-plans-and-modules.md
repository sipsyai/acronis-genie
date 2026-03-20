---
title: "Protection plans and modules"
section: "Working with plans"
subsection: null
page_range: "231-232"
tags: ["protection-plans", "modules", "backup", "antivirus", "EDR", "URL-filtering", "vulnerability", "patch-management", "DLP", "GenAI"]
acronis_version: "26.02"
---

# Protection plans and modules

To protect your data, you must create protection plans, and then apply them to your workloads.

A protection plan consists of different protection modules. Enable the modules that you need and configure their settings to create protection plans that meet your specific needs.

> **Note:** Module availability depends on the offering items that are enabled for your account and the administration level in the Cyber Protect console.

## Available modules

The following modules are available:

- **Backup** — Backs up your data sources to a local or cloud storage.
- **Disaster Recovery** — Launches exact copies of your machines in the cloud site and switches from corrupted original machines to the recovery servers in the cloud. See "Implementing disaster recovery" (p. 930).
- **Antivirus and Antimalware protection** — Checks your workloads by using a built-in antimalware solution.
- **Endpoint Detection and Response (EDR)** — Detects suspicious activity on the workload, including attacks that have gone unnoticed, and generates incidents to help you understand how an attack happened and how to prevent it from happening again.
- **URL filtering** — Protects your machines from threats originating from the Internet, by blocking access to malicious URLs and downloadable content.
- **GenAI Protection** — Enables you to control, monitor, and enforce secure usage of supported generative AI applications across protected workloads.
- **Windows Defender Antivirus** — Manages the settings of Windows Defender Antivirus to protect your environment.
- **Microsoft Security Essentials** — Manages the settings of Microsoft Security Essentials to protect your environment.
- **Vulnerability assessment** — Checks Windows, Linux, macOS, Microsoft third-party products, and macOS third-party products installed on your machines and notifies you about vulnerabilities.
- **Patch management** — Installs patches and updates for Windows, Linux, macOS, Microsoft third-party products, and macOS third-party products on your machines, to resolve the detected vulnerabilities.
- **Data protection map** — Discovers data in order to monitor the protection status of important files.
- **Device control** — Specifies devices that users are allowed or prohibited to use on your machines.
- **Data Loss Prevention** — Prevents leakage of sensitive data via peripheral devices (such as printers or removable storage), or through internal and external network transfers, based on a data flow policy.

## Creating a protection plan

You can create a protection plan in the following ways:

### From the Devices tab

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the workloads that you want to protect, and then click **Protect**.
3. [If there are already applied plans] Click **Add plan**.
4. Click **Create plan** > **Protection**.
5. [Optional] To rename the protection plan, click the pencil icon, enter a new name, and then click **OK**.
6. [Optional] To enable or disable a module in the plan, toggle the switch next to the module name.
7. [Optional] To configure a module, expand it, and then change the settings.
8. Click **Create**.

### From Management > Protection plans

1. In the Cyber Protect console, go to **Management** > **Protection plans**.
2. Click **Create plan**.
3. Select a template that is based on a built-in plan, or select **Create your own plan** to configure a plan from scratch, and then click **Next**.
4. [Optional] To rename the plan, click the pencil icon, enter a new name, and then click **OK**.
5. [Optional] To enable or disable a module in the plan, toggle the switch next to the module name.
6. [Optional] To configure a module, expand it, and then change the settings according to your needs.
7. [Optional] To add workloads to the plan, click **Add devices**, and then select the workloads.
8. Click **Create**.

To run a module on demand (such as **Backup**, **Antivirus and Antimalware protection**, **Vulnerability assessment**, **Patch management**, or **Data protection map**), click **Run now**.
