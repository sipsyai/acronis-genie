# Backup fails with ACCESS DENIED Error code: 20250646

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-fails-access-denied-error-code-20250646

## Original Post
**Author:** Unknown

Backup fails with ACCESS DENIED Error code: 20250646

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mbiko Ngoma
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Additional info:
------------------------
Error code: 20250646
Fields: {"$module":"mms_vsa64_31791","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/08/2023 - 10:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mbiko.
The error code you mention is generic so It can be applied to several scenarios.
Please check if it is related to this KB and apply the solutions: https://kb.acronis.com/content/70057
If you are executing the backup to a NAS, please reboot the NAS and try to backup again.
Check also if the file isn't blocked by another application and also check the VSS with this app: https://www.acronis.com/en-eu/products/vss-doctor/
Please let me know if any of those solutions solved the issue.
If then please send us the following details: 
- The product you use ( name ).
- Full error code.
- The storage you use ( Cloud, NAS etc ).
- What kind of devices are being backed up?
Thanks in advance!

      
                
                
                    
                                                    Tue, 05/09/2023 - 09:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mbiko Ngoma
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hello Jose
i had already run the VSS doctor before posting this error to this forum and had fixed volume shadow copy which was not enabled but am still experiencing the same error.
i have restarted the NAS but am still experiencing the same error.
My Product name is Acronis 15.0.31791
storage NAS
am backing sheared files on a file saver platform win2k22
full error below:
MESSAGE
Access is denied.

Additional info:
------------------------
Error code: 20250646
Fields: {"$module":"mms_vsa64_31791","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'APPDB01'
------------------------
Error code: 20250646
Fields: {"$module":"agent_protection_addon_vsa64_31791","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'APPDB01'
------------------------
Error code: 20119593
Fields: {"$module":"agent_protection_addon_vsa64_31791"}
Message: Failed to execute the command.
------------------------
Error code: 20250677
Fields: {"$module":"agent_protection_addon_vsa64_31791","FailCount":2}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 20250646
Fields: {"$module":"service_process_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 20250646
Fields: {"$module":"gtob_backup_command_addon_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 10551508
Fields: {"$module":"disk_bundle_vsa64_31791","IsReturnCode":1}
Message: Failed to find archive 'AppDB01.unity.co.zm-6C6F129F-935C-4335-9315-6AA098308A79-AAB165F3-EDDE-4424-976B-59697706AF7AA'.
------------------------
Error code: 10551497
Fields: {"$module":"disk_bundle_vsa64_31791"}
Message: Failed to get information about the archives.
------------------------
Error code: 262145
Fields: {"$module":"disk_bundle_vsa64_31791","function":"NtOpenFile","path":"\\\\?\\UNC\\unity-san01\\ReadyNASPro\\"}
Message: Error occurred while reading the file.
------------------------
Error code: 65520
Fields: {"$module":"disk_bundle_vsa64_31791","code":2147943672}
Message: You can't access this shared folder because your organization's security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network
------------------------
 

      
                
                
                    
                                                    Thu, 05/11/2023 - 06:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mbiko Ngoma wrote:

hello Jose
i had already run the VSS doctor before posting this error to this forum and had fixed volume shadow copy which was not enabled but am still experiencing the same error.
i have restarted the NAS but am still experiencing the same error.
My Product name is Acronis 15.0.31791
storage NAS
am backing sheared files on a file saver platform win2k22
full error below:
MESSAGE
Access is denied.

Additional info:
------------------------
Error code: 20250646
Fields: {"$module":"mms_vsa64_31791","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'APPDB01'
------------------------
Error code: 20250646
Fields: {"$module":"agent_protection_addon_vsa64_31791","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'APPDB01'
------------------------
Error code: 20119593
Fields: {"$module":"agent_protection_addon_vsa64_31791"}
Message: Failed to execute the command.
------------------------
Error code: 20250677
Fields: {"$module":"agent_protection_addon_vsa64_31791","FailCount":2}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 20250646
Fields: {"$module":"service_process_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 20250646
Fields: {"$module":"gtob_backup_command_addon_vsa64_31791","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 10551508
Fields: {"$module":"disk_bundle_vsa64_31791","IsReturnCode":1}
Message: Failed to find archive 'AppDB01.unity.co.zm-6C6F129F-935C-4335-9315-6AA098308A79-AAB165F3-EDDE-4424-976B-59697706AF7AA'.
------------------------
Error code: 10551497
Fields: {"$module":"disk_bundle_vsa64_31791"}
Message: Failed to get information about the archives.
------------------------
Error code: 262145
Fields: {"$module":"disk_bundle_vsa64_31791","function":"NtOpenFile","path":"\\\\?\\UNC\\unity-san01\\ReadyNASPro\\"}
Message: Error occurred while reading the file.
------------------------
Error code: 65520
Fields: {"$module":"disk_bundle_vsa64_31791","code":2147943672}
Message: You can't access this shared folder because your organization's security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network
------------------------
 


Hello!
That error seems to be related with the lack of permissions ( Windows error ).
Please check this web guides and try to fix the issue: 
- https://learn.microsoft.com/en-us/answers/questions/59309/you-can-t-acc…
- https://www.techcrumble.net/2018/03/you-cant-access-this-shared-folder-…
Thanks in advance!
 

      
                
                
                    
                                                    Thu, 05/11/2023 - 09:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
