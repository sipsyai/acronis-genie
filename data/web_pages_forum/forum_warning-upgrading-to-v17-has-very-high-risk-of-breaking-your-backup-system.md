# Warning: upgrading to V17 has very high risk  of breaking your backup system

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-17-forum/warning-upgrading-v17-has-very-high-risk-breaking-your-backup-system

## Original Post
**Author:** Unknown

Warning: upgrading to V17 has very high risk  of breaking your backup system

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Yesterday I attempted to upgrade from Cyber Protect V16 to V17 after reading the release notes, seeing there were security fixes included and finding nothing particularly worrying in the "Known issues" that could affect me. The process took unusually long compared to past version or release updates I've done in the past. When it got to 99% it threw a failure to register agent error and broke access to AMS. Apparently, this is a well-known issue (https://care.acronis.com/s/article/After-upgrading-to-Acronis-Cyber-Pro…) and has been under investigation for a week now, as shown in that article's publication date.
Nothing I have tried to get it complete the installation worked so today I had to open a ticket with support which is still pending. Now not only we cannot make any backups but also, we have no restoring option from previous backups in case of a failure. 
If this problem is occurring frequently this release should be pulled out and not rereleased until fully fixed. Quite honestly, this doesn't speak too well of Acronis QA department. I hope Acronis gives this the highest priority and puts all necessary resources to correct the situation as quick as possible, meaning hours rather than days or weeks.
I strongly recommend everyone to not upgrade to V17 until a build is released with the required corrections.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/06/2025 - 10:57

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Javier,
We are sorry to hear about the issue with the registration.
Please note that our support team is already reviewing your case.
I have added notes to the ticket to highlight the importance of the matter and to ensure proper follow-up.
You can expect to be contacted as soon as possible.
If you need any updates in the meantime, feel free to message me here.
Best regards,

      
                
                
                    
                                                    Thu, 11/06/2025 - 11:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            A new build has been released that fixed my installation problem and I'm able to access the AMS console again but I'm still having many issues.
I can't do anything with tapes, erasing, moving to another pool or backing up is impossible, hopefully I can get this sorted out tomorrow with Acronis support.
I can use USB attached HDDs but performance is atrocious, maybe is related to Storage Node but backups that would usually take 3-5min have taken today 56 and thrown out plenty errors in the process.
All in all, it has been a bad start but it seems there might be some light at the end of the tunnel.
Cheers
 
Update:
Our tape problems persists, nothing seems to work, also I found that MS Exchange has serious issues too. Almost impossible to backup mailboxes because of continuous disconnections and databases need to be backup up one by one to get at least some minor reliability.
Any one considering updating... don't!!!! 

      
                
                
                    
                                                    Thu, 11/06/2025 - 17:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            UPDATE 2:
The tape issues we were having j¡have been solved by Acronis support. The problem was that the ARSM sqllite database had not been properly updated in the upgrade process.
OTOH, the problems with the Exchange server agent still persist. We cannot backup anything neither to tape nor to HDD. A new ticket has been opened and I have been warned that this one may take longer to solve. My advice to anyone considering upgrading is to never update a working system until at least a few months after its release, wait for al teething problems to be solved, at least the more serious ones.
 
UPDATE 3:
MS SQL server is also affected, it hangs upon completion and job freezs until forcefully terminated by stopping services at the VM with the agent. Cancelling the job in the console does not stop it.
 

      
                
                
                    
                                                    Wed, 11/12/2025 - 14:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

UPDATE 2:
The tape issues we were having j¡have been solved by Acronis support. The problem was that the ARSM sqllite database had not been properly updated in the upgrade process.
OTOH, the problems with the Exchange server agent still persist. We cannot backup anything neither to tape nor to HDD. A new ticket has been opened and I have been warned that this one may take longer to solve. My advice to anyone considering upgrading is to never update a working system until at least a few months after its release, wait for al teething problems to be solved, at least the more serious ones.
 
UPDATE 3:
MS SQL server is also affected, it hangs upon completion and job freezs until forcefully terminated by stopping services at the VM with the agent. Cancelling the job in the console does not stop it.
 


Hello,
Thank you for sharing the update and details.
Glad to hear the tape issue was resolved — indeed, that ARSM database update can sometimes cause inconsistencies after upgrades.
Regarding the Exchange and SQL agents, please keep working with our support team under the new ticket so they can review the logs in depth. These cases often require a closer look at the agent-side components and scheduler services.
Best regards,
José
 

      
                
                
                    
                                                    Wed, 11/12/2025 - 17:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tappsy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Javier,
