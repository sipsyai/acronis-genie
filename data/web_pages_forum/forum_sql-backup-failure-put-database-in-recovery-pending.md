# Sql backup failure put database in recovery pending

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-backup-failure-put-database-recovery-pending

## Original Post
**Author:** Unknown

Sql backup failure put database in recovery pending

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
From time to time I have a backup failure for the SQL agent. When I check the SQL server, the database is in recovery pending mode. It's annoying beacause I have to restart the SQL service to unlock the DB.
Details of backup error :
CODE0x01350001
MODULE309
MESSAGEThe activity state has been repaired after unexpected failure.
Additional info:------------------------
Error code: 1
Module: 309
LineInfo: 0x7564DA35B0F1EB08
Fields: {"$module":"mms_vsa64_1150"}
Message: The activity state has been repaired after unexpected failure.
I already tried to reinstall the software and still the same error. It's happening randomly.
Thanks for your help !
Kevin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/18/2015 - 10:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             Hello Kevin,
Thank you for addressing your query on forum, I'll be happy to assist.
The error message "The activity state has been repaired after unexpected failure." comes after a process crash, and the module name addresses it to mms.exe. Please make sure that in Windows Event Viewer > System Log you can locate a respective error message. If you identify a crash of another process, e.g. service_process.exe, then this one is causing the problem and should be investigated instead of mms.exe.
To investigate this issue we would need to check the process crash dump file. Please collect the dump with procdump, get system information from the machine and submit a support request.
You could monitor memory usage for the process mms.exe/service_process.exe during backup before crash to describe what exactly happens and provokes the crash, in comparison to a successful SQL backup. Changing the backup source and destination could also help to localize the issue.
Let me know if you have additional questions.

      
                
                
                    
                                                    Tue, 08/18/2015 - 11:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
