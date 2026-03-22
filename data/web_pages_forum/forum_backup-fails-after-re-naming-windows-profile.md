# Backup fails after re-naming Windows Profile

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-fails-after-re-naming-windows-profile

## Original Post
**Author:** Unknown

Backup fails after re-naming Windows Profile

        
  



    
  


  
              
          
        Thread needs solution      
      
      





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a Windows 7 Pro machine that has been working fine.  The User Profile was recently renamed (from COLLEEN to KIM) instead of creating a new one, as there are a lot of settings that needed to be kept intact.
Now the backup fails every time with the errors below. I have deleted the old backup schedule and created a new one. It seems like it's stuck seeing the old username but I cannot believe that the software wouldn't be smart enough to just work around the renaming of a profile...
Any suggestions would be greatly appreciated.
Thanks,
Glen
==================================
 
Error details
Error
DATE AND TIME
Sep 03, 2017, 03:59:36 PM
MODULE
309
MESSAGE

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_3917"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_3917"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 252
Module: 161
LineInfo: 0x9FC3EE39511C2B90
Fields: {"$module":"disk_bundle_vsa64_3917","account":"****@****sics.biz"}
Message: Stream name: 'WASSLAW1-B48444D1-36DD-4368-A285-ABDF95EF3911-0823AAAC-047D-41FA-8959-8A6E01A98203AF.TIB'.
------------------------
Error code: 3
Module: 329
LineInfo: 0x1CD98AAE889424F9
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Backup has failed.
------------------------
Error code: 1060
Module: 1
LineInfo: 0x958D99FE3B224FD6
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: 
------------------------
Error code: 2064
Module: 23
LineInfo: 0xA61565B622786DD2
Fields: {"Path":"C:/Users/Colleen/AppData/Roaming/Microsoft/Windows/Cookies/","$module":"disk_bundle_vsa64_3917"}
Message: Failed to enumerate directory 'C:/Users/Colleen/AppData/Roaming/Microsoft/Windows/Cookies/'. It may be corrupted or does not exist, please check disk for errors.
------------------------
Error code: 7
Module: 4
LineInfo: 0xF35F747B3B21FAAE
Fields: {"path":"\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy21\\Users\\Colleen\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\*","function":"FindFirstFileW","$module":"disk_bundle_vsa64_3917"}
Message: Error occurred while opening the file.
------------------------
Error code: 65520
Module: 0
LineInfo: 0xBD28FDBD64EDB8F1
Fields: {"$module":"disk_bundle_vsa64_3917","code":"2147942403"}
Message: The system cannot find the path specified

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 09/04/2017 - 20:38

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
