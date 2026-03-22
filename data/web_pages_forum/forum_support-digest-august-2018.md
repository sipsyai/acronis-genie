# Support Digest: August 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-august-2018-0

## Original Post
**Author:** Unknown

Support Digest: August 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
I'm happy to present the latest issue of MSP Support digest. In August, we've published Update 2 for Acronis Data Cloud 7.7 platform. With this update, the Acronis flagship cloud product offers enhancements and addresses the issues found in the previous releases. Apart from that, plugins for several cloud integration systems (WHM, cPanel, ConnectWise Automate) have also been updated.
Hot topics
New KB articles
Datacenter and agent updates
Release notes and documentation
Hot topics
As usual, in August we've reviewed all questions coming from Partners and prepared answers for 3 most common ones. Let's go through the questions and answers for them:
#1 ► Acronis Data Cloud maintenance impact and notifications
Each maintenance event that concerns Acronis Data Cloud platform, is being preceded by notification sent by Data center Monitoring team. Partner administrators can subscribe to those distributions by marking the "Maintenance notifications" checkbox under their account's settings. If the option is not visible, it's necessary to contact your reseller to have the notifications forwarded. Depending on upcoming maintenance type notification is being sent proactively. The table below shows dependence between email dispatch time and maintenance type:
Event type
Notification time
Major release
1 week before release
Minor release
2 weeks before release
Hotfix
1 day (minimum) before release
 
The possible impact of each maintenance is always specified under the notification text. Some specific components may be unavailable during the time while works are in progress. In general, backup and recovery operations stay intact regardless of event type.
 
#2 ► Application-aware backup
Acronis Backup Cloud provides 2 ways how Windows application (Exchange, SQL, Active Directory) can be protected:
database backup
using application-aware backup
Unlike simple entire machine or disk-level backup, application aware backup guarantees that applications are backed up in a consistent state and thus will be available immediately after the machine is recovered. This is achieved by backup of transaction log belonging to protected applications. Application aware backup allows to recover specific application items (SQL databases, Exchange databases, Exchange mailboxes) from entire machine backup.
Once application backup option is turned on, it's necessary to choose the applications that are needed to be protected and specify credentials for users who have required privileges for accessing the respective applications (see more).
In case some application is planned to be protected using application-aware backup, it's necessary to install the respective Acronis Backup Cloud agent inside the machine running application (Agent for AD/SQL/Exchange). If application is installed on a VMware virtual machine and application-aware backup is performed using Agent for VMware (agentless backup), it is not required to install Agent for AD/SQL/Exchange installed inside the VM.
Note: Application-aware disk-level backup is available for physical machines and for ESXi virtual machines.
  Interested in monitoring backup statuses for all your customers in a single place?  Click here to know more about dashboards. 
 
#3 ►Acronis Data Cloud API
Many Partners are interested in integrating Acronis Data Cloud into their own management and provisioning systems. Such operation can be achieved using API - application programming interface. Currently Acronis Data Cloud introduces 2 versions of API:
Version 1: Legacy API for basic account management operations
Version 2: New API for full functionality of Management portal
Detailed documentation for both versions is available under Acronis Data Cloud in Integrations tab under Settings menu. It can also be accessed directly after opening any of the links below:
https://[dc]-cloud.acronis.com/api/1/doc
https://[dc]-cloud.acronis.com/api/2/doc
where [DC] is the name of particular data center your organization belongs to. E.g. if your partner group belongs to EU2 data center, the URL will look like this: https://eu2-cloud.acronis.com/api/1/doc. Note that in order to access the page it's necessary to be logged in to Acronis Data Cloud (it is usually done in a separate tab of your web browser.)
Additional information regarding integration for certain business systems is available here.
 
 We are happy to introduce new form for contacting Support Team.
     https://support.acronis.com/msp/submit-ticket
Please use the following form to submit your request to MSP Support Team. Providing the full issue description will help us assist you faster.
 
New KB articles
Acronis Backup Cloud

KB 61698: Acronis Backup Cloud: backup fails with "Internal error: An expression test has failed"
 
 
KB 61674: Acronis Backup Cloud: "The storage quota is exceeded. Further backups will fail." error
 
 
KB 61668: Acronis Backup Cloud: local storage usage calculation
 
 
KB 61650: Acronis Backup Cloud: "The activity has failed due to a restart of the service" error
 
 
KB 61648: Acronis Backup Cloud Integration with ConnectWise Automate: alerts and ticket creation frequency
 
 
KB 61628: Acronis Backup: activities of host-level backup plans are not shown for protected VM
 
 

See all new KB articles here: https://kb.acronis.com/new
 Did you know that in order to become Acronis certified service provider it's necessary to pass the respective certification exam? Find the list of exams for all MSP products at https://kb.acronis.com/MSPtraining
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.10330)
Backup Agent for Mac (v.12.5.10330)
Backup Agent for Linux (v.12.5.10330)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.8


Backup
File Sync&Share


St. Louis (BETA2)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.7 Update 2


Backup


Frankfurt (EU2)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.7 Update 2


Backup


Zurich (EU5)


7.7 Update 2


Backup


Ashburn (US2)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share


Ashburn (US5)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.7 Update 2


Backup
Disaster Recovery
File Sync&Share


Singapore (SG1)


7.7 Update 2


Backup


Sidney (AU1)


7.7 Update 2


Backup


Moscow (RU2)


7.7 Update 2


Backup

 
Release notes and documentation
Acronis Data Cloud 7.7 Update 2 release notes 
Acronis Data Cloud ConnectWise Automate integration Update 4 (Integration guide)
Acronis Data Cloud WHM & cPanel integration Update 1 HF1 (Integration guide)

      
                                            
                
            
                            
                    
                        
                            
                              Wed, 09/12/2018 - 19:40

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
