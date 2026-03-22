# Support Digest Q3 - Q4 2020

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q3-q4-2020

## Original Post
**Author:** Unknown

Support Digest Q3 - Q4 2020

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrey Vislyaev
                            

                            
                    
                        Acronis Trainer
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello colleagues,
Let me present a new version of the Acronis Digest for Service providers. During the past quarter, we have received several exciting updates, including:
Acronis Cyber Infrastructure 4.0 and Update 1
Acronis Cyber Files 8.7
Acronis Cyber Infrastructure 3.5 Update 5.1
New version of Cyber Protection agent is available for download – 15.0.26077
The platform has received multiple stability and performance improvements 
As usual, we are reviewing the most common questions and problems asked by Partners. Here are the top ones.
#1 How to understand the principles of monthly – weekly – daily retention rules?
By default, the retention rules are specified for each backup set (monthly – weekly – daily) separately.
Monthly backup is the first backup created after a month starts
Weekly backup is the first backup created in the day selected in the weekly backup option.
Daily backup is the first backup created when the day starts unless it is not monthly nor weekly backup.
Let’s have an example here. We setup the retention policy to keep the backups for 3 months 4 weeks and 7 days.

So, the retention will keep each type of backup (Monthly/weekly/daily) no longer than the given value.
For example, if we have:
Monthly backup created on September 15th
Weekly backup created on September 21st
Daily backups created on September 22/23/24.
Then there were no backups till October 2nd, when backup runs on October 2nd the retention policy will check and see that September 22/23/24 backups are already expired and remove them because the daily retention is set to keep backups for 7 days. (it does not mean there always will be seven daily backups). 
If you think this retention policy is too complicated then you can, of course, switch to a simple retention policy by number of backups.
#2 How to exclude specific files/folders from backup?
Let’s suppose that we would like to backup files with .xml extension only. In this case, we should configure file filters in the backup plan options.
To enable file filters:
Select the data to back up in the Protection plan.
Click Change next to Backup options.
Select File filters.
File filters are available for disk-level backups, entire machine backups, and file-level backups. In our scenario, we will select the file filter option, called Backup only files matching the following criteria: *.xml
An asterisk symbol here means that the name of the file could be any, however, the extension of this file should be .xml. The asterisk substitutes for zero or more characters in a file name. For example, the criterion doc*.txt matches files such as doc.txt and document.txt.
In the same way, you could exclude files or folders from backup, in this case you should use Do not back up files matching the following criteria. The criteria could be a full file/folder path or file/folder name.
 
#3 Difference between “Self-service” and “Managed by service provider” management modes.
During tenant creation process, there is an option to select “Management mode”, surprisingly this option also causes confusion for our partners. There are the following modes available:
Self-service – this mode limits access to this tenant for administrators of the parent tenant: they can only modify the tenant properties, but cannot access or manage anything inside (e.g. tenants, users, services, backups, and other resources).
Managed by service provider – this mode grants full access to the tenant for administrators of the parent tenant: modify properties, manage tenants, users, services; access backups and other resources.
Example: I create a partner called “Partner C” under partner “Partner A” and set “Self-service” mode for him, then “Partner C” administrator creates a customer tenant called “Customer D”. Administrators of partner “Partner A” won’t be able to manage anything in “Customer D” (e.g. they won’t’ be able to manage quotas or available services).
Partner A administrator also won’t be able to change the Management mode of Partner C if it is Self-service. For this, the administrator of the created tenant (Partner C) can go to Settings > Security of the management console and set up the Support access switch.
 
#4 How to turn off Antivirus & Antimalware protection?
Sometimes partners complain about the fact that there is no way to disable Antivirus & Antimalware protection if third-party antivirus software is installed on the machine.
Please remember that the corresponding service Cyber Protect Service is always installed along with the agent. However, we do have an incoming feature request to exclude the Antimalware component during the installation procedure (the internal reference is RM-1409), until it is implemented, the best way to disable the service is to turn it off from the Cyber Protection plan:
 
#5 How to continue backing up to an existing archive with a new backup plan?
First of all, we need to know the archive name, which we want to continue. In order to figure this out we can go to the Cyber Protection console > Backup storage, select the location where our archive is located, select it, and hit the Details tab. From there we can see the archive name, in our case it is: Andrew-PC-28C95698-D14D-409C-8EDA-DF56D8628822-298924CF-DA3C-4CA0-B833-CE4D39225206A
 
