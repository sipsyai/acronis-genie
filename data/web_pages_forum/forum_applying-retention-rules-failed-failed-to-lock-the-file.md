# 'Applying retention rules' failed. Failed to lock the file.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/applying-retention-rules-failed-failed-lock-file

## Original Post
**Author:** Unknown

'Applying retention rules' failed. Failed to lock the file.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kwok Yin , Dick Wan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dears,
Sometime the backup is failed with  'Applying retention rules' failed. Failed to lock the file.
The backup loaction is the cloud storage on Azure with ASG in Azure VM.
Please kindly advise. Thank you very much.
Error
DATE AND TIME
Oct 13, 2016, 11:47:32 PM
MODULE
309
MESSAGE

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"mms_vsa64_3539","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"gtob_backup_command_addon_vsa64_3539","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 2
Module: 329
LineInfo: 0x8EDC81EA38FABA3A
Fields: {"StepType":"6","TraceLevel":"1","$module":"gtob_backup_command_addon_vsa64_3539"}
Message: Step 'Post-backup replication/cleanup' has failed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"mms_vsa64_3539","CommandID":"FFBC7082-9C55-47D1-A6D2-1744EC8D7481"}
Message: TOL: Failed to execute the command. Replication
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"staging_command_vsa64_3539","CommandID":"FFBC7082-9C55-47D1-A6D2-1744EC8D7481"}
Message: TOL: Failed to execute the command. Replication
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"mms_vsa64_3539","CommandID":"08BE2B76-A95F-4FD4-AC32-AF26210E3A33"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"staging_command_vsa64_3539","CommandID":"08BE2B76-A95F-4FD4-AC32-AF26210E3A33"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"mms_vsa64_3539","CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"service_process_vsa64_3539","CommandID":"45D64182-5DF4-4AE0-9D42-55E1C3DB942B"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"staging_command_vsa64_3539","CommandID":"45D64182-5DF4-4AE0-9D42-55E1C3DB942B"}
Message: TOL: Failed to execute the command. Applying retention rules
------------------------
Error code: 217
Module: 161
LineInfo: 0x0B320396ADFE3D90
Fields: {"$module":"disk_bundle_vsa64_3539","IsReturnCode":"1"}
Message: Failed to delete the backups.
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC223
Fields: {"$module":"disk_bundle_vsa64_3539"}
Message: Failed to lock the file.
------------------------
Error code: 1040
Module: 152
LineInfo: 0xA46E8D7BA5BB85F2
Fields: {"$module":"disk_bundle_vsa64_3539"}
Message:

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/14/2016 - 03:51

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dick Wan,
According to internal notes retention rules fail randomly if customer browsed backups in the same time when agent try to delete recovery point that is subject to deletion.
In such case retention rules will be applied after next backup if this collision will not occur again.
If problem is persistent, then please submit ticket to Acronis Service Provider Support team (mspsupport@acronis.com).
Best Regards,
Eugene.

      
                
                
                    
                                                    Fri, 10/14/2016 - 15:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daryl Armstrong
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Is this also true with local install, non Cloud. I had about 6 Clients receive this message yesterday. Does this mean that I browsed in the Backup software during backup time?
My errors were;
Activity 'Applying retention rules' failed. The activity has failed due to a restart of the service

      
                
                
                    
                                                    Fri, 10/27/2017 - 19:46
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Gwenaël Paumat
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I also receive the same error for one VM backup since 2 weeks.
Same error as Daryl Armstrong:
Activity 'Applying retention rules' failed. The activity has failed due to a restart of the service.

      
                
                
                    
                                                    Tue, 02/06/2018 - 14:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Gwenaël, thank you for your posting! I see, that you already have an open support ticket for the issue and would recommend to continue investigation with the help of the support engineers. Without analysis of the logfiles it's hard to understand what could have caused the service to restart/crash. We'd be also grateful if you share the outcome here, so that other users can find this information. Thank you!

      
                
                
                    
                                                    Wed, 02/07/2018 - 15:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have the same problem. Activity 'Applying retention rules' failed. The activity has failed due to a restart of the service.”
This happened while backing up to a NAS.

      
                
                
                    
                                                    Tue, 02/05/2019 - 11:03
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud
