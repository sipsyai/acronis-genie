# Support Digest: September 2017

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-september-2017

## Original Post
**Author:** Unknown

Support Digest: September 2017

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
In September we had a number of new product features and updates that brought a lot of questions. The biggest change is the new Acronis Data Cloud 7.5, which now supports multiple cloud services, and Acronis Backup Cloud becomes one of them. Let's go one by one through most popular questions and new materials to get you ready for support in October:
Hot topics
New KB articles
New training materials
New features
Datacenter and agent updates
Release notes
 
Hot topics
Here are the top 3 questions regarding Acronis Data Cloud in September:
  #1 ► New Management Portal is totally different from the previous version. Where to start?
Management Portal in Acronis Data Cloud 7.5 replaces the Account Management Console of Acronis Backup Cloud. Get familiar with the UI changes and new features to be prepared:
All changes in UI layout and functionality are explained in detail in KB60464
New documentation is available on our support page
Full list of changes and new features is available in the release notes
API v.1 is fully supported in new Management Portal. New features are available with API v.2. See more in KB60486
  #2 ► How do I get through with notifications setup: branding, multiple email addresses, correct level of information etc.?
Every cloud service in Acronis Data Cloud has its own notification settings, and you have to be specific when you decide what and how you want to be notified of. Here are the ground rules:
Notifications from Management Portal and Backup Service are enabled in the Management Portal. Modify user account settings to manage notifications
Branding notifications is part of Management Portal functionality, and applies to underlying partners and customers, but not to immediate users of the partner group where branding is configured. See more here
To send notifications to multiple addresses, create multiple users with different emails, or a user with an alias (a distribution list) where you can include multiple recipients. Partner users will receive business and backup notifications for all underlying partners and customers
Business notifications are sent when quota is exceeded or when datacenter maintenance is planned
Backup notifications are sent immediately after a backup activity finishes
Daily recap emails are sent once a day (at 10:00 am local DC time) and include only alerts that are currently active in the Backup Console. If there are no problems by this moment, the recap is not sent
In case you don't receive a business or backup notification, check that you enabled correct level and specified the right address. See more in KB49778
Notifications from Files Cloud are managed in Files Cloud Administrators console. See more here
  #3 ► I understand how quotas work. But how do I actually delete backups when I need to free up some space? What if I only delete a backup plan?
Backup plan is only a setting that defines how, where and how often backups are created and how they are retained. When it comes to actually deleting backups, here is what you need to know:
Deleting a backup plan will not remove backups. See more about backup plans here
Deleting a machine from backup console or uninstalling the agent software will not remove backups. See more about deleting machine here
Automatic retention of backups runs as part of the backup plan and is unique for every location. See more about retention rules here
To delete one recovery point, select the Device > Recover > click on Recycle. This will not free up space in the cloud storage or in Always-incremental archive
To delete the entire archive, go to Backups > select the location > select the group name by Machine and Plan name > Delete. See more on how to delete backups here
To free up Cloud Storage space, remove incomplete backups or delete the entire archive from Backups tab or Web Restore console
Deleting the user account will remove all backups from Cloud Storage. Local backups will not be affected
 
New KB articles
Acronis Data Cloud
KB60464: Acronis Data Cloud: Management portal changes in version 7.5
Acronis Backup Cloud
KB60265: Acronis Backup Cloud: browsing a 1TB+ GPT partition in cloud backup fails with "Server is not available at the moment"
KB60241: Acronis Backup Cloud: Backup of SQL instance fails with "There are no SQL writers"
KB60216: Acronis Backup Cloud: backup of Hyper-V VM fails with "Failed to obtain an instance of service class 'Msvm_VirtualSystemManagementService"
KB60157: Acronis Backup Cloud: "GXT: The item provider has skipped the report of an item with key" error
KB60443: Acronis Backup: you receive "Quota exceeded" error, but do not use cloud storage
KB60311: Acronis Backup: "Resource quota exceeded" alert
KB60309: Acronis Backup: "Backup failed" alert
KB60264: Acronis Backup: backup fails with "WMI 'ExecQuery' failed"
KB60253: Acronis Backup: recovery of a Windows Server 2008 hangs at 88%
KB60226: Acronis Backup: backup fails with "The shadow copy provider had an unexpected error"
Acronis Storage
KB60214: Acronis Storage Gateway: Data migration to Acronis Storage 2.x
KB60331: Acronis Storage: "Free storage space check result: -5 (No space/quota exceeded while local file io)" error
KB60223: Acronis Storage and Acronis Storage Gateway: how to clear FES address from Agent's cache
Acronis Backup Advanced for vCloud
KB60261: Acronis Backup Advanced for vCloud: how to improve vCDA web console's performance
KB60258: Acronis Backup Advanced for vCloud: attempt to log in to vCDA fails with "Credentials are incorrect" error if you have vCloud Director v 8.2
KB60244: Acronis Backup Advanced for vCloud: how to change time zone on vCDA
See all new KB articles here: https://kb.acronis.com/new
 Did you know that most Frequently Asked Questions on Acronis Backup Cloud are already covered in one single place? Follow this link to find more: https://kb.acronis.com/content/49028

 
New training materials
Acronis Data Cloud in Acronis Backup Cloud Product Training
Active Protection in Acronis Backup Cloud Product Training
Acronis Files Cloud - coming soon!
See all training materials here: https://kb.acronis.com/MSPtraining
 Did you know that during support technical webinar you can actually try how product works and experience the support process? Attend one of our webinars and become a skilled support professional for Acronis Cloud Products!

 
New features
Acronis Data Cloud
Fully redesigned user interface
Improved reporting functionality
Average usage calculation mode (can be set through API)
Offering items—an improved and extended version of the quotas existing in Acronis Backup Cloud 7.0 
Integration with Autotask PSA. Provisioning, tickets, quota setup
Removed features:
The Pricing parameters section was removed from the user interface.
The Agent auto update switch was removed from the user interface.
File Sync&Share service
Acronis Files Cloud integration with the Cloud Platform
Office Online web editing integration
Multi-select in the web UI
Sharing of File Sync & Share nested subfolders
Syncing of subfolders
Backup Service
Active Protection. Protects your data from ransomware and other threats. This feature is available only in Agent for Windows. Learn more about it in KB60452
Acronis Asign. Allows a backed-up file to be signed by several people
O365 cloud-to-cloud. Backup of Microsoft Office 365 mailboxes without the need to install Agent for Office365 on premises
VMware vSphere 6.5 support
Multiple selection of backup agents for update
 Did you know that to enable Active Protection you must make sure you update the agent to the latest build (12.0.4290).

 
Datacenter and agent updates
Current agent version: 12.0.4290

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.5


Backup Service, Files Service


St. Luis (BETA2)


7.5


Backup Service, Files Service


Strasbourg (EU1)


7.5


Backup Service


Frankfurt (EU2)


7.5


Backup Service


London (EU3)


7.5


Backup Service, Files Service


Frankfurt (EU4)


7.5


Backup Service


Zurich (EU5)


7.5


Backup Service


Ashburn (US2)


7.5


Backup Service


Ashburn (US5)


7.5


Backup Service, Files Service


Nagano (JP1)


7.5


Backup Service


Singapore (SG1)


7.5


Backup Service


Sidney (AU1)


7.5


Backup Service


Moscow (RU2)


7.5


Backup Service

 
Release notes:
Acronis Data Cloud 7.5
 
Share your experience!
What do you think about new Acronis Data Cloud interface, did you have any issues working with it?
Did Acronis Active Protection already save your data from ransomware?
Share below your experience and your questions.

      
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/06/2017 - 09:37

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
