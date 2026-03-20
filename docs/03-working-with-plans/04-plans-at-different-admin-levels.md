---
title: "Plans at different administration levels"
section: "Working with plans"
subsection: "Understanding plans"
page_range: "228-230"
tags: ["administration-levels", "partner", "customer", "unit", "access", "permissions", "plan-status"]
acronis_version: "26.02"
---

# Plans at different administration levels

Depending on their hierarchical level, administrators can create and manage plans at the following levels:

- Partner level (**All customers**)
- Customer level
- Unit level

Higher-level administrators can create and apply plans in their own tenant and in the child tenants that they manage. Lower-level administrators have read-only access to the plans that are applied by higher-level administrators, and cannot delete, edit, or revoke these plans.

When working on a lower administration level, a higher-level administrator has the rights of the lower level administrator. For example, when a partner administrator works at the customer level, the partner administrator has the rights of a customer administrator.

## Access levels by administrator hierarchy

### Partner-level account (Company administrator, Cyber administrator, Administrator)

| Administration level | Plans | Access |
|---------------------|-------|--------|
| Partner level | Partner plans (owner*) | Full access |
| | Customer plans, including plans in units | Full access |
| | Unit plans | Full access |
| Customer level (for customers managed by the service provider) | Partner plans applied to workloads of this customer | Read-only |
| | Customer plans, including plans in units (owner*) | Full access |
| | Unit plans | Full access |
| Unit level (for customers managed by the service provider) | Partner plans applied to workloads of this unit | Read-only |
| | Customer plans applied to workloads of this unit | Read-only |
| | Unit plans (owner*) | Full access |

### Customer-level account (Company administrator, Cyber administrator, Administrator)

| Administration level | Plans | Access |
|---------------------|-------|--------|
| Customer level | Partner plans applied to workloads of this customer or unit | Read-only |
| | Customer plans, including plans in units (owner*) | Full access |
| | Unit plans | Full access |
| Unit level | Partner plans applied to workloads of this unit | Read-only |
| | Customer plans applied to workloads of this unit | Read-only |
| | Unit plans (owner*) | Full access |

### Unit-level account (Unit administrator, Cyber administrator, Administrator)

| Administration level | Plans | Access |
|---------------------|-------|--------|
| Unit level | Partner plans applied to workloads of this unit | Read-only |
| | Customer plans applied to workloads of this unit | Read-only |
| | Unit plans (owner*) | Full access |

*The owner of a plan is the tenant in which the plan was created. For example, if a partner administrator creates a plan at the customer level, the customer tenant is the owner of that plan. If a partner administrator creates a plan at the partner level (**All customers**), the partner tenant is the owner of the plan.

---

# Plan status

For some plans, such as protection plans and VM replication plans, a clickable color-coded status bar is available. It indicates the status of the plan on all workloads on which that plan is applied, as follows:

- **OK** (green)
- **Warning** (orange)
- **Error** (red)
- **The plan is running** (blue)
- **The plan is disabled** (gray)

You can click a section in the status bar to see the number of workloads that have the corresponding status.

> **Note:** The plan status might not correspond to the workload status. For example, a protection plan might be successfully applied to a workload, and its status will appear as **OK** (green). At the same time, the workload could be offline, so its status on the **Devices** tab will be red.
