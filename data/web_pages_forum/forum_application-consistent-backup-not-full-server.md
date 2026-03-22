# Application consistent backup, not full server

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/application-consistent-backup-not-full-server

## Original Post
**Author:** Unknown

Application consistent backup, not full server

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ivo ITC
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            It has been a while since I had to create or change settings in Acronis.
A client has just joined our services.
They have a server with quite a large amount of data.
I would like to install Acronis on it, just for their SQL data and AD.
However, I can only select application consistent backups when I select Full Server backup.
This would result in a large amount of data needing to be uploaded to the cloud, which they don't have the internet connection for.
Is there any other way I can do an application consistent backup without doing a full server backup?
I have used the search button, but I might have put in the wrong search options as it did not come back with any usable results.
 
Thank you.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/26/2019 - 16:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ivo ITC,
it's possible to create backups of SQL databases, if an Agent for SQL is installed on the machine with the SQL. Check out https://www.acronis.com/en-us/support/documentation/BackupService/index.html#33572.html
A machine running Active Directory Domain Services can be protected by application-aware backup only.

      
                
                
                    
                                                    Sat, 03/30/2019 - 20:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
