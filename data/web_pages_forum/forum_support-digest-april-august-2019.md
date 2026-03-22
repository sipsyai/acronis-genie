# Support Digest: April-August 2019

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-april-august-2019

## Original Post
**Author:** Unknown

Support Digest: April-August 2019

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello dear colleagues,
Allow me to present the newest edition of support digest for Service Providers! Past few months have brought multiple exciting news such as:
Acronis Data Cloud platform has been renamed to Acronis Cyber Cloud.
A recent update of Acronis Cyber Cloud to v.7.9 has introduced the G Suite backup feature. Now your Google cloud apps can be protected with an ease of just a couple of clicks!
New version of backup agent is available for download - 12.5.12960
The platform has received multiple stability and performance improvements.
 
Hot topics
New KB articles
New training materials
Data center and agent updates
Release notes and documentation

Hot topics
As usual, we are reviewing the 3 most frequently asked questions during the past few months.
 
#1 ► Physical Data Shipping
When using cloud services, you might need to transfer large volumes of data to the cloud storage. Physical Data Shipping helps you save time and network traffic by sending the first backup, which is full and usually the largest,  to the cloud data center on a hard drive. The data center personnel receives the drive and then uploads the data to the storage. The subsequent data transfers will reflect only the changes to the initially uploaded data and thus can be performed over the network.
The Physical Data Shipping service management is available through the Management Console of Acronis Cyber Cloud platform.
Detailed instructions on how the archive can be created and prepared for shipping can be found here. Before the package with the drive is sent, it's necessary to create a shipping label. Once the disk is shipped, you can track the order processing status under the tracking console.
Make sure your web browser is supported and the hard drive interface is in the list.
 
#2 ► Backup Options: Error handling
These options enable you to specify how to handle errors that might occur during backup.

Re-attempt, if an error occurs: when a recoverable error occurs, backup agent re-attempts to perform the unsuccessful operation, attempts will be stopped as soon as the operation succeeds or if the number of specified attempts are performed, whichever happens first
Do not show messages and dialogs while processing (silent mode): when enabled, the agent will automatically handle situations requiring user interaction, if an operation cannot continue without user interaction, it will fail
One of the possible use cases of error handling option can be backup over an unstable network. If connectivity is lost at some point during a backup operation, backup agnt will attempt to re-establish a connection to the target destination (according to the number of re-attempts specified under the option).
 
#3 ► Physical to Virtual recovery
Recovery of a backup of a physical device as a new virtual machine is quite a common scenario nowdays. Imagine a case where a local server goes down due to hardware failure, and you need it back in production as soon as possible. Fortunately, if you have a hypervisor, you can recover the backup of the faulty machine as a VM. There are two different approaches for such operation:
Using the web interface
This method allows you to perform recovery through Acronis Backup Cloud user interface. In order to restore the source machine this way first, you'll need to install backup agent for your hypervisor and registered under Acronis Backup Cloud. Then, you can choose either to create a brand new VM or to overwrite an existing one. Recovery through the web interface does not allow to choose particular disks/volumes to recover as disk mapping is performed automatically by the product.
 If you'd like to map the disks/volumes manually proceed to next item below.
Using bootable media
This option is applicable in case of recovery through Backup Console is impossible for some reason: BMR recovery, machine running macOS, specific disk configuration, no agent for hypervisor is available. Exact steps are described under the respective user guide article. This method is applicable for recovering backup image both to a new physical or virtual machine. Check this page for the steps describing Bootable media's creation. Once the recovery process is finished, make sure to apply Acronis Universal Restore (AUR) in case performing a restore to dissimilar hardware /P2V or V2P migration/BMR recovery. Also, keep in mind, that the Bootable Media not only allows you to recover an entire machine's image or particular volumes, but also particular files from backup.
Overall recovery cheat sheet for all data types is available here.
 

New KB articles
Acronis Backup Cloud

KB63346: Acronis Cyber Cloud: integration with Active Directory 


KB63331: Acronis Backup Cloud: backup of Office 365 group mailbox fails with "The primary SMTP address must be specified when referencing a mailbox" 


KB63323: Acronis Backup: Backup fails with "The snapshot creation has failed due to a hardware issue or a conflict with your disk hardware. Windows has reported the following error: The device has a bad block" 


KB63313: Acronis Backup Cloud: Office 365 "Users" tab is missing 


