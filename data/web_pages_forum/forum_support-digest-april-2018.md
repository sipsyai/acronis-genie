# Support Digest: April 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-april-2018

## Original Post
**Author:** Unknown

Support Digest: April 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
I’m glad to present you the digest for April 2018. This month has witnessed a release of Acronis Data Cloud v 7.7 containing numerous new features and improvements. A new version of backup client software will be available soon, that supports new generation archive format and reworked mechanism of agent’s registration (based on Auth2.0 technology) without asking for user’s credentials during installation.
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
Hot topics
A big number of questions asked by Partners in April was related to deletion of on premise Cloud storage from Acronis Backup Cloud's Management console. Let’s review the prerequisites and necessary steps for storage's removal. Also we will cover 2 more popular topics: what to do if email notifications are not received and what is the recommended way to back up files/folders located on network share.
#1 ►Deleting Partner-Hosted Cloud storage from Management console
Along with Acronis-hosted Cloud storage Partners are allowed to set up an unlimited number of their own on-premise Cloud storages. Check the quick start guide for more details regarding its setup. Unlike Acronis-hosted storage, on-premise installations can be deleted from Cloud Management console in case they are not needed any more. The following conditions should be met prior to removal:
The storage should not be inherited from higher level Partner group.
If the storage is assigned to any customer tenants, you must disable the service that uses the storage for all customer tenants before deleting the storage.
Once both items above are met, you should follow step-by-step guidance on storage's removal. As an alternative method on-premise storage can be removed using Acronis Backup Cloud's RestAPI, see this KB article.
 
#2 ►Email notifications are not received
Acronis Backup Cloud brings various options for centralized monitoring the backup statuses of protected devices: backup notifications, daily recap of active alerts and customizable backup reports. In case of coming across a situation when any of those reports are not being delivered to recipients it’s necessary to check some basic things, namely:
Branding settings. In case you’ve set up to use your own SMTP server, try to send “Test Email” from branding tab. If test email is also missing, switch SMTP settings to Acronis default mail server and click “Test Email” again.
 
(If you are interested in not only customizing the console’s view but also the URL your customers will use to access management portal, click here)
Junk/Spam folders. Make sure emails from Acronis Backup Cloud (default sender is noreply-abc@acronis.com, or the one specified in the User-defined e-mail settings) are not being filtered by your mail client.
Verify if @acronis.com was not blacklisted on local mail server.
If the issue is with backup notifications only, verify backup notifications level settings.
See this KB article for details.
#3 ►Backing up network shares
A lot of people are keeping their important data on CIFS/SMB shares and thus, they are very interested in backing up network shares. Given the nature of the way how backup is performed in such cases, Acronis provides the following best practices:
Backup of mapped network drives is not supported, so do not map network shares a local disks. Instead, use UNC path to the share under “Items to backup” using “Files/folders backup” plan. More details are available under the following KB article.
Windows VSS technology does allows to create a snapshot of local volumes only, but not network shares. Therefore Acronis Backup Client requires exclusive access to all files on the network share at the time when backup takes place. In case some file is opened by 3rd party application during backup, this file is going to be skipped, moreover, backup may fail. To avoid such issues follow these simple instructions.
Set up backup schedule on out-of-production hours to decrease the chance some files will be unexpectedly opened during backup. See the complete guidance on the way to set up backup plan’s options in our November’s digest.
New KB articles
Acronis Backup Cloud
KB61267: Acronis Backup Cloud: Backup fails with "Failed to parse the XML"
KB61243: Acronis Backup Cloud: how to update the credentials to Microsoft SQL/Exchange databases in the web console
KB61190: Acronis Backup Cloud: backup of an SQL Cluster cannot be browsed
KB61147: Acronis Backup: Application backup (SQL and/or Exchange) fails with "Failed to resolve item by its reference"
KB61106: Acronis Backup Cloud: Enabling Automatic Dump Creation for Acronis Processes
KB61100: Acronis Backup Cloud: Windows Services and Processes
KB61092: Acronis Backup Cloud and Acronis Backup 12.5: "The credentials for Exchange server are incorrect. Error code 1802."
Acronis Storage

KB61054: Acronis Storage: how to change lost passwords

 

 


Acronis Disaster Recovery Cloud
KB61131: Acronis Disaster Recovery Service: mouse not working within server console
KB61126: Acronis Disaster Recovery Cloud: registering Disaster Recovery VPN Appliance fails with "Got unexpected response code [404]"


 


 

See all new KB articles here: https://kb.acronis.com/new
 Did you know that Acronis not only provides you with world-class backup & disaster recovery solutions, but also is capable of assisting you with the design, integration, implementation, and on-going operation with our products? See more details about Acronis Professional Services at https://www.acronis.com/en-gb/business/enterprise-solutions/professional-services/#service-providers
New training materials
Acronis Data Cloud v.7.7: What’s new
Acronis Backup Cloud v.7.7: Product training
Acronis Backup Cloud v.7.7: Certification exam
Acronis Files Cloud: Product training
Acronis Files Cloud: Certification exam
Acronis Disaster Recovery Cloud: Product training
Acronis Disaster Recovery Cloud: Certification exam
Acronis Storage v.2.4: Product training
Acronis Storage v.2.4: Certification exam
 
Training and certification materials for all MSP products can be found at: https://kb.acronis.com/MSPtraining
 Did you know that the most recent release of Acronis Storage - v 2.4 - allows not only allows to expand your local storage by attaching iSCSI disks, but also gives an opportunity to replicate your customers’ data between different Acronis Storage Clusters? Try it for free at https://www.acronis.com/en-us/business/software-storage/
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.0.4670)
Backup Agent for Mac (v.12.0.4670)
Backup Agent for Linux (v. 12.0.4670)
 

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


7.5HF2


Backup


Frankfurt (EU2)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


London (EU3)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.5HF2


Backup


Zurich (EU5)


7.5HF2


Backup


Ashburn (US2)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Ashburn (U S5)


7.5HF2


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.5HF2


Backup


Singapore (SG1)


7.5HF2


Backup


Sidney (AU1)


7.5HF2


Backup


Moscow (RU2)


7.7


Backup

 
Release notes and documentation
Acronis Data Cloud backup agent v 12.0.4670
Acronis Backup Cloud v 7.7 User Guide

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/08/2018 - 13:30

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
