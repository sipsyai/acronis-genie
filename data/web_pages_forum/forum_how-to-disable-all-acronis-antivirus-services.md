# How to disable ALL Acronis antivirus services

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-disable-all-acronis-antivirus-services

## Original Post
**Author:** Unknown

How to disable ALL Acronis antivirus services

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Cocke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Twice this week I have encountered an issue with one of my customer's machines I manage in that something we're trying to install isn't working only to eventually figure out it is Acronis that was blocking it.  It would be helpful if we had some type of alert that it's blocking the process(es).   Today I was trying to install an antivirus product for another vendor and it kept failing.  It appears it is the Windows Service named AcronisCyberProtectionService that is causing the interference but we cannot stop or disable this service.  
Further, we do not use the Acronis antivirus product, nor do we have the Acronis "Active Protect" feature enabled in the Backup Plans.
The only way I have found to proceed with what I needed to do was to uninstall the Acronis Agent, install the needed software, then reinstall Acronis (for backups).  We just need Acronis for backups, so how do we disable the other antivirus functions (even temporarily)?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/23/2020 - 18:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello David,
Acronis Cyber Protection and Acronis Active Protection services are marked as "NOT_STOPPABLE" and "NOT_PAUSABLE" by design as a part of self-protection mechanism. In current implementation the services can't be manually stopped or restarted, which is why to resolve any issues caused by these service a device reboot would be required, only possible workaround at the moment.
However, at the same time we understand that your customers is not using any Active or Cyber Protection features and having those services unmanageable looks like an issue to them.
1. For customers using Standard Edition without Active Protection functionality this shouldn't be an issue however, but the services are still running and are not stoppable.
2. Development team is currently estimating and planning the implementation that would allow to avoid running services that are not actively used or at least removing the dependencies where possible.
3. Preliminary estimations to provide delivery dates of this feature were not yet provided.
4. An internal development task with ID AMP-2649 was provided by the Security Team that we can follow, but as of now it's in the early state with no dates confirmed or even suggested.
Thank you.

      
                
                
                    
                                                    Fri, 07/31/2020 - 08:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello David,
We need more info about 3rd party antivirus product from another vendor that you are trying to install so we can ensure that internal development task AMP-2649 will help and you'll be able to use both without conflicts of the services.
Name, vendor, exact version and build, running services, OS where we get these problems.
Thank you.

      
                
                
                    
                                                    Wed, 08/12/2020 - 07:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Leon McKinney
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I think it's pretty arrogant to not allow users to disable services.  I did stop AcronisActiveProtectionService - it was hogging my CPU - but as you said above, I can't stop AcronisCyberProtectionService.  So here it two months later, I have Acronis TrueImage 2021 and the problem is still there. FIX THIS!!!

      
                
                
                    
                                                    Sat, 09/26/2020 - 14:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Boreas Jeff
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We use Acronis to back up over 300 machines.  Recently I was troubleshooting issues with machines that looked like a problem with two antivirus/malware programs running at the same time.  We only use Sophos as our antivirus and make sure all others are disabled.  So I thought, maybe the user installed something.  I see this service for Cyber Protection as the culprit.  So I wonder what the user installed this time?  Turns out that we got it as part of an update to our Acronis BACKUP software! WTF!?  So now we have 300+ machines running both Sophos and Cyber Protection and seeing all kinds of issues, new issues crop up every day.  So now I'm scrambling to find a way to fix this mess.  any suggestions?  And it's not just the Cyber Protection, we've identified issues with Active Protection that manifest even when disabled, so it needs to be comletely removed.  The only workaround we currently know of is to remove Acronis from all machines.  If it comes to that, then we will be looking for a true backup solution to get away from this disaster.
How do you disable Acronis Cyber Protection Service?  If I try to Stop or Disable, I get Access Denied.  I need to know how to remove and disable the anti-virus components of Acronis as they are causing all kinds of problems, interfering with Sophos, hangs, performance, etc. Every day we find a new issue that it's causing. This is critical. We only use it for backup and now it's our top problem.

      
                
                
                    
                                                    Thu, 10/01/2020 - 18:43
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud Backup 12.5

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Boreas Jeff wrote:

How do you disable Acronis Cyber Protection Service?  If I try to Stop or Disable, I get Access Denied.  I need to know how to remove and disable the anti-virus components of Acronis as they are causing all kinds of problems, interfering with Sophos, hangs, performance, etc. Every day we find a new issue that it's causing. This is critical. We only use it for backup and now it's our top problem.


Dear Boreas,
first of all, please accept our apologies for the negative experience. Currently, the user can disable Acronis Cyber Protection feature from the Protection Plan (disable "Active Protection" or "Antivirus & Antimalware protection" in the Protection Plan).
The services active_protection_service.exe and cyber-protect-service.exe specifically are always installed together with the agent. We do have an incoming feature request to exclude Antimalware components from being installed (internal ID for reference RM-1409 Allow Agent installation without Antimalware components). I've added your feedback as a vote for this change, thank you!
 

      
                
                
                    
                                                    Fri, 10/09/2020 - 11:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Leon McKinney wrote:

I think it's pretty arrogant to not allow users to disable services.  I did stop AcronisActiveProtectionService - it was hogging my CPU - but as you said above, I can't stop AcronisCyberProtectionService.  So here it two months later, I have Acronis TrueImage 2021 and the problem is still there. FIX THIS!!!


Hello Leon,
thank you for your feedback! I've created a change request based on your comment (internal ID for reference TI-213392 Allow installation without Antimalware components). The product management will consider the changes based on the collected feedback.
In the current implementation, we cannot allow disabling the services, because it would make them exposed to the external threats (malicious processes will have the possibility to disable our protection). However, when protection is deactivated (go to Protection section, click Pause protection and select Turn off protection or select the length of the pause), related Acronis processes and services while still active should use minimal resources. 
Note, that a perpetual license Acronis True Image 2021 Standard and Acronis True Image Essential subscription do not include the Antivirus. 

      
                
                
                    
                                                    Fri, 10/09/2020 - 12:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    John Wellard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
I think that I might have the answer to your problem.
I have recently started programing first in C++ but when I could not find a way of using Unicode characters. My location in Spain meant that I needed the accented characters the € and ¿. I transferred my attention to Python. I then ran into other problems. When I used pyinstaller to write the .py script into .exe the file appeared in the correct folder but after approximately 2 seconds it was reduced to zero bytes.
At first I thought that this was the intervention of my Norton software. I have found this to be particularly aggressive in the past. So I disabled Norton temporarily and it still happened. I then turned my attention to Acronis.
With WE open in one window showing the .exe file destination; Task Manager in another window showing the Acronis modules I ran the compiler again and low and behold when the .exe file appeared in its destination the CPU usage for Acronis Cyber Protect Service jumped to 20% for a few seconds; the .exe was reduced to zero bytes and then the CPU requirement dropped to near zero.
I then disabled the Cyber Protect in Acronis via. The Protection option and tried again. The file stayed in place, was there some 15 minutes later and after re-activation the protection is still there.
My conclusion therefore is that the problem is solved by temporarily turning off this protection and in my case with Norton installed I will turn it off permanently as this program will provide the same protection.
Trying this solution temporarily may solve your problem.

      
                
                
                    
                                                    Wed, 11/04/2020 - 15:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SmashBro
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
Why do I have to have all of those things running even though I have directly disabled them in Acronis settings? I installed a BACKUP solution, not an antivirus. I don't need all this crap running in the background.

Why do those setting exist in the first place? To give me an illusion of choice?
It is now getting to a point now where I don't trust my backup solution. Guess I will have to find a new one.

      
                
                
                    
                                                    Wed, 11/18/2020 - 09:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    erik santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I ran into this issue minutes after upgrading.. wish I hadnt. I purchase a backup program I expect a backup program. I tried to turn off protection only to get  the " Cannot Disable All Active Protections" error.. and I HAVE the standard 3 pc perpetual license.. fix this.. I wish I would have tried before upgrade.. This may be the reason I need not to upgrade again and end use of Acronis altogether.

      
                
                
                    
                                                    Thu, 11/26/2020 - 18:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    R
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm having this problem as well.  I just upgraded to Acronis 2021 and I got a notification that a scan had been completed, which I thought was odd since I couldn't imagine what it was scanning.  Come to find out that not only did Acronis "quarantine" some of my files, but I can't restore them, it just says "cannot restore filename". 
This is like the literal opposite of backup software.
Luckily I was able to grab them off my NAS and put them back where they belong, but I can only assume Acronis is going to quarantine them again next time the scan runs.  Though considering the files it quarantined are on a RAID that Acronis isn't even supposed to be accessing for backups, let alone virus scanning, who knows what will happen.
I was able to disable Ransomware Protection and Web Filtering, but when I disable Real Time Protection and hit OK it's still on when I recheck the settings.  I can't disable Vulnerability Assessment either, same issue.
Similarly, if I change the Antivirus Scan to "Do Not Schedule" it just returns to Weekly when I check the settings again.
And no, I don't want to go around making exclusions every time Acronis thinks a file is unsafe, because that's not Acronis' job.
Guys, this is a real issue and it needs to be fixed.

      
                
                
                    
                                                    Sat, 12/05/2020 - 21:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivan Van Lommen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have the same problem Since installing Acronis 2021 my Mac got slow, showing the Spinning Beach Ball.
