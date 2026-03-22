# Support Digest: May 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-may-2018

## Original Post
**Author:** Unknown

Support Digest: May 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
I'm happy to present to you the Support Digest for May, 2018. During the month we've continued to update our Cloud data centers to Acronis Backup Cloud v 7.7. Along with the server-side infrastructure upgrade, a new version of backup client software (agent build 12.5.9940) has been published and available for download on every data center where Acronis Data Cloud 7.7 is available. New agent enables the possibility to use new generation backup archive format (version 12), which is faster, supports all kinds of data and even more reliable than previous archive version (version 11).
Hot topics
New KB articles
New training materials
Data center and agent updates
Release notes and documentation
Hot topics
One of the most important news in May was ratification of General Data Protection Regulation (GDPR). Let's cover GPDR's key points and also review 2 more important features introduced in Acronis Backup Cloud 7.7: new generation archive format and monitoring Dashboard in Account management console.
 
#1 ► GDPR compliance
The European Union (EU) General Data Protection Regulation (GDPR) is coming into effect on May 25, 2018 (see the list of affected countries here). But what is GDPR?  In short words it is a law that regulates how the data belonging to EU residents should be stored and the way this data can be processed by data keeper. Acronis responsibilities as data keeper (or data processor):
Protection of personal data
Easy access to / control of personal data at data owner's request
Monitoring / reporting of breaches
Control of data location
If you are interested in the measures Acronis takes to protect the data stored at Cloud please check this document. You may also refer to the following web page describing most common GDPR-related questions.
#2 ► New archive format (Version 12)
Starting from backup agent v. 12.5.9940 it is possible to choose whether to use old archive format (version 11) or new format (version 12). Among the benefits of new format are better I/O performance, in-built deduplication on archive-level and improved reliability. Note that there are some certain limitations for using version 12 archive format, namely:
New format can be enabled under plan's options only when creating a new backup plan. Once plan is created, it is impossible to change it.
When creating a new backup plan, version 12 format is chosen by default.
Format of existing backup plans cannot be changed.
Version 11 archive format cannot be converted into version 12 format. Conversion tool is going to be introduced in one of the next versions of Acronis Data Cloud.
Complete description and archive format's comparison can be found on this page.
If you'd like to perform a centralized update of all you Customer's agents, check this guide.
#3 ► Dashboards
Dashboard is the new monitoring tool designed for service providers who are  interested in monitoring multiple customers' backup statuses in a single place. Using seven different widgets it is possible to adjust what information will be reflected under Account Management console's and how it will be represented. The list of available widgets is the following:
Activities (Shows results of activities for the last seven days)
Active alerts details (Shows active alerts)
Active alerts (Shows the most recent active alerts)
Alerts summary (Shows alerts that occurred during a specified time period)
Alerts (Shows alerts that occurred during a specified time period)
Protected devices (Shows the devices and backup plans applied to them)
Activities summary (Shows results of activities performed during a specified time period)
More details about the dashboard's configuration is available under Acronis Backup Cloud user guide.
Note: Dashboard shows information only for Customer and Unit group types under particular Partner group. If there are some Sub-partner groups under that Partner, Sub-partner's Customers data won't be shown under widgets. To bypass this limitation, it is possible to perform conversion of your sub-partner groups to "Folder" type. Backup events for Customer under Folders will be shown under Dashboard.
 
New KB articles
Acronis Backup Cloud
KB61346: Acronis Backup Cloud: size of individual slices (recovery points) is missing
KB61356: Acronis Backup Cloud: Physical Data Shipping option is missing for Entire Machine backup
Acronis Storage
KB61184: Acronis Backup 12.5: creating a vault in Acronis Storage fails with "Permission denied"
See all new KB articles here: https://kb.acronis.com/new
 Did you know that migration from Acronis Storage 1.x/Acronis Storage Gateway to Acronis Storage 2.4 can be configured from Storage 2.4's control panel? See here for details.
 
New training materials
Acronis Files Cloud Support Training: Webinar Recording
Acronis Backup Cloud v 7.7 Support Training: Webinar Recording 
Acronis Storage 2.4 Support Training: Webinar Recording
Acronis Disaster Recovery Cloud Support Training: Webinar Recording
Training and certification materials for all MSP products can be found at: https://kb.acronis.com/MSPtraining
 Did you know that support certification for any product makes you eligible for Acronis Support and provides with faster responses from Acronis Support Team? See these guidelines for more details.
 
Data center and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.9940)
Backup Agent for Mac (v.12.5.9940)
Backup Agent for Linux (v.12.5.9940)

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.7


Backup
File Sync&Share


St. Luis (BETA2)


7.7


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.7


Backup


Frankfurt (EU2)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


London (EU3)


7.7


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.7


Backup


Zurich (EU5)


7.7


Backup


Ashburn (US2)


7.7


Backup
Disaster Recovery
File Sync&Share


Ashburn (US5)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.7


Backup
Disaster Recovery
File Sync&Share


 



Singapore (SG1)


7.7


Backup


Sidney (AU1)


7.7


Backup


Moscow (RU2)


7.7


Backup

 
Release notes and documentation
Release notes for Acronis Data Cloud 7.7
Acronis Backup Cloud v 7.7 User Guide

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/29/2018 - 15:53

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
