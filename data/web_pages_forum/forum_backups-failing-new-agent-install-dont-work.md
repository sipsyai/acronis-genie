# Backups failing, new agent install don't work

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backups-failing-new-agent-install-dont-work

## Original Post
**Author:** Unknown

Backups failing, new agent install don't work

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    dasky
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I'm having an issue with taken backups or installing new agents. My agent version is 12.5.22750. 
If I try to install an agent on a new Windows machine will fail. On the cloud management console I can see in the activity view the below:
- Adding agent 'PC' to the management server
- Removing agent 'PC' from the management server
The above is keep repeating itself every second for a long time, then on the client computer will get something like installation successful, but the agent activation is not.
If I reboot the computer, eventually it will show up on the management console. By creating a new backup plan, the backup will never succeed.
On the client PC I can see it is showing "calculating time remaining". The management console show backup in progress 0%.
Which will eventually fail with this error:
"The running backup has not shown any progress for some time and may be frozen."
I also get these as well:Activity 'Refreshing recovery points' failed. Failed to establish connection with cloud storage 'hxxps://eu2-cloudbackup.comodo.com:443'. This may happen due to a blocked port or other network issue.
So my testing shows that the backups is not working on new computers that never had acronis installed them before. Which is more frustrating that they don't work on PC where they were working for years.
I got the below error on the old installs:
"Request to the cloud platform failed because the agent is not registered."
or
"Failed to establish connection with cloud storage 'hxxps://eu2-cloudbackup.comodo.com:443'. This may happen due to a blocked port or other network issue."
Cannot even browse the backup plan on these. 
I have tested the connection with port_checker_en-US_x86.exe, all checks out, no errors.
Any help would be appreciated!
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/04/2020 - 17:46

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dasky,
Thank you for reporting your issues in our Cloud Forum.
For the error "The running backup has not shown any progress for some time and may be frozen." we can suggest to increase the Archive3 cache that will boost the speed of processing the backups. Before applying the changes you might first check the current Archive3 cache in the MMS log: C:\ProgramData\Acronis\BackupAndRecovery\MMS\mms.0.log
Look for a line where the backup service_process has started, it should contain the message like:
service_process(5912): Using default page cache size 63 MB
63 MB is the default cache size. I would suggest you increase the cache size to 1 GB first, follow the instructions from this KB article for Windows: https://kb.acronis.com/content/61758
But the best I would suggest is opening a Support ticket as the reported issues seem complicated and they require deeper investigation, collection of system information logs from the affected machines (logs will be big in size and a Support FTP is required, Cloud Forum will not handle all logs collection), also read-only access to your Backup Console from a Support engineer to check all issues in place.
Please, open a Support ticket, share the same description and provide your Acronis Cyber Cloud account login name, DC of your account, affected tenant group, affected machine/machines, and our Support engineers will investigate it.
Thank you.

      
                
                
                    
                                                    Fri, 06/05/2020 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dasky
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ivaylo,
Thanks for your reply. I have checked the MMS logs for the last few days but there is no mention of the cache size at all.
I would love to log a ticket, however, I have purchased the service/license from a partner iTarian (Comodo). Unfortunately, they do not support it at all, just keep telling me Acronis supports it. I don't get support from Acronis either since I'm not able to present a license key (guessing Comodo has it). I have tried already to talk to Acronis's licensing support, but they said that cannot find any information related to my email address, so they cannot help.
Could you recommend a way of getting support?
I'm login into Comodo's backup portal https://eu2-cloudbackup.comodo.com with my creds, but that does not seem to be registered with Acronis.
Any help would be appreciated!
Regards, dasky

      
                
                
                    
                                                    Mon, 06/08/2020 - 11:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello dasky,
checking internally with the team, please accept our apologies for the unpleasant experience! 

      
                
                
                    
                                                    Mon, 06/08/2020 - 14:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dasky
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
Just wanted to check if you have managed to find a way for me to get support?
Thanks!

      
                
                
                    
                                                    Wed, 06/10/2020 - 12:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello dasky,
please accept our apologies for the delay! Would you mind sharing the ticket ID of your support case with Comodo, if there was any? 

      
                
                
                    
                                                    Fri, 06/19/2020 - 10:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dasky
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
The issue has been resolved. Apparently it was caused by an expired certificate somewhere between Acronis and Comodo.
 
 

      
                
                
                    
                                                    Sat, 10/10/2020 - 08:05
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            dasky wrote:

Hi,
The issue has been resolved. Apparently it was caused by an expired certificate somewhere between Acronis and Comodo.


Thank you for posting an update\feedback!  

      
                
                
                    
                                                    Mon, 10/12/2020 - 11:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
