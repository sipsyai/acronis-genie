# Server Agent Installation has failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/server-agent-installation-has-failed

## Original Post
**Author:** Unknown

Server Agent Installation has failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Serhat Hergüner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
I was trying to install Server agent but gave me a warning that is "install was not successful" when its finished.
Server information is Windows Server 2008 R2 Standard and currently .NET Framework version is 4.7.
Please Could you help me? 
 
=== Verbose logging started: 8/17/2017  13:09:36  Build type: SHIP UNICODE 5.00.7601.00  Calling process: C:\Users\Administrator\Downloads\Backup_Agent_for_Windows_web (2).exe ===
MSI (c) (80:84) [13:09:36:215]: Resetting cached policy values
MSI (c) (80:84) [13:09:36:215]: Machine policy value 'Debug' is 0
MSI (c) (80:84) [13:09:36:215]: ******* RunEngine:
           ******* Product: C:\Users\ADMINI~1\AppData\Local\Temp\4\377A1135-4072-445A-A803-2A0340CE40EF\BackupClient64.msi
           ******* Action: 
           ******* CommandLine: **********
MSI (c) (80:84) [13:09:36:215]: Client-side and UI is none or basic: Running entire install on the server.
MSI (c) (80:84) [13:09:36:230]: Grabbed execution mutex.
MSI (c) (80:84) [13:09:36:355]: Cloaking enabled.
MSI (c) (80:84) [13:09:36:355]: Attempting to enable all disabled privileges before calling Install on Server
MSI (c) (80:84) [13:09:36:371]: Incrementing counter to disable shutdown. Counter after increment: 0
MSI (s) (70:AC) [13:09:36:402]: Running installation inside multi-package transaction C:\Users\ADMINI~1\AppData\Local\Temp\4\377A1135-4072-445A-A803-2A0340CE40EF\BackupClient64.msi
MSI (s) (70:AC) [13:09:36:402]: Grabbed execution mutex.
MSI (s) (70:F0) [13:09:36:402]: Resetting cached policy values
MSI (s) (70:F0) [13:09:36:402]: Machine policy value 'Debug' is 0
MSI (s) (70:F0) [13:09:36:402]: ******* RunEngine:
           ******* Product: C:\Users\ADMINI~1\AppData\Local\Temp\4\377A1135-4072-445A-A803-2A0340CE40EF\BackupClient64.msi
           ******* Action: 
           ******* CommandLine: **********
MSI (s) (70:F0) [13:09:36:418]: Note: 1: 2203 2: C:\Users\ADMINI~1\AppData\Local\Temp\4\377A1135-4072-445A-A803-2A0340CE40EF\BackupClient64.msi 3: -2147286960 
MSI (s) (70:F0) [13:09:36:418]: MainEngineThread is returning 1620
MSI (s) (70:AC) [13:09:36:433]: User policy value 'DisableRollback' is 0
MSI (s) (70:AC) [13:09:36:433]: Machine policy value 'DisableRollback' is 0
MSI (s) (70:AC) [13:09:36:433]: Incrementing counter to disable shutdown. Counter after increment: 0
MSI (s) (70:AC) [13:09:36:433]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
MSI (s) (70:AC) [13:09:36:433]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
MSI (s) (70:AC) [13:09:36:433]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\InProgress 3: 2 
MSI (s) (70:AC) [13:09:36:433]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\InProgress 3: 2 
MSI (s) (70:AC) [13:09:36:433]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
MSI (s) (70:AC) [13:09:36:433]: Restoring environment variables
MSI (c) (80:84) [13:09:36:433]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
MSI (c) (80:84) [13:09:36:433]: MainEngineThread is returning 1620
=== Verbose logging stopped: 8/17/2017  13:09:36 ===

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 08/17/2017 - 11:54

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Serhat Hergüner!
The part of the log that you have shared does not contain any hint of the error message nor it's possible causes, could you please attach the full log?
I would also advise you to run the full installer instead of a Web-version to rule out any connection related issues.
To get a full installer, click on the user picture (where you would be able to log out) and select Downloads, the full installer is one of the first two links.
 
Please let me know how it goes!

      
                
                
                    
                                                    Thu, 08/17/2017 - 13:07
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
