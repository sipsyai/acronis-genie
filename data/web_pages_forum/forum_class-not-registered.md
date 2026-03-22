# Class not registered

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/class-not-registered

## Original Post
**Author:** Unknown

Class not registered

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I got a customer running on Microsoft Windows Server 2012 R2 Standard and these two days the microsoft SQL backup is giving me class not registered  error and unable to backup straight from the SQL. But i have another backup running on that server which backup folders returns me a successful . Does anyone have a solution to it ?
MODULE 309
Additional info:------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"$line":"457","$func":"Tol::`anonymous-namespace'::MakeFailResult","$file":"e:\\571\\enterprise\\common\\tol\\command\\command.cpp","$module":"ervice_process_vsa64_14730","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"$line":"457","$func":"Tol::`anonymous-namespace'::MakeFailResult","$file":"e:\\571\\enterprise\\common\\tol\\command\\command.cpp","$module":"tob_backup_command_addon_vsa64_14730","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 103
Module: 623
LineInfo: 0x94F5F955B13DE060
Fields: {"$line":"198","$func":"`anonymous-namespace'::ApplicationBackupProcess::Execute","$file":"e:\\546\\enterprise\\applications\\managers\\gtob\\backuper.cpp","$module":"rsAgentProvider_vsa64_14800","IsReturnCode":"1"}
Message: A generic error of Microsoft SQL backup component.
------------------------
Error code: 271
Module: 87
LineInfo: 0x7F9E79F979CFBE98
Fields: {"$line":"149","$func":"MsSqlBackup::BackupSqlServer","$file":"e:\\546\\enterprise\\applications\\mssql\\managers\\gtob\\backuper\\src\\backuper_utils.cpp","$module":"rsAgentProvider_vsa64_14800","IsReturnCode":"1"}
Message: Failed to back up Microsoft SQL Server.
------------------------
Error code: 1713
Module: 349
LineInfo: 0xE821934A13FC0030
Fields: {"$line":"268","$func":"AppBackup::SnapApi::SnapapiBackupSession::CreateVssSnapshot","$file":"e:\\546\\enterprise\\applications\\technology\\snapapi\\src\\backup_session.cpp","$module":"rsDbBackupProvider_vsa64_14800"}
Message: Failed to process the shadow copy operation.
------------------------
Error code: 33
Module: 7
LineInfo: 0xE24F93D0B8D8C530
Fields: {"$line":"156","$func":"InitSnapshotBitmap","$file":"e:\\546\\core\\resizer\\generic\\snapinit.cpp","$module":"rsDbBackupProvider_vsa64_14800"}
Message: Failed to create volume snapshot.
------------------------
Error code: 50248
Module: 16
LineInfo: 0x3FEC04E376B8A224
Fields: {"$line":"1353","$func":"win_snapshot_core::AppendVolumesToSnapshot","$file":"e:\\546\\core\\fdisk\\win_snapshot.cpp","$module":"rsDbBackupProvider_vsa64_14800"}
Message: Failed to add the volume to the snapshot.
------------------------
Error code: 9
LineInfo: 0x02AACB7B2AB852A4
Fields: {"$func":"Fdisk::AddKstatusError","$line":"40","code":"2147746132","$file":"e:\\546\\core\\fdisk\\ver2\\arch\\windows\\win_errors.cpp","$module":"rsDbBackupProvider_vsa64_14800"}
Message: Unknown status.
------------------------
Error code: 65520
LineInfo: 0xBD28FDBD64EDB768
Fields: {"$func":"Common::Error::AddWindowsError","$line":"314","code":"2147746132","$file":"e:\\546\\core\\common\\error.cpp","$module":"rsDbBackupProvider_vsa64_14800"}
Message: Class not registered

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 12/16/2019 - 07:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Are you running the latest agent version? Might be related to https://kb.acronis.com/content/63821

      
                
                
                    
                                                    Mon, 12/16/2019 - 11:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yeah i am running on the latest version 12.5 14800. There is no prompt for update of the agent.

      
                
                
                    
                                                    Tue, 12/17/2019 - 00:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I also updated the agent through the Backup Console, but was still getting errors with MSSQL. I then downloaded the latest agent (Windows Server & MSSQL addon) and manually installed them in Windows using the Repair option.
After that, my backups completed successfully. 

      
                
                
                    
                                                    Tue, 12/17/2019 - 07:55
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks George for the idea, it solve the problem. For some reason, mine is not repair option . Instead it shows as update option. So i just update it and now my backup is able to complete, even at the backup console there is no available update for it .

      
                
                
                    
                                                    Tue, 12/17/2019 - 09:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Great to hear it's working for you now!

      
                
                
                    
                                                    Tue, 12/17/2019 - 21:42
