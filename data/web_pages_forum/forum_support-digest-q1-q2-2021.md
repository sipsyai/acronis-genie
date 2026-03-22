# Support Digest Q1-Q2 2021

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q1-q2-2021

## Original Post
**Author:** Unknown

Support Digest Q1-Q2 2021

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrey Vislyaev
                            

                            
                    
                        Acronis Trainer
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello colleagues,
 
Let me present a new issue of the Acronis Digest for Service providers. During the past quarter, we have received several exciting updates, including:
Acronis Cyber Infrastructure 4.5 release
Acronis Cyber Infrastructure 4.5 Update 1
New version of Cyber Protection agent is available for download – 15.0.27147
There were several updates during this period with platform improvements (21.01 – 21.06)
Table of contents:
Do you know?
Most frequently asked questions and reported problems
New KB articles
Release notes and documentation
Do you know?
Acronis Data Centers are located all over the world and we constantly expanding the number and country coverage. You can check the map of Acronis Data Centers here:
https://www.acronis.com/en-us/data-centers/ 
Most frequently asked questions and reported problems:
1. "Protection plan '...' cannot be applied to '...' because assigned quota does not allow functionality".
Here is an example of such issue:
A customer has Cyber Protect with any billing mode and no advanced packs available 
When he tries creating a protection plan, which has features includes in advanced packs (e.g. when he tries to backup SQL/Exchange cluster, which are included in Advanced Backup pack) an error occurs: "Protection plan cannot be applied or updated as the device has no appropriate quota". 
At the moment this behavior is by design. The reason behind this is that Cluster backup functionality is only available in “Advanced Backup” pack.  We plan to add more detailed information message that provides clear explanation in which packs this functionality is available (Internal link to the feature request is RM-2605).
Check here the list of features and packs: https://kb.acronis.com/content/64747 
2. Cannot perform recovery if no online machines in the account.
Here is how the issue could be reproduced:
Create a backup of the machine with the Cyber Protection agent.
Turn off the machine or simply stop Acronis Managed Machine Service from the list of services in the OS. After some time the machine will be shown as offline in the Cyber Protection console.
Select the offline machine.
Go to the recovery tab of the Cyber Protection console and try to recover any items.
Actual result:
It is not possible to recover any items from the Cyber Protection console if there are no online agents. In order to overcome this, you can use the following methods:
Web Restore panel, which is available from the Cyber Protection console > Recover > Download files 
Bootable media, you can download the ISO image from the same Recovery tab and boot any available machine using it and then recover the data
Check here all available recovery methods here: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#recovering-machine.html  
3. File-level restore from image backup of NTFS dedup volumes: how-to.
In this scenario, there is a Windows Server 2012 (or later) with Data Deduplication enabled for its NTFS volumes. You have created a backup of this server and want to restore some files from this backup.
Due to the mechanism of deduplication, it is impossible to recover files from deduplicated volumes directly from backup. First, it is necessary to recover the volume, where the files were contained. There are several ways to do that:
If you have Agent for VMware or Agent for Hyper-V, run the backup as a virtual machine and copy files from the VM. Learn how to use the Run as VM feature in this topic.
Use any virtualization platform (e.g. Oracle Virtual Box), create an empty VM and recover the entire machine backup to it using Bootable Media. See this topic for instructions. After recovery is completed, copy the necessary files from the VM.
Recover the backup of entire machine to a spare physical machine, then copy the required files.
Mount the backup (you should have Acronis Cyber Protection agent installed to do that) as in read-only mode and recover the file:
Navigate via the file explorer from the backed-up server to the location where the backups are, e.g. \\Share\backups
Open the backup archive and navigate to the point where the hard disks (C: | D: etc.) are displayed
Right-click the drive letter from which files are to be restored and select "Mount in read-only mode"
The hard disk is then attached directly to the server. Here you can navigate to the folder or file that you want to restore Then simply copy the desired file to the destination.
Then disconnect the "backup hard drive" via the Explorer by right-clicking and selecting "unmount".
See more details here: https://kb.acronis.com/content/60669 
4. How to export archive from storage and save it on another storage?
There could be a situation when you decided to move archives from one storage to another.
Currently, we have the following options to do that:
Enable replication in the protection plan. You can replicate a backup from any of these locations: Local/Network folder/Secure zone. You can replicate a backup to any of these locations: Local/Network folder/Cloud. See more details here: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#replication.html 
For the archives stored at the Cloud storage the solution is to use Large Scare Recovery (LSR) to download the archive, see details here: https://kb.acronis.com/content/56070 The same tool could be used to upload the archive to another storage (e.g. partner-hosted storage).
5. Moving devices between tenants: procedure to re-register agents, export/import plans, continue backups to the same archive.
Let us discuss the situation when it is required to move devices from one account to another.
The workflow is the following:
Unregister devices from the original account
Export the plans
Import the plans to the new account
Re-register the agents
Continue backing up to the old archives
In order to unregister an already registered agent from Cyber Protection console, you need to go to the Devices > All devices tab, select the agent that you are going to move, and click the delete button: 
Now, let’s export the plan, it can be done from the Plans tab (this tab could be missing if you use Standard legacy edition), by selecting the corresponding plan and clicking Export. 
After the plan is exported, it is saved on the local machine as .json file, now you can login to the new account Cyber Protection console, navigate to the Plans and click Import, choosing the .json file saved on the previous step. 
Re-register the agents in the new account, using the KB https://kb.acronis.com/content/55244 
When the agent appears in the new account Cyber Protection console after registration, you can edit the imported protection plan and select the old archive to continue. It can be done if the archive is located on local disks or a network share. If the archive is located in the Cloud, it should be downloaded locally using https://kb.acronis.com/content/56070. Note that in Where to backup you should select the destination, which contains the archive file (e.g. if the previous archive was saved to a network share \\192.168.0.1\ then a new plan should have the destination in where to backup).
In order to continue the old archive, go to the Backup options > Backup file name 
Click Select and select the old archive that you want to continue 
6. How to protect Agent for Windows from uninstallation?
Let’s suppose that the Windows Agent machine has been attacked by a hacker. The hacker had manually uninstalled the Acronis Cyber Protect agent, before installing viruses.
Partners asked if we could block the uninstall process initiated by a user.
Recently we added a new feature called Self-Protection. Self-protection prevents unauthorized changes to the software's own processes, registry records, executable and configuration files, and backups located in local folders. It is enabled by default and we do not recommend disabling it.
As a part of self-protection, we also have the password-protection feature, that prevents unauthorized users or software from uninstalling Agent for Windows or modifying its components. These actions are only possible with a password that an administrator can provide.
In order to enable the password-protection feature, you need to create a new protection plan for the Windows device. Go to Antivirus & Antimalware protection, select Self-protection. 
Enable the password-protection option: 
7. Not possible to change Enhanced security option.
The Enhanced security mode provides special settings for clients with increased security demands. It can be setup during customer account creation. 
You can check if Enhanced security mode is enabled or disabled for a tenant from the management console:
Navigate to the tenant, where you want to check the setting
Click Configure
Scroll down to the bottom of the page and check the setting under General information 
When enabled, all backups created in a customer tenant and its units are automatically encrypted with the AES algorithm and 256-bit key.
At the moment it is not possible to disable this mode after the tenant is created, as a workaround the customer tenant should be recreated. However, we have a plan to implement such feature in the future – disabling the enhanced security mode after tenant creation. The internal link to this feature request is RM-2571.
New KB articles:
Acronis Cyber Protect Cloud:
KB 67884: Acronis Cyber Protect Cloud: Unable to save backup plan of network share due to the error "The credentials for location are not specified"
KB 67895: Acronis Cyber Protect Cloud: Microsoft Security Essentials interferes with Acronis Cyber Protection
KB 67900: Acronis Cyber Protect Cloud: Activity fails with "Failed to connect to the Agent Core service on this machine"
KB 67903: Acronis Cyber Protect Cloud: pending activity "Setting up disaster recovery infrastructure for protection plan" in Activities after creating or editing protection plan
KB 67905: Acronis Cyber Protect Cloud: Active Protection service cannot be started on Windows 7
KB 67908: Acronis Cyber Protect Cloud: how to fix corrupted archives in network locations
KB 67913: Acronis Cyber Protect Cloud: Unable to register Google Workspace account to tenants with branded URL
KB 67914: Acronis Cyber Protect Cloud: Archives with "<device_name>-Remediation" names
KB 67917: Acronis Cyber Protect Cloud: Vulnerability assesment activity completes with warning "PmWinUpdatesPaused"
All other new KBs can be found here:
https://kb.acronis.com/new?taxonomy_vocabulary_6_tid%5B%5D=11343&sort_by=created&sort_order=DESC 
Acronis Cyber Infrastructure:
KB 67949: Acronis Cyber Infrastructure: 'Network interface is missing important features (or has them disabled)' alert
KB 68011: Acronis Cyber Infrastructure: Error "The IP X.X.X.X does not belong to any of available networks.”
KB 68016: Acronis Cyber Infrastructure: How to measure network throughput between nodes using iPerf3
KB 68018: Acronis Cyber Infrastructure: Error "iSCSI LUN X of target group X is set to failure domain "disk" even though 5 nodes are available. It is recommended to set failure domain to "host" so that the LUN can survive host failures in addition to disk failures"
KB 68019: Acronis Cyber Infrastructure: Failed to deploy Compute Cluster in a Hyper-V VM due to error "Some nodes did not pass hardware validation. Node "XXXX" must have hardware virtualization enabled."
KB 68236: Acronis Cyber Infrastructure: After update ACI to release 4.5.0 (284) the Backup Storage configuration is absent in UI with 'Failed' status of service on Nodes view
KB 68284: Acronis Cyber Infrastructure: Unexpected append throttling ABGW installations with public cloud backend
Acronis Cyber Files Cloud
KB 68026: Acronis Cyber Files Cloud: Files upload fails with python errors: unbalanced parenthesis
Acronis Disaster Recovery Cloud
KB 67981: Acronis Disaster Recovery Cloud: How to configure Acronis IPSec VPN Gateway and pfSense firewall
KB 68042: Acronis Disaster Recovery Cloud: How to configure Acronis IPSec VPN Gateway and Sophos XG Firewall
KB 68045: Acronis Disaster Recovery Cloud: How to configure Acronis IPSec VPN Gateway and WatchGuard
KB 68049: Acronis Disaster Recovery Cloud: How to configure Acronis IPSec VPN Gateway and Cisco ASA
KB 68070: Acronis Cyber Disaster Recovery Cloud: Creating a primary or recovery server fails with "Quota is reached"
KB 68071: Acronis Cyber Disaster Recovery Cloud: Recovery/Primary server does not have Internet access
KB 68074: Acronis Cyber Disaster Recovery Cloud: Failover or test failover of a Recovery server fails
KB 68076: Acronis Cyber Disaster Recovery Cloud: How to find group ID
KB 68078: Acronis Cyber Disaster Recovery Cloud: How to find server id of a cloud, recovery or primary server
KB 68080: Acronis Cyber Disaster Recovery Cloud: Unable to initiate a failover or test failover
All other new KBs can be found here:
https://kb.acronis.com/new?taxonomy_vocabulary_6_tid%5B%5D=11343&sort_by=created&sort_order=DESC 
All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining 
Release notes and documentation:
Acronis Cyber Infrastructure 4.5 release https://dl.acronis.com/u/vstorage/relnotes.html 
Acronis Cyber Infrastructure 4.5 Update 1 https://dl.acronis.com/u/vstorage/relnotes.html 
Latest Acronis Cyber Protect agent release notes: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProtectionAgent_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.01 platform update: https://dl.managed-protection.com/u/baas/rn/21.01/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.02 platform update: https://dl.managed-protection.com/u/baas/rn/21.02/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.03 platform update: https://dl.managed-protection.com/u/baas/rn/21.03/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.04 platform update: https://dl.managed-protection.com/u/baas/rn/21.04/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for Acronis Cyber Cloud 21.05 platform update: https://dl.managed-protection.com/u/baas/rn/21.05/en-US/AcronisCyberCloud_relnotes.htm 
Release notes for latest Acronis Cyber Cloud 21.06 platform update: https://dl.managed-protection.com/u/baas/rn/21.06/en-US/AcronisCyberClo…  

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/07/2021 - 11:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
