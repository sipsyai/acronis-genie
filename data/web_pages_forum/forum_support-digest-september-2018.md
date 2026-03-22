# Support Digest: September 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-september-2018

## Original Post
**Author:** Unknown

Support Digest: September 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            

Hello dear colleagues,
We're happy to announce that September's edition of monthly support digest for service providers is ready! During this month we've released a new version of backup agent containing fixes for most common technical issues. Product's stability improvements have already been confirmed both by automated and manual testing. Also, in September a new version of Acronis Files Cloud Android application has been introduced in Google Play.
Hot topics
New KB articles
Datacenter and agent updates
Release notes and documentation
Hot topics
The most common questions coming from Partners this month were related to recovering huge portions of data from Cloud in terms of slow internet connection, recovering data from Backup Management console and performing bare metal restore onto hardware with RAID controllers.
#1 ► Recovery of large data sets from Cloud
Restoring a huge portion of files or entire server from Cloud having poor bandwidth may result not only into prolonged waiting but even business-down situation. Is there a way to avoid it and not to wait for days until recovery is complete?
Fortunately, Acronis already has the process that is helpful in such cases. It is called Large Scale Recovery (or simply LSR). LSR allows to download the data to a local disk of a machine with strong bandwidth and then send this disk to Customer who desperately needs his data. In order to perform LSR operation, it is necessary to install a utility called IS/LSR tool on Windows or Linux machine according to instructions. All the manipulations with the tool including installation and data download are performed by Service Provider.
It is also possible to request for LSR process from Acronis team directly, however, this procedure has some certain pre-requisites:
Customer's backup source data set size exceeds 5 TB and Customer location is one of data centers listed below, Acronis provides an assistance with uploading such backups.
Here is the list of data centers where Acronis provides assistance with Physical Data Shipping and Large Scale Recovery services:
EU1, EU7 (Strasbourg)
EU2 (Frankfurt)
EU3 (London)
EU6 (Cologne)
US2, US5, Kaseya (Ashburn, VA)
SG (Singapore)
JP (Nagano)
 
  Interested in uploading large set of data to Cloud? Use Initial Seeding option! Click here for instructions how to set up IS backup plan.
 
#2 ► Recover Vs Download
Most probably, you have already noticed that Backup Management console provides two possible options to restore data: Recover and Download (click here for step-by-step instructions). But what is the difference between these methods?
Recover operation allows to restore data to any online machine registered under the same Customer group (particular machine is chosen via Machine to browse from dialog under BACKUPS tab). During the process Backup Agent connects to Cloud storage, access the files and then steams the necessary data to target destination chosen under recovery task's options (either original folder or a custom location). Recover process is persistent to network disruptions during the process since Backup Agent has built-in functionality that allows to re-establish connection as soon as link is up. Acronis recommends to use Recover option in case large set of data needs to be retrieved.
Download option also involves Backup Agents into the restore process. Data from Cloud storage is being transferred to Backup Agent, then streamed from the Agent  to Cloud Backup Management server. Management server zips the data and allows you to download it via web browser. Last part of the process - downloading the ZIP archive - is very vulnerable for network interruptions since there is no way to reestablish connection once it is lost. This results in creation of damaged ZIP archives which cannot be opened. Acronis' recommendation is to use Download option only when the goal is to recover not more than 100 MB of data. For other cases, use Recover option.
 
 Did you know that recovery can be performed not only from Backup Management console? Check all the methods here.
 
#3 ►Image recovery to machines with RAID controllers
The general approach in case of BMR recovery is using Acronis Bootable Media. Standard Bootable Media is linux-based, therefore there migth be some occasions when it  does not detect RAID arrays because RAID controllers use proprietary drivers. A simple example are DELL Poweredge servers. Their RAID drivers cannot be integrated into a Linux-based bootable media and thus, a different approach should be applied here. It is necessary to use a WinPE-based Media to boot machines with specific hardware. While being built, WinPE Media allows to include the special drivers that are missing in standard Linux-based Bootable Media (not necessary that would be RAID controller drivers, it can be any other driver).
Since WinPE media is not available for direct download, it's necessary to create it first. Detailed step-by-step recommendation can be found under the following KB article.
 
New KB articles
Acronis Backup Cloud
KB 61859: Acronis Backup: How to disable VDDK transports on agentKB 61809: Acronis Backup Cloud: Time settings on the Acronis Storage cause miscommunication with AgentsKB 61805: Acronis Backup Cloud: Manual registration fails with "Couldn't connect to host at localhost:43234"KB 61714: Acronis Backup Cloud: backup fails wih "VSS writer 'System Writer' with class ID 'E8132975-6F93-4464-A53E-1050253AE220' has timed out" error"
 
See all new KB articles here: https://kb.acronis.com/new
 
  Acronis Data Cloud 7.8 is going to be released into production within next couple of weeks. Want to try all new features before the release? Click here to access beta-test!
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.10790)
Backup Agent for Mac (v.12.5.10790)
Backup Agent for Linux (v.12.5.10790)
 

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
Acronis Files Cloud application for Android. Direct download link.  



      
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/09/2018 - 07:54

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
