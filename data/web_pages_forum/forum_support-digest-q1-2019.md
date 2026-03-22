# Support Digest: Q1 2019

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q1-2019

## Original Post
**Author:** Unknown

Support Digest: Q1 2019

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
I welcome all of you to the latest edition of support digest for service providers!  This issue of MSP digest aggregates the most important news related to Acronis Data Cloud platform for the last three months (Jan - March 2019), so there are quite a lot of exciting updates included!
At the beginning of the year, Acronis Data Cloud 7.8 Update 2 was rolled out on all Acronis data centers. With this update, the Acronis flagship cloud product offers enhancements and addresses the issues found in the previous releases. Apart from that, the Platform now supports seven more languages:
●    Bulgarian                    ●    Norwegian                   ●     Swedish                      ●    Finnish
●     Serbian                       ●    Malay                          ●     Indonesian
 
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
As usual, we’re reviewing the most common questions coming from Partners during the past month. Below are the most common topics.
#1 ► Protecting applications
Acronis Backup Cloud provides two options to protect Microsoft applications (Exchange, SQL, Active Directory):
Application-aware entire machine backup
Database backup
When using option #1 Acronis Backup Agent not only backs up the entire device but also collects meta-data of MS applications. Thus, the applications are backed up consistently and in a state, they were at the moment when the backup was taken. When the entire machine archive with application option is restored, the application itself will be available immediately after the machine is recovered. Moreover, it will be possible to recover specific application items (Exchange Databases, SQL Databases, Exchange mailboxes) right from entire machine backup!
Application-aware disk-level backup is available for physical machines and for ESXi virtual machines.
 
Option #2 suits the needs of those, who want just the applications to be backed up, nothing else. With such approach, Acronis Backup Agent backs up only Exchange SQL Databases and the files associated with them. Resulting archive is much smaller compared to the one created using the "entire machine" option. In this case, SQL/Exchange databases can be recovered either as files to any available destination or directly into running SQL/Exchange server without causing any interruptions to production. Exact description of SQL and Exchange items can be found here: SQL Databases, Exchange Databases, Exchange mailboxes.
Before using either of the options above make sure all pre-requisites are met.
 
#2 ► Recovery point vs archive deletion 
Sometimes it is not obvious for Partners who just started using the service what is the difference between deleting a recovery point and deleting an archive. Let's compare both operations and how to perform them.
Deletion of a recovery point means you delete a single backup from backup's chain. Others just stay in place intact.  To delete a recovery point, choose the archive you want to remove backups from and click (x) icon under particular recovery point. Please check step-by-step instruction.

Opposite to that, whenever one is intended to remove an entire archive, the entire backup chain is being deleted. That means once the entire archive is erased, there is no way to recover any items from that. Archive's deletion is irreversible! To perform the removal navigate to BACKUPS tab, choose the archive(s) you'd like to delete and click (x) icon to the right:

 
#3 ► Cloud storage usage under Backup console differs from usage under Account management console
A common scenario:
Some backup is finished successfully
Cloud storage usage under Backup console is updated according to the amount of data transferred to Cloud during backup.
You switch to Account console and see that Cloud storage usage value is different from the numbers you saw at Backup console.
The root cause of such behavior is the mechanism of Cloud space usage recalculation. The algorithm that gathers statistics is a cyclic one, therefore the usage is not updated immediately after some changes happened, but with a small delay. Overall Acronis guarantees that Cloud space usage will be updated within 8 hours since the moment when the value of Cloud storage has been changed.
Also, you may refer to the following article describing other possible reasons of Cloud storage space usage discrepancy.
 
  Did you know that we've just introduced a new support channel for Service Providers - Live chat:

To submit a support request via chat:
Log in to your Acronis Account or create a new one if you haven't registered yet   https://kb.acronis.com/regacc 
On the Support tab select Support for Service Providers https://www.acronis.com/en-us/support/contact-us/ 
Select Technical issue
Select the product you are using and click Chat now to start the live chat 
New KB articles
 
Acronis Backup Cloud
KB62659: Acronis Data Cloud: downgrading APS package 
KB62640: Acronis Backup: Backup fails with "The specified file does not exist" 
KB62636: Acronis Backup: backups in Version 11 format write excessive .meta files to temp 
KB62621: Acronis Backup: multiple 'Event 81' messages in Windows Event logs on Windows Server 2019 with Hyper-V 
KB62618: Acronis Backup Cloud: logging in to Web Restore fails with "504 Gateway Time-out" for large accounts 
KB62607: Acronis Data Cloud: migration from US2 to US6 data center 
KB62576: Acronis Backup Cloud: Live update does not start 
KB62569: Acronis Backup: device does not appear in backup management console after installation 
KB62559: Acronis Backup: Linux bootable media fails with "Kernel panic - VFS: Unable to mount root fs on unknow-block(1,0)" 
KB62556: Acronis Backup plugin for WHM & cPanel: backup fails with "Internal error: record is greater then 32K" 
KB62554: Acronis Backup Cloud: notifications for Office 365 backups are not available 
KB62552: Acronis Backup: hidden partitions become visible after installing Acronis Agent in macOS 
KB62539: Acronis Backup Cloud: backup hangs at 0% 
 
Acronis Software-Defined Infrastructure
KB62408: Acronis Software-Defined Infrastructure: registration of Storage SPLA fails with "Internal Server Error"
KB62294: Acronis Storage: properly configuring network connections before upgrading to Acronis Software-Defined Infrastructure 2.5
 
Acronis Software-Defined Infrastructure Appliance
KB62326: Acronis SDI Appliance country availability
KB62324: Acronis SDI Appliance licensing
 
Acronis Files Cloud
KB62645: Acronis Files Cloud: integration with Office Online
KB62567: Acronis Files Cloud: Guest user account type
KB62412: Acronis Files Cloud: how to collect Client logs
 
See all new KB articles here: https://kb.acronis.com/new
 
New training materials
Acronis plugin for CW Automate - new video tutorials:
How to Install and Configure the Acronis Data Cloud Plugin for ConnectWise Automate
How to Use the Acronis Data Cloud Plugin for ConnectWise Automate
 
 All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.12420)
Backup Agent for Mac (v.12.5.12420)
Backup Agent for Linux (v.12.5.12420)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.8 Update 2


Backup
File Sync&Share


Strasbourg (EU1)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
File Sync&Share
Physical Data Shipping


Frankfurt (EU2)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


London (EU3)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Zurich (EU5)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US2)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US5)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Nagano (JP1)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Singapore (SG1)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share


Sydney (AU1)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share


Moscow (RU2)


7.8 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0

 
Release notes and documentation
Acronis Data Cloud 7.8 Update 2 release notes 
Acronis Backup plugin for WHM & cPanel
Acronis Backup Cloud APS 2.0 Update 14 (2.2-2052) Release Notes
Acronis iOS Files Cloud Release 8.2.5

      
                                            
                
            
                            
                    
                        
                            
                              Thu, 04/11/2019 - 07:46

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