In Activity Monitor I see cyber-protect-service is using 99,5% of CPU !
This cannot be disabled or switched off in the Acronis settings.  Even when switching off Protection the Acronis setting, cyber-protect-service continues to operate.
This make Acronis practically unusable.  Is the only solution to uninstall the program completely?
ACRONIS, FIX THIS IMMEDIATELY!

      
                
                
                    
                                                    Thu, 12/10/2020 - 14:04
                                                                            
                                
                            
                                            
                                            
    
                    
                 

 

 

 

 

 

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SmashBro, erik santiago, R, Ivan Van Lommen
sorry to know about your negative experience with our protection features! I've registered your feedback as votes for the existing change request TI-213392 Allow installation without Antimalware components.

      
                
                
                    
                                                    Mon, 12/14/2020 - 17:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Waedt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I've registered your feedback as votes for the existing change request TI-213392
Please do the same for me.
I purchased a a private version of Acronis 2021.
At work we use many Acronis 2019 and 2020 licenses. I'll postpone any upgrades until it will be possible to install and activate ONLY the backup functionality.

      
                
                
                    
                                                    Mon, 12/14/2020 - 18:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Karl , thank you, added your vote!

      
                
                
                    
                                                    Mon, 12/14/2020 - 18:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    R
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Ekaterina.
In the meantime is there a safe method to downgrade back to Acronis 2020 so I can stop it from deleting my files?

      
                
                
                    
                                                    Wed, 12/16/2020 - 00:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lars Olsson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! I would like to add my vote to request TI-213392. Version 2021 was very aggresive on CPU from start, even if you try to disable what you can disable with antimalware. But the last update 343400 made it completely unusable. It took hours to start and whean it at lost got up running nothing could be done without further long waiting. I have unistalled it and reinstalled 2020. What a relief to run that version.
Lars Olsson

      
                
                
                    
                                                    Sat, 12/19/2020 - 17:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    R
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just updated to True Image 2021 Update 3 (Build 35860) and am now able to turn off virus scanning and real time protection.  I'm not sure if that was part of this most recent update or something else as it's not listed in the release notes, but truly thank you for fixing it regardless.

      
                
                
                    
                                                    Thu, 12/24/2020 - 06:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    system_account
                            

                            
                    
                        Forum Star
                    
                
            
                        
                
                    Posts: 198
                
            
            
                
                    Comments: 840
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My Acronis True Image application continues to freeze up.  Seems to be tied to the part of the programming that Applies User Settings, but even when after "sometimes" getting past Applying User Settings (10+ minutes of inactivity), the application freezes when attempting to select any of the available options.
Why has the 2021 upgrade proved so troublesome?  Can someone please help?  I'm getting ready to install another backup solution.  Five (5) attempts to resolve this issue with Acronis support have me continuing to battle application freeze-ups, even after seeming to be temporarily fixed.

      
                
                
                    
                                                    Sat, 12/26/2020 - 19:05
                                                                            
                                
                            
                                            
                                            
    
                    
                spam

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hoerééé, disabled acronis security and my computer is working again normally !!!!!!
 

      
                
                
                    
                                                    Thu, 12/31/2020 - 15:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    system_account
                            

                            
                    
                        Forum Star
                    
                
            
                        
                
                    Posts: 198
                
            
            
                
                    Comments: 840
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            May I ask the exact steps you took to disable Acronis Security?

      
                
                
                    
                                                    Thu, 12/31/2020 - 15:57
                                                                            
                                
                            
                                            
                                            
    
                    
                spam

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Gregory Kline wrote:

May I ask the exact steps you took to disable Acronis Security?



      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      563870-209732.JPG

                      24.21 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 12/31/2020 - 16:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Richard F
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm also having an issue with these two services. We have 5 or 6 licenses for ATI 2020, and while the backup works great, this active protection issue does not. Just today a machine started abnormally because of the active protection service overloading resources.
We didn't purchase protection. Like others, we already have it. So just give us a way to disable these services and stop stalling.

      
                
                
                    
                                                    Sat, 01/02/2021 - 16:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Richard F wrote:

I'm also having an issue with these two services. We have 5 or 6 licenses for ATI 2020, and while the backup works great, this active protection issue does not. Just today a machine started abnormally because of the active protection service overloading resources.
We didn't purchase protection. Like others, we already have it. So just give us a way to disable these services and stop stalling.


Read messages 19, 20, 21.

      
                
                
                    
                                                    Sat, 01/02/2021 - 18:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    erik santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This piece of garbage STILL wont stop the protection services. I hit the button to turn it off permanently but it started up again at reboot then gives me the "cannot disable all Active protection features." error.. what a p.o.s. It keeps putting random files in quarantine that are most definitely NOT virus.. because the anti-virus and anti-malware I CHOOSE to run clears them. Fix this crap.. or don't.. at this point not worth the frustration.. I will find another solution.. and recommend that no businesses I deal with waste there money or time on this crap.. used to be the best.. now the absolute worst!

      
                
                
                    
                                                    Mon, 01/04/2021 - 03:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Here no problem, see picture. It is in dutch and it says:
Active protection is disabled.
Protection is permanent stopped.
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      564193-209853.JPG

                      52.79 KB
                  
              
                      564193-209856.JPG

                      63.65 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 01/04/2021 - 11:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            R wrote:

Thank you Ekaterina.
In the meantime is there a safe method to downgrade back to Acronis 2020 so I can stop it from deleting my files?


Hi! If you have a subscription license, I could send you the download link for a previous product version. Please let me know, if the old installation file is needed. 

      
                
                
                    
                                                    Tue, 01/05/2021 - 20:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Everyone,
registered your feedback in the change request TI-213392 Allow installation without Antimalware components. If you experience any issues causing the application or system slowness, we' strongly recommend reporting them to the support team, so that our engineers can find the cause and fix it. 

      
                
                
                    
                                                    Tue, 01/05/2021 - 20:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jin Cho
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi! If you have a subscription license, I could send you the download link for a previous product version. Please let me know, if the old installation file is needed. 

 
Can you please include a link to old installation file. Since the upgrade I have clicking noise in my music production software which is resource hungry.  You have to allow total disabling of any software it's just good practice and I'm dissapointed that you are not listening to your users above.. it sounds like a poorly thought up feature.
 
 
 

      
                
                
                    
                                                    Wed, 01/06/2021 - 21:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jin Cho wrote:
Can you please include a link to old installation file. Since the upgrade I have clicking noise in my music production software which is resource hungry.  You have to allow total disabling of any software it's just good practice and I'm dissapointed that you are not listening to your users above.. it sounds like a poorly thought up feature 

Hi! Please check your private messages for the installation file 

      
                
                
                    
                                                    Tue, 01/12/2021 - 08:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lance Hunter
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Please provide me link to previous version that does not have this issue.  

      
                
                
                    
                                                    Mon, 01/18/2021 - 15:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Roger Chambers
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Count me into that request for TI-213392. ATI 2020 was perfect me along with the Anti Ransomware which doesn't cause any issues.  Then  the upgrade came along. Conflicts and problems which I don't need. I was refunded and rolled back to 2020
If the request is acted on, I'll be back for the upgrade again

      
                
                
                    
                                                    Tue, 01/19/2021 - 17:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Roger Chambers wrote:

Count me into that request for TI-213392. ATI 2020 was perfect me along with the Anti Ransomware which doesn't cause any issues.  Then  the upgrade came along. Conflicts and problems which I don't need. I was refunded and rolled back to 2020
If the request is acted on, I'll be back for the upgrade again


Roger, added your vote, thank you! Please note that a perpetual license and Acronis True Image Essential subscription don't have the Antimalware functionality.

      
                
                
                    
                                                    Fri, 01/22/2021 - 10:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Lance Hunter wrote:

Please provide me link to previous version that does not have this issue.  


Hi! Please check your private messages  (at the top of a forum page click on My account and then on Dialogs)

      
                
                
                    
                                                    Fri, 01/22/2021 - 10:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Warren Hayden
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
The Good...
We recently purchased 6 Acronis True Image 2021 standard perpetual licenses to evaluate full image backups and to clone PCs. All our PCs have one of more duplicate backups. We used Acronis Universal Restore to clone a Dell to a Lenovo. The new system just worked. That included moving Office 2019, Visual Studio 2019, and many other software programs. Only had minor cleanup to uninstall Dell software and reinstall some Lenovo drivers and software. Didn't expect Acronis to take care of this.
We would rate this service 5 of 5, but documentation on how to do this efficiently as 3 of 5. We have taken enough notes to reliably reproduce by different individuals. All good up to this point. Would have heartily recommended product at this point if it were not for the bad and the ugly described below.
The Bad...
We were unaware that Acronis had not provisioned a custom install that does not include its Active Protection and Cyber protection. Like many others in the forum, we find it very intrusive to force these services on users.
Malware, by definition is something that runs, does stuff that you do not want or expect, consumes CPU/Memory resources, etc. that it shouldn't. Active Protection and Cyber protection are, by our definition, malware because we did not want it or expect it with our purchase. Our bad for not doing better research.
When you try to stop malware, it usually restarts itself, sometimes creating multiple copies in the process. Malware requires painful intervention to get it stopped.
The Ugly...
We did the following to get cleaned up installs on four PCs, which are now well behaved until updates overwrite our changes (the bad and ugly). We can now boot and get no startup log errors and can run Acronis GUI without setting off error logs. For some, this might be an acceptable solution. That is why I am sharing this process. However, we offer consulting service to businesses and cannot use or recommend a product that requires brittle intervention. If we tried to deploy a 100 or 300 licenses at a business, we would likely incur a large financial liability because it would continually break over time.
Here is what we did.
Changed file names:
    - C:\Program Files (x86)\Common Files\Acronis\ActiveProtection\anti_ransomware_service.stopped.exe
    - C:\Program Files (x86)\Acronis\Agent\bin\adp-agent.stopped.exe
