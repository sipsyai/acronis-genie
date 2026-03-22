# Exchange Back-up suddenly fails and cannot edit Job

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/exchange-back-suddenly-fails-and-cannot-edit-job

## Original Post
**Author:** Unknown

Exchange Back-up suddenly fails and cannot edit Job

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Martin Lion
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            a few days ago Exchange back-up suddenly stopped working and gives me an error (see below)
I am also unable to edit the exchange back-up job. Any clues for me how to solve this?
 
GXT: The item provider has skipped the report of an item with key '('ArxUri=arx%3a%2f%2fis%2fMailbox%2520Database%25200727138697','arx::gct::database_2016')'.
MODULE
307
BERICHT
Cannot resolve inclusion rule '('ArxUri=arx%3a%2f%2fis%2fMailbox%2520Database%25200727138697','arx::gct::database_2016')'.

Aanvullende informatie:
------------------------
Foutcode : 67
Module: 307
Regelinformatie: 0x7409A54C3CC8E41E
Velden: {"$module":"agent_protection_addon_vsa64_3539"}
Bericht: Cannot resolve inclusion rule '('ArxUri=arx%3a%2f%2fis%2fMailbox%2520Database%25200727138697','arx::gct::database_2016')'.
------------------------
Foutcode : 1
Module: 307
Regelinformatie: 0x7409A54C3CC8E3D1
Velden: {"$module":"agent_protection_addon_vsa64_3539"}
Bericht: GXT: The item provider has skipped the report of an item with key '('ArxUri=arx%3a%2f%2fis%2fMailbox%2520Database%25200727138697','arx::gct::database_2016')'.
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/31/2016 - 22:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ilya Stepanov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mr. Lion,
Please be informed that based on the provided output (namely the string "agent_protection_addon_vsa64_3539"}" I can conclude that you are using 3539 build of the Agent.
Let me inform you that the current (newest) build of the Agent is 3917.
New build is known to improve speed and stability of many operations as well as provide some fixes for several known issues.
I would suggest you update the Agent first and then check if the issue persists.
If the issue is still reproduced, then please contact Support.
Here are the links to 3917 build
All agents for Windows (32-bit)  453 MB               
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Windows.exe
All agents for Windows (64-bit)  512 MB           
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Windows_x64.exe
Agent for Windows                         13.7 MB          
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Windows_web.exe
Agent for Linux (32-bit)                304 MB           
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Linux_x86.bin
Agent for Linux (64-bit)                                323 MB           
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Linux_x86_64.bin
Agent for Mac OS (64-bit)            169 MB           
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_MAC_x64.dmg
Agent for SQL                                  13.7 MB          
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_SQL_web.exe
Agent for Exchange                         13.7 MB          
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_Exchange_web.exe
Agent for Active Directory           13.7 MB          
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_AD_web.exe
Bootable media                                 190 MB           
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Boot_media.iso
--
Warm regards,
Ilya Stepanov

      
                
                
                    
                                                    Sun, 01/01/2017 - 08:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Martin Lion
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ilya,
when ik check the link it wants to install 12.0.3894
I have allready version 12.0.3917 installed. So i don't understand exactly where things are going wrong. I allready tried to remove all agents and install them again. It didn't work.
I have attached a screenshot showing the versions
Best regards,
Martin

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      401524-135886.png

                      6.56 KB
                  
          
    

                    
    
                
                
                    
                                                    Sun, 01/01/2017 - 13:06
