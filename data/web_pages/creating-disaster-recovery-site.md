# Creating a disaster recovery site in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Managing the disaster recovery site in Microsoft Azure > Creating a disaster recovery site in Microsoft Azure
Creating a disaster recovery site in Microsoft Azure

Prerequisites

You have a subscription to Microsoft Azure.

Your Microsoft account has one of the following Entra ID roles: Cloud Application Administrator, Application Administrator, or Global Administrator.

Your Microsoft account has the Owner role for the Azure subscription.

The DR and direct backup to Azure offering item is enabled for your tenant.

From All Devices
From Connectivity

To create a DR site in Microsoft Azure

In the Cyber Protect console, go to Devices > All devices.

Select the workloads that you want to protect.

In the Actions menu, click Protect.

Create a protection plan and configure the following settings:

In the Backup module, in the Where to back up field, select the storage location for the backups of your workloads.

Enable the Disaster recovery module, and then click the Location field.

If only DR and direct backup to Azure offering item is enabled for your tenant, the location will not be preselected, and you will see a link Configure.

If both DR to Acronis or hybrid cloud and DR and direct backup to Azure offering items are enabled for your tenant, Cyber Protect Cloud will be preselected as a location.

In the Disaster recovery site configuration wizard, on the Site location tab, select Microsoft Azure Cloud, and then click Next.

On the Azure subscription tab, do the following:

If your Microsoft Azure subscription was already added to the Cyber Protect console, click it, and then click Next.

If you want to add a new Microsoft Azure subscription, click Add subscription, add the subscription, click it, and then click Next.

On the Target region tab, in the Azure region field, select the Azure region for the DR site.

On the Recovery network tab, configure the recovery networks for production and test failover, and then click Next.

Option	Description
Default configuration	Use this option if you want the production and test networks in Azure to be created automatically, with one network for each environment.
Advanced configuration	Use this option if you want to select your existing Azure networks as the production and test networks and configure network mapping.

On the Summary tab, review the parameters of your DR site, and then click Configure.

The protection plan is successfully applied to the selected workloads. The DR site is created in Azure, located in the selected Azure region. On the Disaster Recovery > Connectivity screen, you can view the production and test networks, and the recovery servers that were created, in Standby mode.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.