just wanted to say thanks for sharing your experience. I considered to Update soon because of the SE-Support but this seems like a showstopper at the moment. Kind frustrating but better than a not working backup infrastructure. Worst part for me is the missing support of Windows Server 2016, because i would have to upgrade the server prior installing Acronis 17.
Kind regards!

      
                
                
                    
                                                    Thu, 11/13/2025 - 08:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Tappsy,
We were on Exchange 2019/WS2022 and migrated to Exchange SE/WS2025 and we had no problems with that, it went without any incident. Both of these were VM machines in a Hyper-V host running Cyber Protect V16. There were some hiccups while backing up SE mailboxes Exchange agent when both Exchange servers were running. It took lots of patience and work the iron them out but, once all mailboxes were migrated and the old server decomissioned, we got perfectly fine backups at both levels on the SE. There were no issues backing up either server at any time at the VM+Windows agent or at the database level with the Exchange server agent. 
It was the update to V17 who broke things again. V16 had been extremely reliable for a very long time and I was quite happy with it.
After a little over a week of working with Acronis support we are again able to backup all VMs to tape (our prefered method beacuse of 'air gap' security) but agent based backups are still not functioning and cause many problems. This is quite a problem because those make life much, much esasier in case one needs to recover a single email message or database.
I would recommend you to migrate from whatever Exchange version you have on WS2016 to SE/WS2025 if you can but stay on ACP V16 backup until V17 gets all its bugs fixed. If migration is not possible get the extended upgrades from MS for Exchange until you can move to the latest platform combo.
 
 

      
                
                
                    
                                                    Thu, 11/13/2025 - 08:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tappsy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We already migrated from Exchange 2016 on Server 2019 to Exchange 2019 on Server 2022 and are using the latest CU, so Upgrade to Exchange SE is only a small inplace-Upgrade.
But i won't do it until Exchange SE is fully supported by Acronis. This is done via Cyber Protect 17 but your problems with 17 are a showstopper for me. I will wait a couple of weeks.
Fingers are crossed that all you problems are solved soon!

      
                
                
                    
                                                    Fri, 11/14/2025 - 07:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tappsy wrote:

We already migrated from Exchange 2016 on Server 2019 to Exchange 2019 on Server 2022 and are using the latest CU, so Upgrade to Exchange SE is only a small inplace-Upgrade.
But i won't do it until Exchange SE is fully supported by Acronis. This is done via Cyber Protect 17 but your problems with 17 are a showstopper for me. I will wait a couple of weeks.
Fingers are crossed that all you problems are solved soon!


Hello!
Thank you for the update and for sharing your setup.
Just to note, Exchange Server SE is already fully supported in Acronis Cyber Protect 17, so you can proceed with the upgrade whenever you’re ready.
If you’d like more detailed recommendations or advanced configuration advice, please contact our support team, they can review your specific environment and provide tailored guidance.
Best regards,José
 

      
                
                
                    
                                                    Fri, 11/14/2025 - 11:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I tried to upgrade from V 16.40354 to version 17.0.41224. The same error occurred for me and I have no access to the AMS web interface.
Nothing has changed at Acronis in all these years.

      
                
                
                    
                                                    Mon, 11/17/2025 - 11:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            cerberus wrote:

I tried to upgrade from V 16.40354 to version 17.0.41224. The same error occurred for me and I have no access to the AMS web interface.
Nothing has changed at Acronis in all these years.


Hello!
If you are using Acronis Cyber Protect 17, kindly report this to our support team so it can be reviewed. Also keep in mind that when upgrading to a newer product, certain system conflicts or configuration issues can appear, this does not necessarily indicate a product defect or a root cause that must be escalated. Support will help you verify the setup and resolve the behavior.
Best regards.

      
                
                
                    
                                                    Mon, 11/17/2025 - 15:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I've been using Acronis for 15 years and a new version has never worked. Every time you have to spend hours creating system reports and then the error should be fixed at some point. And for every bug fixed, two new ones are added.
If I had read the first post earlier...

      
                
                
                    
                                                    Mon, 11/17/2025 - 16:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SQL and Exchange Agent backup functionality is still broken, I have been contacted in a few days. Looks like support has more important things to do than fixing V17.
For those still trying to decide whether to upgrade, If you value your data and peace of mind..... DON'T!!! Wait until all critical issues are solved.
 

      
                
                
                    
                                                    Tue, 11/18/2025 - 07:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

