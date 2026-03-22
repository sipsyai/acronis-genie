# Acronis can't find existing backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cant-find-existing-backup

## Original Post
**Author:** Unknown

Acronis can't find existing backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dave White
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            When I go to to do an incremental backup, I get an error message that Acronis can't find the backup file. I have tried the "Add existing backup" and this does not help. I have to delete and start over.  This does not give me a lot of faith that I will be able to access the backup if recovery is needed. What is happening?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/27/2024 - 17:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
When such cases happen, it means that a backup file was deleted manually, which is unsupported, or the backup chain may be corrupt. Also if the backup is a NAS for example and the agent can't connect the error may appear. You should review your storage/NAS to ensure it is in good condition. Also, review your network connections, as bad connections may corrupt the files during the backup.
You should raise a ticket with the team when the issue happens so we can investigate: https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Tue, 05/28/2024 - 08:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
