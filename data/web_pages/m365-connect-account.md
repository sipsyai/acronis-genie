# Connecting to a Microsoft account

RMM > Managing and monitoring the Microsoft 365 environment > Configuring Microsoft 365 connections > Connecting to a Microsoft account
Connecting to a Microsoft account

As the Partner administrator, you can connect to your Microsoft CSP account or regular Microsoft account.

When you log in to your Microsoft CSP account, the system automatically retrieves all customer tenants associated with the CSP account.

When you log in to a regular Microsoft account, you can connect to your customers' Microsoft accounts one by one, providing you have the relevant credentials.

When onboarding tenants with a large number of users (for example, over 1000), the system might take some time to retrieve all the relevant details. This is because each user needs to be verified, and some Microsoft APIs can only be triggered once every two seconds. This issue is relevant to both CSP and regular Microsoft accounts.

To connect to a Microsoft account

Microsoft CSP account
Regular Microsoft account

In the Cyber Protect console, go to M365 management > Configuration.

Click Connect Microsoft account.

You are redirected to the Microsoft login page.

Sign in to the Microsoft account with your CSP credentials, and accept the permissions requested by Acronis. When you click Accept, you are redirected to the Cyber Protect console.

The permissions requested when signing in to a Microsoft account are for the Octiga Multi-Tenant Security enterprise application registered in Entra ID. This application is connected with the service providers' Microsoft 365 tenant, and enables them to manage their clients' security operations.


In the displayed Customer mapping tab, map the Microsoft 365 clients with the relevant customers in Cyber Protect Cloud. For more information, see Customer mapping.

The system automatically lists all the Microsoft 365 tenants associated with the Microsoft account in the Customer mapping tab, each with the initial status of Onboarding tenant.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.