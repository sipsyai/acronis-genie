# Support Digest: December 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-december-2018

## Original Post
**Author:** Unknown

Support Digest: December 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
Allow me to introduce you to the latest edition of Acronis Digest for Service Providers – December, 2018. 
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
As usual, we’re reviewing the frequently asked questions coming from Partners during past month. Below are the most common topics.
#1 ► Migration of backups between Acronis data centers and partner-hosted storage
This one is quite a popular question among the Partners. There might be various reasons for such request, like security law regulations, privacy policy, lowering expenses etc. 
Though current version of Acronis Data Cloud platform neither provides native tools for moving backups from partner storage to Acronis data center, nor vice versa, still the procedure is possible. In order to organize the process it is recommended to involve Acronis Professional Services team, who will make all necessary preparations and overlook the process. If you are interested in pricing for Professional Services, please contact your Acronis sales representative.
The possibility to move data between partner-hosted and Acronis data center storages without Professional Services involvement is going to be added in the next major release of Acronis Data Cloud – v. 8.0 – which is planned on second half of year 2019.
 
#2 ► Download option availability under Backup Console 
As it was explained in one of the previous digests, Recover option is preferred over Download due to mechanics of Download process (vulnerability to connection interruptions). For better user experience, we’ve limited the possibility to download files larger than 100 MB using Download option in the most recent update of Acronis Data Cloud’s server side.

Acronis' recommendation is to use Download option only when the goal is to recover not more than 100 MB of data. For other cases, use Recover option.

#3 ► Cloud space usage is not  decreased after deleting recovery point, why?
To understand how quotas work, it's necessary to remember about cloud backup technology. Here are the most important notes:
When you remove a recovery point, cloud archive size remains the same, unless it contained unique data which is not present under other recovery points
Cloud console will show updated cloud storage space after 8 hours: KB59979
Incomplete cloud backups are not deleted automatically. If you know that some incomplete backups are not needed, you can delete them manually as explained in KB59015
When agent quota is exceeded, the agent download link disappears from the web console. See more here: KB57328
 
New KB articles
Acronis Backup Cloud
KB62202: Acronis Backup: backup fails "Selected network files or network folders were not found"
KB62177: Acronis Backup, Acronis Backup Cloud: backup fails with "no disk space or quota" 
KB62176: Acronis Backup: how to set up a limited vSphere account
Acronis Storage
KB62182: Third-party software used in Acronis Storage
Acronis Files Cloud
KB62149: Acronis Files Cloud: how to transfer files from version 7.5.4 to 7.8+
 
See all new KB articles here: https://kb.acronis.com/new
 
New training materials
Acronis has just produced three new video guides as a part of the Acronis Data Cloud Technical Training series to help our partners and their customers get familiar with the Acronis Files Cloud. These video guides focus on the major Acronis Files Cloud business processes from the viewpoint of a Customer.
Acronis Files Cloud: Web-based Version
Acronis Files Cloud: Desktop Client
Acronis Files Cloud: Mobile Client
Also, we’ve published the localized training materials related to Acronis Backup Cloud v.7.8:
Acronis Backup Cloud 7.8: Product training – Presentation (German)
Acronis Backup Cloud 7.8: Product training – Presentation (Spanish)
Acronis Backup Cloud 7.8: Product training – Presentation (French)
Acronis Backup Cloud 7.8: Product training – Presentation (Japanese)
Acronis Backup Cloud 7.8: Troubleshooting training – Presentation (German)
Acronis Backup Cloud 7.8: Troubleshooting training – Presentation (Spanish)
Acronis Backup Cloud 7.8: Troubleshooting training – Presentation (French)
Acronis Backup Cloud 7.8: Troubleshooting training – Presentation (Japanese)
Acronis Backup Cloud 7.8: Product training – Webinar Recording (English)
 
 All available training and certification materials for Acronis MSP products can be found at: https://kb.acronis.com/MSPtraining
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.12210)
Backup Agent for Mac (v.12.5.12210)
Backup Agent for Linux (v.12.5.12210)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.8 Update 2


Backup
File Sync&Share


St. Luis (BETA2)


7.7 Update 2


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Strasbourg (EU1)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
File Sync&Share
Physical Data Shipping


Frankfurt (EU2)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


London (EU3)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Zurich (EU5)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US2)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US5)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Nagano (JP1)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Singapore (SG1)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Sydney (AU1)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Moscow (RU2)


7.8 Update 1


Backup
Office 365 Cloud-To-Cloud 2.0

 
Release notes and documentation
Acronis Data Cloud 7.8 Update 1 release notes 
Acronis Backup Cloud v 7.8 User Guide
Acronis Data Cloud backup agent release notes

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/15/2019 - 20:08

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
