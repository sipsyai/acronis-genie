# Do local agent credentials need to possess access to Azure storage account?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/do-local-agent-credentials-need-possess-access-azure-storage-account

## Original Post
**Author:** Unknown

Do local agent credentials need to possess access to Azure storage account?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tony B
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am inheriting a setup that was mostly working with some backups going to Acronis Cloud and others to an Azure storage account.  The latter is encountering issues with either access denial (credentials) or not able to perform operations even with contributor role assigned.  I am trying to theorize some options with this as ACP is all new to me though I am familiar with managing agent/monitoring (RMM).  My googlefu is not helping me out here so I am wondering if anyone has any pointers.  (Basically, what creds do I need and where should I plug them in?)
 
TIA

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 09/06/2023 - 16:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Tony,
You mentioned that the tenant was inherited. Please note that all tenants are linked to their respective storages. Azure implementation requires Acronis Cyber Infrastructure. If you have only inherited the tenant and not the infrastructure, it's normal that you can't execute backups directed to that storage. You will need to deploy an infrastructure yourself or request the credentials for their infrastructure. Please be aware that adding a new storage to existing tenants is not possible if backups are already stored there.
I recommend reaching out to our support team or your service provider to open a ticket for more information and guidance: https://kb.acronis.com/content/8153.
Thanks in advance!

      
                
                
                    
                                                    Thu, 09/07/2023 - 12:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
