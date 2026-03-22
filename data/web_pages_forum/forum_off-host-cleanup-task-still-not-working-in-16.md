# off-host cleanup task - still not working in 16 ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/host-cleanup-task-still-not-working-16

## Original Post
**Author:** Unknown

off-host cleanup task - still not working in 16 ?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey there,
I feel a bit like in Groundhog Day ;-)
In 2023 I had an issue with off-host cleanup: Cleanup Task not working
As there were higher prio tasks my hope was, that any update or at latest V16 shall solve the issue,m so I did not contact support.
Yesterday I tried it and....this issue seems to be still a problem.
I have backup plans - one for each machine.
One of these plans protected a server that was replaced in the last weeks.
So I setup am off-host task with rerention times but although there are recovery points that should be deleted, they are still available.
Setup:
- Acronis Cyber Backup 16, most recent version, on-premise installation
- installed on Windows Server 2022
Backup-plan:
- full backups on saturday, incrementals on all other days of the week
- retention setup: full backups: 8 weeks, incrementals 28 days
- encrypted 
Off-Host cleanup plan
- retention setup: full backups: 8 weeks, incrementals 28 days, differentials 8 weeks
- applied to only one backup chain
- no schedule
The bacjup plan was running for 3 years (beginning with V15) and the cleanup was done properly.
I disabled the plan on 30th of december so the backup chain contains full backups back to 15th november and 2nd december 2025. So far so good.
If I execute the off-host cleanup plan the activity shows me that the plan ended successfully after only a few seconds. As a full backup is about 25GB this is veeeeery fast.
And after the off-site cleanup all recovery points are still there.
And yes, also after anupdate of the recovery point list, they are still there.   
Is this feature still not working?
Regards
Sven

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/20/2026 - 10:09

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Sven,
Thanks for the detailed description.
Off-host cleanup issues like this are typically environment-specific and require logs to diagnose properly.
Please contact Acronis Support with the backup server logs, along with the affected backup plan and any relevant details attached. The support team can safely review the execution and retention data.
Avoid manually deleting recovery points, as this can corrupt the backup chain.
Best regards,

      
                
                
                    
                                                    Tue, 01/20/2026 - 14:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
to be clear: I delete recovery points only via the correct way: the management server, so no worry.
Well I hope the ticket is answered a bit faster than the last one.
Honestly spoken it is really disappointing that such easy tasks cannot run properly on a completely fresh install (!) of V16 on a complete freshly installed machine.
Are there no tests done?
Regards 
Sven

      
                
                
                    
                                                    Tue, 01/20/2026 - 17:06
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hey Jose,
to be clear: I delete recovery points only via the correct way: the management server, so no worry.
Well I hope the ticket is answered a bit faster than the last one.
Honestly spoken it is really disappointing that such easy tasks cannot run properly on a completely fresh install (!) of V16 on a complete freshly installed machine.
Are there no tests done?
Regards 
Sven


Hi Sven,
I understand your frustration. As mentioned, each environment is unique, and only Support with access to the logs can properly analyze and resolve this issue. The forum is not the channel for case-specific troubleshooting. Please continue following up directly via your Support ticket.
Thank you for your understanding,
 

      
                
                
                    
                                                    Wed, 01/21/2026 - 15:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey there,
I had now good contact with support.
The result:  this is not a bug, it is a feature.
For an off-host retention plan the time/datet o which the retention rule refers is NOT the date on which the plan runs, but the date of the last backup. 
So to clarify:
- assumed there is a backup chain with the last recovery point dated 30th december 2025
- there is an off-host plan with retention rules that are configured to remove full backups that are older than 8 weeks and incrementals that are older than 28 days
Then you run this plan today on 28th jan.
The result: full backups before 5th of NOV and incrementals before 2nd DEC are deleted.
This is not described anywhere in the manual and maybe it helps any other people who run in that situation.
 
In my eyes it is a strange behaviour and not expected, but well...it is as it stands so I have to deal with it.
Greets S.

      
                
                
                    
                                                    Wed, 01/28/2026 - 17:37
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SvenT wrote:

Hey there,
I had now good contact with support.
The result:  this is not a bug, it is a feature.
For an off-host retention plan the time/datet o which the retention rule refers is NOT the date on which the plan runs, but the date of the last backup. 
So to clarify:
- assumed there is a backup chain with the last recovery point dated 30th december 2025
- there is an off-host plan with retention rules that are configured to remove full backups that are older than 8 weeks and incrementals that are older than 28 days
Then you run this plan today on 28th jan.
The result: full backups before 5th of NOV and incrementals before 2nd DEC are deleted.
This is not described anywhere in the manual and maybe it helps any other people who run in that situation.
 
In my eyes it is a strange behaviour and not expected, but well...it is as it stands so I have to deal with it.
Greets S.


Hi Sven,
Thank you for following up and sharing this clarification with the community.
I will certainly pass your feedback regarding the documentation to our technical writing team to ensure this behavior is more clearly defined in the user manual.
Best regards.
 

      
                
                
                    
                                                    Thu, 01/29/2026 - 08:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
