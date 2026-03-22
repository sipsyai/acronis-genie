# Incremental, differential, dedup?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/incremental-differential-dedup

## Original Post
**Author:** Unknown

Incremental, differential, dedup?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lars Schärer
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Does anybody know how Acronis Backup Cloud backups the ongoing jobs?
For instance if I create a backup job for the entire machine how will the second, third (and so on) job go though?
Until now I didnt find any options to select the backup method.
Thank you for your help

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 04/04/2017 - 13:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Lars,
Welcome to Acronis user forums! When you back up your data to Cloud, a default scheme "always incremental" is always used. The first backup will be full and then only incremental changes are written to the archive. Here you can read more about "always incremental" archive and on how retention rules work with cloud backups. You cannot change the backup scheme for Cloud storage as it's dependent on the archive type used to store data on datacenters, only configure schedule and cleanup policy. 
What do you mean under "backups the ongoing jobs"? If a backup of the entire PC is in progress, all tasks where the same data are selected as backup source will wait untill the running task has been finished. 

      
                
                
                    
                                                    Thu, 04/06/2017 - 07:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
