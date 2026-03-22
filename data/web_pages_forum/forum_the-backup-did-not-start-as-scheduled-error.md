# The backup did not start as scheduled error

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-did-not-start-scheduled-error

## Original Post
**Author:** Unknown

The backup did not start as scheduled error 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Error message :
The backup did not start as scheduled. Either it was skipped automatically because the previous backup was still running, or a backup scheduler error had occurred.
I tried edit the backup task start time , the alert appears again . I deleted the first task scheduler and created another one. On the first few days , i backup as plan but after 4th day , than on the 15 march it start stopping again. Than i change task failure handling  to number of attempts to 8 and interval between attempts 1 hour . On the 16th , it back to normal . On the 17th the backup didnt work again and till 18th than it backup 17th backup. For more clearer picture , please take a look at 2020-03-10_1025 picture to understand better. 
Anyone met this problem before ?

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2020-03-19_1015.png

                      28.93 KB
                  
              
                      2020-03-19_1025.png

                      41.35 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/19/2020 - 02:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    IanL-S
                            

                            
                    
                        Forum Hero
                    
                
            
                        
                
                    Posts: 219
                
            
            
                
                    Comments: 5536
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I suspect additional information is necessary before we can offer any assistance. Not sure what Acronis product you are using, I suspect it is not True Image. Please provide details of the operating system (for example Windows 10 Pro 64bit build 1909, and the version and build of Acronis product: for example ATI 2020 build 22510.
Ian
PS you have been (yet another) victim of the forum bug that places some new threads in off topic area. That is why I am uncertain what product you are using.

      
                
                
                    
                                                    Thu, 03/19/2020 - 05:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Gigabyte Aorus GA-AX370-Gaming 5 M/B; AMD Ryzen 1700X; 16gig RAM; 2 x 500 gig Samsung 970 EVO PCIe NVMe, 1 x 250 gig Samsung 960 EVO PCIe NVMe drives + other drives (Windows 10 Pro 64)
Gigabyte Aorus B360 Gaming 3M/B, Intel i5 9400; 16gig RAM; 1 x 500 gig Samsung EVO Plus PCIe NVMe +  1 x 250 gig Samsung 960 EVO PCIe NVMe + other drives (Windows 10 Enterprise 64)
Gigabyte Aorus H370 Gaming 3M/B, Intel i5 9400; 16gig RAM; 1 x 500 gig Samsung EVO Plus PCIe NVMe + 3 x Kingston HyerX Fury 240gig RAID 5 + other drives (Windows 10 Enterprise 64)
Synology DS414 NAS 4 x 4TB WD Red HDD

            
                            
                Products: 
                Cyber Protection Home Office (latest build); Disk Director 12.5 

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ian
I am using acronis cyber cloud. 
Using Windows Server 2012 R2 Standard 64 bits.
Agent for windows (64-bit)
v12.5.15300
Agent for SQL
v12.5.15300
But when i run it manually from the console ,its able to backup successfully everytime i run it. But when it comes to let it goes by schedule , it did not run properly for file to cloud. Direct from SQL management studio no problem at all with the schedule plan.
 

      
                
                
                    
                                                    Thu, 03/19/2020 - 06:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Steve Smith
                            

                            
                    
                        Legend
                    
                
            
                        
                
                    Posts: 116
                
            
            
                
                    Comments: 31715
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sorry but you will need to raise this issue in the Acronis Business product forums or wait for the forum moderator to move it to the correct Acronis Cyber Backup 12.5 forum for you as both Ian & I only have experience with the Acronis True Image application range.

      
                
                
                    
                                                    Thu, 03/19/2020 - 10:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Please do NOT send private messages - open a forum topic instead where you will get a quicker response!!
I have very great difficulty opening private message due to Acronis forum 504 errors!

            
                            
                Products: 
                Acronis True Image 9.0 - 11.0, 2009 - 2026

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Péter Szatmári
                            

                            
                    
                        Frequent Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 619
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello jianzhi low!
I'm not sure I see the nature of your problem in the attached pictures without having a look at the backup plan itself. Can you export and share the plan you have problems with?
I frequently have this alert when the machines are turned off at the time of the next scheduled backup, but I don't think that's a usual case for a server. Windows updates causing some issues maybe?
I see you have a separate plan for SQL backup. Do you have these problems with that plan?
-- Peter

      
                
                
                    
                                                    Thu, 03/19/2020 - 17:21
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup 12.5
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Peter,
How to do export the plan using cyber cloud ? Yes i have a separate plan for SQL backup and its not having any problem. 

      
                
                
                    
                                                    Fri, 03/20/2020 - 04:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Péter Szatmári
                            

                            
                    
                        Frequent Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 619
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello jianzhi low!
Have a look at the screenshot I attached. Export will produce a json file. You might want to rename your internal archtecture elements you deem sensitive.
-- Peter

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      532699-180586.jpg

                      367.85 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 03/20/2020 - 06:20
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup 12.5
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello jianzhi low,
thank you for posting on Acronis forums!
I have moved your topic to Acronis Cyber Backup Cloud Forum. 
But when i run it manually from the console ,its able to backup successfully everytime i run it. But when it comes to let it goes by schedule , it did not run properly for file to cloud.

There was such a problem that if you run a scheduled task manually, it will not start that day on scheduled time as "already done". I suggested that you re-schedule this task (slightly change its schedule), do not run it manually and wait till scheduled time.

      
                
                
                    
                                                    Fri, 03/20/2020 - 06:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I too started getting those "backup did not start" notifications since yesterday.
Upon inspection, the backup jobs appear to have completed successfully and no further information is given.
https://share.getcloudapp.com/NQuDKXye
https://share.getcloudapp.com/nOu8Dy6l
https://share.getcloudapp.com/QwuKb1xA 
https://share.getcloudapp.com/04uPNw0w
https://share.getcloudapp.com/7Ku0b9xz
https://share.getcloudapp.com/BluZQ6Ov
This has happened yesterday and today at the same time (I run backups every 8 hours so in between backup jobs worked fine).

      
                
                
                    
                                                    Tue, 04/28/2020 - 17:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AndrewT
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This same issue started for us upon upgrading an agent to 12.5.22410.

      
                
                
                    
                                                    Mon, 05/04/2020 - 12:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Andrew, George_Fusioned
I'd try the steps from the article https://kb.acronis.com/content/57910
If the agent machine was available during the backup start time:
Edit the backup task start time.
If the alert appears again, recreate the backup task.
If the newly created backup task also triggers the alert, please contact Acronis Customer Central for assistance, so that our engineers can look into the situation on your environment and find the proper solution. 
 

      
                
                
                    
                                                    Mon, 05/04/2020 - 10:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AndrewT
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm not interested in unnecessarily recreating the backup task. The task can be run manually and it succeeds without issue, it just doesn't schedule the next run which ultimately results in this error and the backup not running automatically.
This only started with the agent upgrade as explained. Agents that have not been upgraded continue to work normally.
Normally, the only Acronis related background process running on these agents is /usr/lib/Acronis/BackupAndRecovery/mms. Since upgrading the agent the following have been running:
/opt/acronis/aakore
/opt/acronis/bin/task-manager
/opt/acronis/bin/adp-agent
/opt/acronis/bin/grpm-sync-unit
/opt/acronis/bin/updater
/usr/lib/Acronis/BackupAndRecovery/mms
/usr/lib/Acronis/Schedule/schedul2-bin
It seems pretty clear that a process is not completing and the agent upgrade is some how related.
From examining /var/log/acronis, I did discover /var/log/acronis/atp-downloader/stderror being updated every minute since the agent was upgraded on May 2nd. This file is now 23MB in size as a result. Every minute it reports the following:
04.05.2020 11:27:51.141673 [0x0000203e] [0x00007f3e96e8f700] [debug] [UpdaterBrain] : UpdateIndices()[710] UpdateIndices()[710] [>>> Update Indexes]: http://127.0.0.1:9772/api/atp-agent/v1/update_config is Failure
04.05.2020 11:27:51.143656 [0x0000203e] [0x00007f3e97492700] [debug] [ServerProxy] : DownloadPackage()[140] DownloadPackage()[140] escaped url: http://127.0.0.1:9772/api/atp-agent/v1/update_config
04.05.2020 11:27:51.145282 [0x0000203e] [0x00007f3e97492700] [error] [ServerProxy] : DownloadPackage()[188] DownloadPackage()[188] HTTP download error 404
04.05.2020 11:27:51.145640 [0x0000203e] [0x00007f3e97492700] [error] [ServerProxy] : DownloadNewUpdateIndex()[348] DownloadNewUpdateIndex()[348] error while downloading update index
04.05.2020 11:27:51.145687 [0x0000203e] [0x00007f3e97492700] [debug] [ServerProxy] : DownloadNewUpdateIndex()[352] DownloadNewUpdateIndex()[352] req: 'http://127.0.0.1:9772/api/atp-agent/v1/update_config' status: 404
04.05.2020 11:27:51.145716 [0x0000203e] [0x00007f3e97492700] [error] [UpdaterBrain] : ProcessNewUpdateIndex()[760] ProcessNewUpdateIndex()[760] update index error

      
                
                
                    
                                                    Wed, 05/06/2020 - 16:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have updated to agent version 12.5.22410 on a few of the affected boxes to see if anything changes.
BTW in my case the notification is a false positive, the jobs do run. There are no errors whatsoever. 
BTW2 where can I find the release notes for 12.5.22410? Here I see up to 12.5.22390: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProt…

      
                
                
                    
                                                    Wed, 05/06/2020 - 17:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Everyone,
I can’t tell much without complete System Information logs, Scheduler logs should be investigated in such issue but they are linked to MMS logs and many traces can be checked having the complete set of logs. I'd strongly recommend opening a support ticket, looks like the issue requires the attention of the expert engineers and development. 
 
George_Fusioned
 
> BTW2 where can I find the release notes for 12.5.22410? Here I see up to 12.5.22390: http://dl.managed-protection.com/u/baas/rn/agent/en-US/AcronisCyberProt…

I'll add a link here, once the release notes are updated, sorry for the inconvenience!  
 
 

      
                
                
                    
                                                    Fri, 05/08/2020 - 08:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    AndrewT
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fortunately, we test these agent upgrades on one server to make sure there are no issues before deploying them to our entire fleet. The agent in question here was initially upgraded via the console after which this issue started. 
In our case, the notification was definitely not a false positive - backups weren't being run / scheduled properly. Earlier this week, I manually re-installed (not via the console) the same version of the agent (12.5.22410) and the scheduling issue was resolved. 
The additional processes and excess duplicated logging of those errors every minute continues but that appears to have started in 12.5.21780 and is likely unrelated to this issue.
We'll continue to monitor this for a few days before testing with other low impact agents.

      
                
                
                    
                                                    Fri, 05/08/2020 - 16:42