Changed Registry:
    Registry Key: AcronisActiveProtectionService
        ErrorControl 1 => 0
        Start 2 => 0
    
    Registry Key: AcronisCyberProtectionService
        ErrorControl 1 => 0
        Start 4 => 0
    
    Registry Key: mmsminisrv
        ErrorControl 1 => 0
        Start 2 => 0
    
    Services Altered: Run services.msc
        Under Recovery, set failures to Take No Action and reset fail count to 1000 days. This may not be necessary.
        Acronis Active Protection (TM) Service
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Agent Core Service
            Changed to Disabled
        Acronis Cyber Protection Service
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Managed Machine Service Mini
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Mobile Backup Server
            Changed to Disabled
        Acronis Mobile Backup Status Server
            Changed to Disabled
Your needs may vary and these settings have only been checked for the standard perpetual licenses that we purchased.
I hope Acronis will decouple backup/recovery/cloning completely from Active Protection and Cyber security. Please do not foist services on unsuspecting customers that are strictly coming to you for your most excellent backup/recovery/cloning capabilities.
I might take a serious look at some of your other intra-network solutions, not the cloud, but not while they are bundled into one application. Hint... keep them separate as licensable, purchasable modules. Let me choose what I want and need. No surprises. I will monitor Acronis for a while to see if there is any improvement here. If not, we'll move on to find a different intranet solution or may be forced to write our own.
Happy mole whacking to all...

      
                
                
                    
                                                    Wed, 01/27/2021 - 19:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Simpel: Ik wil Acronis True Image ZONDER antimalware !!!!
Regel dat..

      
                
                
                    
                                                    Thu, 01/28/2021 - 10:35
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Virtum
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:

R wrote:

Thank you Ekaterina.
In the meantime is there a safe method to downgrade back to Acronis 2020 so I can stop it from deleting my files?


Hi! If you have a subscription license, I could send you the download link for a previous product version. Please let me know, if the old installation file is needed. 


Please put in a vote for me for this change as well, and message me the link for the old installation.

      
                
                
                    
                                                    Thu, 02/11/2021 - 02:59
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                ATI
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    r kent
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Warren Hayden wrote:

Hello,
The Good...
We recently purchased 6 Acronis True Image 2021 standard perpetual licenses to evaluate full image backups and to clone PCs. All our PCs have one of more duplicate backups. We used Acronis Universal Restore to clone a Dell to a Lenovo. The new system just worked. That included moving Office 2019, Visual Studio 2019, and many other software programs. Only had minor cleanup to uninstall Dell software and reinstall some Lenovo drivers and software. Didn't expect Acronis to take care of this.
We would rate this service 5 of 5, but documentation on how to do this efficiently as 3 of 5. We have taken enough notes to reliably reproduce by different individuals. All good up to this point. Would have heartily recommended product at this point if it were not for the bad and the ugly described below.
The Bad...
We were unaware that Acronis had not provisioned a custom install that does not include its Active Protection and Cyber protection. Like many others in the forum, we find it very intrusive to force these services on users.
Malware, by definition is something that runs, does stuff that you do not want or expect, consumes CPU/Memory resources, etc. that it shouldn't. Active Protection and Cyber protection are, by our definition, malware because we did not want it or expect it with our purchase. Our bad for not doing better research.
When you try to stop malware, it usually restarts itself, sometimes creating multiple copies in the process. Malware requires painful intervention to get it stopped.
The Ugly...
We did the following to get cleaned up installs on four PCs, which are now well behaved until updates overwrite our changes (the bad and ugly). We can now boot and get no startup log errors and can run Acronis GUI without setting off error logs. For some, this might be an acceptable solution. That is why I am sharing this process. However, we offer consulting service to businesses and cannot use or recommend a product that requires brittle intervention. If we tried to deploy a 100 or 300 licenses at a business, we would likely incur a large financial liability because it would continually break over time.
Here is what we did.
Changed file names:
    - C:\Program Files (x86)\Common Files\Acronis\ActiveProtection\anti_ransomware_service.stopped.exe
    - C:\Program Files (x86)\Acronis\Agent\bin\adp-agent.stopped.exe
Changed Registry:
    Registry Key: AcronisActiveProtectionService
        ErrorControl 1 => 0
        Start 2 => 0
    
    Registry Key: AcronisCyberProtectionService
        ErrorControl 1 => 0
        Start 4 => 0
    
    Registry Key: mmsminisrv
        ErrorControl 1 => 0
        Start 2 => 0
    
    Services Altered: Run services.msc
        Under Recovery, set failures to Take No Action and reset fail count to 1000 days. This may not be necessary.
        Acronis Active Protection (TM) Service
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Agent Core Service
            Changed to Disabled
        Acronis Cyber Protection Service
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Managed Machine Service Mini
            Changed to Disabled, but after reboot, it was changed to Boot
        Acronis Mobile Backup Server
            Changed to Disabled
        Acronis Mobile Backup Status Server
            Changed to Disabled
Your needs may vary and these settings have only been checked for the standard perpetual licenses that we purchased.
I hope Acronis will decouple backup/recovery/cloning completely from Active Protection and Cyber security. Please do not foist services on unsuspecting customers that are strictly coming to you for your most excellent backup/recovery/cloning capabilities.
I might take a serious look at some of your other intra-network solutions, not the cloud, but not while they are bundled into one application. Hint... keep them separate as licensable, purchasable modules. Let me choose what I want and need. No surprises. I will monitor Acronis for a while to see if there is any improvement here. If not, we'll move on to find a different intranet solution or may be forced to write our own.
Happy mole whacking to all...
I have 2018 version and have been ignoring their requests for update. They somehow managed to attack me by  putting this 'protection' MALWARE on my machine! without me updating! So... I did some digging, as you can too. This is not a "real software company" anymore. It is an investor shell company, now for the purpose of making dividends (cash). ALERT the public and every site you can that Acronis is now Malware infected. USE the Windows backup. I am going to Microsoft - hesitation but I will. Now you know why Acronis is a 32-bit program - it WILL NEVER be made a 64-bit. There are no programmers at the company (the investors use outside consultants). I too, changed the filename and it took my WIN10 and twisted it inside and out. No icons on start page. You will NEVER get a moral response - good grief. Investors are all over the world and could care less about a program running in the background which cannot be turned off and hogging your CPU. UNINSTALL ACRONIS. TRY ANOTHER BACKUP (it'll hurt for awhile). DO NOT CONTINUE TO FEED THE INVESTORS.
 



      
                
                
                    
                                                    Fri, 02/12/2021 - 07:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi! I have a subscription license, please, could you send me the download link for a previous product version just with Backup, please, nothing else. Please let me know

      
                
                
                    
                                                    Mon, 03/01/2021 - 10:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, is there any chance I will have the answer, please? Its very important, I have big troubles using and combining Acronis security, I need just Backup and I need to resolve a big problem now with the unwanted security in there. Please! I disabled that services, but not sure all is gone..
 

      
                
                
                    
                                                    Tue, 03/02/2021 - 19:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Miroslav, you may be able to download a previous product version from the Acronis Product Updates page which has links to the latest / final versions of a range of different Acronis products.
If you have an active subscription product then you should open a Support ticket direct with Acronis Support and raise any issues you have with them, including asking to be provided with a version of the product which meets your requirements.

      
                
                
                    
                                                    Tue, 03/02/2021 - 20:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ray Engelking
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is horrible, I was using True Image Home 2010 and upgraded to 2021 and now I see 10 other services running!  I tried disabling them, didn't work. I tried msconfig and removed them from starting, and they still are there on reboot. My entire machine is lagging now. I need a refund for this, this is a mess.

      
                
                
                    
                                                    Tue, 03/02/2021 - 22:34
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Please see KB 21242: Refund policy for Personal products for information that should help you if you want to request a refund for your recent purchase.
Please submit Feedback directly to Acronis (use the tool provided in the GUI Help section) and ask for your vote to be added to the Acronis internal feature request: TI-213392 Allow installation without Antimalware components

      
                
                
                    
                                                    Wed, 03/03/2021 - 10:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Miroslav Bulka wrote:

Hi! I have a subscription license, please, could you send me the download link for a previous product version just with Backup, please, nothing else. Please let me know


Hello Miroslav,
could you please share your serial number in a private message? Under your account I only see a perpetual license of Acronis True Image 2021 which unfortunately cannot be used to activate an older version. Otherwise you'd need to request downgrade from Acronis support team, 

      
                
                
                    
                                                    Mon, 03/15/2021 - 08:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Waedt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yesterday I installed the the latest Acronis 2021 update.
While I still have all protection disabled, there are 12 Acronis tasks continuously running,
several of them with some workload, see 2 screenshot extracts below.
While each of the tasks seems to have a load of less than 0.9% (on an Intel Core i9),
Acronis still has BY FAR the highest processor usage when the computer is idle.
Could the Acronis developers PLEASE change this so the task are not started, when threat protection is disabled?
Or not consume processing power, if starting cannot be disabled?
Also, shouldn't this be 64bit tasks?
 


Thanks a lot!

      
                
                
                    
                                                    Mon, 03/15/2021 - 08:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Virtum wrote:

Ekaterina wrote:

R wrote:

Thank you Ekaterina.
In the meantime is there a safe method to downgrade back to Acronis 2020 so I can stop it from deleting my files?


Hi! If you have a subscription license, I could send you the download link for a previous product version. Please let me know, if the old installation file is needed. 


Please put in a vote for me for this change as well, and message me the link for the old installation.


Hi! Added your vote and sent you the link in a private message 

      
                
                
                    
                                                    Mon, 03/15/2021 - 09:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Should be very fine to use your perfect backup software (and not protection) once I have also another in place and disabling it is not the correct procedure. So, yes, it should be very fine to have Just Only Backup.

      
                
                
                    
                                                    Mon, 03/15/2021 - 10:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Miroslav Bulka wrote:

Should be very fine to use your perfect backup software (and not protection) once I have also another in place and disabling it is not the correct procedure. So, yes, it should be very fine to have Just Only Backup.


Miroslav, thank you for sharing your opinion! Added the comment as a vote for the change request.  

      
                
                
                    
                                                    Mon, 03/15/2021 - 21:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            OK, Goodbye Acronis, welcome Macrium Reflect, works perfect in all ways.
 

      
                
                
                    
                                                    Sun, 04/11/2021 - 13:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SJ
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            >> OK, Goodbye Acronis, welcome Macrium Reflect, works perfect in all ways.
 
At twice the price.
 

      
                
                
                    
                                                    Sun, 04/18/2021 - 12:06
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image Products (currently 2017 Beta)
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Not twice the price, I am talking about and working with the free version !

      
                
                
                    
                                                    Sun, 04/18/2021 - 13:02

## Original Post
**Author:** Unknown

How to disable ALL Acronis antivirus services

        
  



    
  


  
              
          
        Thread needs solution      
      
      







            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Zardoc
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, please include my name and send me a link thanks.

      
                
                
                    
                                                    Fri, 04/23/2021 - 01:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Original Drive Image user (bought by Syman...) Long time ATI supporter: TI10 (10.0.4942 ) TI11 (11.8101) TI 2009 (9796) TI2010 (7160) TI2011 (6597) Acronis Disk Director (10.0.2160) Disk Director (2011) TI2012 (7133) TI2013 (Beta) TI2015 TI2016 TI2017 TI2018 TI2019 TI2020 www.zardoc.com

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tim Stubbs
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            A vote from me too - adding this flexibility of reducing the overhead for people choosing alternative antimalware solutions is a really good idea.  Appreciate that this wasn't seen during the initial development phase but loading components and services when needed is a good ethos to have.  I sympathise (I'm in SW development).
I have both corporate use of this (via my work account) and home.  For work we don't want some of these services running on our build server (for example) and of course our own central IT (we're 35k employees world wide) need to make their own decisions.  Personally I'd also like the choice as my 6 personal systems have diverse use cases but all need the core backup functionality.
 
 

      
                
                
                    
                                                    Sun, 04/25/2021 - 05:54
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image 2021
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Zardoc
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Steve Smith wrote:

