# Support Digest Q2 2022

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q2-2022

## Original Post
**Author:** Unknown

Support Digest Q2 2022

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrey Vislyaev
                            

                            
                    
                        Acronis Trainer
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello colleagues,

Please welcome a new version of the Acronis Digest for Service Providers. The past quarter brought several exciting updates, including:
A new release of Acronis Cyber Infrastructure 5.1
New version of Cyber Protection agent is available for download 15.0.29805
Acronis Cyber Protect Cloud platform has been updated to the new version 22.06
Table of contents:
Do you know?
Most frequently asked questions and reported problems
New KB articles
Release notes and documentation
Do you know?
Now a service provider has an ability to consult with Acronis Account Manager about Acronis products and other sales-related questions. We implemented a chat button available in the management portal. Note, this button is not used to contact the support department.
Most frequently asked questions and reported problems.
1. Microsoft Office 365 items are missing.
Let’s review the following situation: a partner created a customer account, enabled SharePoint Online, Teams offering items, and set some quotas sufficient for backup. He then added Microsoft 365 organization in the Cyber Protection console. After checking the Microsoft 365 tab, he figured out that some items are missing. For example, SharePoint and Teams are shown, while user mailboxes are not.
The reason of this problem is not all required sub-offerings are enabled.
In order to resolve the problem, corresponding sub-items should be enabled either Mailboxes or OneDrive or both of them. This can be done from the management portal:
Login to the management portal as a partner administrator
Navigate to the problem customer tenant in the partner’s hierarchy 
Click the Edit button and enable corresponding offering items


We also have internal feature request to improve the situation with the Microsoft 365 licensing and make it clear for the partners. The internal improvement ID of the request is UXI-29. The exact implementation date is currently a subject of discussion, but you can track implementation status through the platform’s release notes.
In order to get more information on how to configure offerings, quotas and services, check the Partner Guide.
2. Company information prompt can be skipped but occurs on every login to Management portal.
C22.04 release delivered a new feature - Company information window for each customer tenant:

However, it started triggering difficulties for partners right away. Namely, it is not clear why the Company information prompt occurs by each login of partner and customer admins and how to stop that.
According to R&D, this is expected: it's obligatory to fill in the form and save changes. After that, the prompt won't appear anymore. From the form itself, it's not obvious that this is obligatory - user can just close it without any warning.
Also, there are two issues in regards to this form:
Company information page is shown to a customer/unit admin, however it should not. This is a known issue PLTFRM-38889, which was fixed in C22.05.
It's unclear that an admin has to specify all 3 contacts. So, even if admin specified one of those contacts, the system continues to ask him to specify all 3 contacts again during the next login(s). We plan to improve the situation within the feature request: PLTFRM-40607. It will be implemented in one of the nearest platform updates.
3. Security product conflict.
In case if customer’s machine contains two or more antiviruses it may lead to unexpected behavior and different problems. Here are a few examples:
A machine has both Windows Defender and Acronis real-time protection enabled. As a result, and alert is generated within Acronis Cyber Protect: Windows Defender is blocked by a third-party antivirus software. Windows Defender is blocked because Acronis Cyber Protect is installed on machine.
A similar alert is raised in case if other antiviruses are enabled along with Acronis real-time protection (e.g. Kaspersky antivirus): Windows defender is blocked by a third-party antivirus software. Windows Defender is blocked because any third-party antivirus and Acronis Cyber Protect is installed on the machine

Actually, it is not recommended to run two antiviruses on one machine as they will conflict with each other and may cause multiple issues.  One of them should be disabled/uninstalled:Solution 1: If you want to use Acronis real-time protection then you need to uninstall third-party antivirus from the system and disable Windows Defender antivirus from the device protection plan (it should be disabled automatically).Solution 2: If you want to use third-party antivirus (e.g. Kaspersky) then please disable Acronis real-time protection, URL filtering and Windows Defender antivirus in the protection plan. Note, it is not necessary to completely disable antivirus and antimalware protection module in machine’s protection plan: disabling Acronis real-time protection and URL-filtering is enough.
Keep in mind that Acronis Ransomware protection does not generate such conflicts and can be used along with other 3rd partly antivirus/antimalware solutions.
KB describing the issue. Check the following Support Digest link to find out information on how to completely disable Active Protection & Antivirus protection features.
4. Unclear Advanced Email Security usage shown in Management Portal.
Partners often complain on incorrect usage of Advanced Email Security pack. This usage is reported from Perception point, which has its specific logic. However, this logic is not obvious for service providers because it is totally different from other Acronis services. Here is how the problem occurs:
Create a customer tenant.
Enable Advanced Email Security pack.
Open Cyber protection console and go to Perception point.
Configure the Perception point service, add several mailboxes.
Wait for the usage to be synchronized (4-6 hours) and check usage values in Management portal. The value is X.
Go to the Perception point console and remove several mailboxes.
Wait for the usage to be synchronized (4-6 hours) and check usage values in Management portal again.
As a result, the usage doesn't reflect the fact that some mailboxes were deleted and aren't protected anymore. It still shows the same usage, value X. At the moment this is the current design of the product. However, we plan to improve the situation within the scope of UXI-30 feature request. 
Check more details on usage monitoring.
5. The procedure of moving tenants is not clear and causes how-to questions.
The management portal enables you to move a tenant from one parent tenant to another parent tenant. This may be useful if you want to transfer a customer within the partner hierarchy, or if you created a folder tenant to organize your clients and want to move some of them to the newly created folder tenant.
There are a few restrictions though:
A partner/folder tenant can be moved only to a partner/folder tenant.
A customer tenant can be moved only to a partner/folder tenant.
A unit tenant cannot be moved.
A tenant can be moved only if the target parent tenant has the same or a larger set of services and offering items as the original parent tenant.
Tenants can be moved only inside one partner account hierarchy. Moving customers between partner account hierarchies is not supported.
When moving a customer tenant, all storages assigned to the customer tenant in the original parent tenant must exist in the target parent tenant. This is required because the customer service-related data cannot be moved from one storage to another storage.
Here is how you can move a tenant:
Log in to the management portal.
On the Clients tab, select the target tenant to which you want to move a tenant.
On the tenant properties panel, click the vertical ellipsis icon, and then click Show ID.

