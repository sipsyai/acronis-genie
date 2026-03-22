# Support Digest: November 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-november-2018

## Original Post
**Author:** Unknown

Support Digest: November 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
We are ready to present the latest edition of Support digest for service providers – November, 2018! During the past month Acronis Data centers have been updated to Acronis Data Cloud 7.8 Update 1 that brought several improvements and brand new features to the platform. Let’s review the most important ones and also cover the most common questions that were asked by Partners in November.
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
 
Hot topics
#1 ► Google/Azure storage support
One of the most exciting new Acronis Data Cloud’s features is native support of Microsoft Azure and Google Cloud storages. From now on, apart from storing your customers’ data at Acronis Cloud Storage, you can also choose to save it at Microsoft or Google datacenters. This does not mean Acronis Datacenter storages are not good enough: they are the best storages, designed for use exclusively with Acronis backup solutions. Still there might be cases when one cloud storage option is just not enough – for compliance reasons, certification requirements, data sovereignty laws, connectivity issues, or internal policies. That’s where Azure and Google storages come to aid.  Among the benefits are:
Store data remotely with greater choice of worldwide data centers
Control data locations with flexible storage options
Attract millions of customers who already use Google/Azure Cloud Platform
Employ secure AES-256 data encryption at-rest and using strong SSL-encrypted channels in transit
and many others.
  Assignment of Google/Azure storage is possible to newly created customer groups by default.
If you want to change Cloud storage for existing group from Acronis DC to Google/Azure, you will first have to remove existing cloud backups for this group and ensure that Cloud usage is zeroed In Account Management console as shown on the screenshot . Migration of backups is currently not supported (thought is stays on our roadmap).

 
#2 ► Archive browsing questions
Backup Management console of Acronis Data Cloud allows live browsing of the backed up data, regardless of its location: it can be Cloud storage, a network share or a local disk. Backups for all devices can be found under BACKUPS tab. The general prerequisites for archives browsing at Backup Management console are the following:
There should be at least one machine with Acronis Backup Cloud agent installed 
Machine with agent should be online
Machine with agent should be registered under the same customer user as the ones the backups belong to. It is impossible to browse backups belonging to User A with agent machine registered under User B.
It is always recommended to use latest version of backup agent to browse backups: it is possible that legacy agent won’t be able to browse backups made by modern versions.
Apart from the ones above, there are some more prerequisites in specific cases:
Browsing backup of particular application backup (MS Exchange/MS SQL/Office 365) is possible only in case using a machine with respective agent installed (Acronis Backup Cloud Agent for Exchange/Agent for SQL/Agent for Office 365)
The dialogue that allows to choose the agent you are going to browse backups from can be found at the top of the screen under BACKUPS tab:

 
#3 ► Notifications settings
Every cloud service in Acronis Data Cloud has its own notification settings, and you have to be specific when you decide what and how you want to be notified of. Here are the ground rules:
Notifications from Management Portal and Backup Service are enabled in the Management Portal. Modify user account settings to manage notifications.
Branding notifications is part of Management Portal functionality, and applies to underlying partners and customers, but not to immediate users of the partner group where branding is configured. See more here.
To send notifications to multiple addresses, create multiple users with different emails, or a user with an alias (a distribution list) where you can include multiple recipients. Partner users will receive business and backup notifications for all underlying partners and customers
Business notifications are sent when quota is exceeded.
Maintenance notifications: announcements about upcoming updates of Acronis Data center infrastructure sent by Acronis Data center Monitoring team updates Check here how to subscribe to management notifications. 
Backup notifications are sent immediately after a backup activity finishes
Daily recap emails are sent once a day (at 10:00 am local DC time) and include only alerts that are currently active in the Backup Console. If there are no problems by this moment, the recap is not sent
In case you don't receive a business or backup notification, check that you enabled correct level and specified the right address. See more in KB49778
Notifications from Files Cloud are managed in Files Cloud Administrators console. See more here
 
New KB articles
Acronis Backup Cloud
KB62133: Acronis Backup Cloud: Warning "The 'Full Disk Access' permission was not granted to the app"
KB62013: Acronis Data Cloud: space usage report in CSV format contains unnecessary info
Acronis Storage
KB62017: Acronis Storage: update of storage certificate fails with "Can't read a response: gzip: invalid header"
See all new KB articles here: https://kb.acronis.com/new
 
New training materials
Acronis has just produced three new video guides as a part of the Acronis Data Cloud Technical Training series to help our partners and their customers get familiar with the Office 365 backup and recovery operations for Acronis Data Cloud and Acronis Backup 12.5 Cloud Deployment.
How to Backup & Recover Corporate Office 365 Mailboxes
How to Backup & Recover Users' OneDrive for Business
How to Backup & Recover Office 365 SharePoint Sites
 
  Want to participate in a live Acronis Data Cloud training? Check the schedule of upcoming webinars and sign up for the suitable date: https://kb.acronis.com/MSPtraining
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.12210)
Backup Agent for Mac (v.12.5.12210)
Backup Agent for Linux (v.12.5.12210)
 

Datacenter


Platform version


Available services

 

Strasbourg (BETA)


7.8 Update 1


Backup
File Sync&Share

 

St. Luis (BETA2)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping 


 
 



Strasbourg (EU1)


7.8 Update 1


Backup
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping 


 
 



Frankfurt (EU2)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping


 
 



London (EU3)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping


 
 



Lupfig(EU5)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


 
 
 


Ashburn (US2)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping


 
 



Ashburn (US5)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping


 
 



Nagano (JP1)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0
Physical Data Shipping


 
 



Singapore (SG1)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0

 

Sydney (AU1)


7.8 Update 1


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0

 

Moscow (RU2)


7.8 Update 1


Backup
O365 Cloud-To-Cloud 2.0

 
 
Release notes and documentation
Acronis Data Cloud 7.8 release notes 
Acronis Backup Cloud v 7.8 User Guide

      
                                            
                
            
                            
                    
                        
                            
                              Fri, 12/14/2018 - 19:31

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
