# Backups Missing after Recovery Failure

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backups-missing-after-recovery-failure

## Original Post
**Author:** Unknown

Backups Missing after Recovery Failure

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have been backing up a large amount of files to an external hard drive successfully for months.  During a restore attempt, I was told it failed (it gave me a warning saying that the restoration was frozen).
I rebooted the Server thinking that would clear things up.  Now when I access the web portal and look at the backup, the saved job that has been running for months is gone and it shows me a fresh setup. (Acronis 1)
When I try to restore files again, it tells me "There are no backups of the selected devices in the known locations." (Acronis 2)
I can see the files on the external drive but somehow the Agent seems to have forgotten where to look.  How do I re-attach it?  Or at least how can I recover the data?  
I was in the middle of a large, important restore that I was hoping to get done overnight so that it would be ready in the morning but now I'm stuck.
Any help would be appreciated.
This is on a Server 2008 machine.
p.s. Just noticed an additional error message (Acronis 3)

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      acronis_1.jpg

                      37.78 KB
                  
              
                      acronis_2.jpg

                      47.31 KB
                  
              
                      acronis_3.jpg

                      26 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/16/2017 - 02:16

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello PCBMerchy,
In first place I'd focus on checking agent being online in backup console, since messsage acronis_2.jpg appear when recovery points can't be browsed by agent, appearing offline.
General suggestion here is to check if:
1. Acronis Managed Machine service is running
2. manually run agent reregistration guiding KB https://kb.acronis.com/content/55244
A good alternative to recover disk/volumes and files is to use Bootable Media ISO over blank VM.
Here is a User Guide reference:
https://dl.managed-protection.com/u/baas/help/7/admin/en-US/index.html#33487.html
https://dl.managed-protection.com/u/baas/help/7/admin/en-US/index.html#33518.html
Message acronis_3.jpg appear if agent service was interrupted unexpectedly, while backup/restore process was running. It is quite explainable if OS was restarted.
Issue acronis_1.jpg with disappering applied backup plans is quite unusual and should be investigated by Development Team. Possibly there is a sync issue between Backup Console Web service and Cloud Management Server. I'd suggest to submit a support ticket to mspsupport@acronis.com.
In case you are an End User, then request assistance from your Partner.
Regards,
Eugene Tanasiev

      
                
                
                    
                                                    Thu, 03/16/2017 - 10:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you so much for your fast reply.
It seemed to re-connect automatically during the next scheduled backup.  The backup appears to have completed successfully.
However, I set the recovery operation to go overnight and when I checked it this morning, it was "frozen" again at the exact same 6% spot.  I thought I may have ended it prematurely the first time but it has been almost 10 hours now and it's still stuck. (Acronis 4 pic)
Is there a "graceful" way to stop this if it's frozen?  Do I continue to let it run?  Is it possible it's still working but just appears to be be frozen?
The restore is somewhere between 200-300GB of files from a local external hard drive.
I would request support from the Partner but their help is so completely awful, I'd rather switch backup software than use them.  It's been 5 days since I last requested support from them on a separate issue and they have not responded.  They took a 7-10 days on the issue before that.  They waste time asking useless questions that I already provided information on and then only reply to emails every 24-36 hours.  I can't wait that long when a client is looking to me for an immediate answer.
Hopefully you can provide some more guidance on this.  Again, I appreciate any help you can offer me.

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      407352-137476.jpg

                      23.83 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 03/16/2017 - 13:57
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Generally, recovery progress % on the backup console has an update timeout. More often timeout is increased due to Cloud Management Server overload. Sometimes this cause general backup console timeout.
Anyway the progress usually change once the recovery move to next stage. What I want to say is that:
a)even if backup is stuck on 6%, then it doesn't mean that recovery halted.
b) alert, shown in backup console mean that the timeout for progress update has exceeded.
This could be troubleshooted real easy. We know that service_process.exe process is in charge of all backup/restore opperations.
So if you open Process Monitor and check its activiry, then you may see the real progress going. In case there is no movement, but service_process.exe exist and RAM/CPU usage don't change, then we may collect process dump for hang process (http://kb.acronis.com/content/27931 ), needed command procdump -ma service_process.exe. Share the dump output here.
>Is there a "graceful" way to stop this if it's frozen?  Do I continue to let it run?  Is it possible it's still working but just appears to be be frozen?
Unfortunately the only way is to cancel process from backup console. This process may take a while. The fastest way - kill service_process.exe
>The restore is somewhere between 200-300GB of files from a local extrenal hard drive.
For this big restore I would definately use Bootable media. This is a solid way to accomplish this task.
I am always at your service should you have any further questions.
Regards,
Eugene Tanasiev

      
                
                
                    
                                                    Thu, 03/16/2017 - 13:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Wow, such amazingly quick replies.  I was going to check back in a couple of hours and you replied while I was still editing my post...  :D
