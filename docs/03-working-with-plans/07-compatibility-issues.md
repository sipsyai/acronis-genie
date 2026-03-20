---
title: "Compatibility issues with plans"
section: "Working with plans"
subsection: "Protection plans and modules"
page_range: "238-241"
tags: ["compatibility", "conflicts", "troubleshooting", "plans", "hosting-control-panel"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#compatibility-issues-plans.html"
---

# Compatibility issues with plans

In some cases, applying a plan on a workload might cause compatibility issues. You might observe the following issues:

- **Conflicting plan** — there is a conflict between the plan that you are applying and an already applied plan. For example, some settings in the plan might conflict with the settings in the already applied plan, or the same workload might already have been protected as part of a device group.
- **Incompatible operating system** — the operating system of the workload is not supported.
- **Unsupported agent** — the version of the protection agent on the workload is outdated and does not support the configured functionality.
- **Insufficient quota** — there is not enough service quota in the tenant to assign to the selected workload.
- **Incompatible workload type** — the selected functionality is not available for this workload type.
- **Missing advanced pack** — the selected functionality is not available because a required advanced pack is not enabled for this customer.

## Compatibility issues by plan type

| Issue/Plan type | Protection plan | Scripting plan | Monitoring plan | Remote management plan | Software deployment plan |
|----------------|----------------|---------------|-----------------|----------------------|------------------------|
| Conflicting plan | +* | - | - | + | - |
| Incompatible OS | + | + | + | + | + |
| Unsupported agent | + | + | + | + | + |
| Insufficient quota | + | + | + | + | - |
| Incompatible workload type | + | + | + | + | - |
| Missing advanced pack | + | - | - | - | - |

*No conflicts are triggered if different backup settings are configured in multiple protection plans for the same workload.

If the plan is applied to up to 150 individually selected workloads, you will be prompted to resolve the existing conflicts before saving the plan. If you do not resolve the conflicts, the whole plan or some of its modules will be disabled on the incompatible workloads, and alerts will be shown.

If the plan is applied to more than 150 workloads or to device groups, first it will be saved, and then checked for compatibility.

## Resolving compatibility issues

### Conflicting plan

1. Click **Review issues**.
2. [To resolve the issue by removing workloads from the new plan]
   a. On the **Conflicting plan** tab, select the workloads that you want to remove.
   b. Click **Remove selected workloads from the plan**.
   c. Click **Remove**, and then click **Close**.
3. [To resolve the issue by disabling the plans that are already applied to the workload]
   a. Click **Disable applied plans**.
   b. Click **Disable**, and then click **Close**.
4. [To resolve the issue by disabling the conflicting modules in the plans already applied to the workload]
   a. Click **Disable conflicting modules in applied plans**.
   b. Click **Disable**, and then click **Close**.

### Incompatible OS / Unsupported agent / Insufficient quota / Incompatible workload type

1. Click **Review issues**.
2. On the corresponding tab, select the workloads that you want to remove.
3. Click **Remove workloads from plan**.
4. Click **Remove**, and then click **Close**.

### Missing advanced pack

1. Click **Review issues**.
2. [To resolve by removing workloads] On the **Missing advanced pack** tab, select the workloads to remove, click **Remove workloads from plan**, click **Remove**, and then click **Close**.
3. [To resolve by enabling the required advanced pack] [For partner administrators] Go to Management Portal, and then enable the required advanced pack for this customer.

---

# Individual protection plans for hosting control panel integrations

When you enable hosting control panel integrations on your web hosting servers that use DirectAdmin, cPanel, or Plesk, the Cyber Protection service automatically creates an individual protection plan under your user account for each workload. This protection plan is associated with the particular workload that initiated the protection plan creation, and cannot be revoked or assigned to other workloads.

To stop using an individual protection plan, you can delete it from the Cyber Protect console. You can identify individual protection plans by the lock sign next to their name.

If you want a protection plan to protect multiple web hosting servers that use hosting control panel integrations, you can create a regular protection plan in the Cyber Protect console and assign these workloads to it. However, any modifications to a protection plan that is shared by multiple web hosting control panels, can only be made in the Cyber Protect console, and not from within the hosting integrations.