Copy the text string shown in the Internal ID field, and then click Cancel.

On the Clients tab, select the tenant which you want to move.
On the tenant properties panel, click the vertical ellipsis icon, and then click Move.
Paste the internal identifier of the target tenant, and then click Move.


Also, we are working on UI improvements which suppose to ease the tenant moving processes: UXI-48.
Here is the user guide link, describing the “move” process.
New KB articles:
Acronis Cyber Protect Cloud:
KB 70732: Acronis Cyber Protect Cloud: Agent auto-update fails with "Internal error of the installation or update service. Error: CopyFilesFailed"
KB 70711: Acronis Cyber Protect Cloud: Installation fails with "Fatal error during installation. Failed to wait for filter driver 'ngscan' to unload" or "The activity failed because the cyber protection agent process terminated unexpectedly"
KB 70707: Acronis Cyber Protect Cloud: Agent auto-update fails with "The Windows Installer service cannot be accessed. This can occur when the Windows Installer is not installed correctly"
KB 70702: Acronis Cyber Protect Cloud: Agent auto-update fails with "Failed to download installation file from the server"
KB 70698: Acronis Cyber Protect Cloud: Agent auto-update fails with "Internal error of the installation or update support service. Error: UnexpectedInstallerStop"
KB 70692: Acronis Cyber Protect Cloud: Backup fails with "Failed to verify the TLS/SSL certificate while connecting to the cloud"
KB 70686: Acronis Cyber Protect: Backups to Cloud fail with "The cloud storage quota is exceeded. Further backups will fail" even after storage quota was increased
KB 70681: Acronis Cyber Protect Cloud: Trial tenant doesn’t switch to Production mode after a month
KB 70619: Acronis Cyber Protect Cloud: Cloud backups fail with “[Archive Server]: storage request timeout” or “Cloud storage is temporarily unavailable” on US5 DC
KB 70615: Acronis Cyber Protect Cloud: Agent update installation fails with "SSL peer certificate or SSH remote key was not OK"
Acronis Cyber Infrastructure:
KB 70402: Acronis products: Spring4Shell vulnerability
KB 70611: Acronis Cyber Infrastructure: Failed update to version 5.1: "error while scan configs: 'abgw-address' is missing" error
KB 70636: Acronis Cyber Infrastructure: Troubleshooting Update Alerts
KB 70673: Acronis Cyber Infrastructure: Alert "Cluster has reached X % of licensed storage capacity" appears unexpectedly
Acronis Cyber Files Cloud:
KB 70404: Acronis Cyber Files Cloud: The Unified agent cannot sync down a RO folder from the Cloud
KB 70409: Acronis Cyber Files Cloud: Files client gets logged out after machine reboot
KB 70517: Acronis Cyber Files Cloud: Cyber Files Desktop agent for Mac doesn't start after update to Mac OS 12.3
Acronis Cyber Disaster Recovery Cloud:
KB 70437: Acronis Cyber Disaster Recovery Cloud: Activity "Creating Recovery Server" fails on applying Protection Plan with error 'Your "Internet access" quota is not enabled'
All other new KBs can be found here:
https://kb.acronis.com/new?taxonomy_vocabulary_6_tid%5B%5D=11343&sort_by=created&sort_order=DESC
All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining
Release notes and documentation:
Acronis Cyber Infrastructure 5.1 release https://dl.acronis.com/u/vstorage/relnotes.html 
Latest Acronis Cyber Protect agent release notes: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProtectionAgent_relnotes.htm
Release notes for Acronis Cyber Cloud 22.06 platform update https://dl.managed-protection.com/u/baas/rn/22.06/en-US/AcronisCyberCloud_relnotes.htm 

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/27/2022 - 18:25

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