SQL and Exchange Agent backup functionality is still broken, I have been contacted in a few days. Looks like support has more important things to do than fixing V17.
For those still trying to decide whether to upgrade, If you value your data and peace of mind..... DON'T!!! Wait until all critical issues are solved.
 


Hello Javier.
I've requested the team to review the ticket.
You can expect a reply as soon as possible.
Best regards. 

      
                
                
                    
                                                    Tue, 11/18/2025 - 10:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mr Simon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Upgrading to V17 is risky because it can break your existing backup system. It’s best to test it first in a safe environment or wait until compatibility is fully confirmed.

      
                
                
                    
                                                    Tue, 12/16/2025 - 16:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mr Simon wrote:

Upgrading to V17 is risky because it can break your existing backup system. It’s best to test it first in a safe environment or wait until compatibility is fully confirmed.


Thanks for the comment.
While upgrading to v17 is generally safe, best practice is to test major upgrades in a non-production environment first. If you have any doubts about compatibility with your current setup, we strongly recommend contacting Acronis Support so they can review your specific configuration and advise on the safest upgrade path.
Best regards.
 

      
                
                
                    
                                                    Wed, 12/17/2025 - 13:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Not everyone can afford to duplicate its infrastructure to have an identical testing platform, it would be great but it can get quite costly. Asking support to evalute one's system to check potentital issues, if at feasible, can be quite a long process and when there are "security" patches included in an upgrade/update with no additional info provided "for security reasons" one has to choose between two evils, braking your backup systems or have a security problem.

      
                
                
                    
                                                    Wed, 12/17/2025 - 14:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Not everyone can afford to duplicate its infrastructure to have an identical testing platform, it would be great but it can get quite costly. Asking support to evalute one's system to check potentital issues, if at feasible, can be quite a long process and when there are "security" patches included in an upgrade/update with no additional info provided "for security reasons" one has to choose between two evils, braking your backup systems or have a security problem.


You’re right that not everyone can maintain a fully mirrored test environment, and that’s a valid concern. In practice, testing doesn’t always require an identical infrastructure — even a limited or staged validation can significantly reduce risk.
When security fixes are involved, updates are released to address potential risks while maintaining backward compatibility. Although detailed information may be limited for security reasons, upgrades are designed not to break existing backup configurations.
If a full test environment isn’t feasible, the recommended approach is to upgrade in phases and, when in doubt, involve Support so they can review the setup and advise on the safest path forward.
Best regards.
 

      
                
                
                    
                                                    Wed, 12/17/2025 - 14:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Unless you mean a multi-system deployment I don't understand how can anyone upgrade in phases? like not upgrading agents to same release as Management Server?
We have a single virtualization host running ACP so I don't think that applies to us?

      
                
                
                    
                                                    Wed, 12/17/2025 - 14:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

Unless you mean a multi-system deployment I don't understand how can anyone upgrade in phases? like not upgrading agents to same release as Management Server?
We have a single virtualization host running ACP so I don't think that applies to us?


Hi Javier,
By “upgrade in phases,” we don’t necessarily mean a multi-system or large-scale deployment. In simpler environments, this can be as straightforward as validating the upgrade on a limited scope before committing fully.
For example, this may include upgrading the management components first, verifying core functionality (backup, recovery, access, scheduled tasks), and only then proceeding with the remaining components. In single-host or small environments, this validation phase is naturally more limited, but the principle remains the same.
If your setup consists of a single virtualization host running ACP17, there is no true “phasing” in the enterprise sense. In such cases, the recommended approach is to ensure compatibility, take a precautionary backup, and involve Support ( https://support.acronis.com/ ) if there are concerns specific to your configuration.
Best regards,
 

      
                
                
                    
                                                    Wed, 12/17/2025 - 14:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Javier
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            After 2.5 months our problem has not been solved.
 
 

      
                
                
                    
                                                    Mon, 01/26/2026 - 17:17
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Javier wrote:

After 2.5 months our problem has not been solved.
 
 


Hi Javier,
I understand the ongoing frustration. As previously mentioned, for your single-host setup, the recommended approach is to ensure compatibility, take a precautionary backup, and involve Support (https://support.acronis.com/) for any configuration-specific concerns.
Forum posts are intended for peer-to-peer discussion and knowledge sharing. They are not handled as support tickets and do not follow ticket SLAs, so we cannot provide resolution timelines here.
I encourage you to open a ticket with Support so the issue can be investigated directly. Once you have an update from them, feel free to share relevant information here for discussion with the community.
Thank you for your understanding.
Best regards,
 

      
                
                
                    
                                                    Mon, 01/26/2026 - 17:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
