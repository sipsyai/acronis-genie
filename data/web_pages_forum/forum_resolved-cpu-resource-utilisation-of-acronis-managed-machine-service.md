# [RESOLVED] CPU resource utilisation of Acronis Managed Machine Service

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-cpu-resource-utilisation-acronis-managed-machine-service

## Original Post
**Author:** Unknown

[RESOLVED] CPU resource utilisation of Acronis Managed Machine Service

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                
                    
                        
            When we look at the CPU resources of our customers where we have Acronis Backup Cloud rolled out we can see the Acronis Managed Machine Service is using a fair amount of CPU power. This service/processs is constantly in the upper 3 programs of "most CPU utilisation".
 
Is there an explanation for this? Even when there are no jobs running its using a lot of CPU power.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/31/2016 - 09:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
If you see a process service_process.exe running, it means that there is currently some operation in progress (backup, validation, restore, replication etc.). As explained in this article, Acronis Backup Cloud will use all available free resources not affecting OS performance, and thus you can safely ignore this behavior. You can then navigate to Backup Monitor in system tray to see which operation is running.
If you see no running service_process.exe, all demanding operations are complete and mms.exe should also reduce CPU usage. If it continues to utilize the resources, this might be due to running cataloging of the backup content. This is possible when you are creating a backup to a local/network folder and backup contains multiple files (thousands) inside. Is this your case?
Please provide information on how much time passed after last backup and what was the backup source and destination.
Furthermore you can use Process Monitor to check what files are being accessed by mms.exe at this moment, this will give me more data to provide you with an elaborate answer to your question.
Thank you,

      
                
                
                    
                                                    Thu, 03/31/2016 - 10:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the information.
This solves my questions.

      
                
                
                    
                                                    Tue, 04/05/2016 - 10:50
