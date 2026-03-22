# Plans at different administration levels

Working with plans > Understanding plans > Plans at different administration levels
Plans at different administration levels

Depending on their hierarchical level, administrators can create and manage plans at the following levels:

Partner level (All customers)
Customer level
Unit level

For more information, see Administration levels in the Cyber Protect console.

Higher-level administrators can create and apply plans in their own tenant and in the child tenants that they manage. Lower-level administrators have read-only access to the plans that are applied by higher-level administrators, and cannot delete, edit, or revoke these plans.

When working on a lower administration level, a higher-level administrator has the rights of the lower level administrator. For example, when a partner administrator works at the customer level, the partner administrator has the rights of a customer administrator.

The following table summarizes the plans at different administration levels, according to the administrator hierarchy.

Administrator hierarchy	Administration level	Plans	Access


Partner-level account with one of the following roles in the Protection service:

Company administrator
Cyber administrator
Administrator
Partner level

Partner plans (owner*)



Full access




Customer plans, including plans in units



Full access




Unit plans



Full access




Customer level

(for customers that are managed by the service provider)



Partner plans that are applied to workloads of this customer



Read-only




Customer plans, including plans in units (owner*)



Full access




Unit plans



Full access




Unit level

(for customers that are managed by the service provider)



Partner plans that are applied to workloads of this unit



Read-only




Customer plans that are applied to workloads of this unit



Read-only




Unit plans (owner*)



Full access




Customer-level account with one of the following roles in the Protection service:

Company administrator
Cyber administrator
Administrator
Customer level

Partner plans that are applied to workloads of this customer or unit



Read-only




Customer plans, including plans in units (owner*)



Full access




Unit plans



Full access


Unit level

Partner plans that are applied to workloads of this unit



Read-only




Customer plans that are applied to workloads of this unit



Read-only




Unit plans (owner*)



Full access




Unit-level account with one of the following roles in the Protection service:

Unit administrator
Cyber administrator
Administrator
Unit level

Partner plans that are applied to workloads of this unit



Read-only




Customer plans that are applied to workloads of this unit



Read-only




Unit plans (owner*)



Full access

* The owner of a plan is the tenant in which the plan was created. For example, if a partner administrator creates a plan at the customer level, the customer tenant is the owner of that plan. If a partner administrator creates a plan at the partner level (All customers), the partner tenant is the owner of the plan.

Not all types of plans are available on all administration levels. For more information, see Understanding plans.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.