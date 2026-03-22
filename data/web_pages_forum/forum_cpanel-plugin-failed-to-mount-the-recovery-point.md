# cPanel Plugin "Failed to mount the recovery point."

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/cpanel-plugin-failed-mount-recovery-point

## Original Post
**Author:** Unknown

cPanel Plugin "Failed to mount the recovery point."

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
When I'm trying to restore files or databases through the Acronis cPanel plugin, I get the following error after selecting the date/time of the recovery point. 
Failed to mount the recovery point.

This error comes up after 5 minutes of "Loading the backup. This may take a while."
While I can restore individual files/folders from the Acronis Backup Cloud web interface, the same doesn't apply for databases for example, which can only be restored from the cPanel plugin interface.
Any ideas?
Thanks in advance,
George

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Screenshot 2019-01-30 at 10.51.31.png

                      40.56 KB
                  
              
                      Screenshot 2019-01-30 at 10.45.54.png

                      25.51 KB
                  
              
                      Screenshot 2019-01-30 at 10.50.47.png

                      26.99 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/30/2019 - 08:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello George,
I see the issue has been already forwarded to the RnD for investigation. We'd appreciate if you could share the results of the investigation with the community. 
Thank you in advance! 

      
                
                
                    
                                                    Mon, 02/04/2019 - 08:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    ThisWebHost
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We're experiencing the same problem here. Have you had any update from Acronis, George?

      
                
                
                    
                                                    Wed, 02/13/2019 - 15:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We were told that this can be solved by not excluding any files in the backup job, however I'm still evaluating this. Can't call it a solution either tbh...
