# Acronis Cyber Protect unattended installation issue

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-protect-unattended-installation-issue

## Original Post
**Author:** Unknown

Acronis Cyber Protect unattended installation issue

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Adrien VANACKERE
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I’m currently trying to make it work unattended installation with msiexec like that : 
msiexec /i "D:\Acronis\BackupClient64.msi" /qn /l*v "D:\Logslog.txt" TRANSFORMS="D:\Acronis\BackupClient64.msi.mst"
I generated the files for the installation with the full offline Acronis package « Cyber_Protection_Agent_for_Windows_x64 »
Unfortunatelly I the installation failed every time that I started the command.
Here the end of the logs. I’ve also attached the full log file.
I created a case -> here is the case number : 04840681
Logs details : 
MSI (s) (0C:48) [10:04:09:811]: Note: 1: 1708 
MSI (s) (0C:48) [10:04:09:811]: Note: 1: 2205 2:  3: Error 
MSI (s) (0C:48) [10:04:09:811]: Note: 1: 2228 2:  3: Error 4: SELECT `Message` FROM `Error` WHERE `Error` = 1708 
MSI (s) (0C:48) [10:04:09:811]: Note: 1: 2205 2:  3: Error 
MSI (s) (0C:48) [10:04:09:811]: Note: 1: 2228 2:  3: Error 4: SELECT `Message` FROM `Error` WHERE `Error` = 1709 
MSI (s) (0C:48) [10:04:09:811]: Produit : Cyber Protect Agent -- L’installation a échoué.
 
MSI (s) (0C:48) [10:04:09:811]: Windows Installer a installé le produit. Nom du produit : Cyber Protect Agent. Version du produit : 15.0.26473. Langue du produit : 0. Fabricant : Acronis. Réussite de l’installation ou état d’erreur : 1603.
 
MSI (s) (0C:48) [10:04:09:827]: Attempting to delete file C:\windows\Installer\eccdc6d.mst
MSI (s) (0C:48) [10:04:09:827]: Unable to delete the file. LastError = 32
MSI (s) (0C:48) [10:04:09:827]: Deferring clean up of packages/files, if any exist
MSI (s) (0C:48) [10:04:09:843]: Attempting to delete file C:\windows\Installer\eccdc6d.mst
MSI (s) (0C:48) [10:04:09:843]: MainEngineThread is returning 1603
MSI (s) (0C:20) [10:04:09:843]: No System Restore sequence number for this installation.
=== Fin de l’écriture dans le journal : 17/03/2021  10:04:09 ===
MSI (s) (0C:20) [10:04:09:843]: User policy value 'DisableRollback' is 0
MSI (s) (0C:20) [10:04:09:843]: Machine policy value 'DisableRollback' is 0
MSI (s) (0C:20) [10:04:09:843]: Incrementing counter to disable shutdown. Counter after increment: 0
MSI (s) (0C:20) [10:04:09:843]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
MSI (s) (0C:20) [10:04:09:843]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
MSI (s) (0C:20) [10:04:09:843]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
MSI (s) (0C:20) [10:04:09:843]: Destroying RemoteAPI object.
MSI (s) (0C:6C) [10:04:09:843]: Custom Action Manager thread ending.
MSI (c) (7C:20) [10:04:09:843]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
MSI (c) (7C:20) [10:04:09:843]: MainEngineThread is returning 1603
=== Verbose logging stopped: 17/03/2021  10:04:09 ===
 
PS : I also tried this tool : Acronis Cyber Protect, Acronis Cyber Backup: Cleanup Utility | Knowledge Base
But nothing changed -> still having the same issue
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Logslog.txt

                      1.46 MB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/17/2021 - 09:04

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Adrien, 
I can see that the case you have mentioned is marked as resolved. Please let me know if you still need assistance in regards to this.

      
                
                
                    
                                                    Tue, 03/23/2021 - 07:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
