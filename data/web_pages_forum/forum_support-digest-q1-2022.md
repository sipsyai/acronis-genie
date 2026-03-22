# ❗️?  Support Digest Q1 2022

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q1-2022

## Original Post
**Author:** Unknown

❗️?  Support Digest Q1 2022

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrey Vislyaev
                            

                            
                    
                        Acronis Trainer
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello colleagues,
Please allow me to introduce a new version of the Acronis Digest for Service providers. The past several months brought multiple exciting updates, including:
Acronis Cyber Protect Cloud platform has been updated to the new version (22.01 – 22.04)
New version of Cyber Protection agent is available for download – 15.0.29439
A major release of Acronis Cyber Infrastructure 5.0
Table of contents:
Do you know?
Most frequently asked questions and reported problems
New KB articles
Release notes and documentation
Do you know?
The Unified Desktop Agent has been added in Acronis Cyber Cloud, which integrates both Acronis Cyber Files Cloud and Acronis Cyber Protect Agent. With the unification in the single Cyber Protect Agent, it takes less time for technicians to deploy and maintain the agents. Customers can benefit from a better user experience provided by a modern look, ease-of-use and lower system resource usage. Partners can more easily increase usage and agent delivery with higher productivity.
Most frequently asked questions and reported problems.
1. How to disable Active Protection & Antimalware protection features. The corresponding agent services cannot be stopped or disabled manually.
First, let’s discuss what the protection services do on the system:
Acronis Active Protection service: It is used for self-protection of Acronis agent components (executables, processes, configuration files and backups located in local folders). It can detect cryptocurrency mining software and block it. Also, it can identify malicious software using behavioral heuristics.
Acronis Cyber Protection service: Used for malware detection in the real-time protection and on-demand modes. Also, it can detect malicious behavior in processes (for Windows) and blocking access to malicious URLs (for Windows).
By design, these protection services cannot be stopped manually, otherwise any malware software could potentially stop them as well. The best way to disable Activate Protection & Antimalware protection is through the protection plan:
Open the Cyber Protection console
Open the All devices tab and select target device
Navigate to the Protection tab and choose the plan, where you want to disable the Antimalware & Antivirus protection
Edit the plan and deselect the Antimalware & Antivirus protection option

2. How to remove backup from Cloud location if there are no online machines in the account
There could be a problem with an archive deletion in case no machines are available (online) in the account or if all machines are deleted. You may get the following messages while trying to delete a backup:
The machine with ID '...' is offline or is not available"  
This behavior is by design, it is not possible to delete an archive from the Cyber Protection console if there are no available(online) agents present.
As a solution, you can bring an agent online or temporary install an agent on any available machine and register it in the account. Once the agent is online, you can choose it in the Machine to browse from field:
And proceed with archive removal, choose the archive and click the Delete button:
If there are no machines, where an agent can be temporary registered, you can also use Web Recover console in order to delete archives: https://kb.acronis.com/content/61443

3. The Cyber Protection console does not show all SharePoint sites
The problem here comes from the fact that SharePoint sites are distributed between different groups and can't be found and selected in one tab, for example in “All site collections”. At the moment this is the product design, the following items are available for selection:
To back up all classic SharePoint sites in the organization, including sites that will be created in the future, expand the Site collections node, select All site collections, and then click Group backup.
To back up individual classic sites, expand the Site collections node, select All site collections, select the sites that you want to back up, and then click Backup.
To back up all group (modern team) sites, including sites that will be created in the future, expand the Groups node, select All groups, and then click Group backup.
To back up individual group (modern team) sites, expand the Groups node, select All groups, select the groups whose sites you want to back up, and then click Backup.
However, we also plan to improve SharePoint site representation in the following feature request RM-4926. As it is a feature request, we cannot provide ETA when it will be implemented in the product.
4. New group "Cyber Operators" is created after C21.09 release

Starting from C21.09 update, a new Windows group Cyber Operators is created on the machine after Agent installation.
This is an internal group that will be used in future versions of the product for new functionality. While this group is not used in current product design, we do not recommend deleting this group, to avoid issues in future.
5. Impossible to disable Files Sync & Share service although there is no usage.

