# Support Digest: June 2018

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-june-2018

## Original Post
**Author:** Unknown

Support Digest: June 2018

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
Welcome to service providers’ digest June, 2018 edition. During the month we’ve finished the process of major upgrade of our Acronis Data Cloud’s data centers to v.7.7. Let’s review the most popular topics of this month (according to our Partners) and highlight the most important things.
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes and documentation
 
Hot topics
All the top-3 questions are related to the release of latest version of backup agent, so here they are:
#1 ►Local backup 
Starting from v.7.7, usage of local backup storage is reported to Acronis Data Cloud and the usage data is available for partners, the same way as for any other offering item. Now it is possible not only to allow or disallow the possibility to use local storage as backup destination, but also track its usage and charge for it. The following locations are treated as local: It includes the following backup destinations:
Local folders
Network folders
NFS folders
Secure Zone
Local backup usage is recalculated after each of the following operations: manual and scheduled backup, backup replication, backup retention, deletion of backup slice, deletion of archive, deletion of backup location from the management console.
There are some certain limitations that should be kept in mind:
Manual deletion of backup files directly from file system won’t trigger recalculation
Local usage numbers under management portal are updated daily at 5AM GMT
Only soft quotas are supported for local backup offering item
If local storage usage is calculated twice, apply the following fix. In case for some reason it is impossible to choose local destination under new backup plan, though respective offering is present, refer to this solution.
 
#2 ►Microsoft One Drive backup
OneDrive is a file hosting service operated by Microsoft as part of its suite of Office Online services. OneDrive folder on machine’s local disk is not actually a directory with data, but rather a symbolic link to the files kept at Microsoft cloud servers. When Backup Agent tries to back up data inside OneDrive folder, it is unable to do so, since it sees no files to save. Therefore backup of OneDrive folder may fail.
The easiest way to deal with this issue is to exclude OneDrive folder from the list of items that will be backed up.  As an alternative method, you can also use disk-level backup plan, which works on a lower level than disk’s file system and thus not dependent on OneDrive’s design. 
The entire list of all possible solutions for OneDrive backup issue is described here.
#3 ►Registration of backup agent
Upon successful installation of Acronis Backup Cloud’s backup agent, it is necessary to register it under Cloud Management server, otherwise it would be impossible to manage the device where the software was distributed. Registration can be performed 3 different ways:
If you have downloaded the installation .EXE file from the very same machine which you are going to protect, you just need to click “Register Now” button upon successful installation. After that you’re automatically redirected to backup console for the Customer group where you wanted the machine to belong to and confirm registration. 
In case the machine where agent was installed temporary does not have access to internet, you may register it from another device which has. To do so, click “Show registration info” after successful installation of backup software and copy “registration code”. Next, on the machine which has internet connection open backup management console for the Customer you want your machine to be registered at and click “ADD” button and then choose “Registration via code” option. Specify the registration code obtained from the installed and confirm registration.
When necessary, a device can be registered manually using OS’ command line interface. See here for detailed instruction.
For the cases where agent’s registration fails with “Agent is already registered” error, please refer to known solutions section from this article. Entire process of agent's installation is described under Acronis Backup Cloud's user guide. 
 
New KB articles
Acronis Backup Cloud

KB61484:  Acronis Backup: exclusion of a partition does not work
KB61477:  Acronis Backup Cloud: local backup cannot be selected after upgrade to version 7.7
KB61469:  Acronis Backup Cloud: local storage usage calculated twice
KB61454:  Acronis Backup Cloud: agent registration fails with "Agent is already registered. Please deregister agent in Backup Console"
KB61451:  Acronis Backup Cloud: "Failed to find directory '/lib/modules/2.6.32-504.16.2.el6.x86_64/build' that contains the kernel source code." error
KB61429: Acronis Backup Cloud: error when backing up OneDrive folder


Acronis Disaster Recovery Cloud
KB61437:  Acronis Disaster Recovery Cloud: enabling promiscuous mode in hypervisors for the VPN connection
KB61435:  Acronis Disaster Recovery Cloud: remote console is disconnected
KB61433:  Acronis Disaster Recovery Cloud: Disaster Recovery Storage usage

 

 

 
 
 
 
See all new KB articles here: https://kb.acronis.com/new
 
Did you know that training materials and certification exams for MSPs are now available not only in English, but also in French, Spanish, German and Japanese? Find the full list of learning documentation at https://kb.acronis.com/MSPtraining.
 
New training materials
Acronis Data Cloud v.7.7 Account Management console
Acronis Backup Cloud v.7.7 Support Q/A session - Webinar Recording
Acronis Storage 2.4 Migration from Acronis Storage Gateway - Video
Training and certification materials for all MSP products can be found at: https://kb.acronis.com/MSPtraining
 
Did you know that Acronis Certified MSP partners’ revenue is 30% higher compared to non-certified ones? Pass the certification now and become certified: https://www.surveygizmo.com/s3/4306181/Service-Provider-Certification-Exam-Acronis-Backup-Cloud-v-7-7 
 
Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.1.10170)
Backup Agent for Mac (v.12.5.1.10170)
Backup Agent for Linux (v.12.5.1.10170)
 

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


7.7


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


7.7


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

      
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/06/2018 - 17:33

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
