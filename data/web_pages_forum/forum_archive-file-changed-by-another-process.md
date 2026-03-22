# Archive File Changed by another process

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/archive-file-changed-another-process

## Original Post
**Author:** Unknown

Archive File Changed by another process

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Moreland
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have 10 VMs that i backup regularly.  I have 2 of the 10 VM's that fail constantly and give the same error "archive file was change by another process."  I'm not sure why.  The only way i can get the server to backup with out errors is to restart the backup maybe 5 or 7 times until it finally completes.  Below is the latest error I received on one of the 2 Problem child VM's:
Archive file was changed by another process
MESSAGE
Archive file was changed by another process

Additional info:
------------------------
Error code: 20250646
Fields: {"$module":"service_process_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 20250646
Fields: {"$module":"gtob_backup_command_addon_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 21561347
Fields: {"$module":"disk_bundle_vsa64_31791"}
Message: Backup has failed.
------------------------
Error code: 66596
Fields: {"$module":"disk_bundle_vsa64_31791"}
Message: Failed to commit operations.
------------------------
Error code: 43717531
Fields: {"$module":"disk_bundle_vsa64_31791","function":"archive_stream_write_shbuf","path":"\\\\?\\UNC\\acronis\\k\\\\FS1.HIGHPOINT.LOCAL-F68032C9-0C11-432E-91C5-42D802216578-200052E8-8AC8-4964-BCBE-570A99821138A.tibx"}
Message: Archive file was changed by another process
------------------------

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 08/23/2023 - 22:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! Kevin!
Welcome to the forum.
It appears that you're encountering a series of error codes while using Acronis Cyber Protect Cloud for backup operations. The error messages you've provided indicate that the backup process has encountered issues at various stages. Here's a breakdown of the error codes and their potential causes:

Error code: 20250646 This error code suggests that the command to add a backup task failed. The provided message "TOL: Failed to execute the command. Backing up" indicates that the command execution for the backup task encountered an issue. This could be due to various factors such as incorrect configuration, resource limitations, or conflicts with other ongoing operations.


Error code: 21561347 Error code 21561347 points to a general backup failure. The message "Backup has failed" indicates that the backup process itself could not be completed successfully. This could be caused by issues with data integrity, hardware failures, or connectivity problems.


Error code: 66596 This error code signifies a failure to commit operations. It's likely that the backup process encountered an issue during the finalization stage, preventing the changes made during the backup from being properly saved. This could be due to file system issues, disk errors, or resource constraints.


Error code: 43717531 The error message "Archive file was changed by another process" indicates that the backup archive file is being modified or accessed by another application or process while Acronis Cyber Protect Cloud is attempting to perform the backup operation. This interference from another process can lead to data inconsistency and cause the backup to fail.

Given the complexity and variety of these errors, it's recommended to perform the following troubleshooting steps:

Review Configuration: Double-check your backup task configuration to ensure it's set up correctly, including source and destination paths, schedules, and any additional settings.


Resource Check: Verify that your system has sufficient resources (disk space, memory, CPU) to complete the backup operation.


Check for Interference: Make sure that there are no other applications or processes accessing the backup files during the backup process. This is essential. 


Check Disk Health: Verify the health of the source and destination disks. Disk errors can lead to backup failures. https://learn.microsoft.com/en-us/windows-server/administration/windows…


Update Software: Ensure that you are using the latest version of Acronis Cyber Protect Cloud, as updates often include bug fixes and improvements.


Make sure the backup isn't corrupted: https://kb.acronis.com/content/67908


Contact Support: https://kb.acronis.com/content/8153

Feel free to reply if you have any questions.
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/28/2023 - 15:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
