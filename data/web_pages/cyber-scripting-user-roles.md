# User roles and Cyber Scripting rights

Managing workloads in the Cyber Protect console > Cyber Scripting > User roles and Cyber Scripting rights
User roles and Cyber Scripting rights

The available actions with scripts and scripting plans depend on the script status and your user role.

Administrators can manage objects, such as plans or workloads, in their own tenants and in their child tenants, with the following limitations:

Customer tenants can restrict access for partner administrators.
Units can always be accessed by customer administrators and partner administrators who manage the parent customer tenant.

Administrators cannot see or access objects at a level above their own tenant.

Lower-level administrators have only read-only access to the scripting plans applied to their workloads by an upper-level administrator.

The following roles provide rights with regard to Cyber Scripting:

Company administrator

This role grants full administrator rights in all services. With regard to Cyber Scripting, it grants the same rights as the Cyber administrator role.

Cyber administrator

This role grants full permissions, including approval of scripts that can be used in the tenant, and the ability to run scripts with the Testing status.

Administrator

This role grants partial permissions, with the ability to run approved scripts as well as create and run scripting plans that use approved scripts.

Read-only administrator

This role grants limited permissions, with the ability to view scripts and protection plans that are used in the tenant.

User

This role grants partial permissions, with the ability to run approved scripts as well as create and run scripting plans that use approved scripts, but only on the user's own machine.

The following table summarizes all available actions, depending on the script status and the user role.

Role	Object	Script status
Draft	Testing	Approved


Cyber administrator

Company administrator

Scripting plan

Edit (Remove a draft script from a plan)

Delete

Revoke

Disable

Stop



Create

Edit

Apply

Enable

Run

Delete

Revoke

Disable

Stop



Create

Edit

Apply

Enable

Run

Delete

Revoke

Disable

Stop


Script

Create

Edit

Change status

Clone

Delete

Cancel running



Create

Edit

Change status

Run

Clone

Delete

Cancel running



Create

Edit

Change status

Run

Clone

Delete

Cancel running




Administrator

User (for their own workloads)

Scripting plan

View

Edit

Revoke

Disable

Stop



View

Cancel run



Create

Edit

Apply

Enable

Run

Delete

Revoke

Disable

Stop


Script

Create

Edit

Clone

Delete

Cancel running



View

Clone

Cancel running



Run

Clone

Cancel running


Read-only administrator	Scripting plan	View	View	View
Script	View	View	View
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.