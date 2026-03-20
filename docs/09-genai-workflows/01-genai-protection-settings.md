---
title: "GenAI Protection Settings"
section: "Configuring your GenAI Protection"
subsection: "GenAI Protection settings"
page_range: "1112-1114"
tags: [genai, generative-ai, usage-monitoring, scope-of-protection, data-loss-prevention, prompt-injection, ai-security, shadow-ai, browser-protection]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#generative-ai-protection-settings.html"
---

# Configuring Your GenAI Protection

GenAI Protection enables you to monitor and enforce secure usage of supported generative AI (GenAI) applications across protected endpoints from a single console. It logs events to a dedicated Events log, and provides summary and trend information through built-in reports and widgets.

GenAI Protection helps reduce the risk of sensitive and regulated data from being transmitted through GenAI applications.

**Important:** The availability of this feature depends on the license that you have.

- In solution-based licensing, the feature is available with the Workstations offering item under the Ultimate Protection license.
- In service-based licensing, the feature is available with the Endpoints offering item under the GenAI Protection service.

**Note:** GenAI Protection supports Windows 11 and Windows 10 (version 1809 or newer) 64-bit editions only.

## Enabling GenAI Protection

1. In the Cyber Protect console, go to **Management > Protection plans**.
2. Select the relevant protection plan from the displayed list and, in the right sidebar, click **Edit**.
3. Alternatively, you can create a new protection plan.
4. In the protection plan sidebar, enable the **GenAI Protection** module by clicking the switch next to the module name.

**Note:** GenAI Protection cannot be enabled for a plan that already has the Data Loss Prevention module enabled.

## GenAI Protection Settings

GenAI Protection offers settings to configure how a protection plan monitors and protects the use of generative AI applications across workloads.

### Usage Monitoring

Usage monitoring tracks the use of generative AI (GenAI) applications in your managed organizations. It provides visibility into GenAI adoption and usage patterns to help you identify shadow AI usage and define appropriate policies.

Default setting: **Disabled**.

To enable Usage monitoring, go to the **GenAI Protection** module of a protection plan and turn on the **Usage monitoring** switch.

### Scope of Protection

Specify where GenAI Protection monitors GenAI-related activity:

- **Browser only** -- Monitors activity and analyzes user prompts in web browsers when users interact with web-based generative AI applications.
- **Full protection** -- Monitors GenAI-related activity across the endpoint and analyzes user prompts and file uploads from both web-based and desktop generative AI applications.

Default setting: **Browser only**.

### Data Loss Prevention

Data loss prevention detects and prevents sensitive or confidential data from being shared with generative AI (GenAI) applications. GenAI Protection evaluates user prompts and supported file types (for example, PDF and Word documents) against sensitive data definitions.

Data loss prevention currently supports the following:

- Content coverage: Analyzes text-based content (text extracted from images is not included yet).
- Browser compatibility: Works with Google Chrome version 130 or later.

Default setting: **Enabled**.

#### Configuring Action on Detection for Data Loss Prevention

1. In the **GenAI Protection** module of a protection plan, click **Data loss prevention**.
2. In the dialog, specify the **Action on detection**:
   - **Detect only** -- Detects sensitive data that is sent to AI applications, and records details in the events log.
   - **Block** -- Prevents sending sensitive data to AI applications, records details in the events log, and notifies the user.
3. Click **Done**.

### Prompt Injection Protection

Prompt injection protection helps secure interactions with generative AI (GenAI) applications by detecting malicious or suspicious prompts. Prompt injection is a type of attack where a user or attacker attempts to manipulate the behavior of a GenAI application (for example, by bypassing safeguards or forcing unintended actions).

Default setting: **Enabled**.

#### Configuring Action on Detection for Prompt Injection Protection

1. In the **GenAI Protection** module of a protection plan, click **Prompt injection protection**.
2. Specify the **Action on detection**:
   - **Detect only** -- Detects potential prompt injection attacks, and records details in the events log.
   - **Block** -- Blocks potential prompt injection attacks, records details in the events log, and notifies the user.
3. Click **Done**.

## GenAI Protection Events

GenAI Protection generates events in the events log. The events log provides a chronological view of detection and enforcement actions performed by GenAI Protection and helps administrators investigate sensitive data transmission attempts and potentially harmful prompts.

The events log includes security events generated by GenAI Protection settings, such as:

- **Data loss prevention** events, when sensitive data is detected in prompts sent to generative AI applications.
- **Prompt injection protection** events, when potentially harmful prompts are detected or blocked.

The events log is available at both partner and customer level.

### To View the Events Log

1. Log in to the Cyber Protect console as an administrator.
2. Navigate to **Protection > GenAI Protection**.
3. Select **Events log**.

Use the events log to:

- Review security events related to generative AI usage.
- Understand when and why interactions with generative AI applications were blocked.
- Support internal investigations related to GenAI activity.