BTW I was excluding:
error_log
debug.log
/home/*/lscache/*
Do you also use exclude files from your backups via Backup Options -> File Filters?

      
                
                
                    
                                                    Wed, 02/13/2019 - 22:02
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    telmo.calhaco@ptisp.pt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Any news on this subject ?

      
                
                
                    
                                                    Tue, 06/04/2019 - 15:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This issue was assigned ABR-210974 which was fixed in v7.9 but it turns out the fix was not for the problem itself (being able to exclude files without breaking the cPanel plugin functionality), but to allow the user to increase the timeout using ACRONIS_MOUNT_DAEMON_TIMEOUT environment variable.
Now there's ABR-222940 which should resolve the issue with excludes, that is going to be fixed in v8.0 (no ETA).
A KB article has been posted as well: https://kb.acronis.com/content/62899
For now, the only solution in order for the cPanel plugin to work and for your customers to be able to use the cPanel plugin and restore files, databases etc themselves, is not to use excludes in your backup jobs.

      
                
                
                    
                                                    Wed, 06/05/2019 - 15:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dennis Nind
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there,

We are using the Acronis Cyber Cloud, along with the cPanel plugin and also get this issue on a few of our servers. 

We aren't excluding any files, however, but get the same error...
 
Failed to mount the recovery point.


      
                
                
                    
                                                    Sun, 06/16/2019 - 15:35
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dennis,
How large are your drives? Our cPanel servers are around 600-800GB large (SSD storage) and we haven't experienced this (when not using file excludes). If you have larger volumes, you might need to use the ACRONIS_MOUNT_DAEMON_TIMEOUT environmental variable.
Please create an executalbe file /usr/lib/Acronis/system_libs/7.2.0/config with the following content:
#!/bin/bash
export ACRONIS_MOUNT_DAEMON_TIMEOUT="1800"
restart the acronis_mms service and try again.

      
                
                
                    
                                                    Mon, 06/17/2019 - 09:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dennis Nind
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there,
Thank you for the reply. I have tried this, but unfortunately it hasn't helped. 
We do have fairly large servers, the majority are 6x 1TB SSDs in raid10, so closer to 3TB.
Should we increase the timeout further?
The strange thing is, it doesn't seem to hang for all that long - the message appears after only a few seconds. 
Many thanks

      
                
                
                    
                                                    Mon, 06/17/2019 - 09:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dennis Nind
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the additional information
I have tried this however, but unfortunately it still isn't working and is failing with the same error.
The servers are fairly large, with around 3TB usable space.
The strange thing, is the fact that the error appears after only a few seconds as opposed to a long delay, then the failure taking place. 
Has anyone else experienced this at all?
 

      
                
                
                    
                                                    Mon, 06/17/2019 - 12:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If the error shows up immediately then it's probably an already (failed) open mount. Normally, restarting acronis_mms should fix this, but in some cases, a server reboot might be necessary.

      
                
                
                    
                                                    Mon, 06/17/2019 - 14:47
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dennis Nind
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have tried to restart acronis_mms but that hasn't helped unfortunately.
Can you advise if there is a way around the reboot? It's a production server, so it's tricky scheduling in downtime
I checked /var/lib/Acronis/mount but this is empty also, and checked the Linux mounts and saw nothing relating to Acronis also.
I tried mount | grep Acronis but there was nothing there. I was hoping to somehow force it to unmount.
Appreciate your help on this!

      
                
                
                    
                                                    Mon, 06/17/2019 - 14:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Just got the same problem. There was an issue with the server and it had to be rebooted. After the server comes back online the Acronis Backup WHM plugin is no longer working.
I noticed if try to run the backup from the web console it returns an error like
The SnapAPI kernel module is not loaded for the kernel 3.10.0-962.3.2.lve1.5.26.9.el7.x86_64 currently running in this system. Install the module for this kernel version, and then retry the backup.
I have also emailed Acronis about it. Acronis Backup was running fine for several months until this issue.
Regards,
Chris

      
                
                
                    
                                                    Tue, 12/10/2019 - 16:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Chris,
It looks like the snapi module is not installed for the kernel you're currently running (probably a newer one than the one you were running before, due to the server reboot).
First check the running kernel version with uname -r, then check if you have the respective kernel-devel package installed with yum install kernel-devel-$(uname -r)
Once that is out of the way, you can go ahead and build/install the snapi module:

$ service acronis_mms stop
$ dkms {build,install} -m snapapi26 -v 0.7.126
$ service acronis_mms start
(-v 0.7.126 is currently applicable for the latest 12.5 14800 agent version)
Give it a try and let us know.
-G.

      
                
                
                    
                                                    Tue, 12/10/2019 - 17:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi George,
Thanks for your reply.
I got
 
# uname -r
3.10.0-962.3.2.lve1.5.26.9.el7.x86_64
# yum install kernel-devel-$(uname -r)
Package 1:kernel-devel-3.10.0-962.3.2.lve1.5.26.9.el7.x86_64 already installed and latest version
Nothing to do
# service acronis_mms stop
Redirecting to /bin/systemctl stop acronis_mms.service
# dkms {build,install} -m snapapi26 -v 0.7.126
Error! Could not find module source directory.
Directory: /usr/src/snapapi26-0.7.126 does not exist.
Error! Could not find module source directory.
Directory: /usr/src/snapapi26-0.7.126 does not exist.
In the Acronis WHM plugin at the bottom of the page, it reports
Version 1.3.300
Regards,
Chris
 

      
                
                
                    
                                                    Tue, 12/10/2019 - 19:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Oh, I went /usr/src and saw older version and so ran it with that version and now it works.
 
Many thanks, George! I owe you a beer (or two) some time.
 
Cheers,
Chris

      
                
                
                    
                                                    Tue, 12/10/2019 - 19:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Can you please post the output of ls -lad /usr/src/snapapi26-* and dkms status | grep installed ?

      
                
                
                    
                                                    Tue, 12/10/2019 - 19:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            # ls -lad /usr/src/snapapi26-*
drwxr-xr-x 2 root root 4096 Jul 11 14:16 /usr/src/snapapi26-0.7.122

# dkms status | grep installed

snapapi26, 0.7.122, 3.10.0-962.3.2.lve1.5.25.10.el7.x86_64, x86_64: installed
snapapi26, 0.7.122, 3.10.0-962.3.2.lve1.5.26.3.el7.x86_64, x86_64: installed
snapapi26, 0.7.122, 3.10.0-962.3.2.lve1.5.26.9.el7.x86_64, x86_64: installed

      
                
                
                    
                                                    Tue, 12/10/2019 - 19:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            (sorry I didn't notice you already found the solution earlier - no need for those after all :)

      
                
                
                    
                                                    Tue, 12/10/2019 - 19:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Though how come it is not updating from
 
0.7.122
 
to
 
0.7.126

      
                
                
                    
                                                    Tue, 12/10/2019 - 20:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You'll need to log into your Backup Management Console at cloud.acronis.com then go to Settings -> Agents (screenshot: https://share.getcloudapp.com/7Kuy2ldN) and update the machine agent(s) to their latest versions.

      
                
                
                    
                                                    Tue, 12/10/2019 - 20:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks. I  noticed that earlier. Does it update automatically at some point or do you have to update the agent for each machine manaully all the time?
Ps at Acronis the preview button doesn't work on the forum.

      
                
                
                    
                                                    Wed, 12/11/2019 - 04:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I updated an agent to test it and it updated, and now WHM Acronis plugin shows
CLOUD STORAGE USAGE 0.0 B
Though I read it can take up to 8 hours for the stats to be updated. Is there a way to force update cache/stats?

      
                
                
                    
                                                    Wed, 12/11/2019 - 06:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm not sure you can force update the stats. Have you tried running a backup from the WHM plugin? Does it work as expected?

      
                
                
                    
                                                    Wed, 12/11/2019 - 06:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I tried refreshing the recovery point to see if it updated the stats but it doesn't.
 
I noticed when I updated the agent on VPS not using EPEL the stats updated right away, but with servers using EPEL the stats only updates after rerunning the backup. But either way the backup/restore seems to be working after updating the agent. I think just depending on whether using EPEL or not the storage stats might not update after updating the agent.
 
Cheers,
Chris

      
                
                
                    
                                                    Wed, 12/11/2019 - 06:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good point, I was also sceptical about how epel updates the dkms package every so often with new versions, and if that would cause any compatibility issues with the Acronis driver, considering they assume people use the RHEL/CentOS provided package.
I will try adding dkms to the excludes list of the epel repo file on a new server and see how it goes.

      
                
                
                    
                                                    Wed, 12/11/2019 - 07:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok great.
 
When update agent on a server with no EPEL installed no update is available for DKMS but there is when EPEL is installed. Even after applying to update for DKMS on a server with EPEL it doesn't automatically update the stats. Seems to only update after the next backup has run.
 
Only had EPEL on for Memcached, but if it's going to cause trouble for Acronis then Memcached needs to go. Redis should still work.
 
Please let me know what you find/recommend George.
 
Thanks again.

      
                
                
                    
                                                    Wed, 12/11/2019 - 11:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            PS it does seem to work if you goto Backups - Locations - select machine and click Show Backups and click Refresh button which reloads the recovery points and updates the stats right away.

      
                
                
                    
                                                    Wed, 12/11/2019 - 11:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the tip Chris. Were you able to restore backups from your backup server, or is it failing again with the same error? "Failed to mount the recovery point."
We're getting this since the Acronis Cyber Cloud 8.0 rollout in EU1.

      
                
                
                    
                                                    Wed, 12/11/2019 - 14:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            For some reason, it now says "There are no backups yet. The next backup is scheduled at 12 Dec 2019 04:18" because I'm sure I didn't reinstall the agent.
I updated the agent from 122 to 126 and now it even shows incorrect size
 
CLOUD STORAGE USAGE
0.0 B
"An error has occurred. Please try again later or contact your administrator."
 
I refreshed the recovery point but still shows the same size. The backup button is "On". If I try to turn it off it says "An error has occurred. Please try again later or contact your administrator."
As for your last question, I updated the agent on the other servers and I restored a file from public_html which did say it succeed so guess it's ok unless you mean full cPanel account restore or something else?

      
                
                
                    
                                                    Wed, 12/11/2019 - 15:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just tried to restore the full cPanel account on a server different to the one I had trouble in this thread and it restored fine
 
https://i.imgur.com/dOMOixh.png
 
Using the latest agent, but not using Acronis storage, using own backup dedicated server for storage.
 
The issue I have a server in this thread is now
 
https://i.imgur.com/0uGegzL.png
https://i.imgur.com/xr0j6AE.png
https://i.imgur.com/UGsyfs1.png
 
As you can see, the backups are still there, just the WHM plugin is not connected to it for some reason. Hopefully, can get that resolved with help from the new thread I created https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-continue-backing-server-old-backup-after-reinstall-agent
 

      
                
                
                    
                                                    Wed, 12/11/2019 - 15:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

I just tried to restore the full cPanel account on a server different to the one I had trouble in this thread and it restored fine
 
https://i.imgur.com/dOMOixh.png
 
Using the latest agent, but not using Acronis storage, using own backup dedicated server for storage.
 
The issue I have a server in this thread is now
 
https://i.imgur.com/0uGegzL.png
https://i.imgur.com/xr0j6AE.png
https://i.imgur.com/UGsyfs1.png
 
As you can see, the backups are still there, just the WHM plugin is not connected to it for some reason. Hopefully, can get that resolved with help from the new thread I created https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-continue-backing-server-old-backup-after-reinstall-agent
 


As mentioned at https://forum.acronis.com/comment/523741#comment-523741 after running it the second time it did work. Strange. 

      
                
                
                    
                                                    Wed, 12/11/2019 - 17:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Getting this error again. I am trying to restore a cPanel account on the server but I have received this message again. It seems to be due to timeout.
What is the default timeout limit and should I follow https://kb.acronis.com/content/61762
Or this https://forum.acronis.com/comment/501242#comment-501242
Current disk usage:
72G /
551G /home

      
                
                
                    
                                                    Tue, 12/17/2019 - 13:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It stopped working. Recovery doesn't work at all. Acronis not reliable to use on cPanel servers anymore. Time to switch back to alternative solutions.

      
                
                
                    
                                                    Tue, 12/17/2019 - 14:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If I try to disable Acronis using plugin it says "An error has occurred. Please try again later or contact your administrator."
It seems the last update from Acronis completely messed up the cPanel plugin. I'm surprised there isn't a flood of issue about it on the forum?

      
                
                
                    
                                                    Tue, 12/17/2019 - 15:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It seems to back up the data fine but you can't restore any data or enable/disable the backup within the Acronis WHM/cPanel plugin.
 
Terrible.

      
                
                
                    
                                                    Tue, 12/17/2019 - 16:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I had no luck with restores from within the cPanel/WHM plugin either, I always get "Failed to mount the recovery point." on any server I tried.
I have a ticket open with Acronis Service Providers Support Team regarding this matter (04248491) but there hasn't been any progress since I provided the sysinfo files they requested a couple of days ago.
I'm also very worried with all these issues happening. Backup software should be 100% reliable. What's the point in taking backups if we can't restore them? What will happen if we really need to restore stuff for a customer and we're unable to do so?

      
                
                
                    
                                                    Tue, 12/17/2019 - 16:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

I had no luck with restores from within the cPanel/WHM plugin either, I always get "Failed to mount the recovery point." on any server I tried.
I have a ticket open with Acronis Service Providers Support Team regarding this matter (04248491) but there hasn't been any progress since I provided the sysinfo files they requested a couple of days ago.
I'm also very worried with all these issues happening. Backup software should be 100% reliable. What's the point in taking backups if we can't restore them? What will happen if we really need to restore stuff for a customer and we're unable to do so? 


Thanks for your update. I 100% agree with what you said.
I prefer to use slow and reliable (JetBackup) over fast and unreliable (Acronis) any day.
Acronis cPanel/WHM plugin was working fine for several months and I was impressed with it, but now it's been playing up for over a week and they seem to be taking their sweet time to fix it. Not impressed by that at all.
I signed up with reseller to test it and should I start to meet minimum requirement could have gone directly with Acronis, but after this, I don't think I'll bother.
I've removed the Acronis plugin on some bigger servers for now because I don't trust it. I noticed it was doing fsck.ext check and showing errors in VNC console for some servers and the load on storage server goes very high when it didn't do that in the past.

      
                
                
                    
                                                    Tue, 12/17/2019 - 16:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I noticed there was an update for the cPanel Acronis plugin and so reinstalled that version and now a backup does restore on a smaller server that I tried but I noticed it takes a lot longer to restore a full cPanel account than it used to
I see fsck is running during the mount which I don't remember seeing before
https://i.imgur.com/rJZsDc8.png
It is the fsck check that has been added slowing the restore down? If so, you have to remember you can have fairly large cloud servers but disk IO is capped at datacentre and if that is the case it can take a lot longer to restore data even if SSD is being used! Even when I just tested it on a dedicated server with SSD NVMe the restore was not as quick as it used to be when trying to restore a full cPanel account which requires mount. If just restoring file/folders then it is quicker because it only rsync the files across i.e no need to compress cPanel account first. But for full cPanel account seems to take much longer. Again, if because fsck check has been added, maybe allow server admin to turn that on or off to speed up the restore which would be useful for those with limited disk IO etc.

      
                
                
                    
                                                    Tue, 12/17/2019 - 19:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If just restoring file/folders then it is quicker because it only rsync the files across i.e no need to compress cPanel account first. 

Actually, I see it does fsck and is slow just for restoring a few files/folders too.

      
                
                
                    
                                                    Tue, 12/17/2019 - 19:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

I noticed there was an update for the cPanel Acronis plugin and so reinstalled that version and now a backup does restore on a smaller server that I tried but I noticed it takes a lot longer to restore a full cPanel account than it used to


What is the version of the Acronis cPanel plugin you're running now (that updated one I mean)?

      
                
                
                    
                                                    Tue, 12/17/2019 - 21:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

HostXNow wrote:

I noticed there was an update for the cPanel Acronis plugin and so reinstalled that version and now a backup does restore on a smaller server that I tried but I noticed it takes a lot longer to restore a full cPanel account than it used to


What is the version of the Acronis cPanel plugin you're running now (that updated one I mean)?


Version 1.3.300 which is the same version. Not sure why when wget it is said it was a newer version if the number is the same unless they updated the script but not updated the version number.

      
                
                
                    
                                                    Tue, 12/17/2019 - 21:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Can you share what you did to get the newer version, so I can try it out as well? I'm also in v1.3.300 for a few weeks now btw.

      
                
                
                    
                                                    Tue, 12/17/2019 - 22:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Can you share what you did to get the newer version, so I can try it out as well? I'm also in v1.3.300 for a few weeks now btw.


I had -N after wget so only downloads a new file to the server if there is a newer version and it said there was. Maybe it updated the old file and never did that before because the agent was already installed. But I tried to install Acronis a few times so don't think that to be the case.
 
Spent most of the day trying to get Acronis to work. Actually quite hating the product with a passion right now. The backup system is supposed to be for extra peace of mind. Totally the opposite today.
 
I thought maybe the issue was when using own storage server instead of Cloud hosted by Acronis but it affects the Cloud-hosted one too and so know I can rule out self-hosted being an issue.
 
Seems an issue since an update from 7.9 to 8.0
 
Have they still not provided you with an update yet? I also mentioned the issue to a staff member on the phone and mentioned your ticket number too.

      
                
                
                    
                                                    Tue, 12/17/2019 - 22:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Nope, no response to this point.
Funny thing is that I'm able to restore from other cPanel servers that save to the same particular backup server without a problem. cPanel accounts count also doesn't seem to make any difference as I have servers with ie 40 accounts that give the "Failed to mount recovery point" error, while there are servers with 200 accounts that can restore files just fine.

      
                
                
                    
                                                    Wed, 12/18/2019 - 11:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Nope, no response to this point.
Funny thing is that I'm able to restore from other cPanel servers that save to the same particular backup server without a problem. cPanel accounts count also doesn't seem to make any difference as I have servers with ie 40 accounts that give the "Failed to mount recovery point" error, while there are servers with 200 accounts that can restore files just fine.


Is this to Acronis Cloud Backup storage or your own hosted storage server? Does it make any difference for you whether using their storage or your own? Or it still varies randomly?
I've already readded Jetbackup for now, so if Acronis plays up I can quickly rsync the data every so often incase the Acronis backups cannot be relied upon.
I also found a cheaper script similar to JetBackup that may be good backup script too https://bu-backup.com.ar
How can they say Acronis is #1 backup solution when it acts like that. I guess anyone can have issues, but taking such a massive company like Acronis over a few weeks to fix it and customers not able to restore data for over 2 weeks. Can't be serious :)

      
                
                
                    
                                                    Wed, 12/18/2019 - 11:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            No response from CloudEVO yet
Last Updated: 22 hours ago
Good while it lasted :(

      
                
                
                    
                                                    Wed, 12/18/2019 - 12:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It's just the plugin that isn't working. Server-side, it works fine.
The plugin is saying "Failed to mount the recovery point" because it is doing fsck and because fsck isn't completing quick enough and the plugin times out. But even when it says "Failed to mount the recovery point" I can see on the server it is still fsck the mount point it's trying to mount, and even on the backup server I can see the process is still running.
 
And if check 
 
df -h on the machine I can see it eventually the mount points are set up, but by then the plugin has already timed out. When you go to load the backup again, it goes through the whole process again. Why is taking over two weeks to correct that timeout issue with the Acronis cPanel/WHM plugin?

      
                
                
                    
                                                    Wed, 12/18/2019 - 12:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If you see the first post in this thread, this error has been showing up in various cases since last January.
I've had several tickets opened with msp support since then, first the problem was File Excludes (ABR-210974) which I had to disable (resulting in much larger backup images than actually required for some users who wanted to exclude certain folders from their backups for example - ie higher cost for backup storage) but even after no files were excluded it still was showing up every now and then. 
Then there was a different issue ABR-222940, which was going to be fixed with v8.0, and now that v8.0 is here restores are completely broken for certain servers.
I have servers on the same owned hosted storage server that are working fine, and others that are not. 

      
                
                
                    
                                                    Wed, 12/18/2019 - 13:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            On the servers it does not work properly on, are they Cloud servers or Dedicated servers? Does it work after all the Acronis/updates are the latest and the server has rebooted?
Be sure to backup using a different solution if you haven't already until the issue is fixed properly.

      
                
                
                    
                                                    Wed, 12/18/2019 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            They're all dedicated servers. But I also have other dedicated servers, saving backups on the same backup server, that work fine.
Agents are fully updated, latest kernel version, and rebooted.

      
                
                
                    
                                                    Wed, 12/18/2019 - 16:42

## Original Post
**Author:** Unknown

cPanel Plugin "Failed to mount the recovery point."

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      







            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

They're all dedicated servers. But I also have other dedicated servers, saving backups on the same backup server, that work fine.
Agents are fully updated, latest kernel version, and rebooted.


Yesterday reseller said
Acronis is aware of a problem causing this issue for some users since the update to version 8.0. They will be releasing an update to the cPanel plugin and agent on the 24th of this month with a fix. Until this time you will need to restore files, folders using the Acronis web interface instead of the cpanel plugin.

Unfortunately, using the Acronis web interface instead of the cPanel plugin is not an option for us, as I tried to download a small file from it some weeks ago and it was downloading very slow like at 20KB/sec which makes it useless. That might be because the control panel is hosted in the USA but the data from the server is hosted in Europe and/or Acronis limit the download speeds for the web interface. Also, it only lets you download the data 'as is' which is also not good. There should be an option to download a full cPanel account from within the Acronis web interface too in times like this when the plugin itself doesn't work. It's too much work restore the data to a server otherwise as MySQL takes forever as have to get the tables, restart MySQL service etc. Too much work.
 
Hoping Acronis cPanel/WHM plugin can be improved more. CPanel/WHM should already have Acronis functionally built-in after being over 20 years old. Anyhow.

      
                
                
                    
                                                    Fri, 12/20/2019 - 14:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Everyone,
we've published an article about this issue https://kb.acronis.com/node/63866

      
                
                
                    
                                                    Tue, 12/24/2019 - 09:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:

Hello Everyone,
we've published an article about this issue https://kb.acronis.com/node/63866


Unfortunately, I updated the agent on a test server and now when trying to browse a date from "Backups" the cPanel plugin returns the following error after just 1 second "Failed to mount the recovery point."
I tried to restart the Acronis service and that didn't help.
I uninstalled the agent and readded it only when I entered the username and password and it starts to install the plugin it returns an error.
Failed to install the backup agent. For details, see "/var/log/trueimage-setup.log". Please try to update the operating system by running the "yum update" command. After the update, restart the backup agent installation.

It's a shame because it was working fine since around May. Now it's broken.
I'll check more and update.

      
                
                
                    
                                                    Tue, 12/24/2019 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            UPDATE:
Ok. It seems to be ok now. Backup/Restore working fast again.
Took Acronis some time to provide a fix for this, but it's working now. I thought the fsck was causing the issue. How about if adding such feature in the future to allow it to be enabled/disabled within the web console so if it's causing an issue then admin can disable it?
PS the On/Off button for "Backup" within the cPanel/WHM Acronis plugin is still not working. It returns error
An error has occurred. Please try again later or contact your administrator.

Guess that will be resolved in a different update?

      
                
                
                    
                                                    Tue, 12/24/2019 - 14:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Indeed the new agent resolved this issue. Everything is working fine now.

      
                
                
                    
                                                    Sat, 12/28/2019 - 09:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @George_Fusioned does the file/folder excludes work now? Possible to use the same used for JetBackup to speed things up
*.jpa
backup-*.tar.gz
cpmove-*.tar.gz
site-*.tar.gz
.MirrorSearch
*/com_akeeba/backup/*
*/backupbuddy_backups/*
*/.wysiwygPro_*
*/core.[0-9]*
public_html/cache/*
tmp/*
logs/*
lscache*
.cagefs
.cagefs*
.cpan
.cpanel/caches
.cpanel/datastore
.cpcpan
.sqmailattach
.cpanel/*.sock
access-logs/*
*/error_log
public_ftp/*
softaculous_backups/*
*/wp-content/uploads/wpcf7_captcha/*
*/wp-content/widget-cache/*
*/wp-content/cache/*
*/wptsc-cachedir/*


      
                
                
                    
                                                    Sat, 12/28/2019 - 22:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

@George_Fusioned does the file/folder excludes work now? Possible to use the same used for JetBackup to speed things up
*.jpa
backup-*.tar.gz
cpmove-*.tar.gz
site-*.tar.gz
.MirrorSearch
*/com_akeeba/backup/*
*/backupbuddy_backups/*
*/.wysiwygPro_*
*/core.[0-9]*
public_html/cache/*
tmp/*
logs/*
lscache*
.cagefs
.cagefs*
.cpan
.cpanel/caches
.cpanel/datastore
.cpcpan
.sqmailattach
.cpanel/*.sock
access-logs/*
*/error_log
public_ftp/*
softaculous_backups/*
*/wp-content/uploads/wpcf7_captcha/*
*/wp-content/widget-cache/*
*/wp-content/cache/*
*/wptsc-cachedir/*

 


Using excludes doesn't work. It backup but restore will show "Failed to mount recovery point". But backup is fast without using excludes anyway, and so it doesn't matter.

      
                
                
                    
                                                    Sun, 01/05/2020 - 14:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
