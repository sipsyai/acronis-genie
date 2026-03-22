# File exclusions on Linux

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/file-exclusions-linux

## Original Post
**Author:** Unknown

File exclusions on Linux

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,

I have a small problem, I want to exclude some folders in the backup of a Linux machine.
The exclusion path I entered is /home/backup for example.

But now the backup is completed with warnings, this is what I see in the log:

File exclusion is not supported.
Additional info:
--------------------
Error code: 47
Module: 7
LineInfo: a5695862aaf8e6f9
Fields: PartitionId : 227, $module : disk_bundle_lxa64_215
Message: File exclusion is not supported.
--------------------
Is the feature path exclusion not supported in the BAAS solution?

Best regards,

Eric

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/17/2015 - 06:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Eric,
Thanks for posting your question here.
The issue you mentioned is known, files' and folders' filters (both exclusion and inclusion) do not work on Backup Agent for Linux.
Development team is aware of this and fix is planned for future update. Please note that Acronis Backup Cloud v.4.0 does not include this fix.
File filters do not work for disk-level backups, but work fine for file-level backups. So if this works for you, you can set up a file backup on a higher folder level, and apply exclusion filters to lower-level folders and files.
Let me know if you have any questions.
Best regards,

      
                
                
                    
                                                    Wed, 06/17/2015 - 11:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Dmitry,

Thanks for you reply. File-level backup is not an option for me. When do you expect the future update where this problem is fixed?

Best regards,

Eric

      
                
                
                    
                                                    Thu, 06/18/2015 - 06:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Eric,
I got the information that this fix is planned for Acronis Backup Cloud v.4.1, the next planned update. We are expecting it to be released in July, pretty soon now.
Please remember that the issue will be fixed on the Agent side. Once new version is released, push the update to the respective Agent for Linux to get this fixed.
Let me know if you have more questions.
Best regards,

      
                
                
                    
                                                    Fri, 06/19/2015 - 14:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
