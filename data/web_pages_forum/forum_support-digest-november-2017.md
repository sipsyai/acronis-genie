# Support Digest: November 2017

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/digests-and-support-best-practices/support-digest-november-2017

## Original Post
**Author:** Unknown

Support Digest: November 2017

        
  



    
  


  
          





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Colleagues!
In November we introduced several releases of Acronis Backup Cloud agent software with multiple fixes and improvements. Let's see what else was important for support this month:
Hot topics
New KB articles
New training materials
Datacenter and agent updates
Release notes
 
Hot topics
The most frequently asked question in November was about backup retention rules, e.g. deleting old backups and archives. So let's see what backup types Acronis Backup Cloud supports, how they are configured withing the schedule functionality and how backups are retained.
  #1 ► Backup types. Which types of backups can be created and what are their advantages?
Each backup plan creates one new archive, which consists of several backups that can be logically grouped into sets. There are a few backup types:
Full: A self-sufficient backup containing all data chosen for backup. You do not need access to any other backup to recover the data from a full backup.
Incremental: A backup that stores changes to the data against the latest backup. You need access to other backups to recover data from an incremental backup.
Differential: A differential backup stores changes to the data against the latest full backup. You need access to the corresponding full backup to recover the data from a differential backup.
Single-file: A new backup format, in which the initial full and subsequent incremental backups are saved to a single .tib file, instead of a chain of files. This format leverages the speed of the incremental backup method, while avoiding its main disadvantage–difficult deletion of outdated backups. The software marks the blocks used by outdated backups as "free" and writes new backups to these blocks. This results in extremely fast cleanup, with minimal resource consumption. Read more about this archive in KB57116.
  #2 ► Schedule. How can I setup which backup type is created?
Here is how backup type is configured and what it depends on:
Backup type can be configured within Backup Scheme of the schedule option. Depending on data type and location, one of 4 backup schemes can be chosen: Single-file, Always full, Weekly full > Daily incremental, Custom. See this cheat sheet for more details.
Backup storage location the options for possible backup types. Cloud storage can only store single-file backups. Local and network storage can store different backup types. See all locations and backup plan cheat sheet for more details.
If backup is replicated to cloud storage, any local backup type will be converted to single-file backup on the cloud storage.
Every backup version is marked for retention based on the backup scheme. In case backup scheme creates weekly and monthly backups, they are marked according to the backup option of weekly backup. See more here.
Schedule also defines the backup sets, or how the backup version are grouped together for retention. See more here.
  #3 ► Retention rules. How retention rules work and which backups will be deleted?
Depending on the backup type and retention rules, only specific files or versions of backup will be deleted. Separate retention rules can be configured for different locations. How long to keep option specifies the retention rules:
By backup age: a backup set will be deleted based on its creation date. Different settings are available for different sets: hourly, daily, weekly and monthly.
Backup age - Single rule for all backups: This additional option will apply same rule for all backup sets.
By number: This is the maximum number of backup versions to be kept in the archive.
Indefinitely: No retention is configured, all backups are kept indefinitely.
Consolidation: It is the process of combining two or more subsequent backups into a single backup. It applies only to specific backup schemes and requires sufficient space and time to complete. See more here.
 
New KB articles
Acronis Backup Cloud
KB60700: Acronis Backup Cloud: "Volume Tracker has failed to open session"
KB60759: Acronis Backup Cloud plugin for LabTech: how to collect debug logs for LabTech plugin
KB60677: Acronis Backup: AdGuard causes issues with web console
KB60669: Acronis Backup: how to restore files from backups of NTFS volumes with Windows native Data Deduplication
KB60657: Acronis Backup Cloud: Non-ASCII characters are not displayed in usage reports
KB60655: Acronis Backup Cloud: CheckPoint Sand Blast extention for Google Chrome causes issues with web console
KB60629: Acronis Backup Cloud: newly created administrator cannot log in to backup console
KB60611: Acronis Backup Cloud: Event 513 in Windows Application Log during backup
KB60610: Acronis Backup Cloud: retention rules fail with "Internal error in library. The linked position is unknown." in build 4290
KB60606: Acronis Backup Cloud: retention rules fail with "Cannot free up space taken by the deleted backups. The operation will be retried during next backup deletion"
KB60597: Acronis Backup Cloud: the Size column is removed from the Web Recovery console
KB60593: Acronis Backup Cloud: agent registration fails with "Outgoing connections are not available for the following ports: hostname:44445"
Acronis Storage
KB60621: Acronis Storage: how to update Acronis Storage to the latest version
KB60663: Acronis Storage: "Cluster does not have CSes yet" error
See all new KB articles here: https://kb.acronis.com/new
Did you know that our quick troubleshooting kit is the easiest way to find all troubleshooting articles related to Acronis backup Cloud? See more here: https://kb.acronis.com/backup-cloud-known-solutions

 
New training materials
Acronis Data Cloud 7.5
Acronis Files Cloud
Acronis Disaster Recovery Cloud
See all training materials here: https://kb.acronis.com/MSPtraining
Did you know that certification only requires a basic 2-hour training and a 1.5-hour quiz? Those who have experience with the software successfully pass the exam with the first attempt and receive a verification certificate right away.
 

Datacenter and agent updates
Current agent versions:
Backup Agent for Windows (v.12.0.4496)
Backup Agent for Mac (v.12.0.4496)
Backup Agent for Linux (v.12.0.4499)

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
Let us know what else you would like to know about Acronis Service Provider products.
Share below your experience and your questions.

      
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/12/2017 - 07:41

                                                          
                                                            
                                                                                        
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
