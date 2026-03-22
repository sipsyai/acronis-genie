# ArchivePersistentCache folder

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/archivepersistentcache-folder

## Original Post
**Author:** Unknown

ArchivePersistentCache folder

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mike
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            What is the ArchivePersistentCache folder \ files contained in it used for? Wanting to know if it is fine to clear as this is starting to fill up my system drive (about 600-700GB so far).
C:\ProgramData\Acronis\ArchivePersistentCache\*randomcharacterfoldernames
Haven't had any luck finding articles around this. Any details and help around this would be much appreciated.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/19/2024 - 23:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
The ArchivePersistentCache folder in Acronis Cyber Protect is used to store temporary data related to archive indexing, deduplication, or backup processes, depending on the specific configuration of your backup plan. This cache helps improve the performance of backups and restore operations by storing metadata or pre-processed data for faster access.
Key Points About the Folder:

Purpose: It holds persistent cache data that might be required for optimizing certain backup and restore operations. It is particularly important when deduplication or archive-related tasks are involved.


Size Management: While it can grow large depending on backup configurations and the amount of data processed, such a large size (600-700GB) is unusual and may indicate a configuration issue or old/unnecessary cache data not being cleared automatically.


Clearing the Folder:
Is it safe to clear? Generally, it is safe to delete the contents of this folder. However, doing so may temporarily impact the performance of backups or restores until the cache is rebuilt.
Precautionary Steps: Before clearing, ensure:
No backup or restore operations are currently running.
The system and backups are working properly after the folder is cleared.

How to clear: Stop Acronis-related services, delete the folder contents, and restart the services.


Preventative Measures:
You can manage the folder size by reviewing your backup configurations. Check if deduplication is enabled or if there are logs/configurations causing excessive growth.
Ensure you’re running the latest build of Acronis Cyber Protect, as updates may include fixes for excessive cache growth.

Next Steps:
If the folder continues to grow uncontrollably or clearing it doesn’t help, consider raising a support ticket with Acronis to investigate further. Provide logs and details about your backup configurations to help diagnose the root cause.

      
                
                
                    
                                                    Wed, 11/20/2024 - 15:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