Please see KB 21242: Refund policy for Personal products for information that should help you if you want to request a refund for your recent purchase.
Please submit Feedback directly to Acronis (use the tool provided in the GUI Help section) and ask for your vote to be added to the Acronis internal feature request: TI-213392 Allow installation without Antimalware components


Hello Steve, I sent you a private message.
Thanks
 

      
                
                
                    
                                                    Mon, 04/26/2021 - 02:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Original Drive Image user (bought by Syman...) Long time ATI supporter: TI10 (10.0.4942 ) TI11 (11.8101) TI 2009 (9796) TI2010 (7160) TI2011 (6597) Acronis Disk Director (10.0.2160) Disk Director (2011) TI2012 (7133) TI2013 (Beta) TI2015 TI2016 TI2017 TI2018 TI2019 TI2020 www.zardoc.com

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My First Acronis True Image was € 29.- (2010)
After that every year more expensive.
Now its useable every year again for € 79.- and problems with the build in antivirus.
So I use now the freeware Macrium Reflect and it is great!
Every saturday at 12 o'çlock an automatic image on my D-drive and on my desktop a shortcut for a image to the removable drive.
https://www.macrium.com/reflectfree
 

      
                
                
                    
                                                    Mon, 04/26/2021 - 10:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Zardoc wrote:

Hello Steve, I sent you a private message.
Thanks


Zardoc, I replied to your PM a couple of days ago - please check by clicking on your account icon at the top of each forum page.

      
                
                
                    
                                                    Mon, 04/26/2021 - 10:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear,
I bought Acronis with expectation, that I will have professional backup tool, which I can use.
What happened. I have Acronis including Cyber creepy protection with interrupts and unwanted crackling audio etc. with services, which makes Protexion. I Put proteXion, because, in fact, the protection is good to use and I dont want to speak about protection.
I expected Backup solution.
Finally, after 2 months of my message related to change to the non-protection cyberity version, which I did not receive Acronis in the version without cyberity..
Its sad.
At All, the live is going on and I am looking forward to find the product at my wish for my money, not just saying words like you need to put the request, ask the dev team, your serial is not the serial for the version excluding cyberofson etc...
Yes, the live is going on and I make the decission to exit this forum, this site, this product and going to use another backup solution without the unwanted something...
And...To tell you, I dont want to use something crackling my audio ... Why "Turn Off" does not mean to Turn Off and Do Not Start the services related to protexion ?
Why you dont support the customers and do something as you prefer instead ?
Ok, no matter.
You choose your solution, I will use my protection instead of mix it and use the cpu for nothing.
Just take my money and do as you want.
I will do another way instead of spend the time with this.
Sorry.

Have a Good Luck
All The Best on your way
Miro

      
                
                
                    
                                                    Mon, 04/26/2021 - 20:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Zardoc
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Steve Smith wrote:

Zardoc wrote:

Hello Steve, I sent you a private message.
Thanks


Zardoc, I replied to your PM a couple of days ago - please check by clicking on your account icon at the top of each forum page.


Hi Steve, All I see in my messages is the one I sent to you. I have nothing in my in box. You can mail me on my admin mail admin@zardoc.com. I never read unless I'm waiting for something :)

      
                
                
                    
                                                    Tue, 04/27/2021 - 00:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Original Drive Image user (bought by Syman...) Long time ATI supporter: TI10 (10.0.4942 ) TI11 (11.8101) TI 2009 (9796) TI2010 (7160) TI2011 (6597) Acronis Disk Director (10.0.2160) Disk Director (2011) TI2012 (7133) TI2013 (Beta) TI2015 TI2016 TI2017 TI2018 TI2019 TI2020 www.zardoc.com

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    czbird
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Count me in... I'm just about to uninstall the whole thing and look around for an alternative. I think that all important has already been said. I bought this as a backup solution, not some antimalware "cyber" whatever crap. Currently posessing licence of True Image 2020, and there's no option to disable these "features". If disabled in the GUI, the services are still running and can't be stopped unless tweaking around which I refuse to do after every update.
So, either please provide me with a pure backup-focused version, or say bye bye to another customer.
Thanks for understanding.

      
                
                
                    
                                                    Thu, 04/29/2021 - 21:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marty McFly
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sweet merciful crap! I just upgraded my licenses to 2021 and I'm considering asking for a refund and dropping Acronis entirely and finding another product to back up my customers' computers. I would like Acronis to answer the following questions honestly and with words that aren't on a form somewhere:
Why does your backup software contain "protection" and "malware" services in it? I do not ask your product to do this, I do not want your product to do this, I have other solutions for this. Please explain WHY this terrible decision was made.
Second question:
Will Acronis be removing all this bullcorn from the 2022 version of the product? I won't be purchasing another license if this nonsense continues because I know, KNOW, feature creep will continue making these features not only worse but debilitating.
Perhaps management over there can task the engineers manintaining this code with doing something productive like building an enterprise backup solution that competes with Veeam? I'd LOVE to see that! I've been boxed in with enterprise backup with Veeam, which is a fantastic product, but competition breeds innovation and I'd really like them to earn my business instead of just take it because they're the only backup product in that space that matters.
So to recap, fix your junk, make products people want. If you need any more help running your business I could also take a look at your personnel and tell you who to terminate. But seriously, fix your junk. Now,

      
                
                
                    
                                                    Fri, 04/30/2021 - 20:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Dumesnil
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Same situation 300 Backup advanced licenses upgraded to 15 “Cyber”  
Unable to prevent the protection services or decouple it from our “Backup” solution.  
I will recommend search for another solution to management before next renewal. 
In 12.5 these were disabled services. Now the run all the time using resources and interfering with normal tasks on expensive production servers...the definition of Malware!
Tedious web interface with Name column using 8% of width truncating Descriptive plan names requiring clicking on Detail to see full name, click click click click my carpel tunnel is hurting again.

      
                
                
                    
                                                    Wed, 05/05/2021 - 01:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lewis Lisle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Same issue. Acronis 2021 is killing my machine. A total resource hog. Any final suggestions to tame this?  I loved the older Acronis but this is a joke. If not good reply from Acronis then I'm off for a replacement.

      
                
                
                    
                                                    Sun, 05/09/2021 - 23:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Lewis Lisle wrote:

Same issue. Acronis 2021 is killing my machine. A total resource hog. Any final suggestions to tame this?  I loved the older Acronis but this is a joke. If not good reply from Acronis then I'm off for a replacement.
So I use now the freeware Macrium Reflect and it is great!



      
                
                
                    
                                                    Mon, 05/10/2021 - 08:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AlexV
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello.
Another vote for TI-213392. Please allow the installation of the backup component without any of the cyberprotection modules.
The main idea is sound but should be opt-in, not forced.
I ensured that the protection was turned off to not collide with my current AV solution but after the last automatic upgrade I noticed the notification of a sucessfull scan. Upon checking it it was "half-running" while appearing to be turned off. The solution was to fully enable it in the Protection tab, reboot the computer and then disabling it again.
Thank you.

      
                
                
                    
                                                    Mon, 05/10/2021 - 22:06
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office Premium
Acronis Cyber Protect Standard
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Ekatarina - I kindly ask you to add my vote to the CR, too.
We're also not really happy with not being able to sustainably disable AV-related ressources in Cyber Protect (same goes for True Image, which I use at home). It's just adding more complexity and more load where it's not needed - or rather not desired.
 
