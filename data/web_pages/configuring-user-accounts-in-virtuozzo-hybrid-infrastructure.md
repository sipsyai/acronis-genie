# Configuring user accounts in Virtuozzo Hybrid Infrastructure

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) > Configuring user accounts in Virtuozzo Hybrid Infrastructure
Configuring user accounts in Virtuozzo Hybrid Infrastructure

To configure the virtual appliance, you need a Virtuozzo Hybrid Infrastructure user account.

You can use one of the following accounts:

System administrator (in the Default domain or in another domain)

Ensure that you grant this account access to all projects in the selected domain. Thus, the virtual appliance will be able to back up and recover all virtual machines in all child projects of the selected domain.

Project administrator

With this account, the virtual appliance will be able to back up and recover only the virtual machines in the project in which the account is created. No information about other projects in the domain will be available to the virtual appliance.

If you want to protect multiple projects, you must deploy a separate virtual appliance for each project.

Each virtual appliance must use a separate project administrator account that is created in the corresponding project. The appliance can be deployed anywhere in the Virtuozzo Hybrid Infrastructure cluster, even outside the protected project.

You can use the project administrator account only with Virtuozzo Hybrid Infrastructure 6.2 and later.

For more information about domains and projects, see Multitenancy in the Virtuozzo Hybrid Infrastructure documentation.

Using a system administrator account

Using a project administrator account

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.