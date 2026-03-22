# Acronis Backup keeps failing

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-backup-keeps-failing

## Original Post
**Author:** Unknown

Acronis Backup keeps failing

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jose Gomez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
             
Backup failed
Invalid parameters were specified.
Error code 0x01330029+0x01350016+0x01350016+0x0133002B+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00F90004+0x00950001
DetailsSupportDownload log
Next backup
Apr 26, 2018, 11:02 PM
RUN NOW
  
Error details
Error
DATE AND TIME
Apr 26, 2018, 02:01:15 PM
MODULE
307
MESSAGE

Additional info:
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DDE7
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: Failed to execute the command.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"mms_vsa64_4560","CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"agent_protection_addon_vsa64_4560","CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 43
Module: 307
LineInfo: 0xE873A234106E3486
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: Failed to execute an internal command while resolving items selected for backup.
------------------------
Error code: 4
Module: 249
LineInfo: 0xD9612B4AAEBB8E3F
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: ASYNC: Unidentified job.
------------------------
Error code: 4
Module: 249
LineInfo: 0xB43D3EB4F18A8FE8
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: Job resolves the selection rules specified in the centralized backup plan for managed machine root item backup.
------------------------
Error code: 4
Module: 249
LineInfo: 0xD9612B4AAEBB8E3F
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: ASYNC: Unidentified job.
------------------------
Error code: 4
Module: 249
LineInfo: 0x9174396A01B27CE4
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: ASYNC: Lazy barrier action job.
------------------------
Error code: 4
Module: 249
LineInfo: 0xC8F602C2D3077781
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: GXT searches for items by type.
------------------------
Error code: 4
Module: 249
LineInfo: 0xB7C9D3AE0AAB45C2
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: GXT started going through hierarchy.
------------------------
Error code: 4
Module: 249
LineInfo: 0xB7C9D3AE0AAB4642
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: GXT is going through hierarchy.
------------------------
Error code: 4
Module: 249
LineInfo: 0x9174396A01B27CE4
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: ASYNC: Lazy barrier action job.
------------------------
Error code: 4
Module: 249
LineInfo: 0xD7761D47EDEB39A4
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: ASYNC: Action sequence pending action job.
------------------------
Error code: 4
Module: 249
LineInfo: 0xB7C9D3AE0AAB4642
Fields: {"$module":"agent_protection_addon_vsa64_4560"}
Message: GXT is going through hierarchy.
------------------------
Error code: 4
Module: 249
LineInfo: 0xD7761D47EDEB39A4
Fields: {"$module":"mms_vsa64_4560"}
Message: ASYNC: Action sequence pending action job.
------------------------
Error code: 4
Module: 249
LineInfo: 0x368CB7423C1C08D9
Fields: {"$module":"mms_vsa64_4560"}
Message: ASYNC: Full barrier action job.
------------------------
Error code: 1
Module: 149
LineInfo: 0x79DEEDF1510B1103
Fields: {"$module":"disk_bundle_vsa64_4560"}
Message: Invalid parameters were specified.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      logs (1).zip

                      1.92 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 04/26/2018 - 18:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hi Jose!
 
From the logs that you have provided I am only able to tell that the first thing you should try in order to solve the issue - update to the latest build (b4670).
 
I see that the main error message is " Invalid parameters were specified", however, in such cases it is important to know more:
 - what data is being backed up
 - backup plan settings
 - where the data is being backed up to
Additional information that may be helpful:
 - was it working before and if yes, when did the issue start
 

      
                
                
                    
                                                    Wed, 05/02/2018 - 14:18
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
