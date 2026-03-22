# Local backup of C2C app

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/local-backup-c2c-app

## Original Post
**Author:** Unknown

Local backup of C2C app

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Joshua Wisniewski
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, 
 
We currently backup our organizations emails to acronis (C2C). We are looking to bulk download our backups to a local location. I can't seem to find any options to do this. Is it even possible? I see options for using acrocmd, but this tool doesn't support C2C. 
Is there a way to have acronis download this data and ship it to us, or possibly a tool to download our backups to a local machine?
We will also consider 3rd party vendors, however, I cannot seem to find any options for this either. 
Thank you in advance!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 04/24/2024 - 15:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Joshua.
The C2C backups don't use a local agent. With this said, it's not possible to download them directly from the storage. You can simply restore them by following this user guide: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#recovering-mailbox-items.html
You can try to download the files/folders from the cloud: https://kb.acronis.com/content/36478
Regarding the physical data shipping, only the following backup types are supported:
Disk-level backups and file backups created by Agent for Windows, Agent for Linux, Agent for Mac, Agent for VMware, Agent for Hyper-V, and Agent for Virtuozzo are supported.
https://dl.managed-protection.com/u/physical-data-shipping/help/admin/en-US/index.html#cyber-protection-service.html#kanchor3
Best regards.

      
                
                
                    
                                                    Thu, 04/25/2024 - 10:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