Thanks!

      
                
                
                    
                                                    Tue, 05/11/2021 - 09:28
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brent Rutherford
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Changing the services you don't want running to "Log on as" an account with an invalid password, and then changing "Recovery" to "Take no action" seems to do the trick.
Edit: Well, it did until I started the app, now logs getting filled with failure messages... services still disabled though.
Brent

      
                
                
                    
                                                    Tue, 05/18/2021 - 22:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrey Ilkanych
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Same issue here. Cannot disable the protection, and their "protection" thinks that my work software is a problem, so it blocks it. By the way, I work for a cybersecurity firm. Believe me when I say my work software isn't a virus.
I bought this so that I could back up my work drive as I have a lot of sensitive data, instead, they included some half-baked protection software into it, that doesn't work, or turn off when you disable it in the settings.
To top it all off, I just asked for a refund, and guess what I got as an email response? I was told to TURN THE SERVICES OFF (which as has been mentioned here MANY times, you cannot do.) I love how people who work at this very company are giving me a response that is false.

      
                
                
                    
                                                    Thu, 05/20/2021 - 05:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andrey, I haven't tried the following with the Acronis business Cyber Backup product version of protection, but have been able to stop all the Protection services for the True Image 2021 equivalent.
The steps needed are:
Set all the Acronis Services to Disabled Start instead of being set to Automatic.
Restart the system and ensure that you do not launch the Acronis application (as will override the Disabled status!).
Rename the associated service executable files which tend to be spread around various different folders in ATI 2021 at least.
Restart again and all the protections services should remain 'Stopped' in the Services panel.
Note 1: all the above will be reversed / undone by any new build of Acronis being installed.
Note 2: the AAKORE service should be included in the above as will also try to download protection related data.

      
                
                
                    
                                                    Thu, 05/20/2021 - 10:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:

Miroslav Bulka wrote:

Hi! I have a subscription license, please, could you send me the download link for a previous product version just with Backup, please, nothing else. Please let me know


Hello Miroslav,
could you please share your serial number in a private message? Under your account I only see a perpetual license of Acronis True Image 2021 which unfortunately cannot be used to activate an older version. Otherwise you'd need to request downgrade from Acronis support team, 
 
I have shared serial, to be true and serious, this is a joke.
 
 



      
                
                
                    
                                                    Thu, 05/20/2021 - 20:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Steve, really to be serious, you are joking, right ? Or try to read this your post again :
 
 
Steve Smith wrote:

Andrey, I haven't tried the following with the Acronis business Cyber Backup product version of protection, but have been able to stop all the Protection services for the True Image 2021 equivalent.
The steps needed are:
Set all the Acronis Services to Disabled Start instead of being set to Automatic.
Restart the system and ensure that you do not launch the Acronis application (as will override the Disabled status!).
Rename the associated service executable files which tend to be spread around various different folders in ATI 2021 at least.
Restart again and all the protections services should remain 'Stopped' in the Services panel.
Note 1: all the above will be reversed / undone by any new build of Acronis being installed.
Note 2: the AAKORE service should be included in the above as will also try to download protection related data.



      
                
                
                    
                                                    Thu, 05/20/2021 - 20:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Miroslav, unfortunately it is no joke with the way Acronis has imposed Cyber Protection in such a way that it cannot be stopped fully if users choose not to use it or want it to be active!
It seems that Acronis know what users want far better than users know themselves!
The steps I outlined do work for Acronis True Image and I have used them to prove that all the new protection services can be stopped, but that offers no guarantee that Acronis will not counter such steps in a future build or version.  Note: my earlier post was intended to refer to only the new protection services rather than all Acronis services as it read (in line with the title of this forum topic)!
I have no issue with Acronis wanting to move into the Cyber Protection arena but they should offer users the choice of whether such features are installed else stop all such services / processes from running in the background if the user elects to turn them off!

      
                
                
                    
                                                    Thu, 05/20/2021 - 20:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Miroslav Bulka
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Steve, yes. Thank you. Unfortunately, there is no question, if you have issue or not. 
Thank you for your answer, its something I did not experienced before. Any answer just like "share your serial" etc. is joking once I did not receive any answer.
To your post. If you read your post and you will think about, what are people=customers saying here, its very sad to read your lines. You just put forward something with no listening and understanding.
Its not only Miroslav, its not only about money. Please, think about that.
Its bad joke you make those comments to 'somebody', who also supported you.
 
At All, I dont understand (and really not only me) this and there is no sense to answer a) protection b) downloading data through.. please, once again, think about, what you are saying and what was the question, request.
If you are saying, that you are for the new protection in your earlier post - what kind of protection, my god ?
If you are thinking about the backup, what do you need for services constantly running and - as you can read in the multiple posts before, its something, what a lot of people does not want to have. So, what protection ?
Basically, if your opinion is to protect, spend the time to protect and protect it all. Note: make some good name like "Cyber", put at least 5 or 6 services related to it, make it consumes unnecessary resources... but, let me know, what kind of protection you are saying about here on the forum. Its joke.. think about that basically, you are telling us about the protection ?
Please, who request you to protect someting and do you really protect it or you are speaking about the protection ?

