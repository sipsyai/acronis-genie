---
title: "Default plans, Favorite plans, and Preselected plans"
section: "Working with plans"
subsection: "Understanding plans"
page_range: "220-228"
tags: ["default-plans", "favorite-plans", "preselected-plans", "plan-selection", "administration-levels"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#setting-favorite-plans.html"
---

# Default plans

The default plan is a plan that is preselected and is displayed first in the plans lists and in the plan selection fields. You can have only one default plan per tenant per supported plan type at a time.

The plans list and the default plan that you will see depend on the level at which you are using the Protection console.

Default plans are supported for the following plan types: protection plans, monitoring plans, and remote management plans.

## Setting plans as default

> **Note:** The feature is not available for users who are assigned the **Read-only administrator** role for the Protection service.

### Protection plans

1. On the **Protection plans** screen, select the plan that you want to set as default, and then click **Details**.
2. Click the ellipsis icon, and then click **Set as default**.
3. In the confirmation window, click **Set**.

### Remote management plans

**Prerequisites:** 2FA is enabled for your user account.

1. On the **Remote management plans** screen, locate the plan that you want to set as default.
2. In the same row, click the **More actions** icon.
3. Click **Set as default**.
4. In the confirmation window, click **Set**.

### Monitoring plans

**Prerequisites:** 2FA is enabled for your user account.

1. On the **Monitoring plans** screen, locate the plan that you want to set as default.
2. In the same row, click the **More actions** icon.
3. Click **Set as default**.
4. In the confirmation window, click **Set**.

## Clearing default plans

You can clear the default protection plan. After you do that, the plan will no longer be preselected in the plan selection fields.

The procedure is the same for all plan types — select the default plan, click the ellipsis icon, and then click **Clear default**.

---

# Favorite plans

Favorite plans appear at the top of the plans list, after the default plans. You can add a plan to favorites if you want to ensure that it is visible and easy to find, even when your organization has many plans.

The plans list and the favorite plans that you will see depend on the level at which you are using the Protection console.

Favorite plans are supported for the following plan types: protection plans, monitoring plans, and remote management plans.

You can set up to 10 favorite plans per supported plan type (protection plan, monitoring plan, or remote management plan) per tenant.

### Setting plans as favorite

For all plan types: select the plan, click the ellipsis icon (...), and then click **Add to favorites**. A star icon appears next to the plan name.

### Removing plans from favorites

For all plan types: select the plan, click the ellipsis icon (...), and then click **Remove from favorites**. The star icon disappears.

### Setting the order of favorite plans

You can set the order in which plans that are set as favorite will be shown in the plan selection fields.

1. In the Cyber Protect console plans screen, go to **Management** > **[Plan type]**.
2. Click **Manage favorites**.
3. Drag and drop the plans to set the order.
4. Click **Save**.

---

# Preselected plans

If two-factor authentication (2FA) is enabled for your account, a protection plan, a monitoring plan, and a remote management plan are preselected when you register a workload in the Cyber Protect console.

You can change the selection or choose not to apply a plan to the workload.

Which plans are preselected depends on the following:

- User role of the user who registers the workload.
- Account under which the workload will be registered.
- Plan availability.

The possible options are listed hierarchically. If an option is unavailable, the next one in the list is applied. If all possible options are unavailable, no plan will be preselected.

### Preselection hierarchy for Partner-level accounts

**Account in a customer tenant:**
1. Default plan at the customer level
2. Default plan at the partner level
3. First favorite plan at the customer level
4. First favorite plan at the partner level
5. Randomly selected plan at the customer level
6. Randomly selected plan at the partner level
7. Built-in plan* (applied as a customer-level plan)

**Account in a unit:**
1. Default plan on the unit level
2. Default plan at the customer level
3. Default plan at the partner level
4. First favorite plan on the unit level
5. First favorite plan at the customer level
6. First favorite plan at the partner level
7. Randomly selected plan on the unit level
8. Randomly selected plan at the customer level
9. Randomly selected plan at the partner level
10. Built-in plan* (applied as a customer-level plan)

*Built-in plans are only available for protection plans.
