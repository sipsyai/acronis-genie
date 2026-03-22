# Support Digest: Q2 2020

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-q2-2020

## Original Post
**Author:** Unknown

Support Digest: Q2 2020

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            



Hello dear colleagues,
I'm pleased to present the newest issue of Acronis Support digest for service providers!
The past few months have been full of exciting events. Let me highlight the most important ones:
Acronis has introduced Acronis Cyber Protect Cloud: the first solution that combines Backup and Cyber Protection capabilities in a single application.
Acronis Cyber Cloud platform was updated to v.9.0 on all data centers.
The latest release of Acronis Cyber Infrastructure - v.3.5 - is packed with new features that improve the performance, manageability, and availability of clusters storing and running cyber protection workloads.
A new version of the Cyber Protection agent - v.12.5.22750, which includes all features of both Cyber Protect Cloud and Cyber Backup Cloud - is available for download.
Multiple stability and performance improvements for the platform.
 
Hot topics
New KB articles
New training materials
Data center and agent updates
Release notes and documentation
 
Hot topics
According to our good tradition, we are reviewing the most common questions asked by Partners. Let us have a look at the top-4 popular topics.
#1 ► Acronis Cyber Protect Cloud: editions' management
What is the difference between Cyber Protect Cloud and Cyber Backup Cloud services? Are there any side effects of switching between these two, and what are the consequences of downgrading from Cyber Protect Cloud to Cyber Backup Cloud?
The major difference between Cyber Backup Cloud and Cyber Protect Cloud is that the latter one, apart from basic functionality (which is available in both services):
Backup
Vulnerability assessment
Active protection
also includes cyber security-oriented features, namely:
Antivirus and anti-malware protection
URL filtering
Data protection map
Patch management
Windows defender management
Microsoft security essentials management
And that is it! All the other functionalities' availability completely depends only on the service editions chosen for the particular Customer group. You can find the description of each edition and the included features in the product's manual.
The most common concern is that if Cyber Protect is downgraded to Cyber Backup, this will delete all the backups/ all registered machines/ all users. In fact, none of those events actually happen. The most obvious thing that happens after such downgrade is that the Cyber Protect edition features (listed above) become unavailable for the Customer group that is switched to Cyber Backup Cloud. The rest of the changes depend on what edition switch is performed for the particular Customer group.
If you'd like to check all effects of changing a service's edition, please refer to the following article.
 
#2 ►Cyber Protection agent: new services
The latest major update of  Acronis Cyber Cloud platform - v.9.0 - has also introduced the Cyber Protection agent: a successor to the legacy Backup agent. From now on, the agent combines backup, recovery, and cyber-security functionality. Due to this fact, the agent software was reworked and there were several new services that were added. The table below describes the complete list of services depending on the OS type:

Now, let's discuss the responsibilities of each service:
Acronis Managed Machine service: general backup and recovery-related operations
Acronis Schedule2 service: execution of scheduled backup and cyber protection tasks
Acronis Cyber Protection service: entire cyber protection functionality: anti-malware scans, vulnerability assessment, patch management, data protection map, URL filtering, etc.
Acronis Active Protection service: protection against ransomware and cryptomining
Acronis Agent Core service: communication with Cloud components 
 Active Protection and Cyber Protection services are always in a running state, regardless of the fact if you have active protection or cyber-security policies applied or not. These services are controlled only through the Cyber Protection console and cannot be stopped from services.msc! 
 
#3 ►  How to change an email address for a user in Acronis Cyber Cloud 
Surprisingly, this simple question has caused quite a lot of concerns among partners. Let's discuss this process step-by-step.
In the Acronis Cyber Cloud's Management portal, go to Users.
Select the user account whose email that needs to be changed, and then click the pencil icon in the General information section. 
Replace the existing email with the email of the future account owner, and then click Done.
Confirm the action by clicking Yes.
Let the future account owner verify their email address by following the instructions sent there.
The complete instructions of changing an account's owner (both changing user's email and password) can be found under Acronis Cyber Protect Cloud's user manual.
 Until the new account owner confirms the change by clicking a link in the confirmation email, the user's email won't be changed!
