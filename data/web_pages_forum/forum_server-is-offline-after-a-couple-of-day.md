# Server is offline after a couple of day

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/server-offline-after-couple-day

## Original Post
**Author:** Unknown

Server is offline after a couple of day

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a problem with one Windows 2012 R2 server, after I install the Acronis backup client the server is going offline after a few weeks in the Baas overview. And its stopping making backups. Solution is to remove the client and install again, how can I solve this problem? (This happens only on one server, all other windows machines are working fine).
What I did
- Uninstall and remove all in program files and program data
- Check firewall connectioin
Best regards,
Eric

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/03/2015 - 18:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Eric,
There can be 2 major reasons why the agent is shown as offline in the console:
 
  1. Agent registration parameters changed, old machine ID does not sync anymore
In this case when you re-install the agent, you assign a new ID to this machine and then register it anew. Then after a few weeks something happens on the machine locally that changes these settings and it is not synced anymore.
You can check whether it is true by re-registering the agent with the same ID in Acronis Backup Cloud following https://kb.acronis.com/content/55244.
 
  2. Sync between the agent and the Backup Management Server is blocked
Agent pings the Backup Management Server once in a while and sends statistics about completed actions. If there is something blocking these statistics and connections on the machine, it will go offline.
Here please check that when the machine is already offline:
it can reach out to all necessary servers: https://kb.acronis.com/content/47678
all necessary ports are open at all times: https://kb.acronis.com/content/47189
no antivirus software blocks the folder C:\ProgramData\Acronis\ and it's subdirectories (temporary files will be created in C:\ProgramData\Acronis\BackupAndRecovery\Temp, C:\ProgramData\Acronis\BackupAndRecovery\MMS\Outbox and C:\ProgramData\Acronis\BackupAndRecovery\MMS\Inbox)
 
If it is not the second case and you don't manage to identify the root cause, please create 2 system reports from the machine: one when the machine is offline and one when you re-register or re-install it and it is online, so that support team can compare the two and localize the problem, and submit a new case.
Thank you,

      
                
                
                    
                                                    Wed, 11/04/2015 - 08:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dmitry,
Thanks for your reply. Solution was to reregister the client by using https://kb.acronis.com/content/55244. What can I do to prevent that this will happen again?
Best regards,
Eric

      
                
                
                    
                                                    Mon, 11/09/2015 - 08:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Eric,
The fact that you managed to bring the client online simply by re-registering it in Acronis Backup Cloud means that the overall setup on it is correct and the problem is not trivial. Please submit a support case with a system information from this client. We would need to first localize what causes it to go offline to fix it for good, support team will assist you with that.
Thank you,
P.S. If the agent is not up to date, it makes sense to reproduce the issue first, then update and reproduce it again to make sure whether the issue is gone. If you update immediately then you'd have to wait another month before you are sure.

      
                
                
                    
                                                    Mon, 11/09/2015 - 09:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