Turn off the protection ?
How you are thinking the protection to turn off ? (is there any sense ?)
What is the really need to consume resources for this mentioned protection ?
Maybe, you can turn off protection (if not services.., maybe you can spend some time to disable it, maybe you can spend the time to try to understand the protection, maybe.. but, Do you want to ?
Or, back, what was the original idea and usage of this tool ?
I remember few words describing such moments,..: "Like to change tires on the flying boeing"
Thank you
Have a nice day
Miroslav
 
Steve Smith wrote:

Miroslav, unfortunately it is no joke with the way Acronis has imposed Cyber Protection in such a way that it cannot be stopped fully if users choose not to use it or want it to be active!
It seems that Acronis know what users want far better than users know themselves!
The steps I outlined do work for Acronis True Image and I have used them to prove that all the new protection services can be stopped, but that offers no guarantee that Acronis will not counter such steps in a future build or version.  Note: my earlier post was intended to refer to only the new protection services rather than all Acronis services as it read (in line with the title of this forum topic)!
I have no issue with Acronis wanting to move into the Cyber Protection arena but they should offer users the choice of whether such features are installed else stop all such services / processes from running in the background if the user elects to turn them off!



      
                
                
                    
                                                    Thu, 05/20/2021 - 21:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I really wish Acronis had seperated the whole cyber protect system from the original backup system. It's such a headache for an MSP.

      
                
                
                    
                                                    Wed, 06/23/2021 - 16:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Keith Jenkinson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My PC periodically hangs, crashes and runs very slowly when I open Acronis. The Acronis Backup UI is incredibly slow:- Click a backup, go & make a cup of tea, drink it & if I'm lucky the backup details will be displayed. Click the start start button and it takes many seconds, sometimes minutes to appear. 
If I uninstall Acronis, my PC doesn't hang or crash & everything runs quickly.This never used to be the case.
Please, please, please remove all antivirus protection processes from the software that I purchased purely for backup! 
If this doesn't happen before my next renewal, I will switch to a backup provider that does just backups. 

      
                
                
                    
                                                    Wed, 07/07/2021 - 18:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jan legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Since the trouble with Acronis I use now the free program Macrium reflect and it works perfect.
Goodbye Acronis !

      
                
                
                    
                                                    Wed, 07/07/2021 - 18:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael Stoeckli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So, I bought True Image 2021 for my main PC under the assumption to get a reliable backup solution.
There is also cyber protection? OK, why not. Can obviously be disabled, right?
Days later the problems started.
I am a software developer and the "Cyber Protection" blocks my own developed applications (no, I don't program viruses). A simple file stream writing operation seems to trigger the protection. Writing files seems to be very dangerous, OK.
Tried to disable the protection and blocking was going on. Then stumbled upon this thread.
Really? I payed for backup and not disturbing my work!
So, I will happily spend another 200-400 $ to get a new Synology (or something similar) instead of running this piece of disappointing sabotage software any longer... If this is not fixed within reasonable time.

      
                
                
                    
                                                    Fri, 07/09/2021 - 21:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Guys, we've been heard (at least for the Cyber Protect Cloud version of Acronis).
According to the release notes of C21.05, the anti-malware components are only now only installed if antimalware is activated in the corresponding protection plan.
- If they are not installed and the protection plan is changed to have malware protection, the components are installed automatically
- Dito for the other way around, once malware protection is deactivated in the protection plan, the antimalware components are uninstalled automatically.
 
Haven't tested this yet myself - but still nice of Acronis not to hold on to the previous solution. 

      
                
                
                    
                                                    Tue, 07/13/2021 - 14:51
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Waedt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            > ... Haven't tested this yet myself
Please give us a feedback, in case this is really effective now.
There was a similar note some time ago.
But despite being able do click some disable related setting, the Acronis processes were still running and consuming considerable processor time.
Thanks!

      
                
                
                    
                                                    Tue, 07/13/2021 - 18:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I use the cyber protect module, I don't think it's 100% yet with deselecting the antimalware module. 
It is much better. 

      
                
                
                    
                                                    Tue, 07/13/2021 - 20:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Waedt wrote:

> ... Haven't tested this yet myself
Please give us a feedback, in case this is really effective now.
There was a similar note some time ago.
But despite being able do click some disable related setting, the Acronis processes were still running and consuming considerable processor time.
Thanks!


What I can confirm so far:
- Backing up one customer Agentless: No antimalware services around
- Backing up one customer Agent-based: antimalware services present - agent settings screen shows "Antimalware module" active. After updating the agent, the module is no longer displayed as active. Right now, the actual services are still running on the machine (has only been 10 minutes though). Going to check again in the evening, potentially restarting the server during the night.
 
Cheers
 
Edit: All of the above mentioned clients don't have and never had any antimalware-modules active in their protection plans - always only the backup module

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      582947-286876.png

                      22.32 KB
                  
              
                      582947-286878.png

                      41.89 KB
                  
              
                      582947-286879.png

                      49.43 KB
                  
          
    

                    
    
                
                
                    
                                                    Wed, 07/14/2021 - 06:36
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mischa Künzle wrote:

Karl Waedt wrote:

> ... Haven't tested this yet myself
Please give us a feedback, in case this is really effective now.
There was a similar note some time ago.
But despite being able do click some disable related setting, the Acronis processes were still running and consuming considerable processor time.
Thanks!


What I can confirm so far:
- Backing up one customer Agentless: No antimalware services around
- Backing up one customer Agent-based: antimalware services present - agent settings screen shows "Antimalware module" active. After updating the agent, the module is no longer displayed as active. Right now, the actual services are still running on the machine (has only been 10 minutes though). Going to check again in the evening, potentially restarting the server during the night.
 
Cheers
 
Edit: All of the above mentioned clients don't have and never had any antimalware-modules active in their protection plans - always only the backup module


Acronis Active Protection Service still installed/active, even after a reboot. Too bad.

      
                
                
                    
                                                    Thu, 07/15/2021 - 11:45
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Warren Hayden
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            FAKE NEWS!!!
Was optimistic based on the forum post until I installed the latest build, as of July 14th 2021, on a couple laptops.
BAD NEWS!!!
All protection modules still active and consuming CPU, disk, and memory resources. Bait and switch!!??
LOST ANITHER CUSTOMER TODAY!!!
Switching to the competitor's product mentioned in this forum post. 

      
                
                
                    
                                                    Thu, 07/15/2021 - 16:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Warren Hayden wrote:

FAKE NEWS!!!
Was optimistic based on the forum post until I installed the latest build, as of July 14th 2021, on a couple laptops.
BAD NEWS!!!
All protection modules still active and consuming CPU, disk, and memory resources. Bait and switch!!??
LOST ANITHER CUSTOMER TODAY!!!
Switching to the competitor's product mentioned in this forum post. 

Since the trouble with Acronis I use now the free program Macrium reflect and it works perfect.
Goodbye Acronis !




      
                
                
                    
                                                    Thu, 07/15/2021 - 16:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mark M
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Waedt wrote:

Yesterday I installed the the latest Acronis 2021 update.
While I still have all protection disabled, there are 12 Acronis tasks continuously running,
several of them with some workload, see 2 screenshot extracts below.
While each of the tasks seems to have a load of less than 0.9% (on an Intel Core i9),
Acronis still has BY FAR the highest processor usage when the computer is idle.
Could the Acronis developers PLEASE change this so the task are not started, when threat protection is disabled?
Or not consume processing power, if starting cannot be disabled?
Also, shouldn't this be 64bit tasks?
 
Thanks a lot!


I agree with Karl.
I have been using Acronis True Image since True Image 11 (perpetual) and recently upgraded to True Image 2021 for Windows 10 support (upgraded the v11 perpetual license to a v2021 3-PC perpetual license).
Don't get me wrong here, I think Acronis is a great and very useful product with some very nice features. However, I have always found it to be rather service heavy. Too many non-essential things running by default. Why does there have to be an Acronis notifications service in the system tray, when Windows 10 notifications tells me the same info. Seems redundant.
And why does everything have to run as a service? Why so many services? In the old version you could disable a lot of the services without impact to the core functionality (ex: Try and Decide, Scheduler, etc.). I never intended to use ATI as an anti-malware product, I just want to make images, clone partitions, and do backups with ease on the fly, manually. That is what the core of the product is really good at.
But I look at it like this, I bought the hardware, I manage the system, so I want to be able to decide what runs on my system or not. When every vendor uses a bunch of services out of the box and wants their product to be the end-all-be-all-does-everything solution for everyone, then our system starts to get so much bloat that it can feel like running Win98 with 32MB of RAM on a Pentium 133. I mean come on, please let the user choose.

      
                
                
                    
                                                    Tue, 08/17/2021 - 21:53
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image Home 11

Acronis True Image 2021
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Martin Beattie
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Please add me to the list.
I have removed ATI2021 from my machines and reverted back to ATI2016 which I believe was the last true/Sole backup version.

      
                
                
                    
                                                    Fri, 08/27/2021 - 06:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Alexander Schwarz
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I think we won't be able to deactivate those services in the future, too as I just got a mail, that Acronis is going to rename the product to "Cyber Protect Home Office" pointing out that it does more than simple backups.
I respect that they need a selling point and when you want to charge more you need more features, because simply saying "our costs went up, too" won't cut it. But still: let users decide at the end of the day which parts of your software they need. 
 

      
                
                
                    
                                                    Tue, 08/31/2021 - 12:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Hetzel
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I totally removed Cyber Protect and re-installed version 2018 of Acronis backup, dé-activating the cyber protection.
I  have purchased the 2019, 2020 and 2021 upgrades but won't install those again as long as Acronis is forcing the cyber security services.
This is definitely too invasive !
 

      
                
                
                    
                                                    Thu, 10/14/2021 - 11:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Waedt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Right. This is sooo implolite and annoying for long-term customers!
They have now "Acronis Cyber Protect". Great!
But that's not a valid reason to enforce it on "Acronis True Image" users!
We have shipped "Acronis True Image 2020", "Acronis True Image 2019", ... to dozens of customers for use on maintenance devices that are occasionally connected to embedded automation systems.
I don't understand why they want to ldisappoint and lose customers who used to appreciate their backup solution.

      
                
                
                    
                                                    Thu, 10/14/2021 - 11:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Petros Petrides
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Is there a workout for this? It's getting annoying!

      
                
                
                    
                                                    Sat, 10/23/2021 - 15:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Petros Petrides
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Is there a workout for this? It's getting annoying

      
                
                
                    
                                                    Sat, 10/23/2021 - 15:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ziopino
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Guys, the biggest problem consists in having a third party antivirus activated automatically during start-up, that will conflict with the acronis in-memory antivirus module loaded at startup: I have had many BSOD after few minutes after start-up because of this, and honestly nobody understands why this Acronis antivirus module is automatically loaded if the complete set of options are fuuly deactivated and the other antivirus software is white listed...

      
                
                
                    
                                                    Wed, 12/01/2021 - 17:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    J. Legierse
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            ziopino wrote:

Hi Guys, the biggest problem consists in having a third party antivirus activated automatically during start-up, that will conflict with the acronis in-memory antivirus module loaded at startup: I have had many BSOD after few minutes after start-up because of this, and honestly nobody understands why this Acronis antivirus module is automatically loaded if the complete set of options are fuuly deactivated and the other antivirus software is white listed...
End of your problems: Macrium Reflect
 



      
                
                
                    
                                                    Thu, 12/02/2021 - 10:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kacey Green
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Been an Acronis user since 7 or 8, 2020 had a bunch of annoying stuff I could turn off, but 21 even with the antivirus (I didn't request or activate in my backup and imaging software) turned off the thing is still hogging resources and making other programs display notifications that Acronis is doing stuff.
I don't use it for scheduled backups or anything, just imaging, and universal restore, guess I'll have to just re-install it or use the bootable when I need something, we'll see what a future update brings.

      
                
                
                    
                                                    Sat, 12/04/2021 - 23:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Papolytic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            After reading through all of this thread, I'll add that I've had system reboots (bugchecks fatal) in Win 10 after installing whatever True Image became, (Cyber protect). I already was using a service that was fine. If I can't install whatever 2021 True Image is without all the virus stuff, I'll just uninstall permanently the new unwanted cyber version.
I used to like True Image backup and used it a few times, but it's not worth a system crash every day.
Edit: So to add to this: I uninstalled Cyber Protect last night as I wrote this reply and my system log is clean with no crashes for 10+ hours. I do have True Image 2020 but aren't sure it's clean of anti-virus code. Does anyone know? Many thanks.
 
M

      
                
                
                    
                                                    Fri, 12/31/2021 - 22:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Papolytic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:

Virtum wrote:

Ekaterina wrote:

R wrote:

Thank you Ekaterina.
In the meantime is there a safe method to downgrade back to Acronis 2020 so I can stop it from deleting my files?


Hi! If you have a subscription license, I could send you the download link for a previous product version. Please let me know, if the old installation file is needed. 


Please put in a vote for me for this change as well, and message me the link for the old installation.


Hi! Added your vote and sent you the link in a private message 
 
Hi Ekaterina,
 
How would (or can I) convert the Acronis Cyber Protect Home Office (which costs more) to the Acronis True Image 2021 Standard edition (I mean trade it in or at least get something without protection I can use ONLY for backups.
 
Many thanks, Mick



      
                
                
                    
                                                    Thu, 01/13/2022 - 13:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Keith Lawson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have the same problem with 2021, I use Bitdefender as my anti-Virus.  Sometimes when I boot the Acronis active protection service just takes over and hogs my processing power.  There is no way to turn this off!!!  I just want a backup product or at least one that does not impose unwanted protection.  I can't work like this!!!!
Version 2021, Build 39216


      
                
                
                    
                                                    Sun, 01/23/2022 - 12:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Lyubomir Pashov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I was using Acronis True Image 10 years ago and it was an excellent and intuitive tool.
Now I am using the 2021 and I am disappointed - it's usage is not intuitive, but in any way I got used to it somehow.
The most annoying things however are the unstoppable services:
Acronis Active Protection (TM) Service
Acronis Agent Core Service
Acronis Cyber Protection Service
Acronis Managed Machine Service Mini
Acronis Mobile Backup Server
Acronis Mobile Backup Status Server
.....
.....
I have permanently stopped Acronis' protection and still the above services are turned on. 
I use Acronis True Image ONLY to make local master backups from time to time and restore very seldom. I want Acronis turned off in all the other time. I do not want to use the resources of my laptop when I do not need its services.
Can you tell me how can I turn these services off?
I do not want to uninstall Acronis True Image each time I make a backup or install it again when I need to restore a backup.
 

      
                
                
                    
                                                    Sun, 03/13/2022 - 20:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AlexV
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Lyubomir.
It seems there is no reliable and permanent way of doing this. I read somewhere that the backup component is extremely interconnected with the protection module that this is impossible to decouple them.
Well, unless you are willing to pay again and switch to enterprise version of the same software from Acronis. If you swith to Acronis Cyber Protect Standard for example, you will be able to install the agent without the cyber protect antivirus thing. You'll still get lots of services but a bit less than you have right now (see screenshot below).
Two very important caveats with this expensive "workaround": You'll get only 50Gb online storage per workload (unless you pay even more for storage space), loosing access to any online storage you migh have with the home office version, and you also loose the ability to clone a hard drive to another one. You'll still get all the backup modes (files, image, etc) but you will not be able to clone one disk to another.
I've been using this for a while now just to use the license I have until the end of the year, and it is lighter on the resources. A bit harder to manage using a web console.
Once it ends, I will move on to some other solution on the market. This concept is surreal.
In the meantime I'm still diggesting the fact that I have paid beforehand for the home office 1Tb version online storage until 6/10/2026 and I will be loosing that investment. But currently the home office version is simply a complete nonsense.
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      600771-320725.png

                      26.69 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 03/17/2022 - 22:30
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office Premium
Acronis Cyber Protect Standard
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mark M
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Lyubomir Pashov wrote:

I was using Acronis True Image 10 years ago and it was an excellent and intuitive tool.
Now I am using the 2021 and I am disappointed - it's usage is not intuitive, but in any way I got used to it somehow.
The most annoying things however are the unstoppable services:
Acronis Active Protection (TM) Service
Acronis Agent Core Service
Acronis Cyber Protection Service
Acronis Managed Machine Service Mini
Acronis Mobile Backup Server
Acronis Mobile Backup Status Server
.....
.....
I have permanently stopped Acronis' protection and still the above services are turned on. 
I use Acronis True Image ONLY to make local master backups from time to time and restore very seldom. I want Acronis turned off in all the other time. I do not want to use the resources of my laptop when I do not need its services.
Can you tell me how can I turn these services off?
I do not want to uninstall Acronis True Image each time I make a backup or install it again when I need to restore a backup.
 


If you are using this to backup a personal machine (not a server or corporate enterprise) have you considered making a USB stick with WinPE/Acronis boot media? I went this route. It's not a great option if you like or need the scheduled and automated backups, but I do the backups manually and don't even need to have Acronis installed and hogging up my PC. And you don't have to worry about VSS or anything going wrong or leaving files in an inconsistent state because the OS you're backing up isn't even running when you clone/backup using boot media. Kinda old school, but works around the Acronis bloatware garbage.
I don't know about the "Cloud" version, I was able to upgrade to the stand alone perpetual license. I HATE depending on SaaS/Cloud for reasons like this, where the software developer can change things (and throw you a curve ball out of the blue) and force some unwanted feature update on you and also you are renting the software FOREVER. Not good if you're on a small budget or your internet goes down.
SaaS/subscription model is good for their business ($$$), but bad for a consumer who just wants to buy something once, set it up to do something very specific, and have it work the way the consumer wants. I'd rather build and manage my OWN local "Cloud" with my own infrastructure, that I manage and trust and can disconnect or air gap from the Internet. All these data breaches and stuff. IMHO SaaS/Cloud while convenient, has ruined IT. Technology keeps going this route and pretty soon you won't even be allowed to own your own eyeballs/thoughts (or you'll have to rent them FOREVER). I am so tired of "One Size (tries to) Fit All" mentality in software development. Microsoft, Apple, Google, Acronis, Intuit, Adobe, etc. etc., to hell with them all!
 

      
                
                
                    
                                                    Tue, 03/22/2022 - 17:25
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image Home 11

Acronis True Image 2021
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Walter Hawn
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Going on TWO YEARS since the OP pointed out how arrogant and snotty Acronis has become, and yet Acronis is still telling us we are stupid sh*ts because we want to actually control our computers properly.  Well now.  I want nothing but system backup from Acronis.  NOT A D*MNED THING ELSE.  System backup.  Not data backup, not AV, not a burnt wienie sandwich. SYSTEM BACKUP ONLY! Earlier on this thread, we had Acronis employees telling us things would be in process to rectify management's errors.  Have seen no rectification.

      
                
                
                    
                                                    Sat, 04/02/2022 - 05:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is a related issue.  I run Acronis Cyper Protect Home.  I have "Active protection turned off".
However I just saw that Acronis Antivirus took 4 hours to scan my PC!  I do not see a separate setting to turn this off.  Can someone point to that setting? My current antivirus also does this and this is duplicative.
Thanks,
BJBBJB
 

      
                
                
                    
                                                    Sun, 04/10/2022 - 14:45
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license

## Original Post
**Author:** Unknown

How to disable ALL Acronis antivirus services

        
  



    
  


  
              
          
        Thread needs solution      
      
      







            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    system_account
                            

                            
                    
                        Forum Star
                    
                
            
                        
                
                    Posts: 198
                
            
            
                
                    Comments: 840
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            J. Legierse wrote:

Not twice the price, I am tacccccccclking about and working with the free version !



      
                
                
                    
                                                    Fri, 05/13/2022 - 12:16
                                                                            
                                
                            
                                            
                                            
    
                    
                spam

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Huth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Like a lot of other commenters here, I bought a new version of True Image ONLY FOR BACKUPS, especially of Microsoft Storage Spaces, which my previous version didn't handle. I use it for nothing else, and I don't want to use it for anything else. I don't want any services whatever, associated with True Image, running when I'm not actively using the software; but, although I only use the program for backups and nothing else, there are currently ten Acronis services clogging up my computer!
So I plan to start installing the program twice a week, making my backups, then uninstalling it when I'm finished. I have an emergency recovery drive, of course.
Does anyone foresee a problem related to this strategy?
Thanks

      
                
                
                    
                                                    Thu, 06/23/2022 - 22:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AlexV
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel.
Currently the public beta is running for the new version of Acronis Cyber Protect Home Office that finally splits the components and allows you to install the backup module only, without any of the other services.
You can participate here: https://www.acronis.com/en-us/products/home-office/beta/download/
Regards,
Alexandre

      
                
                
                    
                                                    Mon, 06/27/2022 - 10:52
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office Premium
Acronis Cyber Protect Standard
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @DanielHuth,
 
I had similar sentiments as you when I started using acronis Cyber Protect Home.
I ended up just turning off the anti-virus and living with the services running.  As long as your PC is reasonably equipped you shouldn't notice it.
That being said the antivirus services should not be running just for backup. Great to hear they are being split up. Assume that will require an uninstall/reinstall?
Thanks,
BJBBJB 

      
                
                
                    
                                                    Mon, 06/27/2022 - 12:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license 
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Papolytic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            AlexV wrote:

Hi Daniel.
Currently the public beta is running for the new version of Acronis Cyber Protect Home Office that finally splits the components and allows you to install the backup module only, without any of the other services.
You can participate here: https://www.acronis.com/en-us/products/home-office/beta/download/
Regards,
Alexandre
 
Alex, 
 
Is this beta still active and can we still completely disable Cyber Protect 100%? What is the name of the replacement for True Image that has zero Cyber protect built into it now?
 
Mickey
 
PS: What ever happened to my 
Acronis True Image 2017
PERPETUAL LICENSE
 
? 
 
Does perpetual mean something else over at Acronis? I was just charged for a yearly subscription to a 2021 True Image copy which isn't really too perpetual? Can I have my perpetual license back? Doesn't anyone think you should stop trying to foist new products that we didn't pay for or want on the users of True Image? It's hard to imagine that someone didn't notice what a bad idea this is. 



      
                
                
                    
                                                    Tue, 09/06/2022 - 14:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Greetings. I know this thread is old but on point for my question.  I am aware you can now do a custom install to not install the antivirus.  I did this for my Cyber Protect Home update I just did.
Now I am looking at the settings for antivirus/antimalware......I have also looked at the FAQ on these settings...
I still cannot figure out how I leave ON the malware protection and turn OFF the real-time antivirus setting.   
And when it says "a scan is scheduled" is that for malware? Antivirus?  Both?
Thanks for the help, appreciate it.
BJB
 

      
                
                
                    
                                                    Fri, 10/21/2022 - 20:47
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license 
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have now installed the latest ACPHO as an update and deselected Antivirus during the install but kept the malware option.  However, within my "Protection" settings in ACPHO it shows Active Protection with Malicious Files and Malicious websites non-grayed out, and the rest are all grayed out (Ransomware, Cryptomining, Zoom injection.
Further, Antivirus scan STILL shows a "next full scan" scheduled.
There is a "pause protection" button on the left.
It also says my PC is not fully protected and a link to "turn on full protection".
Can someone tell me if this is what I should be seeing if I just want the malware or root protection on and real time antivirus off?  I have a separate antivirus program.
I am glad they provided an option to not install Antivirus but this screen is confusing.
Thanks,
BJBBJB
 

      
                
                
                    
                                                    Sun, 10/23/2022 - 14:24
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license 
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            BJB wrote:

Greetings. I know this thread is old but on point for my question.  I am aware you can now do a custom install to not install the antivirus.  I did this for my Cyber Protect Home update I just did.
Now I am looking at the settings for antivirus/antimalware......I have also looked at the FAQ on these settings...
I still cannot figure out how I leave ON the malware protection and turn OFF the real-time antivirus setting.   
And when it says "a scan is scheduled" is that for malware? Antivirus?  Both?
Thanks for the help, appreciate it.
BJB
 


Dear customer,
Thank you for reaching out. In order to help you we would kindly ask to attach screenshots, to make sure what are talking about. Thank you in advance. 

      
                
                
                    
                                                    Wed, 10/26/2022 - 13:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marty McFly
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            BJB wrote:

I have now installed the latest ACPHO as an update and deselected Antivirus during the install but kept the malware option.  However, within my "Protection" settings in ACPHO it shows Active Protection with Malicious Files and Malicious websites non-grayed out, and the rest are all grayed out (Ransomware, Cryptomining, Zoom injection.
Further, Antivirus scan STILL shows a "next full scan" scheduled.
There is a "pause protection" button on the left.
It also says my PC is not fully protected and a link to "turn on full protection".
Can someone tell me if this is what I should be seeing if I just want the malware or root protection on and real time antivirus off?  I have a separate antivirus program.
I am glad they provided an option to not install Antivirus but this screen is confusing.
Thanks,
BJBBJB
 


LOL! You're using Acronis for some sort of security, a thing they don't do well and shouldn't be doing at all. That's rich.
Thank you for reaching out. In order to help you we would kindly ask to attach screenshots, to make sure what are talking about. Once I receive the screenshots, I'll promptly either ignore you completely, answer questions you never asked, or provide you with a form response that's been copy/pasted from our internal support documentation which will be of ZERO help to you. We hate our customers and appreciate your business. There's no such thing as support from humans anymore. What are you even doing here? Thank you in advance. 

      
                
                
                    
                                                    Wed, 10/26/2022 - 22:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks but I found the setting I needed under settings in the protection area.  The only thing I don't get is that I did a custom install of my update and deselect the anti-virus module.  Yet a few weeks later when I found the settings it was on. I turned off but assumed it would be unavailable/disabled if I didn't install.
Thanks for the followup.
BJB
 

      
                
                
                    
                                                    Thu, 10/27/2022 - 02:22
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license 
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Marty McFly wrote:

BJB wrote:

I have now installed the latest ACPHO as an update and deselected Antivirus during the install but kept the malware option.  However, within my "Protection" settings in ACPHO it shows Active Protection with Malicious Files and Malicious websites non-grayed out, and the rest are all grayed out (Ransomware, Cryptomining, Zoom injection.
Further, Antivirus scan STILL shows a "next full scan" scheduled.
There is a "pause protection" button on the left.
It also says my PC is not fully protected and a link to "turn on full protection".
Can someone tell me if this is what I should be seeing if I just want the malware or root protection on and real time antivirus off?  I have a separate antivirus program.
I am glad they provided an option to not install Antivirus but this screen is confusing.
Thanks,
BJBBJB
 


LOL! You're using Acronis for some sort of security, a thing they don't do well and shouldn't be doing at all. That's rich.
Thank you for reaching out. In order to help you we would kindly ask to attach screenshots, to make sure what are talking about. Once I receive the screenshots, I'll promptly either ignore you completely, answer questions you never asked, or provide you with a form response that's been copy/pasted from our internal support documentation which will be of ZERO help to you. We hate our customers and appreciate your business. There's no such thing as support from humans anymore. What are you even doing here? Thank you in advance. 


Dear Marty,
We bring our apologies if you had a negative experience with Acronis support. We would kindly ask you to send a number of a case in order to analyze it and to improve our services. 
Also, we would kindly ask to post only constructive feedback and respect all Forum participants of Acronis Community, because we aim to have healthy constructive atmosphere. Please refer to https://forum.acronis.com/ToU Acronis actively monitors all posts, and any violations of this rule will result in immediate and permanent bans from posting on our forums.  

      
                
                
                    
                                                    Thu, 10/27/2022 - 14:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            BJB wrote:

Thanks but I found the setting I needed under settings in the protection area.  The only thing I don't get is that I did a custom install of my update and deselect the anti-virus module.  Yet a few weeks later when I found the settings it was on. I turned off but assumed it would be unavailable/disabled if I didn't install.
Thanks for the followup.
BJB
 


Dear customer,
Thank you for the update. In this case we would recommend checking what Acronis services are turned on; and if the Active protection is still on, you can modify it according to the instructions from the article https://kb.acronis.com/content/60190; deselect one more time and if it does not help to delete Active Protection, please contact our support for further investigation.

      
                
                
                    
                                                    Thu, 10/27/2022 - 14:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    BJB
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 52
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Daria,
Thanks, I am good now no worries.  I was just passing this along in case development was interested in that an upgrade install, with antivirus de-selected, still had anti-virus available.
FWIW, I just renewed for a year for 5 PC's. ?
Thanks for your help.
BJB
 

      
                
                
                    
                                                    Fri, 10/28/2022 - 22:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Home Office 5 PC license 
Trueimage 2021 Perpetual 5 PC license 
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear BJB,
We always stay at your disposal, do not hesitate to contact us any time. 

      
                
                
                    
                                                    Mon, 10/31/2022 - 16:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    mbg175623
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have Acronis True Image 2021 installed. Like many experienced users, I am keen to prevent unneeded services etc from running in the background. With this, I have 'Active Protection' turned off in the TI software. However, upon examining the output of various tools, amongst others, I see the following running all the time...
In Services :-
mmsminisrv - mms_mini.exe - Acronis Managed Machine Service Mini
afcdpsrv - afcdpsrv.exe -  Acronis Nonstop Backup Service
AcrSch2Svc - schedul2.exe - Acronis Scheduler2 Service
syncagentsrv - syncagentsrv.exe - Acronis Sync Agent Service
AcronisActiveProtectionService - anti_ransomware_service.exe - AcronisActiveProtectionService
Actively connecting to the internet, and sending and receiving data, I see :-
mms_mini.exe - Acronis Managed Machine Service Mini
anti_ransomware_service.exe - AcronisActiveProtectionService
aakore.exe - Acronis Agent Core
adp-agent.exe - Acronis Cyber Protect Agent
updater.exe - Acronis Updater
Acronis, this is very concerning. I do NOT want anything running in the background - can you tell me (and others equally concerned) how to stop ALL of this background activity. I have no need for it and use your software ONLY for local image backups.

      
                
                
                    
                                                    Sun, 08/20/2023 - 10:53
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Currently Acronis Cyber Protect Home Office

Previously True Image 2021, 2018 and earlier
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            mbg175623 wrote:

I have Acronis True Image 2021 installed. Like many experienced users, I am keen to prevent unneeded services etc from running in the background. With this, I have 'Active Protection' turned off in the TI software. However, upon examining the output of various tools, amongst others, I see the following running all the time...
In Services :-
mmsminisrv - mms_mini.exe - Acronis Managed Machine Service Mini
afcdpsrv - afcdpsrv.exe -  Acronis Nonstop Backup Service
AcrSch2Svc - schedul2.exe - Acronis Scheduler2 Service
syncagentsrv - syncagentsrv.exe - Acronis Sync Agent Service
AcronisActiveProtectionService - anti_ransomware_service.exe - AcronisActiveProtectionService
Actively connecting to the internet, and sending and receiving data, I see :-
mms_mini.exe - Acronis Managed Machine Service Mini
anti_ransomware_service.exe - AcronisActiveProtectionService
aakore.exe - Acronis Agent Core
adp-agent.exe - Acronis Cyber Protect Agent
updater.exe - Acronis Updater
Acronis, this is very concerning. I do NOT want anything running in the background - can you tell me (and others equally concerned) how to stop ALL of this background activity. I have no need for it and use your software ONLY for local image backups.


Hello!
Many of the services mentioned by yourself are needed in order to make the product functional and backup. It's not possible to disable them all.
Please check this KB with more details: https://kb.acronis.com/content/65464
Please also refer to the following KB's with more details: 
https://kb.acronis.com/content/65499 
https://kb.acronis.com/content/60190
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/28/2023 - 15:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tomáš Mark
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello. It is already fixed and I can to stop all the unwanted services?
Or I have to stop paying for subscription next month?

Thanks

      
                
                
                    
                                                    Mon, 01/08/2024 - 22:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tomáš Mark wrote:

Hello. It is already fixed and I can to stop all the unwanted services?
Or I have to stop paying for subscription next month?

Thanks


Hello!
Please refer to the following manuals:
https://kb.acronis.com/content/55052
https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#selecting-components-for-installation.html
As you can see, when you install the program, you can select just the option for the agent without the antivirus and other features. If you install them, it's normal that you will have them running.
Please note that this thread is for MSPs with cloud deployment and not for corporate subscriptions.
If you have any queries, please contact our support at https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Tue, 01/09/2024 - 08:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
