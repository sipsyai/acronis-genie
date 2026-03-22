# 2019 core Hyper-V agent install fail with unrelated missing AD error

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/2019-core-hyper-v-agent-install-fail-unrelated-missing-ad-error

## Original Post
**Author:** Unknown

2019 core Hyper-V agent install fail with unrelated missing AD error

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Victor Pelletier
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, this is my first post 
Prior to this post I had search the web and also opened a ticket with our acronis reseller. See below the last couple of line of the installation log.
Server is a 2019 core (no UI) with Hyper-V rôle. It will never be linked to AD nor get AD rôle so the error I get may be unrelated.
command line I'm using : msiexec /i AB64.msi /qb /l*v install.log
 
--------------------------------------------------------------------------------------------------------------------------------------------------
Action start 09:05:46: MsiAdAgentInstall_ARADAgentCommon__IP.
1: e:\399\enterprise\applications\technology\install\custom_dll_core\common.cpp line: 52 `anonymous-namespace'::MsiHandlerWrapperImpl Microsoft Active Directory is not installed on the machine.
Additional info: 
--------------------
Error code: 301
Module: 555
LineInfo: 616cda42bf9dd4dc, e:\399\enterprise\applications\ad\agent\install\component\custom_dll\main.cpp, `anonymous-namespace'::CheckADInstalled, 33
Fields:  $module : custom_actions_ab_vsa64_s_13400
Message: Microsoft Active Directory is not installed on the machine.
-------------------- 
MSI (s) (20!78) [09:05:46:197]: Note: 1: 2262 2: Error 3: -2147287038 
MSI (s) (20!78) [09:05:46:197]: Product: Acronis Backup -- Microsoft Active Directory is not installed on the machine.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/28/2019 - 13:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Victor,
thank you for your posting! The error message usually comes when installer can't properly detect the Active Directory on the device although the Agent for Active Directory (the component ARADAgentFeature) is being forced with the installation.
I'd suggest trying to run the command with the exact components specified (here under More information you'll find an example https://kb.acronis.com/content/57107)

      
                
                
                    
                                                    Fri, 06/07/2019 - 16:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
