---
title: "Password management"
source: "https://developer.acronis.com/doc/cyberapps/intro/types/password-management.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:58:44.628354"
---

# Password management

Password management
This type of CyberApp provides enterprise password management and security. The purpose is to allow the management of users and their passwords, as well as monitor the overall security score and password strength in Acronis Cyber Platform.


CyberApp scenarios

Typical
Typical password management CyberApps are built around a basic user management scenario and should include the following functionality:


Establish connection to the ISV cloud.
Connection parameters and credentials to allow data to be transferred to Acronis Cyber Platform using the CyberApp enablement form extension point.



Customer mapping.
Pairing ISV customers to Acronis tenants to report the list of protected users to the correct tenant.


Reporting the list of user accounts using password management functionality

Providing actions to support basic management options for reported users.
For example:



Invite a new user.
Update the existing user details.
Reset the master password.






Extended
To increase the value of the CyberApp for MSPs, it is recommended to enhance it with additional functionalities:

Provide an additional page for managing password complexity and authentication policies.

Report an alert related to password management.
|  For example:



A weak password is used for authentication.
The user account for the specific resource has been compromised due to data leakage.



Create CyberApp-specific widgets to display password management information.




Recommended extension points
To be able to extend Acronis Cyber Platform with password management capabilities, the following extension points should be used:

CyberApp enablement form
CyberApp enablement form provides credentials for accessing the ISV cloud and map ISV customers to Acronis customers.

Password management is performed at the customer-level. This means that the Partner needs to configure the CyberApp for each end customer individually.
Typically, a password management CyberApp contains the following settings:




Client ID and client secret
Required to authenticate in the ISV cloud and fetch the list of end customers.
These settings enable the CyberApp for the Partner.



Customers mapping
A list of customers fetched from the ISV cloud that allows the specification of an existing customer mapping or the creation of a new corresponding customer mapping in Acronis Cyber Platform.
Mapping an ISV customer to an Acronis customer results in enabling the CyberApp for the specific customer.




CyberApp configuration and mapping can be done only by the Acronis Partner. It cannot be done by end customers.


Main menu
Main menu configures password policies and manages protected users.

The main menu allows the CyberApp to add a new menu item, dedicated to password management, under the Management menu in Acronis Cyber Protection Console. This page should contain the list of the user accounts provided with Password management functionality. The list should also contain actions to support main password management scenarios: add new users, reset passwords, etc. Page content must be described in Vendor Portal. The user’s list and actions on this page are communicated from and to the ISV’s cloud via API Callback Gateway.
Additionally, the password management page can contain a tab to manage tenant-wide password policies that should be applied to all customers.
For example:


Password strength settings.
Multi-factor authentication settings.
A number of allowed unsuccessful login attempts.
Etc.



Alerts
To be able to notify about password-related security issues, the CyberApp should submit alerts to Acronis Cyber Platform. Such alerts must be submitted as a new alert type. In this case, the typical alert structure would be:

Issue type (account was compromised, the password does not match security settings, etc.).
User account.
Issue description.
Timestamp.

Alert types are declared in Vendor Portal. Alert instances are reported to the platform by the Connector.


Widgets and reports

Widgets and reports can display password management-related statistics.
If the CyberApp reports password management alerts to the platform, it is recommended to add a widget that would show the latest alert of this type to the Overview dashboard.