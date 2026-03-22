# Agent installation failure

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/agent-installation-failure

## Original Post
**Author:** Unknown

Agent installation failure

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Naboth Semwayo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I just signed up for a trial Cloud Backup account: https://baas.acronis.com/
I have had problems installing the agent on my computer using both web installer and full download and its rather disappointing as I am looking at adding this to my MSP offerings. keep getting the error below - can you help please:
=== Verbose logging started: 23/08/2015  1:43:34  Build type: SHIP UNICODE 5.00.9600.00  Calling process: C:\Users\Naboth\Downloads\Backup_Agent_for_Windows_x64_en-US.exe ===
MSI (c) (68:34) [01:43:34:663]: Resetting cached policy values
MSI (c) (68:34) [01:43:34:739]: Machine policy value 'Debug' is 0
MSI (c) (68:34) [01:43:34:818]: ******* RunEngine:
           ******* Product: C:\Users\Naboth\AppData\Local\Temp\55CB07E0-6714-49EE-B1DA-D9BB90D3DBF2\BackupClient64.msi
           ******* Action:
           ******* CommandLine: **********
MSI (c) (68:34) [01:43:34:846]: Client-side and UI is none or basic: Running entire install on the server.
MSI (c) (68:34) [01:43:35:000]: Grabbed execution mutex.
MSI (c) (68:34) [01:43:38:726]: Cloaking enabled.
MSI (c) (68:34) [01:43:38:820]: Attempting to enable all disabled privileges before calling Install on Server
MSI (c) (68:34) [01:43:38:855]: Incrementing counter to disable shutdown. Counter after increment: 0
MSI (c) (68:34) [01:43:38:955]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
MSI (c) (68:34) [01:43:39:052]: MainEngineThread is returning 1618
=== Verbose logging stopped: 23/08/2015  1:43:39 ===
Regards
Semmy

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 08/22/2015 - 16:02

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Semmy,
Thank you for posting your question here. I'll be glad to assist.
The last MSI log line
    MSI (c) (68:34) [01:43:39:052]: MainEngineThread is returning 1618
means the following:
    Another installation is already in progress. Complete that installation before proceeding with this install.
Which means you will see a running msiexec.exe process in Task Manager and this prevents the Backup Agent from installation. In fact, you can try to install any other software with Microsoft Installer, and it will give you the same output.
To solve the problem you can cancel the running update/installation process. If you are not sure what it being installed (it can go in the background), you can kill the msiexec.exe process. But I would recommend to simply restart the system to ensure all processes are stopped correctly.
Let me know if you have more questions, and provide the new MSI log in case you get another error.
Best regards,

      
                
                
                    
                                                    Mon, 08/24/2015 - 08:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
