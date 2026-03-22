# SQL Backup failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-backup-failed

## Original Post
**Author:** Unknown

SQL Backup failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Everything was working okay for several months and then I got this message :
 
Échec sauv.
Several activities have not succeeded. Details: EF1AE2B7-B626-4FFB-8E75-AD429F6247A4: Error 0x15d070a: Failed to create the shadow copy of volume '\\?\Volume{517b0f5f-447f-11e4-80bf-9c8e9962308b}\'. | line info: 0x8a9f7ba9e74d6f1f | $module: ArsDbBackupProvider64_vsa64_1592 C8A1676F-EBC1-49A7-93A3-69041D1A5849: Error 0x1350016: TOL: Failed to execute the command. Backing up | line info: 0x8d165e86fb819595 | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4 | $module: service_process_vsa64_1592 | | error 0x1350016: TOL: Failed to execute the command. Backing up | line info: 0x8d165e86fb819595 | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4 | $module: gtob_backup_command_addon_vsa64_1592 | | error 0x26f0067: A generic error of Microsoft SQL Backuper. | line info: 0x94f5f955b13ddfb8 | IsReturnCode: 0x1 | $module: ArsAgentProvider_vsa64_1592 | | error 0x57010f: Failed to back up Microsoft SQL Server. | line info: 0x7f9e79f979cfc15e | IsReturnCode: 0x1 | $module: ArsAgentProvider_vsa64_1592 | | error 0x15d070a: Failed to create the shadow copy of volume '\\?\Volume{517b0f5f-447f-11e4-80bf-9c8e9962308b}\'. | line info: 0x8a9f7ba9e74d6f1f | $module: ArsDbBackupProvider64_vsa64_1592 74D5E952-EDC7-4EAA-A770-F430EF4C07BF: Error 0x1350016: TOL: Failed to execute the command. Backup workflow | line info: 0x8d165e86fb819595 | CommandID: F30407D6-601F-11E0-9C67-FF46DFD72085 | $module: mms_vsa64_1592 | | error 0x1350016: TOL: Failed to execute the command. Backup workflow | line info: 0x8d165e86fb819595 | CommandID: F30407D6-601F-11E0-9C67-FF46DFD72085 | $module: gtob_backup_command_addon_vsa64_1592 | | error 0x1490002: Step 'Backup' has failed. | line info: 0x8edc81ea38faba3f | TraceLevel: 0x1 | StepType: 0x2 | $module: gtob_backup_command_addon_vsa64_1592 | | error 0x1350016: TOL: Failed to execute the command. Tol::IsolateCommand | line info: 0x8d165e86fb819595 | CommandID: 4504F8D4-2727-42AB-BB4F-A42EDBB790A0 | $module: mms_vsa64_1592 | | error 0x1350016: TOL: Failed to execute the command. Backing up | line info: 0x8d165e86fb819595 | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4 | $module: service_process_vsa64_1592 | | error 0x1350016: TOL: Failed to execute the command. Backing up | line info: 0x8d165e86fb819595 | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4 | $module: gtob_backup_command_addon_vsa64_1592 | | error 0x26f0067: A generic error of Microsoft SQL Backuper. | line info: 0x94f5f955b13ddfb8 | IsReturnCode: 0x1 | $module: ArsAgentProvider_vsa64_1592 | | error 0x57010f: Failed to back up Microsoft SQL Server. | line info: 0x7f9e79f979cfc15e | IsReturnCode: 0x1 | $module: ArsAgentProvider_vsa64_1592 | | error 0x15d070a: Failed to create the shadow copy of volume '\\?\Volume{517b0f5f-447f-11e4-80bf-9c8e9962308b}\'. | line info: 0x8a9f7ba9e74d6f1f | $module: ArsDbBackupProvider64_vsa64_1592
Code d'erreur 0x01330029+0x01350035
Can you help me ?
Kind Regards,
Kevin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 12/28/2015 - 09:31

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin,
Following error message shows a VSS snapshot failure:
    error 0x15d070a: Failed to create the shadow copy of volume
What messages do you see in Windows Application Event log when you start a backup? It should give more details about the VSS problem.
Additionally you can check the snapshot using DiskShadow tool with SQL VSS Writer to localize the problem if the log doesn't show sufficient information.
Please provide more details about the error from Windows log.
Thank you,

      
                
                
                    
                                                    Mon, 12/28/2015 - 11:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi thanks for the support but everithing goes back to normal without me doing anything.

      
                
                
                    
                                                    Tue, 01/05/2016 - 15:40
