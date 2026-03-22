# Support Digest: October 2017

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-october-2017

## Original Post
**Author:** Unknown

Support Digest: October 2017

        
  



    
  


  
          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
In October we started working with the new Acronis Data Cloud platform, and have already released the new Hotfix 1, as well as the new versions of backup agents. Let's see what was the most important for the past month, and what you should be aware of for the upcoming month:
Hot topics
New KB articles
New training materials
New features
Datacenter and agent updates
Release notes
 
Hot topics
The top 3 questions in October were all regarding the agents, so let's look closer at them now:
  #1 ► Agent installation. What to do if agent installation fails or doesn't even start?
Agent software must be installed on every device that should be consistently protected, and the installation process can be roughly split into 3 steps: configuration, installation and registration. Let's see the first 2 steps here:
During configuration, user credentials are verified on the cloud server. If this fails, make sure that you can login with these credentials to https://cloud.acronis.com and check that all ports are open with the Connection Verification Tool
Additional step in configuration involves selection of the agent components to be installed. If some components are missing, make sure you use the latest agent build with the all agents installer, and that the environment is supported
Installation in Windows uses MSI technology and any failure involves interpretation of the MSI log, see KB1647. For example, if MSI module requires system reboot after installing another software, you will get the error "MainEngineThread is returning 1603", see KB59045
Installation in Linux requires a number of packages to be available or already installed. In case the compilation of a kernel module fails, you can compile it manually, see KB1556
Installation in Mac does not compile the SnapAPI module, but yet sometimes requires manual installation. In this case follow KB58154
  #2 ► Agent registration. And what if the agent does not appear in backup console at all? What to do if it appears twice?
The last step of the installation requires the agent to register in the cloud management server with its unique ID. If the agent fails to install, start the local services or connect to the cloud server, the registration will fail.
Registration of Agent for Windows starts at 96%, so hanging or failing at this stage usually indicate, that the registrations process failed.
When installation fails and the agent does not appear in the backup console, verify whether the agent software was installed on the system, or it was removed during rollback. In case of latter, identify and resolve the problem with installation and re-attempt the entire installation procedure.
For the installed software, make sure the Acronis Managed Machine Service is running with administrative privileges.
Finally, register the agent the agent manually in the cloud management server: KB55244
If the agent appears twice in the backup console, this means the software was re-installed and the agent changed its unique ID. Remove the duplicate offline agent
For agentless backup (VMware, Hyper-V and Virtuozzo) the UUID is used to locate and displate the VM. If the VM does not appear in backup console, make sure its UUID is not duplicated within another VM on the same host
  #3 ► Agent synchronization. What to do when the agent is offline or shows incorrect data?
Finally, once you get the agent installed, it starts communicating with the cloud management server via ZMQ protocol. Whenever this communication is broken, the information in the backup console may be out of date or the agent may appear as offline.
Agent may appear as offline when local services are not running, there is a network issue or agent changed its unique ID. Troubleshoot these issues following KB57601
If multiple machines show synchronization problems at the same time, first confirm that the cloud servers are accessible from the local network, and then report the issue to Acronis Support
A way to monitor the agent status is to track the relevant alerts. Alerts "Machine is offline for more than X days", "Backup did not start" and "Backup status is unknown" are good indicators that the agent connectivity may have failed
 
New KB articles
Acronis Backup Cloud
KB60572: Acronis Backup Cloud: retention fails with "Failed to delete the backups" and "An unsupported URI is specified"
KB60586: Acronis Backup Cloud: backup fails with "The user name or password is incorrect"
KB60495: Acronis Backup Cloud: website backup is not available in Backup management console for Partner administrators
KB60597: Acronis Backup Cloud: the Size column is removed from the Web Recovery console
KB60606: Acronis Backup Cloud: retention rules fail with "Cannot free up space taken by the deleted backups. The operation will be retried during next backup deletion"
Acronis Disaster Recovery Cloud
KB60499: Acronis Disaster Recovery Cloud: how to deploy and configure Disaster Recovery VPN Appliance
See all new KB articles here: https://kb.acronis.com/new
 Did you know that you can see all tagged articles if you click the tag in the bottom of the page? Here is an example of all alert-related articles: https://kb.acronis.com/tag/backup-status-alerts

 
New training materials
Acronis Storage 2.3
See all training materials here: https://kb.acronis.com/MSPtraining
 Did you know that a certified Service Provider requires twice as less support assistance from Acronis as a non-certified one?

 
New features
Backup Service
Support for macOS High Sierra 10.13
Support for "hardened" Microsoft SQL Server: backup and recovery of Microsoft SQL Server data no longer requires enabled SQL Server Browser Service and TCP/IP protocol
Disaster Recovery Service
Extending local networks to the Acronis cloud with VPN
Protecting a machine with a recovery server
Testing failover in an isolated network
Machine failover to the cloud
Machine failback
Protecting applications and appliances with a primary server
Acronis Storage
Support for Object Storage (S3, Azure, Swift, etc.) by Acronis Backup Gateway
Automated backup data migration from Acronis Storage Gateway v1.6 and v1.7 via Acronis Backup Gateway
NFS support. Store general purpose files in Acronis Storage cluster via the NFSv4 and pNFS protocols
Acronis Backup Gateway geo-replication (technical availability)
E-mail notifications
Quality of service for iSCSI
Custom SSL certificates for WebCP
Improved Acronis Backup Gateway monitoring
 Did you know that Disaster Recovery Service uses Backup Service as the initial data transport from local network to the Acronis Cloud? Which means that you can already start protecting your backed up devices with the Disaster Recovery Service!

 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.0.4492)
Backup Agent for Mac (v.12.0.4492)
Backup Agent for Linux (v.12.0.4470)

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.5HF1


Backup
File Sync&Share


St. Luis (BETA2)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Strasbourg (EU1)


7.5HF1


Backup


Frankfurt (EU2)


7.5HF1


Backup


London (EU3)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Frankfurt (EU4)


7.5HF1


Backup


Zurich (EU5)


7.5HF1


Backup


Ashburn (US2)


7.5HF1


Backup


Ashburn (US5)


7.5HF1


Backup
Disaster Recovery
File Sync&Share


Nagano (JP1)


7.5HF1


Backup


Singapore (SG1)


7.5HF1


Backup


Sidney (AU1)


7.5HF1


Backup


Moscow (RU2)


7.5HF1


Backup

 
Release notes:
Acronis Data Cloud 7.5 Hotfix 1
 
Share your experience!
What is your experience with new Files Cloud and Disaster Recovery Services?
Did you find all necessary support information on our website and Knowledge Base?
Share below your experience and your questions.

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/07/2017 - 07:46

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Heads up! Release notes for Acronis Storage 2.3 have been published on Support page:
Acronis Storage 2.3

      
                
                
                    
                                                    Thu, 11/23/2017 - 13:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