#4 ► How to use Cyber Protect's Antivirus and Anti-malware protection if there is already a 3rd party AV software installed?
Acronis Cyber Protect Cloud has introduced a built-in antivirus and anti-malware solution. Its effectiveness has been proven against most of the modern cyber threats. In case a device does not have antivirus software yet at the point where Acronis Cyber Protection agent is installed, Acronis Cyber Protect Cloud will be a perfect solution to protect the machine against malware.
However, it is quite a common situation when a device already has a 3rd party Antivirus by the moment Cyber Protection agent is installed. Acronis Cyber Protect Cloud is totally compatible with 3rd party software, meaning both solutions will be able to work simultaneously!  However, if you are concerned about compatibility issues, you can disable 3rd party Antivirus or the Antivirus and Anti-malware module under Acronis Cyber Protect Cloud's protection plan.
In case some conflicts are experienced between Acronis Cyber Protect Cloud and 3rd party Antivirus,  we recommend to put Acronis folders and executables to 3rd party Antivirus' exclusions, as described here.
Also, if either Windows Defender Antivirus or Microsoft Security Essentials are used as a corporate Antivirus solution, Acronis Cyber Protect Cloud provides an easy and effective mechanism to manage those applications right from Cyber Protection Console:
 
New KB articles
Acronis Cyber Protect Cloud
KB65058: Acronis Cyber Protect Cloud: VM quota acquisition
KB65056: Acronis Cyber Protect Cloud cannot be installed on the machine with R1Soft
KB65004: Acronis Backup plugin for WHM and cPanel: download or recovery of databases fails with "MySQLWaitingPidTimeoutError"
KB65000: Acronis Cyber Cloud: How to change the DNS name or IP address used to register Backup Gateway
KB64988: Acronis Cyber Protect Cloud, Acronis Cyber Backup: Activity fails with "Misc error while local file io"
KB64970: Acronis Cyber Protect Cloud: "Cyber Protection (or Active Protection) service is not responding" alerts on Linux and Mac agents
Acronis Cyber Infrastructure
KB64974: Acronis Cyber Infrastructure: low performance of nodes with Mellanox adapter
KB64948: Acronis Cyber Infrastructure: Nodes with AMD Epyc Rome CPU and Mellanox NIC reboot unexpectedly
KB64844: Acronis Cyber Infrastructure: Taking VMware snapshots of cluster nodes
KB64825: Acronis Cyber Infrastructure: Cluster creation fails with "Command time out has expired"
KB64787: Acronis Cyber Infrastructure: How to run storage behind HAProxy
KB64759: Acronis Cyber Infrastructure: How to import VZ7 Virtual Machine into Acronis Cyber Infrastructure
Acronis Cyber Files Cloud
KB64846: Acronis Cyber Files: desktop client error "The path has been selected by another user"
KB64095: Acronis Cyber Files Cloud: simultaneous login on multiple devices
KB64007: Acronis Cyber Files Cloud: installation package for Mac/Windows is not available on Windows/Mac devices
See all new KB articles here: https://kb.acronis.com/new
 
New training materials
Acronis Cyber Cloud: What's new in v.9.0 (Introducing Acronis Cyber Protect Cloud)
Acronis Cyber Cloud: Overview of the platform's services
Acronis Cyber Protect Cloud 9.0: Product training
Acronis Cyber Protect Cloud 9.0: Troubleshooting training
 All available training and certification materials for all MSP products can be found at https://kb.acronis.com/msptraining
 
Data center and agent updates
Current agent versions:
Cyber Protection Agent for Windows (v.12.5.22750)
Cyber Protection Agent for Linux (v.12.5.22750)
Cyber Protection Agent for Mac (v.12.5.22750)
 

Data center


Platform 
version


Available services


Strasbourg (EU1)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Frankfurt (EU2)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


London (EU3)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Lupfig (EU5)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Ashburn (US2)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Ashburn (US5)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Nagano (JP1)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Singapore (SG1)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA


Sydney (AU1)


9.0.2


Cyber Protection 
Office 365 Cloud-To-Cloud 2.0
G Suite
Disaster Recovery
File Sync&Share
Notary
Physical Data Shipping
Storage SPLA

 
Release notes and documentation
Acronis Cyber Cloud 9.0 release notes 
Acronis Cyber Cloud 9.0 Update 1 release notes 
Acronis Cyber Cloud 9.0 Update 2 release notes 
Acronis Cyber Protection agent release notes
Acronis Cyber Protect Cloud User Guide
Acronis Cyber Backup Cloud User Guide
Acronis Cyber Infrastructure 3.5 release notes





      
                                            
                
            
                            
                    
                        
                            
                              Fri, 05/29/2020 - 08:55

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
