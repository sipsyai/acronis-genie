# Mailbox backup

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Mailbox backup
Mailbox backup

Mailbox backup is supported for Microsoft Exchange Server 2010 Service Pack 1 (SP1) and later.

Mailbox backup is available if at least one Agent for Exchange is registered on the management server. The agent must be installed on a machine that belongs to the same Active Directory forest as Microsoft Exchange Server.

Before backing up mailboxes, you must connect Agent for Exchange to the machine running the Client Access server role (CAS) of Microsoft Exchange Server. In Exchange 2016 and later, the CAS role is not available as a separate installation option. It is automatically installed as part of the Mailbox server role. Thus, you can connect the agent to any server running the Mailbox role.

You can recover mailboxes and mailbox items also from database backups and application-aware backups. For more information, see Recovering Exchange mailboxes and mailbox items. With database backups and application-aware backups you cannot create protection plans for individual mailboxes.

To connect Agent for Exchange to CAS

Click Devices > Add.
Click Microsoft Exchange Server.

Click Exchange mailboxes.

If no Agent for Exchange is registered on the management server, the software suggests that you install the agent. After the installation, repeat this procedure from step 1.

[Optional] If multiple Agents for Exchange are registered on the management server, click Agent, and then change the agent that will perform the backup.

In Client Access server, specify the fully qualified domain name (FQDN) of the machine where the Client Access role of Microsoft Exchange Server is enabled.

In Exchange 2016 and later, the Client Access services are automatically installed as part of the Mailbox server role. Thus, you can specify any server running the Mailbox role. We refer to this server as CAS later in this section.

In Authentication type, select the authentication type that is used by the CAS. You can select Kerberos (default) or Basic.
[Only for basic authentication] Select which protocol will be used. You can select HTTPS (default) or HTTP.
[Only for basic authentication with the HTTPS protocol] If the CAS uses an SSL certificate that was obtained from a certification authority, and you want the software to check the certificate when connecting to the CAS, select the Check SSL certificate check box. Otherwise, skip this step.
Provide the credentials of an account that will be used to access the CAS. The requirements for this account are listed in "Required user rights".
Click Add.

As a result, the mailboxes appear under Devices > Microsoft Exchange > Mailboxes.

Selecting Exchange Server mailboxes

Required user rights

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.