KB63306: Acronis Backup: backup of network shared folder fails with 'The credentials for network share are incorrect' 


KB63300: Acronis Backup: "Database has not been backed up because the database files are not included in the single-pass backup" error 


KB63292: Acronis Backup Cloud: how to upload large backup replica to Cloud with InitialSeedingTool 


KB63288: Acronis Cyber Infrastructure Backup Gateway: how to reconfigure ABGW to use another NFS export to store archives 


KB63266: Acronis Backup: activity fails with "No volumes have been found while processing the 'Fixed Volumes' template" 


KB63259: Acronis Backup: "Lost connection to the back-end service" error when working in Backup Console 


KB63232: Acronis Backup: ESXi configuration backup 


KB63229: Acronis Backup: Linux-based bootable media does not detect Intel Optane-accelerated disks 


KB63212: Acronis Backup Cloud: MMS service cannot be started, error "error 0x30002: CannotBind" 


KB63201: Acronis Backup: "Error: Trailing spaces in the path" when backing up SQL database 


KB63198: Acronis Backup Cloud: Agent installation fails on registration step with "Error 0x26a001a: Random bytes generation failed" 


KB63182: Acronis Cyber Cloud Integration with ConnectWise Manage: quota automatically resets to unlimited 


KB63179: Acronis Backup Cloud: after disabling all but TLSv1.2 protocols SQL application-aware backup fails with warning "Failed to collect the metadata of the SQL Server databases selected for backup."
 
Acronis Disaster Recovery Cloud


KB63002: Getting the root privileges and the log file from the VPN Appliance 


KB62658: Acronis Cyber Cloud: Acronis-hosted cloud storages naming convention
 
Acronis Files Cloud

 
 

KB63195: Acronis Files Cloud and Acronis Files Advanced for iOS: Touch ID/Face ID not working 


KB62878: Acronis Files Cloud: Client errors out with "Failed to receive handshake, SSL/TLS connection failed"

 
 
 
 
 
 
 
Acronis Cyber Infrastructure


KB63326: Acronis Cyber Infrastructure: Mellanox ConnectX support 


KB63288: Acronis Cyber Infrastructure Backup Gateway: how to reconfigure ABGW to use another NFS export to store archives 


KB63144: Acronis Cyber Infrastructure: "Write cache disabled" alert 


KB63109: Acronis Cyber Infrastructure 3.0: prerequisites for upgrade from Acronis Software-Defined Infrastructure 2.5 


KB63065: Acronis Cyber Infrastructure 3.0: new features 


KB62963: Acronis Cyber Infrastructure: logs location 


KB62938: Acronis Storage: Configuring LDAP/AD Before Upgrading to Acronis Software-Defined Infrastructure 2.5 


KB62823: Acronis Cyber Infrastructure: Throttling on storage



 


 

 
 
 
 
See all new KB articles here: https://kb.acronis.com/new

New training materials
Get familiar with the full range of backup and recovery operations for G Suite in the case of Acronis Backup Cloud:
How to Set Up a Google Organization for Backing Up the G Suite
How to Back Up and Recover a Gmail Mailbox
How to Back Up and Recover a Google Drive
How to Reveal Unauthorized Changes in a Backup
 
 All available training and certification materials for all MSP products can be found at https://kb.acronis.com/MSPtraining

Data center and agent updates
Current agent versions:
Backup Agent for Windows (v.12.5.12960)
Backup Agent for Mac (v.12.5. 12960)
Backup Agent for Linux (v.12.5. 12960)
 

Datacenter


Platform version


Available services


Strasbourg (BETA)


7.9


Backup
File Sync&Share


Strasbourg (EU1)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
File Sync&Share
Physical Data Shipping


Frankfurt (EU2)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


London (EU3)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Zurich (EU5)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US2)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Ashburn (US5)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Nagano (JP1)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share
Physical Data Shipping


Singapore (SG1)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share


Sydney (AU1)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0
Disaster Recovery
File Sync&Share


Moscow (RU2)


7.9


Backup
Office 365 Cloud-To-Cloud 2.0

 
Release notes and documentation
Acronis Cyber Cloud 7.9 release notes 
Acronis Cyber Infrastructure 3.0 
Acronis Backup plugin for WHM & cPanel (Build #  263)
WHMCS integration (Build #  177)

      
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/30/2019 - 13:38

                                                          
                                                            
                                                                                        
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful
