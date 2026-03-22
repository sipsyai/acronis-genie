# Unable to Install Backup Agent on Server 2012 R2

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/unable-install-backup-agent-server-2012-r2

## Original Post
**Author:** Unknown

Unable to Install Backup Agent on Server 2012 R2

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Taylor Maneri
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi Everyone,
I Have tried two different servers in my organization, both fail with the same error. Any insight on how to fix?
Faulting application name: Backup_Agent_for_Windows_web.exe, version: 12.0.1.3917, time stamp: 0x58517521
Faulting module name: Backup_Agent_for_Windows_web.exe, version: 12.0.1.3917, time stamp: 0x58517521
Exception code: 0xc0000005
Fault offset: 0x0054cbaa
Faulting process id: 0x1890
Faulting application start time: 0x01d3231c53b1d821
Faulting application path: C:\Users\administrator.WAGER\AppData\Local\Microsoft\Windows\INetCache\IE\OR0F2E90\Backup_Agent_for_Windows_web.exe
Faulting module path: C:\Users\administrator.WAGER\AppData\Local\Microsoft\Windows\INetCache\IE\OR0F2E90\Backup_Agent_for_Windows_web.exe
Report Id: a5f2b34a-8f0f-11e7-80d6-00155d01f003
Faulting package full name:
Faulting package-relative application ID: 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/01/2017 - 12:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Taylor!
You haven't mentioned what error message you saw on both server, but I can provide you with some general information about issues with installers.
 
From the technical information that you have pasted I can only see that you are using the Web Installer.
Web Installer has to download it's components from our Data Center, so it you are blocking any IPs or ports, it would fail to download the components, please the full installer instead:
All agents for Windows (32-bit) 
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_…
All agents for Windows (64-bit)
http://dl.managed-protection.com/u/baas/4.0/12.0.3917/Backup_Agent_for_…
 
Please share the error message text and a screenshot of how it looks if the above does not help!

      
                
                
                    
                                                    Mon, 09/04/2017 - 07:45
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
