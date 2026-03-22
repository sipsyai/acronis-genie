# Integrating Cyber Protect Cloud with VMware Cloud Director

Integrating Cyber Protect Cloud with VMware Cloud Director
Integrating Cyber Protect Cloud with VMware Cloud Director

A service provider can integrate VMware Cloud Director (formerly VMware vCloud Director) with Cyber Protect Cloud and provide its customers with out-of-the-box backup solution for their virtual machines.

The integration includes the following steps:

Configuring the RabbitMQ message broker for the VMware Cloud Director environment.

RabbitMQ provides single sign-on (SSO) functionality, so that you can use your VMware Cloud Director credentials to log in to the Cyber Protect console.

In Cyber Protect Cloud version 23.05 (released in May 2023) and older, RabbitMQ is also used for synchronizing the changes in the VMware Cloud Director environment to Cyber Protect Cloud.

Deploying a management agent.

During the deployment of the management agent, a plug-in for VMware Cloud Director is also installed. The plug-in adds Cyber Protection to the VMware Cloud Director user interface.

The management agent maps VMware Cloud Director Organizations to customer tenants in Cyber Protect Cloud, and Organization Administrators to customer tenant administrators. For more information about Organizations, see Creating an Organization in VMware Cloud Director in the VMware Knowledge Base.

The customer tenants are created within the partner tenant for which the VMware Cloud Director integration is configured. These new customer tenants are in the Locked mode and cannot be managed by partner administrators within Cyber Protect Cloud.

Only Organization Administrators with unique email addresses in VMware Cloud Director are mapped to Cyber Protect Cloud.

Deploying one or more backup agents.

The backup agent provides backup and recovery functionality for the virtual machines in the VMware Cloud Director environment.

To disable the integration between VMware Cloud Director and Cyber Protect Cloud, contact the technical support.

Limitations

Integration with VMware Cloud Director is possible only for partner tenants in the Managed by service provider management mode, whose parent tenant (if any) also uses the Managed by service provider management mode. For more information about the types of tenants and their management mode, see Creating a tenant.

All existing direct partners can configure integration with VMware Cloud Director. Partner administrators can enable this option also for sub-tenants by selecting the Partner-owned VMware Cloud Director infrastructure check box when creating a child partner tenant.

If 2FA is enabled for your tenant, you must use a partner administrator account that is marked as a service account. Otherwise, the agent will not be able to authenticate to Cyber Protect Cloud.

We recommend that you use a dedicated account for the agent. For more information about how to create a service account, see Converting a user to a service account.

An administrator who has the Organization Administrator role in multiple VMware Cloud Director Organizations can manage the backup and recovery only for one customer tenant in Cyber Protection.

Cyber Protect console opens in a new tab.

Software requirements

Configuring RabbitMQ message broker

Installing and publishing the plug-in for VMware Cloud Director

Installing a management agent

Installing backup agents

Enabling the FIPS compliance mode for VMware Cloud Director

Updating the agents

Creating a backup administrator

System report, log files, and configuration files

Accessing the Cyber Protect console

Performing backup and recovery

Removing the integration with VMware Cloud Director

Back to Top



Last build date: Tuesday, March 10, 2026

Partner Administrator Help for Management Portal26.02.