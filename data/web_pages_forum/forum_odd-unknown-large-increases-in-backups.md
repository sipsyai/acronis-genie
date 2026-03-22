# Odd, unknown large increases in backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/odd-unknown-large-increases-backups

## Original Post
**Author:** Unknown

Odd, unknown large increases in backups

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a Client (Device named JWPA-Server) that normally has a total backup of about 45-46GB.  We back up files three times daily, with each backup taking under 4 minutes.
On May 1, at 2:08pm, there was an unexpected backup that added about 8GB of data.  It took 3hrs and 45 mins.
On May 2, at 8:08am, there was another unexpected backup that added another 8GB of data.  It took 3hrs and 10 mins.
The Client swears they didn't add any large files and I have looked and cannot find any evidence of any new, large files.
 
Is there any way to determine what specifically was added to the backups on those dates/times?  How can I delete them?  Should I just delete all backups since that first weird 8GB addition?  I'd like to get to the bottom of this so it doesn't happen again.  The account is locked due to storage quote being exceeded and I want to figure it out before having to continually add more unwanted space.
Thanks!
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 05/03/2017 - 01:14

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, PCBMerchy!
Apart from adding new files, there may such a thing as defragmention if they do a disk-level backup.
One more reason is the Retenion Rules. Perhaps customer has hit the maximum amount of recovery points stated in their backup plan, so old files are being recalculated and re-uploaded to be up-to date.
What I am trying to say is that there are many things to consider to have the correct assumption.
 
To answer your question about a way to determine which file was added in the latest backups - it is only possible if they do not have a lot of files to back up. You can try to browse their backup from the Backup Console and see which files/folders have the most recent date of the last change. It may give you an idea.
If that does not prove to be helpfull, submit a suppot ticket to Service Provider Support Team with the following information:
 - login name of the affected user
 - name of the machine (JWPA-Server)
You can also provide them here so I would have a quick peak.
 
Regards,
Fedor

      
                
                
                    
                                                    Wed, 05/03/2017 - 16:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the reply.
I don't think there are any recovery point limitations.  I have it set up the same way on all of my "file only" clients and I've never seen any other giant unknown data backups.  Just to answer some of your thoughts:
1.  It's a file only backup to the Cloud.  They also do a bare metal/full disk backup locally.
2. There are only 8 folders being backed up - the usual Desktop, Downloads, Documents as well as Music, Video, Favorites, etc.  There really should be no surprises.
3. I don't think the 46GB is very much these days.  And the new 16GB is an additional 1/3 of the size of the original backup.
4. The username is was2@pcbasics.biz.
Thanks again for your help.

      
                
                
                    
                                                    Wed, 05/03/2017 - 17:41
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Any further insight on this?  The client is asking for answers and assurance that it won't happen again and I'm not sure what to tell them...

      
                
                
                    
                                                    Thu, 05/04/2017 - 14:31
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sorry for the delay.
 
I went to have a look at the activities. File-level backups do not show how much data was actually sent to the cloud, only how much were processed on the machine.
Please compare to another backup job that does upload data daily (Backup plan name Daily Image)
We can have a look at the meta data in the Cloud Storage to have a better tell, but to proceed, please create a support ticket and attach the online backup certificate from the customer's machine to it. It's stored here C:\ProgramData\Acronis\BackupAndRecovery\OnlineBackup\Default
I cannot confirm to you that such behavior is unexpected, as we cannot be sure whether customer did not change anything or some third-party software was involved.
 
Anyway I wanted to additionally share some links that may come in handy a bit later:
 - how to delete backups (in case you would decide to clear up some space) -> http://dl.managed-protection.com/u/baas/help/7/user/en-US/index.html#35…
 - how cloud archive works (the article explains why the archive does not shrink after you clear some recovery points) -> https://kb.acronis.com/content/57116
 - customer also may have a look at any old backups left in the Cloud using Web Restore -> https://kb.acronis.com/node/59015
And also, keep in mind that the service usage recalculates every 4-6 hours for Cloud Backups.
 
 
 

      
                
                
                    
                                                    Thu, 05/04/2017 - 16:00
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It added another 8GB chunk on 5/3 at 2:08pm.  They now have 24GB of unexplained data backed up.  The client is a two user law firm that doesn't have that much new data on a monthly basis, let alone a daily basis.
There is no new 3rd party software and nothing changes without me to do it for them.  It's been working fine for 8 months until the past few days.
I need to resolve this.  What is my best "quick fix" for things?  Delete all backups since the mystery data chunks started backing up?  Delete the entire backup and start from scratch?
Thanks!
 

      
                
                
                    
                                                    Thu, 05/04/2017 - 16:28
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            A quick fix would be to start from scratch, as deleting some slices (recovery points) will not shrink the archive, as I've mentioned in my previous reply.
One more point to consider here is that if you scroll the list of activities, you would see that the size of the backup started to reach the quota long before you have created this forum thread (Jan 12, 2017 to be exact, as in the attached picture).
If you look at the contents of the backups, you would see a Downloads volder, a Videos folder, etc. It also could be the reason if the increase in storage usage is indeed in place. I also provided some hints on the cause of this in my first reply.
Please submit a case to support if you want to dive deeper, as forum support is limited for general questions and quick solutions, and we cannot guarantee that SLA will be met. Full investigation is only possible via ticket.
 
Thank you for understanding!

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      410945-138424.png

                      110.34 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 05/05/2017 - 07:39
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    PCBMerchy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'll be re-starting from scratch.  At this point, the backup has grown to 95GB of data, double from when it started.  The client is ready to try new software but I've convinced them to give it another try.
I'm curious why it tells me I can no longer backup with this account, yet it continues to grow and charge me for it.  Charges which I guess I'll be eating since I can't explain to the client why it's happening.  This certainly does not inspire confidence in the software.
I've manually checked each folder that is backed up and there is nothing there to justify these insane jumps in backed up data.  While I'd love to really know what's going on, the client doesn't care.  They just want it to work, which I can understand.  Next time I'll put in a ticket first.
If it acts up again, I guess we're on to a different backup option.
 

      
                
                
                    
                                                    Wed, 05/10/2017 - 01:14
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Also having customer where the backupsize goes crazy for no obvious reason.
It can increse with 10-30 GB over a day
In the case im thinking of right now laso include backup of profiles

      
                
                
                    
                                                    Tue, 05/23/2017 - 14:52
