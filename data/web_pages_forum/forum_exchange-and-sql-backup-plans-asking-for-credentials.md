# Exchange and SQL backup plans asking for credentials?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/exchange-and-sql-backup-plans-asking-credentials

## Original Post
**Author:** Unknown

Exchange and SQL backup plans asking for credentials?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Since the new agent update our Exchange and SQL backup plans started asking for special credentials. This is not the case with every account, only with some of them. 
Also, when i enter the domain admin with sysadmin credentials it says "access denied" wich seems to be an error on the Acronis side. Because a domain admin has access to Exchange and SQL databases.
This question for special credentials has only popped up since the last agent update. Is this a bug in the agent? or am i doing something wrong?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/25/2016 - 15:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
We don't have any confirmed issue for this behavior in the latest update.
Could you please confirm that these machines with the same credentials performed SQL/Exchange backup correctly before update? When exactly does the credentials popup appear, when you apply or run the backup plan, or select data for backup?
You can also check whether the Acronis Managed Machine Service user on a specific machine has all required permissions for backup operations as in this article. The account must be a member of the Backup Operators or Administrators group on the machine.
As for the credentials that you should provide when setting up a backup plan, for SQL backup it should be a member of the sysadmin role on each of the instances that you are going to back up (domain admin is by default not a sysadmin). For Exchange backup see this chart with necessary user rights.
Looking forward to more details on this.

      
                
                
                    
                                                    Mon, 03/28/2016 - 16:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The domain admin is a member of the sysadmin role in this case, we have checked this.
After uninstalling the new agent and installing the previous version of the agent ( we still had the install package ), the problem has gone away.
The Acronis Managed Machine Service on the machine is running under the same credentials ( Domain admin with all the necessary rights )

      
                
                
                    
                                                    Tue, 03/29/2016 - 11:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
I see, all indicates that there is an issue with the new agent. Thank you for checking all the prerequisites.
Please submit a support ticket with the AcronisInfo from the old (if possible) and new build of the agent on the same machine. Also please collect procmon log on the machine when you get the credentials prompt. That requires a closer look by the RnD team.
Thank you,

      
                
                
                    
                                                    Tue, 03/29/2016 - 12:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dmitry,
 
I will create a suppor ticket for this issue.
Though it looks like its a bug with the agent, because we are getting this error with several customers.
Do you have an ETA on the new build of the agent? because there are now serveral confirmed bugs with this agent and workarounds are only getting me so far..

      
                
                
                    
                                                    Tue, 04/05/2016 - 09:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Do you have an ETA on the new build of the agent? because there are now serveral confirmed bugs with this agent and workarounds are only getting me so far..

      
                
                
                    
                                                    Wed, 04/06/2016 - 09:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
No, we don't have an ETA for new agents, but we are expecting them shortly. I'll update this thread once they are released.
Thank you
 

      
                
                
                    
                                                    Wed, 04/06/2016 - 11:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dmitry,
 
Thank you for your answer.
I understand you dont have an exact ETA, but "Shortly" will this be a couple of weeks from now? or months?

      
                
                
                    
                                                    Wed, 04/06/2016 - 11:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
Shortly stands here for several days, not weeks or months.
Thank you,

      
                
                
                    
                                                    Thu, 04/07/2016 - 11:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
