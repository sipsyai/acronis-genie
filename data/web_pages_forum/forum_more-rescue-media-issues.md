# More rescue media issues

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/more-rescue-media-issues

## Original Post
**Author:** Unknown

More rescue media issues

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Attempting to do a test rescue media restore and stuck now (again)
Windows 2016 full server backup. System and Data disk
Restoring to latest eval version of ESXi 6.5.
Restore runs ok but on restarting then the machine boots up to the Windows splash and then a black screen. I have a mouse pointer and that's it. Same in Safe Mode
Any ideas? Tried changing display settings etc but to no avail.
Also tried running the Universal restore which runs through but doesn't make any difference

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/25/2018 - 11:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Neil
Sorry for not replying sooner!
 
Most common reason for such issues is that "explorer.exe" is not set up to start automatically. This can happen if you did not recover the registry or if there was an issue in the registry backup/restore.
 
Other than that, there may be other issues, but let's start with "explorer.exe".
 
If you are able to get to the Task Manager after hitting Ctrl+Alt+Del, then click on File -> Run -> explorer.exe
If explorer.exe is launched, you will see the normal UI of Windows, from there - go to the registry editor and make sure that explorer.exe is set to launch on Windows start:
Win+R -> regedit -> Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon -> shell
shell key should be equal to explorer.exe
Once you set it up like this and restart, explorer would be launched automatically.
 
If you would still face this issue, please describe the entire backup process and then the recovery process in as much detail as possible and log a support case as per https://webteam-staging.corp.acronis.com/en-us/support/serviceprovidertemplate/
 
If you would reach resolution with the provided suggestions, please post a reply with confirmation just so me and other readers could be sure that it worked.

      
                
                
                    
                                                    Tue, 01/30/2018 - 08:39
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
