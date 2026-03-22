# Support Digest: July 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-july-2018

## Original Post
**Author:** Unknown

Support Digest: July 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
This July we’ve released Update 1 for Acronis Data Cloud server platform which brought several new features (audit logging, security enhancements). Several cloud integration systems (Plesk, cPanel, Autotask, ConnectWise Manage) have also been updated in order to expand their functionality and improve user experience. Apart from that, a new version of backup agent software (12.5.10330) has been published.
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
Most common questions asked by partners in July were related to new functionality introduced in Acronis Data Cloud 7.7 Update 1 and possible ways of managing quotas for Customers.
#1 ► Customer group and user quotas 
Quotas can be set either when a group/user account is created, or else they can be adjusted later, if necessary. Account management console allows to set independent quotas for any offering items both for Customer group level and for each user account belonging to this Customer. One of the main purposes for that is the fact that a single Customer group may contain more than 1 user account and thus, there should be an easy way to manage the combined number of resources allocated for those accounts. Still, even though the quotas for users and their group can be placed independently, combined actual usage for any particular offering item for all users cannot exceed total quota allocated for this offering item on Customer group level.
Example #1: “Customer group A” contains 2 user account: “user A” and “user B”. 
We set “Cloud storage” quota for “Customer group A” at 100 GB.
Then we set “Cloud storage” quota for “user A” at 500 GB and for “user B” at 300 GB.
In this example quotas for user accounts is bigger than quota for Customer group itself. 
However, neither “user A”, nor “user B” can back up to Cloud more than 100 GB combined (quota set on Customer group level). So either “user A” saves 100 GB and “user B” saves 0 GB, or “user A” saves 30 GB and “user B” saves 70 GB, or “user A” saves 10 GB and “user B” saves 90 GB.
Same applies to any other offering items.
In case quota for some is almost reached or exceeded, Acronis Backup Cloud will clearly indicate the name of respective offering item and customer group/user account whose quota belongs to. In case some quota for customer group is exceeded, adjusting quota for user account won’t help (and vice versa).
Interested in options to deal with quota’s overuse? Click here for instructions.
 
#2 ►File filters
One of the most useful ways to decrease the size of backup archive is to set file filters under backup plan’s options when creating the task. Excluding the unwanted types of data will not only help to make your archives smaller but also speed up backup’s performance and save your money due to lower cloud space consumption. You can either choose to include some specific folders/files from source machine into backup (thus excluding everything else), or exclude some folders/files (therefore, everything BUT those items will be backed up.)
Example #2: We’d like to back up entire Windows machine, except for D: partition. In this case we set the filters the following way: 
Do not back up files matching the following criteria: D:\*
Example #3: We’d like to back up only configuration files located on Linux machine in /usr/lib/config/ folder. In this case we set the filters the following way
Back up only files matching the following criteria: /usr/lib/config/*
Check the following article for complete description of the file filter setting.
 
#3 ►Audit logs
The events initiated by a user of the system itself within Account Management Portal are now tracked and logged: what, when, where and who is an initiator. The following events are currently included (Management portal):
Service events (example: File Sync&Share service was enabled for partner)
Offering item events (add, delete, update, etc)
Infrastructure components events (example: Storage was added)
Quota events (delete, update, etc)
Tenant events (add, delete, update, etc)
User events (add, delete, update, etc)
Current limitations:
Log-in event does not have IP addresses info
Password change event is not traced
No info about unsuccessful logins
Each audit log’s field is described under this page.
New KB articles
Acronis Backup Cloud

 
KB61633: Acronis Backup Cloud: Linux Agent does not detect 'Version 12' backups 
KB61577: Acronis Backup Cloud: Random symbols in WHMCS module 
KB61575: Acronis Backup Cloud: APS Package update pre-check tools 
KB61570: Acronis Backup Cloud: local storage usage is not recalculated after deleting archives 
KB61551: Acronis Data Cloud: how to reset credentials for SQL/Exchange 
KB61548: Acronis Backup Products: Warning "Error: There is a double slash in the path" 
KB61535: Acronis Backup Cloud: Status, last backup & next backup fields are displayed incorrectly for Application backup 
KB61534: Acronis Backup Cloud: backup sporadically fails with "Can't connect to the mailbox of user Mailbox database guid" 
KB61531: Acronis Backup Products: Slow detection of some USB drives 
KB61520: Acronis Backup Cloud: backup finishes with warning "Assertion failed: node->Prev == 0 && node != Head && node->Next == 0" 
KB61517: Acronis Backup Cloud: backup fails with "One or more machines are not assigned a license" or "Functionality 'XX' is not available. Please use the appropriate license." 

See all new KB articles here: https://kb.acronis.com/new
New training materials
Acronis Data Cloud v.7.8: What’s new
Acronis Backup Cloud v.7.8: Product training
Acronis Backup Cloud v.7.8: Troubleshooting training
Acronis Backup Cloud v.7.8: Certification exam
Training and certification materials for all MSP products can be found at: https://kb.acronis.com/MSPtraining
Did you know that Acronis Certified MSP partners’ revenue is 30% higher compared to non-certified ones? Pass the certification now and become certified: https://www.surveygizmo.com/s3/4306181/Service-Provider-Certification-Exam-Acronis-Backup-Cloud-v-7-7 
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.10330)
Backup Agent for Mac (v.12.5.10330)
Backup Agent for Linux (v.12.5.10330)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.7 Update 1


Backup
File Sync&Share


St. Louis (BETA2)


7.7 Update 1


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.7 Update 1


Backup


Frankfurt (EU2)


7.7 Update 1


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.7 Update 1


Backup


Zurich (EU5)


7.7 Update 1


Backup


Ashburn (US2)


7.7 Update 1


Backup
Disaster Recovery
File Sync&Share


Ashburn (US5)


7.7 Update 1


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.7 Update 1


Backup
Disaster Recovery
File Sync&Share


Singapore (SG1)


7.7 Update 1


Backup


Sidney (AU1)


7.7 Update 1


Backup


Moscow (RU2)


7.7 Update 1


Backup

 
Release notes and documentation
Acronis Data Cloud 7.7 Update 1 release notes 
Acronis Backup Cloud v 7.7 User Guide
Acronis Backup Cloud APS Update 13 (2.2-1994 ) Release Notes
Acronis Data Cloud ConnectWise Manage integration Update 2 (Integration guide)
Acronis Data Cloud Autotask PSA integration Update 1 HF1 (Integration guide)

      
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/10/2018 - 21:14

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
