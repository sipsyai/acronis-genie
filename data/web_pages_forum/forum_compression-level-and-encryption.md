# Compression Level and Encryption

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/compression-level-and-encryption

## Original Post
**Author:** Unknown

Compression Level and Encryption

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Filipe Mendes
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I'm using Acronis Cyber Protect Cloud and have attached my own storage backend to my Acronis Cyber Infrastructure (ACI). To optimize deduplication and compression in this setup, disabling compression and encryption can significantly improve efficiency.
Is there a way to configure Cyber Protect Cloud to enforce specific settings for tenants? Specifically:
Can I lock the compression level so that tenants cannot change it?
Can I disable the encryption option entirely for tenants, or is this always available for them to configure?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/22/2024 - 19:44

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Filipe,
Welcome to the forum.
Currently, there is no option to lock backup settings directly.
However, you can configure the desired backup settings for each tenant and then adjust user permissions to restrict their ability to modify the plans. This can be done by assigning appropriate roles to users.
You can find more information about user roles and permissions in the following documentation:
User Roles Available for Each Service
Best regards,

      
                
                
                    
                                                    Mon, 11/25/2024 - 14:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
