# Sql backup plan creation failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-backup-plan-creation-failed

## Original Post
**Author:** Unknown

Sql backup plan creation failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
When I try to configure SQL Backup I have this error message :
Not connected to '96B4EC56-8F7C-428A-80A5-BEF4156508FC'.
DATE AND TIME04 Sept 2015, 16:28:15
CODE0x01350016+0x01350016+0x02480032
MODULE309
MESSAGETOL: Failed to execute the command. Backup::Assistant::Commands::NewPlanDraft
Can you help,
thanks,
Kevin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/04/2015 - 14:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin,
Seems like the Backup Management Server is unable to connect to the agent, or to the SQL instance on it (it's unclear from the message). Could you please check the following?
That the agent is online in the console in the main resources pane (not in the SQL pane)
That you can create backup plans for this machine for other sources (files or disks)
If the above is true, then it's only the SQL instance that is unavailable. In this case make sure the SQL services, including the SQL Browser service are running, and that the Acronis Managed Machine Service user is the SQL admin.
Also please let me know what exactly you select before you click on create backup plan (the whole SQL server or  one instance inside it?), and at what step you get the error (when you click to  confirm the plan creation or at some other point?).
Let me know the above so I can tell you what to do next.
Thank you,

      
                
                
                    
                                                    Fri, 09/04/2015 - 14:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
