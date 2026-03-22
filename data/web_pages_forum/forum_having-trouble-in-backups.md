# Having trouble in backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/having-trouble-backups

## Original Post
**Author:** Unknown

Having trouble in backups

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Souheil Chukry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Everyone,
I am tryign to backup me Virtual machines, i have installed on each an agent and on one on the VMs an ESX agent so that it can discover the reset of the VMs;
Below are the errors i get : Please note that not all the backup failed but some 
Error 1
DATE AND TIME
Feb 07, 2017, 07:19:34 PM
MODULE
307
MESSAGE

Additional info:
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DDE7
Fields: {"$module":"agent_protection_addon_vsa64_3917"}
Message: Failed to execute the command.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94","$module":"mms_vsa64_3917"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94","$module":"agent_protection_addon_vsa64_3917"}
Message: TOL: Failed to execute the command. Resolving items to back up
------------------------
Error code: 43
Module: 307
LineInfo: 0xE873A234106E3486
Fields: {"$module":"agent_protection_addon_vsa64_3917"}
Message: Failed to execute an internal command while resolving items selected for backup.
------------------------
Error code: 68
Module: 307
LineInfo: 0x071E35C26B78D644
Fields: {"$module":"agent_protection_addon_vsa64_3917"}
Message: Cannot resolve any of the following inclusion rules: '[Fixed Volumes]'.
------------------------
Error code: 67
Module: 307
LineInfo: 0x071E35C26B78D5FC
Fields: {"$module":"agent_protection_addon_vsa64_3917"}
Message: Cannot resolve inclusion rule '[Fixed Volumes]'.
------------------------
Error code: 6
Module: 377
LineInfo: 0x20E8C00E3FF3FA4F
Fields: {"$module":"agent_protection_addon_vsa64_3917"}
Message: No volumes have been found while processing the 'Fixed Volumes' template.
This is error 2 :
 
Error
DATE AND TIME
Feb 07, 2017, 06:42:01 PM
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
Error code: 212
Module: 161
LineInfo: 0x0B320396ADFE3EA3
Fields: {"$module":"disk_bundle_vsa64_3917","IsReturnCode":"1"}
Message: Failed to find archive 'BYBSDC-119.byblos.local-DB6164D3-0C30-443F-BCA2-CE3D39EDD0C9-287367B8-EB65-42A6-827C-F9DFF583A4E7A'.
------------------------
Error code: 46
Module: 64
LineInfo: 0x3F26773FAB7BDAC3
Fields: {"$module":"disk_bundle_vsa64_3917","user":"byblos\\administrator","path":"file://192.168.1.147\\VM%20backup\\BYBDC-119\\"}
Message: Failed to open the backup location.
------------------------
Error code: 10
Module: 4
LineInfo: 0xF35F747B3B21F8E7
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Error occurred while creating the file.
 
Your help is much appreciated, since i am a new Acronis user
Regards.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 02/08/2017 - 07:26

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My name is Evgeny, I am from Acronis Service Providers Support.
As far as I understand you have faced two issues with backups of some VMs by Acronis Backup Cloud v6.1. 
I will be glad to assist you!
Unfortunately you have not provided your backup account, so I am unable to check the errors from the console and download the system report from the affected Agent machine. Let me suggest on the errors below:
1) This error may be received when the user for Acronis Managed Machine service has changed either manually from services.msc or if the Agent has been reinstalled incorrectly. 
To confirm this we will need to collect the system report as per the instruction:
https://kb.acronis.com/content/54608 
Please create a support ticket by sending an email  to mspsupport@acronis.com so that we can investigate the issue further.
2) According to the error message, the issue is faced upon a backup operation to a network folder \\192.168.1.147\\VM backup\\BYBDC-119\\
Most frequently the issue is related to the fact that the Agent for Windows/Linux is unable to open the folder to write to it. This can be caused by many factors such as insufficient rights and permissions granted to the user which runs the Agent / incorrect credentials specified within the backup plan.
We will need to troubleshoot and localize the issue to provide you with a solution, so please submit another ticket by sending a separate email  to mspsupport@acronis.com 
If you have any questions, please feel free to contact us, we will be glad to assist.
 
With regards,
Evgeny Ryuntyu
Acronis Service Providers Support
 

      
                
                
                    
                                                    Wed, 02/08/2017 - 14:25
