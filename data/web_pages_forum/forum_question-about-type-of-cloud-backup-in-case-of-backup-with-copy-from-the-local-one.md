# Question about type of cloud backup in case of backup with copy from the local one.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/question-about-type-cloud-backup-case-backup-copy-local-one

## Original Post
**Author:** Unknown

Question about type of cloud backup in case of backup with copy from the local one.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, I noticed a substantial difference which I would like to be sure.
In a unique backup plan with  weekly chain (1 complete and other incremental for week) and cloud copy with backup format 11 the cloud copy is always incremental (even if type of local backup is not always incremental in single file) and with format 12 is the simply an upload of the local backups as it is?
Thanks for any reply and sorry for my bad english.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/23/2019 - 15:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kevin Johnston
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            As far as I understand, Always Incremental jobs are not possible on Format 11, and also not available to the cloud.
I believe your concern is related to how the backups are stored?
Always Incremental jobs are stored in a single archive file. The Full/Incremental scheme will store backups in multiple files like you'd expect for other backup products.
The benefit is that it would save time in the event of removing old backups.
Check out the Web Help link here: https://www.acronis.com/en-us/support/documentation/AcronisBackup_12.5/…

      
                
                
                    
                                                    Mon, 07/29/2019 - 14:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio,
to my knowledge, when backing up to Cloud, Acronis Backup always uses single-file archive format (always incremental backup) - a new backup format, in which the initial backup is full and all subsequent backups are incremental, regardless of the backup format used to create local copies. 
If you are replicating archives of format 12 to Cloud, the data from the local archives will be backed up anew (replication to Cloud is not a simple copy of local archives, but the complete re-backup) 

      
                
                
                    
                                                    Mon, 07/29/2019 - 16:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:
If you are replicating archives of format 12 to Cloud, the data from the local archives will be backed up anew (replication to Cloud is not a simple copy of local archives, but the complete re-backup) 
 

Thanks for reply,  I don't know if I understood this part well...
From what I saw in practice having a unique backup plan of full system (local + cloud copy) with weekly chain as backup type (one weekly complete backup and other incremental) and 1 month history on both local and cloud about the cloud copy seems that do:
- with format 11 on cloud not a simple copy but backup always incremental (probably what you write above)
- with format 12 on cloud do a full copy of all backup present locally.
I'll try to explain better with  a hypothetical example:
A device that have always 100gb if full backup and 1gb incremental each days, local backup will be 106gb each week, 424gb full backup repository after 1 month of 4 week, with cloud based on my experience will be:
- with format 11 will be 127gb of full backup repository cloud
- with format 12 will be 424gb of full backup repository cloud
and will be also different back/copy to cloud time, on both long for the first time and after:
- with format 11 always short time
- with format 12 long time like full backup one time a week, the same day/backup when is full for the local one.
In conclusion seems to me that with format 11 cloud backup is not do a simply copy of local but "re-backup" always incremental and with format 12 a copy of local one, but from your sentence it seems that you say the opposite, isn't it?
Thanks for any reply.

      
                
                
                    
                                                    Wed, 07/31/2019 - 13:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio,
I've clarified your question with the expert team and here the verified information my colleagues shared:
Archive replication to a second location (no matter Cloud or local) is always re-backup (regardless of the archive format in use), not just a copy. This helps to keep a replicated archive consistent. As the result, backup plans to Cloud Storage or replication to Cloud Storage always use "Always incremental" backup scheme.
Other schemes (like "Weekly full, Daily incremental" or "Custom") are available only to a non-Cloud locations.
Resulting archive size depends on different things, such as (but not limited to):
- retention rules scheme
- Storage (in case of Partner-hosted) back-end file-system type\support  of punch-holes and file sparse technology. which help to reduce file size after backups clean-up
- type of backup (file or disk-level backup) disk-level allows to use incremental jobs more effectively

      
                
                
                    
                                                    Mon, 08/26/2019 - 08:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