Sometimes it is required to disable File Sync & Share service for specific customer account, however this option may be greyed-out in the management portal:
If you move the mouse over the option you see the message: "You cannot disable a service with non-zero usage. Contact the Support team for assistance." even though the File Sync & Share storage has 0GB usage.
Also, there are no users are using Files Sync & Share service, but management console shows an active user:
The problem here comes from specifics of product implementation: when there is only 1 user for a customer group (the default company administrator user created with the tenant) and File Sync & Share service is enabled, the company administrator user will automatically gain the File Sync User+Administrator role. 
In order to overcome the problem, you can manually remove the File Sync & Share User+Administrator role from the company administrator:
Open management portal
Navigate to the problem customer account and click the Users tab
Find the File Sync & Share administrator account
Remove Company Administrator role from the user and then remove File Sync & Share User + Administrator role
Wait about 5-10 minutes then disable Files Sync & Share service on the tenant. After this, return Company Administrator role to the user.
Note that starting from C22.02, a separate Administrator role is created for File Sync & Share service, instead of User+Administrator.
New KB articles:
Acronis Cyber Protect Cloud:
KB 70388: Acronis Cyber Protect Cloud: Backups to Cloud are running slowly on CA01 and US DC
KB 70371: Acronis Cyber Protect Cloud: "Callback" file is downloaded when logging in to Cloud Console on Safari
KB 70369: Acronis Cyber Protect Cloud: "Forbidden" error is shown by opening cPanel plugin
KB 70365: Acronis Cyber Protect Cloud: Disabled protection plans are still running on workloads after C22.02 release
KB 70360: Acronis Cyber Protect: Agent registration fails with "Access denied"
KB 70356: Acronis Cyber Backup 12.5, Acronis Cyber Protect 15, Acronis Cyber Protect Cloud: Backup hangs if Kaspersky endpoint security is enabled on agent machine
KB 70353: Acronis Cyber Protect Cloud: Company mapping fails with "failed to validate struct”
KB 70352: Acronis Cyber Protect Cloud: Backup Storage tab does not load
KB 70343: Acronis Cyber Backup 12.5, Acronis Cyber Protect 15, Acronis Cyber Protect Cloud: Microsoft 365 backup fails with “Failed to connect to Microsoft Exchange API by using the following URL”
KB 70333: Acronis Cyber Protect: C2C backup fails with "Cannot open or create backup file. [Archive Server]: internal error" on EU1 DC
KB 70322: Acronis Cyber Protect Cloud: Next backup date is in the past or "Never" after C22.02 release

Acronis Cyber Infrastructure:
KB 70345: Acronis Cyber Infrastructure: creation of backup storage fails with 'Offering items required for infra component registration are not available' error
KB 70212: Acronis Cyber Infrastructure: Updating ABGW certificate fails with '"Missed required body argument 'address'" error
KB 70046: Acronis Cyber Infrastructure: Configuring immutable storage returns the error "Incompatible storages found"

Acronis Cyber Files Cloud
KB 70329: Acronis Cyber Files Cloud: Client registration fails with "token issuer is not trusted" if tenant has branded URL

Acronis Disaster Recovery Cloud
KB 70297: Email notification: No VPN tunnels are available
KB 70203: Acronis Cyber Disaster Recovery Cloud: Activity "Setting up disaster recovery infrastructure for protection plan" fails with an internal error

All other new KBs can be found here:
https://kb.acronis.com/new?taxonomy_vocabulary_6_tid%5B%5D=11343&sort_by=created&sort_order=DESC 
All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining 
Release notes and documentation:
Release notes for Acronis Cyber Cloud 22.01 platform update https://dl.managed-protection.com/u/baas/rn/22.01/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 22.02 platform update https://dl.managed-protection.com/u/baas/rn/22.02/en-US/AcronisCyberCloud_relnotes.htm  
Release notes for Acronis Cyber Cloud 22.03 platform update https://dl.managed-protection.com/u/baas/rn/22.03/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 22.04 platform update https://dl.managed-protection.com/u/baas/rn/22.04/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 22.05 platform update https://dl.managed-protection.com/u/baas/rn/22.05/en-US/AcronisCyberCloud_relnotes.htm 
Acronis Cyber Protection agent release notes http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProtectionAgent_relnotes.htm
Acronis Cyber Infrastructure 5.0 https://dl.acronis.com/u/vstorage/relnotes.html 
 

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/09/2022 - 14:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
