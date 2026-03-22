# Support Digest: Q4 2019

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q4-2019

## Original Post
**Author:** Unknown

Support Digest: Q4 2019

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
I'm happy to present to you the new edition of Acronis Digest for Service providers. During the past three months we have introduced several important updates for Acronis Cyber Cloud platform and have added some brand new features for our Partners, namely:
Acronis Cyber Cloud platform was updated to v.8.0.
A new version of the backup agent is available for download - 12.5.14800.
Released special portals for Partner, who'd like to develop their own services based on Cyber Cloud platform.
Multiple stability and performance improvements for the platform.
 
Hot topics
New KB articles
New training materials
Data center and agent updates
Release notes and documentation
 
Hot topics
As usual, we are reviewing the most frequently asked questions during the past few months. This time we are going to discuss the following four topics:
#1 ► Acronis Backup Cloud: editions' management
Starting from version 8.0 Acronis Backup Cloud service' licensing is implemented via three editions. Each edition includes certain basic product's functionality, and apart from that, Advanced and Disaster Recovery editions some additional features, not included in Standard one. They are (sorted by the number of product's capabilities, from minimal to maximal):
Standard – provides backup and recovery functionality that covers small environment needs.
Advanced – provides backup and recovery functionality designed for big environments. It is dedicated to protect advanced workloads such as Microsoft Exchange and Microsoft SQL cluster and provides group management and plan management.
Disaster Recovery – provides the disaster recovery functionality along with the advanced backup and recovery functionality. It is designed for companies that have high requirements for the Recovery Time Objective and needs in advanced backup and recovery functionality.
By default, after Acronis Cyber Cloud's update to version 8.0 all Customer groups are switched to Standard edition. In order to change the edition, open the Customer group's settings and click the respective radio button.

Important: in order to enable Advanced or Disaster Recovery edition for a Customer group, it is necessary to make sure that those editions are available at Customer's parent Partner
More details regarding editions' management can be found under Acronis Cyber Cloud's Partner guide. The following link describes services, offerings and quotas management.
 
 
 Having trouble backing up your machine with SQL server onboard, where the backup fails with "Device has no quota to apply backup plan" error?
Symptoms:
Backup plan was applied to the device with workstation OS and SQL
Backup plan was working without any issues before the update to Acronis Cyber Cloud 8.0
After the update, quota is not assigned to the resource, backup plan is not running due to error "Device has no quota to apply backup plan" and can't be applied because a Server quota is not acquired automatically by a Workstation resource.
Solution:
Apply server quota manually (go to device → details → service quota → change):

If the manual assignment does not resolve the issue - please raise a support request with Acronis Service provider support team.
 
#2 ►File filters: how to include/exclude some particular files/folders/volumes from the backup
One of the most useful ways to decrease the size of a backup archive is to set file filters under the backup plan’s options when creating the task. Excluding the unwanted types of data will not only help to make your archives smaller but also speed up backup performance and save your money due to lower cloud space consumption. You can either choose to include some specific folders/files from source machine into backup (thus excluding everything else), or exclude some folders/files (therefore, everything BUT those items will be backed up.) You can even exclude the entire partition if you don't want its content backed up.
Example #1: We’d like to back up the entire Windows machine, except for partition F:. Also, we do not need to backup any *.log files. In this case, we set the filters the following way: 

Example #2: We’d like to back up only configuration files located on Linux machine in /usr/lib/config/ folder. In this case, we set the filters the following way

Check the following article for complete description of the file filter setting.
#3 ► Moving groups within Acronis Cyber Cloud's hierarchy
What to do if some Customer group was accidentally created not at the desired level of hierarchy? Not a problem, just use Management console's Move operation:
Find new parent group’s internal ID
Move other group(s) under new parent groups with the selected internal ID

For a detailed step-by-step description, click here.
Important: A tenant can be moved only if the target parent tenant has the same or a larger set of services and offering items as the original parent tenant.
Note: User accounts cannot be moved between Customer groups.
 
#4 ► MacOS Catalina support
We're glad to confirm that starting from Acronis Cyber Cloud v.8.0 macOS 10.15 Catalina is fully supported! In order to protect your Mac with Catalina already installed, you just need to make sure Acronis Agent for Mac is updated to the latest version available - v 12.5.14800. To get the latest version, please follow these instructions, or simply download the installer from Backup Console and run it on the device.
Having troubles backing up your Mac with the latest OS X already installed? Try one of these troubleshooting articles.
 
 Did you know that more than 300 Acronis Partners have already become Acronis Certified Service Providers? Become certified now! Pass the certification exam now: https://www.surveygizmo.com/s3/5235045/Service-Provider-Certification-Exam-Acronis-Backup-Cloud-v-8-0
New KB articles
Acronis Backup Cloud
KB63788: Acronis Backup Cloud: Error "A device has no quota to apply a backup plan" or "cannot apply a backup plan to a device with assigned quota" for device with Workstation OS and enabled application backup after DC is updated to Acronis Cyber Cloud 8.0
KB63784: Acronis Backup: Manual service quota assignment to the device does not work in DC updated to Acronis Cyber Cloud 8.0
KB63780: Acronis Backup: SQL database backup fails with "An invalid file has been detected"
KB63772: Acronis Backup for Plesk/cPanel: mounting backups located on SMB share fails
KB63752: Acronis Backup Cloud: deleting archives from cloud storage fails with "The file is read-only"
KB63737: Acronis Backup: Disk/Volume level backup fails on Linux machine with more than one kernel
KB63723: (FIXED) Acronis Backup: Alert "Backup is missing: No successful backups for XX days" is raised when plan is revoked from all devices
KB63721: Acronis Cyber Cloud: how to switch from non-existent storage infrastructure with usage
KB63713: Acronis Cyber Cloud: how to change Cloud resources on tenant level
KB63709: Acronis Backup Cloud: website backup fails with "Could not connect to remote file system"
KB63663: Acronis Backup: Attempt to enable application-aware backup of a virtual machine fails with "Failed to get the object's property 'disk.EnableUUID'"
KB63541: Acronis Cyber Cloud for WHMCS: Supported languages
KB63536: Acronis Cyber Cloud for WHMCS: How to setup specific Storage in Configurable Options Group
KB63331: Acronis Backup Cloud: backup of Office 365 group mailbox fails with "Cannot back up the primary mailbox of an Office 365 user"
Acronis Cyber Infrastructure
KB63761: Acronis Cyber Infrastructure: how to activate SPLA license
KB63721: Acronis Cyber Cloud: how to switch from non-existent storage infrastructure with usage
KB63431: Acronis Cyber Infrastructure: how to download ISO
KB63414: Acronis Cyber Infrastructure: network performance between VMs is low
KB63326: Acronis Cyber Infrastructure: Mellanox ConnectX support
KB63288: Acronis Cyber Infrastructure Backup Gateway: how to reconfigure ABGW to use another NFS export to store archives
Acronis Files Cloud
KB63346: Acronis Cyber Cloud: integration with Active Directory
KB63195: Acronis Files Cloud and Acronis Files Advanced for iOS: Touch ID/Face ID not working 
See all new KB articles here: https://kb.acronis.com/new
 
 Did you know that now it is possible to integrate and extend applications and services with cyber protection solutions while connecting and selling them with the Acronis community of over 50,000 channel partners? Visit https://developer.acronis.com/ and https://solutions.acronis.com/ for more details, start building your own services and integrations now!
 
New training materials
Acronis Cyber Cloud 8.0: What's new in v.8.0
Acronis Backup Cloud 8.0: product training
 All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining
Data center and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.14800)
Backup Agent for Mac (v.12.5.14800)
Backup Agent for Linux (v.12.5.14800)
 

Data center


Platform 
version


Available services


Strasbourg (EU1)


8.0


Backup
G Suite
Office 365 Cloud-To-Cloud 2.0
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Frankfurt (EU2)


8.0


Backup
Disaster Recovery
G Suite
Notary
Office 365 Cloud-To-Cloud 2.0
File Sync&Share
Physical Data Shipping
Storage SPLA


London (EU3)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Lupfig (EU5)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Storage SPLA


Ashburn (US2)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Ashburn (US5)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Nagano (JP1)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Singapore (SG1)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Sydney (AU1)


8.0


Backup
Disaster Recovery
G Suite
Office 365 Cloud-To-Cloud 2.0
Notary
File Sync&Share
Physical Data Shipping
Storage SPLA


Moscow (RU2)


8.0


Backup
Office 365 Cloud-To-Cloud 2.0
G Suite
Storage SPLA

 
Release notes and documentation
Acronis Cyber Cloud 8.0 release notes 
Acronis Cyber Infrastructure 3.0 Update 4 release notes 
Acronis Files Cloud application for iOS v.8.4 release notes

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/03/2019 - 13:40

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  3 Users found this helpful
