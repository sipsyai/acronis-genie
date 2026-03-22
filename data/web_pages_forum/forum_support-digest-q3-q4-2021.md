# Support Digest Q3 - Q4 2021

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q3-q4-2021

## Original Post
**Author:** Unknown

Support Digest Q3 - Q4 2021

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrey Vislyaev
                            

                            
                    
                        Acronis Trainer
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello colleagues,
Let me present a new issue of the Acronis Digest for Service providers. During the past quarters, we have received several exciting updates:
There were several updates during this period with platform improvements (21.07 – 21.12)
A new version of Cyber Protection agent is available for download – 15.0.28559
Acronis Cyber Infrastructure 4.6 Update2 
Acronis Cyber Infrastructure 4.6 Update 2 Hotfix 2
Acronis Cyber Infrastructure 4.7
 
Table of contents:
Do you know?
Most frequently asked questions and reported problems
New KB articles
Release notes and documentation
 
Do you know?
The Immutable Storage feature has been added recently in Acronis Cyber Protect Cloud. The Immutable Storage allows you to access deleted backups during a specified retention period. You can recover the content of these backups, but you cannot change the backup files or move them back to their original storage. When the retention period ends, the backups in immutable storage are permanently deleted. Refer to the user guide to get more information about the feature:https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#immutable-storage.html 
 
Most frequently asked questions and reported problems
#1.    New Microsoft 365 licensing 
Changes in the Microsoft 365 licensing in Per Workload model in C21.10: Microsoft 365 resources require Seat quotas. 
The Microsoft 365 seats that are subject to a per-seat license are:
Mailbox 
OneDrive
Public folder
Mailbox and/or OneDrive with access to backed-up SharePoint sites and/or Microsoft Teams.
Please note: If a group has access to a SharePoint site, then all users of this group will be counted in the number of seats.
Question: What if the customer deletes or stops protecting a Microsoft 365 seat, but wants to keep the backup archives in the Acronis Cloud? Will it cost anything?
Answer: Partners can store the backup archives from all deleted or non-protected (i.e. with no protection plan) items in the Acronis Cloud, but they will be charged for the used cloud storage. The items subject to such charges are:
Mailbox
OneDrive
Public folder
Microsoft Teams
SharePoint sites
Shared mailboxes
Note: Seats quotas should be enabled in the Per GB model as well, but customers won’t be charged for them.
For more details refer to https://kb.acronis.com/node/69686 
 
#2.    A quota was reverted back after manual change
An example of the problem may be the following: you changed any quota in the account management console, for simplicity, let’s say the Workstation quota from 10 to 20. After some time, you have noticed that the quota is changed back to 10 with no interaction from your side.
A root cause could be an integration system configured for the group.
You can confirm that the changes have been made by the integration system by looking at the Audit log:
Open the account management portal
Navigate to partner account where the problem appears
Open the Audit log tab
Filter events, select Event type equals to quota was updated and approximate time frame 
Look for such events, if it turns out that the quota is updated via API client then the changes are made by the integration system configured in the account

 
#3.    Legacy licensing End of Life
With legacy editions, you can assign only one edition per Customer group. As a result, your customers pay for all features that are included in an edition, even if they do not use some of them. Currently, we switched to another licensing model with billing modes and advanced packs, the functionality is split into multiple offering items and enables multiple offering items per workload. The licensing engine automatically acquires the offering items depending on what features are requested in protection plans. Users can optimize the level of protection and cost by customizing their protection plans.
There are two billing modes available:
Per workload — charged according to the number of protected machines, regardless of the size of backed-up data.
Per gigabyte — charged according to the combined size of data stored in all backup destinations, regardless of the number of protected machines.
By default, Acronis Cyber Protect Cloud includes features that cover most of the cyber security threats. You can use these features without an additional fee. In addition, it is possible to enable advanced features to boost the protection of the workloads. Check the following KB article to get more information about the features included in different advanced packs: https://kb.acronis.com/content/64747 
The legacy licensing End of Life (EOL) was on October 1st, 2021. This means all customers and partners who were using the legacy editions were switched to the new licensing models. Here are the editions that are subject to EOL:
(Legacy) Cyber Backup - Standard
(Legacy) Cyber Backup - Advanced
(Legacy) Cyber Backup - Disaster Recovery
(Legacy) Cyber Protect - Standard
(Legacy) Cyber Protect - Advanced
(Legacy) Cyber Protect - Disaster Recovery
(Legacy) Cyber Protect (Per workload)
(Legacy) Cyber Backup (Per gigabyte)
You can read more about the switch process and mapping between legacy editions and new licensing here: https://kb.acronis.com/licensing-switch https://kb.acronis.com/content/69256
 
#4.    What are the “included features”?
When you enable a service in Cyber Protect Cloud, you enable a number of features that are included and available by default. In addition, you can enable advanced protection packs.
Users can use the included features at no additional charge. However, it is not possible to backup using including features quota, e.g. Virtual Machines (included features) quota.

Here are examples of included features:
#Cyber fit score
Vulnerability assessment
Anti-ransomware protection: Active protection
Antivirus and Antimalware protection: Cloud signature-based file detection (no real-time protection, only scheduled scanning)
Antivirus and Antimalware protection: Pre-execution AI-based file analyzer, behavior-based Cyber Engine
Microsoft Defender management
See the user guide, to get more infomration on the included features: https://www.acronis.com/en-us/support/documentation/AcronisCyberCloud/index.html#cyber-protect-and-advanced-packs.html
 
