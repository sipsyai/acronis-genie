# Acronis Cyber Protect 16: "Failed to find partition with uuid..."

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/acronis-cyber-protect-16-failed-find-partition-uuid

## Original Post
**Author:** Unknown

Acronis Cyber Protect 16: "Failed to find partition with uuid..."

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vadim Krasnyanskiy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            acrocmd recover disk --loc=... --arc=... --disk=1 --target_disk=1 --reboot --nt_signature=existing
Acronis Cyber Protect 15 works perfectly.  Acronis Cyber Protect 16: "Failed to find partition with uuid...". Any ideas?
Acronis 15
Acronis 16

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/19/2024 - 17:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Vadim!
Please review this KB and check if it applies to your situation: https://care.acronis.com/s/article/68859-Acronis-Cyber-Protect-Cloud-impossible-to-load-into-Acronis-boot-environment-during-forensic-backup-if-Bitlocker-is-enabled?language=en_US.
Also, make sure you are using the latest version of Acronis Cyber Protect 16.
I suggest recreating the bootable media as well.
If this is not related and the disk isn't locked, please contact the team so we can test and check the issue with you: https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Thu, 06/20/2024 - 07:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
