# Best way to do immutable backups with cyber protect

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/best-way-do-immutable-backups-cyber-protect

## Original Post
**Author:** Unknown

Best way to do immutable backups with cyber protect

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Marvin Ruiz
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
What’s the best way to create immutable backups when using cyber protect? Seems they’ve now direct integration to wasabi via their advanced pack but they don’t support immutable for wasabi. You can configure ‘s3 compatible’ and enter Wasabi creds and then turn on the immutable option that way. Did it that way run a backup job but not immutable at all..
Any tips?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/24/2025 - 04:13

                                                          
                                                            
                                                                                        
    
                    
                ...

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello and Welcome to the Forum!
Here’s some important information regarding Immutable Storage support and requirements:
Supported Storages and Agents

Supported Storages:
Immutable storage is supported only on cloud storage.
Available for Acronis-hosted and Partner-hosted cloud storages using Acronis Cyber Infrastructure version 4.7.1 or later.
Compatible with storages integrated with the Acronis Cyber Infrastructure Backup Gateway, including:
Acronis Cyber Infrastructure storage
Amazon S3 and EC2
Microsoft Azure



Port Requirements:
TCP port 40440 must be open for the Backup Gateway service in Acronis Cyber Infrastructure.
For version 4.7.1 and later, this port is automatically opened with the Backup (ABGW) public traffic type. Refer to the Acronis Cyber Infrastructure documentation for details on traffic types.


Agent and Backup Compatibility:
Requires protection agent version 21.12 (build 15.0.28532) or later.
Only TIBX (Version 12) backups are supported.

For detailed guidance, refer to the Immutable Storage Documentation.
If you’ve met all prerequisites but still cannot enable the feature, please contact your support team or Managed Service Provider (MSP) to investigate further.
Thanks!

      
                
                
                    
                                                    Fri, 01/24/2025 - 10:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
