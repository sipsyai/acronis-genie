# Removing prior O365 C2C V1 agent?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/removing-prior-o365-c2c-v1-agent

## Original Post
**Author:** Unknown

Removing prior O365 C2C V1 agent?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Bonzo King
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Is it possible to remove the prior O365 Cloud-to-Cloud agent that was installed prior to the 7.8 update? Our account currently has both, and I don't see an option to remove the V1 agent, which is the older one. In return, I cannot seem to login to it following the installation of the new C2C.
Any suggestions are appreciated.
Thanks

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      C2C.png

                      5.54 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 01/21/2019 - 20:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
 
It's Evgeny from Acronis Service Provider Support.
After you configure the new cloud-to-cloud backup, delete backup plans for the previous version to stop backup jobs and, in the case of per-device pricing, avoid billing for the previous backup installation.
 Go to the Devices -> Microsoft Office 365 V1 tab and delete the backup plans applied to the items.

Only if you want to keep your old Office 365 backup archives and be able to recover Office 365 data using them: After you disable the C2C 1.0 backup plans, your Office 365 archives are not affected. It’s your choice how long to keep them in cloud storage. But please note that you will still be billed for the Acronis cloud storage these backups occupy. To be able to perform a future recovery using these backups, you need to keep the C2C 1.0 agent installed in Acronis data center.
Or, if you want to completely delete old backups and the old C2C 1.0 agent:
Delete old backup archives in the Backups tab.
Create a support ticket that contains the C2C 1.0 agent deletion request.

Additional details about moving from C2C 1.0 to new C2C 2.0 are described in
https://kb.acronis.com/content/61993
-----------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Tue, 01/22/2019 - 09:04
