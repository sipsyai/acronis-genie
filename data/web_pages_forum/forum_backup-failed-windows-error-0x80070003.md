# Backup failed Windows error: (0x80070003)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-failed-windows-error-0x80070003

## Original Post
**Author:** Unknown

Backup failed Windows error: (0x80070003)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            when backup starts shows up this error .
 
Error
DATE AND TIME
Sep 05, 2018, 13:53:25
MODULE
309
MESSAGE

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"mms_vsa64_10330"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"gtob_backup_command_addon_vsa64_10330"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"mms_vsa64_10330"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"D77E80BD-410A-468E-B593-FC8467A0D91B","$module":"service_process_vsa64_10330"}
Message: TOL: Failed to execute the command. Running Python script
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"D77E80BD-410A-468E-B593-FC8467A0D91B","$module":"pybind_tol_supp_vsa64_10330"}
Message: TOL: Failed to execute the command. Running Python script
------------------------
Error code: 1
Module: 573
LineInfo: 0x2020586611746950
Fields: {"$module":"pybind_tol_supp_vsa64_10330"}
Message: Failed to run Python script 'pyvfs:staging?calculate_backup_set'.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"3CC14D08-3D75-46C4-AB00-431B0E3868A3","$module":"mms_vsa64_10330"}
Message: TOL: Failed to execute the command. Getting information about backups
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"3CC14D08-3D75-46C4-AB00-431B0E3868A3","$module":"staging_command_vsa64_10330"}
Message: TOL: Failed to execute the command. Getting information about backups
------------------------
Error code: 3
Module: 630
LineInfo: 0x4EE55196063E87BD
Fields: {"$module":"staging_command_vsa64_10330"}
Message: Cannot get access to the user profile.
------------------------
Error code: 13
Module: 627
LineInfo: 0xE839411589F18B52
Fields: {"$module":"access_manager_vsa64_10330"}
Message: Access violation in module 'staging_command.dll' at line '0x4ee55196063e87bd', executable: 'mms.exe'.
------------------------
Error code: 45
Module: 4
LineInfo: 0xF35F747B3B21F916
Fields: {"function":"OpenFileW","path":"\\\\?\\C:\\ProgramData\\Acronis\\BackupAndRecovery\\MMS\\AccessVault\\profiles\\2D607956-00D2-0B61-90B1-0900B8FFC724\\lock","$module":"access_manager_vsa64_10330"}
Message: The specified file path does not exist.
------------------------
Error code: 65520
Module: 0
LineInfo: 0xBD28FDBD64EDB8F1
Fields: {"$module":"access_manager_vsa64_10330","code":"2147942403"}
Message: O sistema não pode encontrar o caminho especificado

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      logs (14).zip

                      2 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 09/05/2018 - 17:03

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! 
It's Evgeny from Acronis Service Provider Support.
 
The error looks as the one described within the following KB article: 
 
Could you please check the solution for error 1 to confirm this resolves the issue?
 
If it still reproduces, please submit a support ticket as per the Service Providers guidelines so  that we can assist you further in finding the root cause.
 
If you have any questions, please feel free to ask.
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Thu, 09/06/2018 - 08:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If i  reinstall and delete the database , will work the same way?
 
Thanks.

      
                
                
                    
                                                    Tue, 09/25/2018 - 20:23
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud
