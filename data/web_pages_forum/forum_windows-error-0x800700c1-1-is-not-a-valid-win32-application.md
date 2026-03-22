# Windows error: (0x800700C1) %1 is not a valid Win32 application

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/windows-error-0x800700c1-1-not-valid-win32-application

## Original Post
**Author:** Unknown

Windows error: (0x800700C1) %1 is not a valid Win32 application

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            i have updated to the last version and error continue.
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"mms_vsa64_10790"}
Message: TOL: Failed to execute the command. Backup plan 'CL009'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"agent_protection_addon_vsa64_10790"}
Message: TOL: Failed to execute the command. Backup plan 'CL009'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE2C
Fields: {"$module":"agent_protection_addon_vsa64_10790"}
Message: Failed to execute the command.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"mms_vsa64_10790"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"gtob_backup_command_addon_vsa64_10790"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 2
Module: 329
LineInfo: 0x8EDC81EA38FABAA4
Fields: {"TraceLevel":"1","StepType":"1","$module":"gtob_backup_command_addon_vsa64_10790"}
Message: Step 'Pre-backup command execution' has failed.
------------------------
Error code: 6
Module: 329
LineInfo: 0xB834ECE096B0F45F
Fields: {"$module":"gtob_backup_command_addon_vsa64_10790"}
Message: The pre- or post-backup command has been executed with an error.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"73417128-5DAC-4263-83CD-4332EF280E7B","$module":"mms_vsa64_10790"}
Message: TOL: Failed to execute the command. Executing pre-backup command
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"73417128-5DAC-4263-83CD-4332EF280E7B","$module":"disk_bundle_vsa64_10790"}
Message: TOL: Failed to execute the command. Executing pre-backup command
------------------------
Error code: 1015
Module: 1
LineInfo: 0x858CC05F488A8DC8
Fields: {"$module":"mms_vsa64_10790"}
Message: Failed to run a child process.
------------------------
Error code: 65520
Module: 0
LineInfo: 0xBD28FDBD64EDB8F1
Fields: {"$module":"mms_vsa64_10790","code":"2147942593"}
Message: %1 is not a valid Win32 application
Download log 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/09/2018 - 11:31

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hello, Suporte!
 
thanks for posting again.
The error stack that you have shared indicates that the backup plan of this user contains pre-backup command (read more here).
Execution of this command fails.
Perhaps, the command was intended for Linux devices but the plan is applied to a Windows device?
 
You also said that you have updated the agent but the issue persists. Was it already reported to the Support team for proper investigation? Are you following up on an existing thread?
I just want to see the whole picture.
Let us know what exactly the plan is intended to do, what are the contents of the pre-backup commands. PM me the login name of such user, I may have a look!

      
                
                
                    
                                                    Thu, 10/11/2018 - 11:55
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Fedor, the problem was  really on Pre-backup . 
 
 
 

      
                
                
                    
                                                    Thu, 10/11/2018 - 23:40
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud
