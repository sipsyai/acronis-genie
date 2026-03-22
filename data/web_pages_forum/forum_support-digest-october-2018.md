# Support Digest: October 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-october-2018

## Original Post
**Author:** Unknown

Support Digest: October 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
This October was full of exciting news: we’ve rolled out new version of Acronis Data Cloud platform – v.7.8 – across all Acronis data centers. Latest release introduces several brand new Cloud services and also brings multiple improvements to existing ones that guarantees exciting experience both at Partner and end-user levels. 
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
Major part of the questions coming from the Partners this October were related to new functionality and changes to the platform delivered in v.7.8. Let’s discuss three most common of them.
#1 ►Office 365 data backup overview
Even though Microsoft Office 365 is a set of cloud services, regular backups provide an additional layer of protection from user errors and intentional malicious actions. You can recover deleted items from a backup even after the Office 365 retention period has expired. Also, you can keep a local copy of the Exchange Online mailboxes if it is required for regulatory compliance. The cloud agent synchronizes with Office 365 every 24 hours, starting from the moment when the organization is added to the backup service. If you add or remove a user, group, or site, you will not see this change in the backup console immediately. See more how to protect specific items of Exchange Online, SharePoint online or OneDrive here.
#2 ► Cloud-to-Cloud agent v.2 versus v.1 comparison
Acronis Data Cloud 7.8 allows to protect entire Office 365 infrastructure using the brand new cloud-to-cloud agent v.2 (C2C 2.0). It is a cloud-based agent that belongs to Acronis data centers infrastructure and designed especially for protecting Office 365 environment. Unlike previous version of Acronis Backup Cloud where the legacy version of agent - C2C 1.0 - allowed to protect Office 365 mailboxes only, C2C 2.0 introduces the possibility to protect entire Office 365 seat: Exchange Online, OneDrive and SharePoint online. 
 If you’ve never used Microsoft Office 365 backup functionality yet, C2C 2.0 will be automatically deployed once you decide to start.  In case you’ve been protecting Office 365 mailboxes already (either using locally installed agent or C2C 1.0), you can follow the instructions from this article to update your legacy Agent for Office 365 to C2C 2.0.
 
#3 ►Changes & improvements of local usage calculation
Acronis Development team is constantly working on improving backup service. Our top priority is to make sure our partners are totally satisfied with the solution’s functionality. Here are the latest changes to the mechanism of calculation of local backups’ size:
Occupied local storage is now calculated every 4 hours
Local storage used on clustered environments (ESXi, Hyper-V) is now included into calculation
If local backup(s) was deleted directly from file system, it is now possible to force recalculation manually clicking Refresh button in Backups tab.
All deletion operations are tracked in Activities tab with details about the size of data at the deletion time and the initiator of this operation
Removable drives are considered as local drives, so as result they will be included into local usage calculation
If Physical Data Shipping was enabled under plan’s options, the local backup created at “Initial seeding” path won’t be counted as local backup.
All the actual information along with the latest changes to the local usage calculation is described in the respective KB article.
The options to disable local backup offering (and, thus, possibility to save backups locally) is described here. 
 
New Acronis Backup Cloud KB articles
 
How to's:
KB61859: Acronis Backup: how to disable VDDK transports on agent 
KB61825: Acronis Backup Cloud: how to use acrocmd on a Mac 
KB61925: Acronis Backup: VM annotation - how to see Backup status in vCenter 
KB61993: Acronis Backup Cloud: how to upgrade to the new cloud-to-cloud Office 365 backup in version 7.8 
KB61980: Acronis Backup Cloud: how to disable local backup offering item 
Solution for technical questions
KB61937: Acronis Data Cloud services availability by data center 
KB61930: Acronis Backup: ESXi configuration backup fails with "too many SQL variables" or "Command definition 'SELECT ...' not found." 
KB61900: Acronis Backup: Hyper-V virtual machine backup produces warning "Changed Block Tracking (CBT) is not used because there are disk files that do not belong to any disk snapshot." 
KB61809: Acronis Backup Cloud: Time settings on the Acronis Storage cause miscommunication with Agents 
KB61805: Acronis Backup Cloud: Manual registration fails with "Couldn't connect to host at localhost:43234" 
KB61908: Acronis Backup Cloud: backup fails with "The network path was not found" or "Cannot connect to the machine where network share ' path' is located" 
KB61913: Acronis Backup Cloud: backup fails with "Failed to resolve hostname" 
KB61714: Acronis Backup: backup fails with "VSS writer 'System Writer' with class ID 'E8132975-6F93-4464-A53E-1050253AE220' has timed out" error 
KB61698: Acronis Backup: backup fails with "Internal error: An expression test has failed" 
KB61674: Acronis Backup Cloud: "The storage quota is exceeded. Further backups will fail." error 
KB61668: Acronis Backup Cloud: local storage usage calculation 
KB61967: Acronis Backup Integration with Plesk/cPanel: plugin fails with "An error had occurred" error 
KB61650: Acronis Backup: "The activity has failed due to a restart of the service" error 
KB61648: Acronis Backup Cloud Integration with ConnectWise Automate: alerts and ticket creation frequency
See all new KB articles here: https://kb.acronis.com/new
New training materials
Acronis Backup Cloud v.7.8: Product training 
Acronis Backup Cloud v.7.8: Troubleshooting training 
Acronis Data Cloud: What’s new in v.7.8
New certification exams:
Acronis Backup Cloud v.7.8 Certification Exam 
Training and certification materials for all MSP products can be found at: https://kb.acronis.com/MSPtraining
 Did you know that Acronis Certified MSP partners’ revenue is 30% higher compared to non-certified ones? Pass the certification now and become certified: https://www.surveygizmo.com/s3/4608450/Service-Provider-Certification-E…
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.12110)
Backup Agent for Mac (v.12.5.12110)
Backup Agent for Linux (v.12.5.12110)
 

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


Strasbourg (EU1)


7.8


Backup
File Sync&Share
O365 Cloud-To-Cloud 2.0


Frankfurt (EU2)


7.8


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


London (EU3)


7.8


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


Zurich (EU5)


7.8


Backup
O365 Cloud-To-Cloud 2.0


Ashburn (US2)


7.8


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


Ashburn (US5)


7.8


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


Nagano (JP1)


7.8


Backup
Disaster Recovery
File Sync&Share
O365 Cloud-To-Cloud 2.0


Singapore (SG1)


7.8 Update 1


Backup
File Sync&Share
O365 Cloud-To-Cloud 2.0
Disaster Recovery


Sidney (AU1)


7.8


Backup
File Sync&Share
O365 Cloud-To-Cloud 2.0
Disaster Recovery


Moscow (RU2)


7.8 Update 1


Backup
O365 Cloud-To-Cloud 2.0

 
You can also check the services availability under the following KB article.
 
 
Release notes and documentation
Acronis Data Cloud 7.8 release notes 
Acronis Backup Cloud v 7.8 User Guide
Acronis Backup plugin for WHM & cPanel (build 219)
Acronis Files Cloud iOS agent new release

      
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/14/2018 - 17:26

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
