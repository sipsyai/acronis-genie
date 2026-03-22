# Protecting web hosting servers

Managing the backup and recovery of workloads and files > Protecting web hosting servers
Protecting web hosting servers

You can protect Linux-based web hosting servers that run Plesk, cPanel, DirectAdmin, VirtualMin , or ISPManager control panels. Servers that run web hosting control panels from other vendors are protected as regular workloads.

Quotas

Servers that run Plesk, cPanel, DirectAdmin, VirtualMin , or ISPManager control panels are considered web hosting servers. Each backed-up web hosting server consumes the Web hosting servers quota. If this quota is disabled or the overage for this quota is exceeded, a quota will be assigned as follows or the backups will fail:

If the server is physical, the Servers quota will be used. If this quota is disabled or the overage for this quota is exceeded, the backup will fail.
If the server is virtual, the Virtual machines quota will be used. If this quota is disabled or the overage for this quota is exceeded, the backup will fail.
Integrations for DirectAdmin, cPanel, and Plesk

Web hosting administrators that use DirectAdmin, Plesk or cPanel, can integrate these control panels with the Cyber Protection service to gain several powerful capabilities, including:

Backing up entire web hosting server to the cloud storage with disk-level backup
Recovering the entire server, including all websites and accounts
Performing granular recovery and downloading of accounts, websites, individual files, mailboxes, or databases
Enabling resellers and customers to perform self-service recovery of their own data

To perform the integration, you need to use a Cyber Protection service extension. For detailed information, please refer to the corresponding integration guides:

DirectAdmin Integration Guide
WHM and cPanel Integration Guide
Plesk Integration Guide

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.