Then we need to create a new backup plan and go to the Backup options
Select Backup file name and hit Select
Select the archive name, from the Step 1.
 
#6 Cannot backup Office 365/Microsoft Teams/OneDrive, the corresponding sources don't appear in console.
The reason behind this issue is the fact that corresponding offering items are disabled for the customer tenant. For example, if a customer would like to backup Office 365 items, his partner administrator or company administrator needs to go to the management portal, select the customer tenant and enable corresponding offering items by clicking on the “Edit” button for the corresponding tenant:
After the corresponding offering items are enabled (Office 365 seats/Mailboxes/OneDrive etc), click on the Save button and go to the Cyber Protect console.
Go to the “All devices” and hit the Add button, now you should be able to see and deploy “Microsoft 365 Business” agent as per the documentation:
https://www.acronis.com/en-us/support/documentation/CyberProtectionService/index.html#protecting-office-365-data.html
#7 What are the prerequisites to use application-aware backup?
I would like to remind you that application-aware backup is a disk-level backup that also contains the applications' metadata. This metadata enables browsing and recovery of the application data without recovering the entire disk or volume. The disk or volume can also be recovered as a whole.
The prerequisites are:
On a physical machine, Agent for SQL and/or Agent for Exchange must be installed, in addition to Agent for Windows.
On a virtual machine, no agent installation is required; it is presumed that the machine is backed up by Agent for VMware (Windows) or Agent for Hyper-V.
Agent for VMware (Virtual Appliance) can create application-aware backups, but cannot recover application data from them. To recover application data from backups created by this agent, you need Agent for VMware (Windows), Agent for SQL, or Agent for Exchange on a machine that has access to the location where the backups are stored.
The whole list of prerequisites is available here:
https://www.acronis.com/en-us/support/documentation/CyberProtectionService/prerequisites.html
 
#8 Difference between agent-based and agentless backup.
Agentless backup means the ability to back up and recover virtual machines without installing agents into the guest OS. This functionality becomes available by using Agent for VMware, Agent for Hyper-V, Agent for Virtuozzo, Agent for Virtuozzo Infrastructure Platform/Acronis Cyber Infrastructure.
Agent-Based backup requires an agent (for Windows or Linux) installed inside Guest OS of each virtual machine on the host.
The are many benefits of agentless backups: 
CPU/RAM/network overhead required to support an agent in every machine, agentless approach effectively eliminate this overhead. 
Centralized administration of the agents and policy-based management of the backup plans. (you can create a single plan that is applied to all VMs)
Agentless solution support application-aware backups
Possibility to run a VM from backup allows to quickly test restore functionality
VMware VM replication (creates an exact copy or replica of a VM to the same or another ESXi host which can be maintained in sync with the original VM)
It makes sense to use agent-based backup in the following cases:
You need to backup files/folders on the machines, which is not possible using agentless backup
You have many physical machines or mixed environment of virtual and physical machines
 
#9 Compatibility with LogMeIn / Bitdefender antivirus software.
Recently we discovered an issue with compatibility with Bitdefender antivirus software, when attempting to install LogMeIn Antivirus to a machine that has Acronis Cyber Protect Cloud (build 22210 or newer) already installed the installation fails with:
Installation failed! LogMeIn Antivirus cannot be successfully installed.
Actually, Cyber Protect is not compatible with other solutions that use Bitdefender Traffic Interceptor SDK. Also, take into consideration the fact that running two security applications simultaneously may cause major problems with the operating system. In addition, we have a feature request, which allows installing Agents without Antimalware components (internal link is RM-2521).
See all new KB articles here: https://kb.acronis.com/new 
All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining 
 
Release notes and documentation:
Acronis Cyber Infrastructure 4.0 Update 1 https://dl.acronis.com/u/vstorage/relnotes.html 
Acronis Cyber Infrastructure 4.0 Release https://dl.acronis.com/u/vstorage/relnotes.html
Acronis Cyber Infrastructure 3.5 Update 5.1 https://dl.acronis.com/u/vstorage/relnotes.html
Acronis Cyber Files 8.7 release https://support.grouplogic.com/?page_id=4566 
Latest Acronis Cyber Protect agent release notes: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProtectionAgent_relnotes.htm 
Release notes for latest Acronis Cyber Cloud 20.12 platform update:
http://dl.managed-protection.com/u/baas/rn/20.12/en-US/AcronisCyberCloud_relnotes.htm

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 12/28/2020 - 12:22

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
