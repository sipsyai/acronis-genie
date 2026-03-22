# Several backup failed messages

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/several-backup-failed-messages

## Original Post
**Author:** Unknown

Several backup failed messages

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    robert Lounsberry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Everything is below, but I think these two are the cause, I'm jus tnot sure how to tell what to do with them.
Error code: 3
Module: 7
LineInfo: 0xDF81DA2C74EC50EB
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Read error.
------------------------
Error code: 50266
Module: 16
LineInfo: 0x3FEC04E376B89EA3
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Failed to read the snapshot.
 
 
 
DATE AND TIME
Feb 12, 2016, 11:56:42 AM
CODE
0x01350016+0x01350016+0x01490002+0x01350016+0x01350016+0x01350016+0x01490003+0x00010424+0x00070003+0x0010C45A+0x00000009+0x00000057+0x0000FFF0+0x80070057
MODULE
309
MESSAGE
Backup failed
Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"mms_vsa64_1621"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"gtob_backup_command_addon_vsa64_1621"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 2
Module: 329
LineInfo: 0x8EDC81EA38FABA3F
Fields: {"$module":"gtob_backup_command_addon_vsa64_1621","StepType":"2","TraceLevel":"1"}
Message: Step 'Backup' has failed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"mms_vsa64_1621"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_1621"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_1621"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 3
Module: 329
LineInfo: 0x1CD98AAE889424F9
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Backup has failed.
------------------------
Error code: 1060
Module: 1
LineInfo: 0xB43E776571144DEE
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Failed to commit operations.
------------------------
Error code: 3
Module: 7
LineInfo: 0xDF81DA2C74EC50EB
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Read error.
------------------------
Error code: 50266
Module: 16
LineInfo: 0x3FEC04E376B89EA3
Fields: {"$module":"disk_bundle_vsa64_1621"}
Message: Failed to read the snapshot.
------------------------
Error code: 9
Module: 0
LineInfo: 0x02AACB7B2AB852AC
Fields: {"$module":"disk_bundle_vsa64_1621","code":"87"}
Message: Unknown status.
------------------------
Error code: 65520
Module: 0
LineInfo: 0xBD28FDBD64EDB8F4
Fields: {"$module":"disk_bundle_vsa64_1621","code":"2147942487"}
Message: The parameter is incorrect

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/12/2016 - 18:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Robert,
Thank you for posting your question here.
The error message is the same as in this KB article: https://kb.acronis.com/content/41152. And it means that although the disk snapshot can be created successfully, it's content cannot be read at some point, where the disk contains errors. You can check whether it's true by selecting different disks (in case you have more than one) or volumes one-by-one and backing them up separately, only those with disk errors should fail. The disk report from the KB article will also be helpful to identify which volume contains errors.
Should this not resolve the issue, please collect the system report as mentioned in the article and contact our support team to troubleshoot the issue.
For your future reference, the most useful message in the error stack is always in the very bottom. Searching for "The parameter is incorrect" and filtering by Acronis Backup Cloud would allow you to find the above mentioned KB article.
Let me know if you have any questions.
Best regards,

      
                
                
                    
                                                    Fri, 02/12/2016 - 21:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    robert Lounsberry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you very much. I actually found that same article and am in the process of going through those steps.

      
                
                
                    
                                                    Fri, 02/12/2016 - 22:10
