# Network connection failed due to timeout.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/network-connection-failed-due-timeout

## Original Post
**Author:** Unknown

Network connection failed due to timeout.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Support Frema
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
After a move to a new office we get an Network connection failed due to timeout often.
This happens on multiple servers and on different backup plans, also this doesn't happen al the time.
After the move the external IP has changed, in the local network nothing has changed.
Can someone point me in the right direction?
Context:
Network connection failed due to timeout.
Date and time
Jun 26, 2020, 01:33:11
Module
309
Message
Backup failed
Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"ms_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Backup plan 'Servers Systeemstatus'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"gent_protection_addon_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Backup plan 'Servers Systeemstatus'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DF38
Fields: {"$line":"234","$module":"gent_protection_addon_vsa64_22750","$file":"e:\\275\\enterprise\\managers\\gtob\\protection\\agent_engine\\protect_command.cpp","$func":"`anonymous-namespace'::ProtectCommand::SafeExecute"}
Message: Failed to execute the command.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"ms_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"tob_backup_command_addon_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 2
Module: 329
LineInfo: 0x8EDC81EA38FAB8C8
Fields: {"TraceLevel":"1","$file":"e:\\275\\enterprise\\managers\\gtob\\backupers\\backup_command\\impl\\backup_workflow_command.cpp","StepType":"6","$line":"776","$module":"tob_backup_command_addon_vsa64_22750","$func":"`anonymous-namespace'::BackupWorkflowCommand::ProcessWorkflowSteps"}
Message: Step 'Post-backup replication/cleanup' has failed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"FFBC7082-9C55-47D1-A6D2-1744EC8D7481","$module":"ms_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Replication
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"FFBC7082-9C55-47D1-A6D2-1744EC8D7481","$module":"taging_command_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Replication
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"08BE2B76-A95F-4FD4-AC32-AF26210E3A33","$module":"ms_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"08BE2B76-A95F-4FD4-AC32-AF26210E3A33","$module":"taging_command_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"ms_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"45D64182-5DF4-4AE0-9D42-55E1C3DB942B","$module":"ervice_process_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"CommandID":"45D64182-5DF4-4AE0-9D42-55E1C3DB942B","$module":"taging_command_vsa64_22750","$file":"e:\\275\\enterprise\\common\\tol\\command\\command.cpp","$line":"464","$func":"Tol::`anonymous-namespace'::MakeFailResult"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 217
Module: 161
LineInfo: 0x0B320396ADFE3D30
Fields: {"$line":"611","$module":"isk_bundle_vsa64_22750","$file":"e:\\275\\enterprise\\mms\\managers\\archive\\impl\\private_manager.cpp","$func":"ArchiveManagement::PrivateArchiveManager::DeleteSlices","IsReturnCode":"1"}
Message: Failed to delete the backups.
------------------------
Error code: 507
Module: 64
LineInfo: 0xA1D3981537C68B80
Fields: {"$line":"821","$module":"isk_bundle_vsa64_22750","$file":"e:\\275\\enterprise\\backup\\impl\\location_impl.cpp","$func":"Backup::Impl::OpenArchiveById","id":"Tuilserver3.tuildomain.nl-5251733B-249A-4590-A7DC-B841D9DE8697-8C6D7784-D824-442B-9D6C-2F9ACE8C06ECA.tibx"}
Message: Failed to open the backup archive by the ID.
------------------------
Error code: 853
Module: 64
LineInfo: 0x6A1198D1B8BE2BE0
Fields: {"$line":"242","$module":"isk_bundle_vsa64_22750","$file":"e:\\275\\enterprise\\backup\\impl\\archive_data_creator.cpp","$func":"`anonymous-namespace'::OpenArchive"}
Message: Failed to open archive 'Tuilserver3.tuildomain.nl-5251733B-249A-4590-A7DC-B841D9DE8697-8C6D7784-D824-442B-9D6C-2F9ACE8C06ECA.tibx'.
------------------------
Error code: 22
Module: 4
LineInfo: 0x8AF64B2C0920F6A0
Fields: {"$line":"191","$module":"ommon_archive_addon_vsa64_22750","$file":"e:\\275\\core\\resizer\\archive3\\archive3_error.cpp","$func":"`anonymous-namespace'::ConvertArchive3Error"}
Message: Network disconnected by timeout.
------------------------
Error code: 5016
Module: 667
LineInfo: 0xC3BC4C1EB22997D8
Fields: {"$file":"e:\\275\\enterprise\\applications\\archiving\\storages\\archive3\\src\\archive3.cpp","path":"Tuilserver3.tuildomain.nl-5251733B-249A-4590-A7DC-B841D9DE8697-8C6D7784-D824-442B-9D6C-2F9ACE8C06ECA.tibx","$line":"322","$module":"ommon_archive_addon_vsa64_22750","function":"archive_open","$func":"`anonymous-namespace'::CoOpenArchive"}
Message: Network operation timed out
------------------------
Error code: 13
Module: 667
LineInfo: 0xC3BC4C1EB22997D8
Fields: {"$file":"e:\\275\\enterprise\\applications\\archiving\\storages\\archive3\\src\\archive3.cpp","path":"/1/Tuilserver3.tuildomain.nl-5251733B-249A-4590-A7DC-B841D9DE8697-8C6D7784-D824-442B-9D6C-2F9ACE8C06ECA.tibx","$line":"322","$module":"ommon_archive_addon_vsa64_22750","function":"astor_file_open","$func":"`anonymous-namespace'::CoOpenArchive"}

 
      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/26/2020 - 11:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Please re-register the backup agents on one device and check if it is fixing the issue for it. Do the same for the rest if that works for this device.
If not resolved we would suggest opening a Support case as deeper investigation will be required. Opening a support case will require sharing the Cloud Account login and DC of the affected tenant. You can also share it here so we can at least clear out some basic investigation by checking your account.
Looking forward to your reply.

      
                
                
                    
                                                    Tue, 06/30/2020 - 15:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