#5.    Agent registration fails with: “Failed to validate possible tenant change: unintended tenant change”
Here is an example of such an issue: you've attempted to register an agent and the registration process failed with the error: “Failed to validate possible tenant change: unintended tenant change”.
Such an issue appears when you re-register the agent without deleting it from the previous tenant (e.g. the original tenant was removed). In this situation the resource remains tied to the previous account and cannot be registered again.
There are two possible workarounds:
Unregister the agent manually using the register_agent tool: register_agent.exe -o unregister https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#registering-machines-manually.html 
Change MMScurrentMachineID and InstanceID on the affected machine: see How to change MMScurrentMachineID and InstanceID for instructions
After applying one of the workarounds, reattempt the registration: see Registering backup client manually.
 
#6.    When a new version of Cyber Protection agent is released?
A new version of Acronis Cyber Protection agent becomes available after one or two weeks since the update of the particular data center. Don’t forget that agents can be updated automatically using the auto-update feature. It can be enabled from the account management portal then the setting will be applied to all sub-customers and sub-partners.
Settings > Agents update

Or from the Cyber Protection console:
Settings > Agents > Edit default agent update settings

Check more information in the user guide: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#updating-agents.html 
 
New KB articles:
Acronis Cyber Protect Cloud:
KB 69867: Acronis Cyber Protect Cloud: Acronis Managed Machine service fails to start due to Scheduler service dependency on build 28156 and higher
KB 69855: Acronis Cyber Protect Cloud: Acronis Agent Core service fails to start due to corrupted .yaml file
KB 69849: Acronis Cyber Protect Cloud: Backup deletion fails with "You try to delete an already deleted archive. Probably list of archives is outdated. Press refresh vault to get the actual archive list"
KB 69838: Acronis Cyber Protect: Backup of VMware ESXi VMs fails with "Failed to authenticate with the guest operating system using the supplied credentials"
KB 69797: Acronis Cyber Protect Cloud: Manual removal and cleanup of Agent for Linux
KB 69793: Acronis Cyber Protect Cloud: macOS backup fails with "Operating system error: Resource deadlock avoided"
KB 69783: Acronis Cyber Protect: Backup fails with “Storage request timeout” and “Storage is unavailable”
KB 69768: Acronis Cyber Protect: Patch management or Vulnerability assessment activities fail with "Failed to parse pending updates JSON fallback"
KB 69762: Acronis Cyber Protect: SQL backup fails with "Unable to find an object that meets the following criteria"
KB 69760: Acronis Cyber Protect Cloud: Attempt to export or validate backup via console fails with "Failed to get archive_replication draft from session"
Acronis Cyber Infrastructure:
KB 69818: Acronis Cyber Infrastructure: cluster update start fails with 'There are inactive nodes. Check "shaman stat -j"' message
KB 69711: Acronis Cyber Infrastructure: 'A CS service has too big journal' alert
KB 69649: Acronis Cyber Infrastructure: ABGW with NFS backend failed after update to ACI 4.6
KB 69436: Acronis Cyber Infrastructure: Updating ABGW certificate fails with 'Cloud installation setup id XXX does not match the response of account server YYY' error
KB 69267: Acronis Cyber Infrastructure: How to collect problem report
KB 69230: Acronis Cyber Infrastructure: "Clusters must be registered at the same account server" error on attempt to set up Backup storage Geo-replication
Acronis Cyber Files Cloud
KB 69765: Acronis Cyber Files Cloud: Desktop client crashes on macOS
KB 69303: Acronis Cyber Files Cloud: Client for Mac does not start after C21.07 update
KB 69254: Acronis Cyber Cloud: How partners using own custom integrations can switch to new Advanced licensing
Acronis Disaster Recovery Cloud
KB 69377: Acronis Cyber Disaster Recovery Cloud: how compute points are consumed
KB 69368: Acronis Disaster Recovery Cloud: Custom DNS settings of VPN Client for Point-to-site connection
KB 69292: Acronis Disaster Recovery Cloud: VPN Appliance registration fails with "User name or password is incorrect" for user with enabled 2FA
KB 69178: Acronis Cyber Disaster Recovery Cloud: Failover of a Linux machine fails with "The backup contains the unsupported volume type"
All other new KBs can be found here:
https://kb.acronis.com/new?taxonomy_vocabulary_6_tid%5B%5D=11343&sort_by=created&sort_order=DESC 
All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining 
 
Release notes and documentation:
Release notes for Acronis Cyber Cloud 21.07 platform update https://dl.managed-protection.com/u/baas/rn/21.07/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.08 platform update https://dl.managed-protection.com/u/baas/rn/21.08/en-US/AcronisCyberCloud_relnotes.htm
Release notes for Acronis Cyber Cloud 21.09 platform update https://dl.managed-protection.com/u/baas/rn/21.09/en-US/AcronisCyberCloud_relnotes.htm
Release notes for Acronis Cyber Cloud 21.10 platform update https://dl.managed-protection.com/u/baas/rn/21.10/en-US/AcronisCyberCloud_relnotes.htm
Release notes for Acronis Cyber Cloud 21.11 platform update https://dl.managed-protection.com/u/baas/rn/21.11/en-US/AcronisCyberCloud_relnotes.htm
Release notes for Acronis Cyber Cloud 21.12 platform update https://dl.managed-protection.com/u/baas/rn/21.12/en-US/AcronisCyberCloud_relnotes.htm
Latest agent release notes build 15.0.28610: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProtectionAgent_relnotes.htm 
Acronis Cyber Infrastructure 4.6 Update 2 https://dl.acronis.com/u/vstorage/relnotes.html
Acronis Cyber Infrastructure 4.6 Update 2 Hotfix 2 https://dl.acronis.com/u/vstorage/relnotes.html
Acronis Cyber Infrastructure 4.7 https://dl.acronis.com/u/vstorage/relnotes.html

      
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/22/2021 - 13:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
