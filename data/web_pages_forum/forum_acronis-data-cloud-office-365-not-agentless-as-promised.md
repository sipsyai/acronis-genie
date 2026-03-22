# Acronis Data Cloud Office 365 - not agentless as promised?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-data-cloud-office-365-not-agentless-promised

## Original Post
**Author:** Unknown

Acronis Data Cloud Office 365 - not agentless as promised?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Brilliant Support
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            OK - trialling an Office 365 backup solution for a client before we take the plunge for all of our Exchange Online users.
Logged into the Management Console and first thing I was prompted to do was download an agent and install - I did this (locally on my laptop).  After this I could login to Office 365 and view the mailboxes.
I added the two mailboxes I wanted to a job and started the backup and left it running.
At the end of the day I packed up my laptop and went home.
I checked the job this morning and it failed when my laptop was powered off due to a kernel API shutdown - which suggests the local agent was involved in the job.
I also notice if I delete my machine from the list of agents, I can no longer login to the Office 365 section.
How can this product be promoted as agentless when an agent is required to login and run the backups even though it's a cloud service to cloud storage solution?  Am I missing something really basic?
Could somebody let me know please.
Peter

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/17/2019 - 05:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good morning Peter!
 
It's Evgeny from Acronis Service Providers Support. 
As far as I understand you tested the Office365 solution and you would like to know more about the agentless setup.
I will be glad to assist. 
 
Based on the description you provided, I can assume you used the locally installed Agent for Office 365 (which is "agent-based"), while you were actually aiming at using the agentless (Cloud Agent for Office 365)
I suggest you proceed with the Cloud Agent deployment to meet your requirement.
 
If you have other questions - don't hesitate to ask.
 
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Thu, 01/17/2019 - 08:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brilliant Support
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Evgeny
Thanks for that.
However, when I login to the console I was prompted to download an agent and install - until I did this the Microsoft Office 365 tab did not appear under the Devices section.
As a test, I have now deleted the machine I added under settings - now when I go to Microsoft Office 365 I am prompted for login details - I enter my Office 365 Global Admin and this now refuses to login successfully - it tries forever with no success.
Also when browsing my backups, because the agent has now been removed I get the message that there are no agents that can browse backups.
I must be missing something simple because when I read the online help page you directed me to it appeared to suggest I could just add the credentials and it would show the mailboxes available but this does not appear to be the case.
If you need any more information to help troubleshoot this I'm happy to supply this to you.
Peter

      
                
                
                    
                                                    Fri, 01/18/2019 - 01:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brilliant Support
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Evgeny
Just to add to this - once I re-registered the machine that had the agent, I could browse the Office 35 section and view mailboxes again.
However, when browsing backups or trying to recover, it tells me there are no backups present.
But if I look at my site dashboard, it tells me I'm using 16.79Gb which I assume I'm going to be charged for - protected Office 365 Seats is showing as 0 though ...
Peter

      
                
                
                    
                                                    Fri, 01/18/2019 - 01:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brilliant Support
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Evgeny
Quick update - I purchased the Acronis Backup option from our local distributor (Ingram Micro) as a monthly subscription and it appears the issue may be related to how they have this configured in their global tenancy.
I've gone and got a separate trial outside of this ecosystem and the setup is different - testing this again now including for archives.
If it all works I'll try to get some support out of our local rep.
Peter

      
                
                
                    
                                                    Fri, 01/18/2019 - 02:28