I checked on the service_process.exe and it was jumping around between 0-50% of CPU.  It's an older, under-powered server so between that and the remote software, the CPU was at 100%.  I closed out the remote software and am hoping that will free up more resources for the Acronis to keep going.
I'm going to request that the client wait until the weekend to see if the restore is working properly.  Otherwise I'll try the boot software or download from my emergency backup option.
Again, thank you so much for the responses.  At least I have some information to relay to the client.  I'm certain once this is resolved the Partner will jump in and ask more silly questions before ultimately stop responding.

      
                
                
                    
                                                    Thu, 03/16/2017 - 14:10
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Lack of HW resources would explain slow recovery processing.
Thank you for your apreciation.
Always ready to help you to drive to success.
Please keep me tuned and don't hesitate to ask additional questions if any.

      
                
                
                    
                                                    Thu, 03/16/2017 - 14:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The restoration is proceeding painfully slow, but at least it's going.  It's at 15% after 36+ hours.  The client has agreed to let it run through the weekend.
My next question - it's adding a random text string at the end of each item's extension, which changes the file's extension (Acronis 5).  So now, for example, a Word document with a ".docx" extension becomes ".docx~A7J49DO3" or something similar.
Will that go away at the end of the restore or will I have to manually edit each file?  I assume it will go away, as I have not seen that happen during my other restore tests but it's giving me heartburn thinking I'm going to have to individually change thousands of files...
Thank you for your help!

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      407484-137545.jpg

                      45.86 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 03/17/2017 - 17:11
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            And now, I just got this message (Acronis 6).
***********
Interaction required
Access Denied.
Retry   Ignore   Ignore All   Cancel
***********
I assume somehow Acronis doesn't have the persmission to restore a file or files?  I'm very hesitant to interrupt this process or stop it.  Please let me know the proper course of action.
Thanks.
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      407500-137557.jpg

                      25.04 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 03/17/2017 - 19:00
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello PCBMerchy,
The ".docx~A7J49DO3" extention will get back to ".docx" once file is recovered completely.
Performance issue, causing slow file downloading from image backup, is fixed in one of the next release Acronis Backup Cloud agent versions.
Sending you in PM custom build agent, that will workaround this.
BTW, I checked server.mrpa.local agent recovery and it goes pretty well now (56% - 179GB recovered)
 
Regards, 
Eugene.

      
                
                
                    
                                                    Sun, 03/19/2017 - 21:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the reply, Eugene.  
It's been 110+ hours now and it seems to be stuck on 81%.  It gave me the "Activity is not responding" error message (Acronis 7) around 2:00am this morning (it's now 6:35pm) and it hasn't moved since then (about 16+ hours).
I certainly don't want to touch it at this point since:
1. it seems close to being done,
2. I don't have another 100+ hours to wait for another restore
3. I don't want to have to manually re-name all the restored files.
Is it possible it's restoring a gigantic file and just appears to be stuck while it slowly restores it?  Is there any way to see exactly what is going on or do I just have to wait?
I can't say enough how frustratingly slow this restore process is.  I hope I never have to restore more than a Word document or two in the future...
Thanks!
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      407723-137608.jpg

                      21.36 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 03/20/2017 - 22:35
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I would recommend to check with Process Monitor. It will show what file service_process.exe is recovering at the moment.
Using agent with custom build will certainly exclude such long restore in future.
I am always at your service should you have any further questions.
Regards,
Eugene

      
                
                
                    
                                                    Mon, 03/20/2017 - 23:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It seems to have finally completed, as of late last night. 
And it did remove all of the temporary "~A93KH2Q" type additions, thankfully.
I haven't heard of any complaints yet from the customer so I will follow up with them tomorrow to make sure all is well.
Thanks again for your replies.  Even though it took quite a while, you at least kept me sane through the process.  :)
 

      
                
                
                    
                                                    Wed, 03/22/2017 - 21:52
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hopefully final question.
Now that the Recovery is over, it seems to have forgotten the backup plan it had been running.  The local backup plan is gone and I wanted to set it up again without overwriting the existing backups.  Is there an easy way to restore the missing backup plan or should I just go ahead and start over by swapping in a new external drive and keeping the current one as an emergency backup?
 

      
                
                
                    
                                                    Thu, 03/23/2017 - 00:47
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Glad to know that the recovery finished successfully and the customer is happy.
Unfortunately there is no option to restore missing backup plan without having at least earlier saved system reports from agent. I guess now is too late, since the report will not include the backup plan scripts saved in scheduler service.
That's why best option here, avoiding time consuming investigation, would be to create a new plan. Of course it would create a new chain, but at least you would be able to run backups starting from today.
 
 

      
                
                
                    
                                                    Thu, 03/23/2017 - 07:49
