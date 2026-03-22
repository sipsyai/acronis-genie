# Is the acronis cpanel plugin compatible with Almalinux 8.4?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cpanel-plugin-compatible-almalinux-84

## Original Post
**Author:** Unknown

Is the acronis cpanel plugin compatible with Almalinux 8.4?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
I just installed the Acronis cpanel plugin on Almalinux 8.4. The installation in the WHM does start normal, but then it stops. Attached you can see the screen.
I'm using the newest kernel:
 4.18.0-305.12.1.el8_4.x86_64 
Regards
Michael

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Screenshot (37).png

                      144.45 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 08/26/2021 - 14:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael, 
Please open a case with our support team so we may gather the details, localize the issue and provide you with a solution specific to this case. 
https://www.acronis.com/en-eu/support/
Thank you for your time.
Best regards, 
Georgi

      
                
                
                    
                                                    Mon, 08/30/2021 - 10:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yeah we're experiencing the same (oddly, it installs fine if you're on CentOS 8 and convert to Almalinux after installing the plugin).
We're opened a case with msp support and currently the information is that the plugin is not compatible with Almalinux:
While the cPanel plugin does not officially support AlmaLinux, we have actively reviewed your findings and have found them very insightful.
This KB article was made public to provide more details on the current situation.
https://kb.acronis.com/node/69273
You may refer to this article and we will be happy to update it with new solutions after further testing is done (if applicable).

I hope they will make it compatible soon, because it's annoying to have to install CentOS first and then convert after installing the Acronis cPanel plugin.

      
                
                
                    
                                                    Mon, 09/06/2021 - 21:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
We also got this answer from the support. But we found out, it works when you install the agent first and then install the cpanel plugin. 
 
Michael

      
                
                
                    
                                                    Tue, 09/07/2021 - 05:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just noticed this problem... doh!
 
Please support it asap since can't use CentOS much longer.

      
                
                
                    
                                                    Tue, 09/14/2021 - 16:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Please add support for AlmaLinux asap

https://www.linkedin.com/feed/update/urn:li:activity:684229523469362380…

      
                
                
                    
                                                    Wed, 09/15/2021 - 08:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Brunner, George_Fusioned, HostXNow
thank you, registered your votes for the request CI-12363 AlmaLinux support for cPanel/Plesk/DirectAdmin. The task is currently under development. 

      
                
                
                    
                                                    Mon, 09/27/2021 - 07:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
Any update or ETA for AlmaLinux support?
Thanks!

      
                
                
                    
                                                    Fri, 11/12/2021 - 20:46
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Hello Ekaterina,
Any update or ETA for AlmaLinux support?
Thanks!


Hi! Clarified the status of the feature request - it is in QA now, the update expected to be released till the end of the month. 

      
                
                
                    
                                                    Sat, 11/13/2021 - 12:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Hello Ekaterina,
Any update or ETA for AlmaLinux support?
Thanks


I just set up a new CentOS 8, converted AlmaLinux 8.5 and then installed the plugin and it seems to work fine.
 
Best,
Chris

      
                
                
                    
                                                    Wed, 11/17/2021 - 12:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

I just set up a new CentOS 8, converted AlmaLinux 8.5 and then installed the plugin and it seems to work fine.
 
Best,
Chris


Cool, I'll give it a try on my next server provisioning. Thanks!

      
                
                
                    
                                                    Tue, 12/14/2021 - 13:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Giovanna Fiscella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            and i thought it was only me who experienced this issue

      
                
                
                    
                                                    Thu, 12/16/2021 - 13:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I can confirm the Acronis cPanel plugin will now install without an issue on AlmaLinux.

      
                
                
                    
                                                    Thu, 12/16/2021 - 13:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

I can confirm the Acronis cPanel plugin will now install without an issue on AlmaLinux.


Thank you for the confirmation\feedback! The fix has been officially delivered in the Version 1.5.6 Acronis extension for Plesk. 
 

      
                
                
                    
                                                    Fri, 12/17/2021 - 14:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

I can confirm the Acronis cPanel plugin will now install without an issue on AlmaLinux.


George_Fusioned   
I can confirm it works on OVH public cloud. But I set up a new 2338G dedicated server with OVH and at first, could not get cPanel to work properly (server would not boot back up after installing cPanel on top of AlmaLinux), but that seems to have resolved itself after some time.
 
But have you tried a full server restore on CloudLinux 8/AlmaLinux 8 because it does not work for me on the OVH dedicated server?
 
I get
 

06:00 PM — 06:00 PM (1 sec)
Recovering volumes
Status:Error
Device: <snipped>
Started by:<snipped>
Start time:Dec 20, 2021, 06:00:00 PM
Finish time:Dec 20, 2021, 06:00:01 PM
Duration:1 sec
Backup file name:<snipped>
What to recover:nvme0n1p1 (EFI_SYSPART) → EFI system partition,nvme0n1p3 (swap-nvme0n1p3) → swap-nvme0n1p3,nvme1n1p1 (EFI_SYSPART) → EFI system partition,nvme1n1p3 (swap-nvme1n1p3) → swap-nvme1n1p3,md2 (boot) → boot (md2),md4 (root) → root (md4),There is 1 item more
An internal error. Please contact the support team.
All properties
Error
An internal error. Please contact the support team.
DetailsSupportAll properties
An internal error. Please contact the support team.MESSAGEAn internal error. Please contact the support team.
Additional info:------------------------
Error code: 6225957
Fields: {"$module":"disk_bundle_lxa64_28323"}
------------------------
Error code: 6225965
Fields: {"$module":"disk_bundle_lxa64_28323"}
------------------------
Error code: 6225965
Fields: {"$module":"disk_bundle_lxa64_28323"}
------------------------
Error code: 19857419
Fields: {"$module":"disk_bundle_lxa64_28323"}
------------------------
 
The backup works fine and trying to restore an account within the cPanel Acronis plugin works, just not a full server restore and gives the above message.
 
I contacted Acronis support and they haven't updated me so guess they don't know what's causing it.
 
Best,
Chris

      
                
                
                    
                                                    Mon, 12/20/2021 - 17:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

But have you tried a full server restore on CloudLinux 8/AlmaLinux 8 because it does not work for me on the OVH dedicated server?


Hey Chris,
I haven't attempted to perform a full server restore with an Almalinux server, but I've tried it a couple of times with Cloudlinux and it worked fine.
I have no experience with OVH's servers / OS installation process, do you use an image or do you perform the installation by hand via KVM/IPMI using an ISO? Do you use UEFI or legacy BIOS? 
Did you clear the drives and created the mdadm setup/partitions by hand or did you try to restore on top of the previously existing RAID setup / partitions?
-G.

      
                
                
                    
                                                    Tue, 12/21/2021 - 07:03
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey G,
 
Yeah isn't AlmaLinux as it happens on CentOS 7, too. I even tried using only 1 drive without any RAID to rule out the RAID issues.  It's an odd booting issue of some sort.
 
It doesn't help when I'm trying to troubleshoot and there are odd issue with whole Acronis account i.e backup failed on all servers this morning because of incorrect snapAPI issue? Aaaaaagggh!!!!
If I try and run anything this morning just stuck on 0%.
 
I even took a look at N-able but they don't support CentOS 8/CloudLinux 8/AlmaLinux 8. I have not tested their CentOS 7 which they support, but it probably works better than Acronis right now :(
 
-C. ;)
 
A

      
                
                
                    
                                                    Tue, 12/21/2021 - 11:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

It doesn't help when I'm trying to troubleshoot and there are odd issue with whole Acronis account i.e backup failed on all servers this morning because of incorrect snapAPI issue? Aaaaaagggh!!!!


Yeah saw that too - looks to be related with the latest agent version 15.0.28559.
Servers where auto update failed and are still on the previous version, don't have this issue.

      
                
                
                    
                                                    Tue, 12/21/2021 - 15:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I don't like Acronis don't send update out about it to let their customers know they are aware of such issue. They could at least have a status page so customers can check if there are any known issues rather than the customer sitting trying to fight a battle they will never win because the issue is on Acronis. I wasted over an hour this morning because of that issue.
Ends up being a problem that will resolve itself if the customer waited. They should their customers know this.
Who do you use if you do not use OVH? A lot of the UK providers have poor specs/high pricing i.e RapidSwitch/iomart.

      
                
                
                    
                                                    Tue, 12/21/2021 - 15:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Regarding the "Backup failed because snapAPI kernel module is not loaded for kernel X" error; this happened to me on servers that had epel's dkms package installed and not the one provided by the OS.
So the fix was to add exclude=dkms into the /etc/yum.repos.d/epel.repo file and run yum downgrade dkms / dnf downgrade dkms to downgrade to the OS provided dkms package.
After that, I downloaded the latest agent installer and re-installed the agent to the server.
HostXNow wrote:

Who do you use if you do not use OVH? A lot of the UK providers have poor specs/high pricing i.e RapidSwitch/iomart.


I run my own Acronis Cyber Infrastructure clusters (5 nodes each) in the Netherlands and in Greece. Depending on each customer needs (faster on-site or slower off-site backups/restores) I setup their account to the appropriate storage location. I also use the EU3 (London) and US5 (Phoenix) Acronis storage locations for certain clients. 

      
                
                
                    
                                                    Tue, 12/21/2021 - 16:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I will check the EPEL/DKMS, I saw you mention that here the other day - thanks!
 
I meant which provider do you get your unmanaged dedicated servers from to offer Shared, Reseller, Managed VPS/Dedicated.
 
I know you have your own Acronis setup using your own servers/storage.
 
I use Acronis Backup Cloud and so use storage in their UK datacentre.
 
PS Acronis should pay you for the help you provide on these forums. It is really good.
 
Best,
Chris

      
                
                
                    
                                                    Tue, 12/21/2021 - 21:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Something is wrong with Acronis today because their own web console is not working properly at all. Try to delete backups.... nothing... try to backup... nothing.... try to recover... nothing.
 
Might as well remove it all and stick with JetBackup. Slower but at least it works 24/7.

      
                
                
                    
                                                    Tue, 12/21/2021 - 21:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HTTP request "/api/vault_manager/v1/sync/archives" failed: 500 - Internal Server Error: server returned: {"created":[],"updated":[],"errors":[{"domain":"General","code":"ReasonConflict","reason":"ReasonConflict","debug":{"msg":"Failed to create or update archive d783d11f-6431-127a-1ae2-f2e9658e5fbc in vault 7aabe542-944d-addb-a957-183cfba2d314 :: archive update has failed because its 'last seen time' is in the past"}}],"_links":[{"rel":"ListArchivesSyncInfo","href":"/api/vault_manager/v1/sync/archives"},{"rel":"UpdateArchivesBulk","href":"/api/vault_manager/v1/sync/archives"}] }
DATE AND TIMEDec 21, 2021, 09:50:38 PM
CODE0x01350016+0x01350016+0x02900003+0x02470017
MODULE309
MESSAGETOL: Failed to execute the command. Dms::Gst::RefreshRecoveryPointsCommand
Additional info:------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"$module":"management_server_lxa64_28553","CommandID":"CF4A80C3-A7BA-4DD0-9491-1031E15E0731"}
Message: TOL: Failed to execute the command. Dms::Gst::RefreshRecoveryPointsCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB8196E0
Fields: {"$module":"ams_dms_lxa64_28553","CommandID":"CF4A80C3-A7BA-4DD0-9491-1031E15E0731"}
Message: TOL: Failed to execute the command. Dms::Gst::RefreshRecoveryPointsCommand
------------------------
Error code: 3
Module: 656
LineInfo: 0x125EC1CCDA84BF00
Fields: {"$module":"ams_dms_lxa64_28553"}
Message: Failed to update archives on VDM.
------------------------
Error code: 23
Module: 583
LineInfo: 0x5B89CDE5313BCE90
Fields: {"$module":"ams_dms_lxa64_28553","uri":"/api/vault_manager/v1/sync/archives","status":"500"}
Message: HTTP request "/api/vault_manager/v1/sync/archives" failed: 500 - Internal Server Error: server returned: {"created":[],"updated":[],"errors":[{"domain":"General","code":"ReasonConflict","reason":"ReasonConflict","debug":{"msg":"Failed to create or update archive d783d11f-6431-127a-1ae2-f2e9658e5fbc in vault 7aabe542-944d-addb-a957-183cfba2d314 :: archive update has failed because its 'last seen time' is in the past"}}],"_links":[{"rel":"ListArchivesSyncInfo","href":"/api/vault_manager/v1/sync/archives"},{"rel":"UpdateArchivesBulk","href":"/api/vault_manager/v1/sync/archives"}]
}

      
                
                
                    
                                                    Tue, 12/21/2021 - 21:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

I meant which provider do you get your unmanaged dedicated servers from to offer Shared, Reseller, Managed VPS/Dedicated.


I don't lease servers from anywhere, I rent full racks at the two locations and own all my servers and network equipment :)

      
                
                
                    
                                                    Tue, 12/21/2021 - 22:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

HostXNow wrote:

I meant which provider do you get your unmanaged dedicated servers from to offer Shared, Reseller, Managed VPS/Dedicated.


I don't lease servers from anywhere, I rent full racks at the two locations and own all my servers and network equipment :)


Oh yeah, I remember you saying now!
 
Well, I downgraded the DKMS and uninstalled the agent via SSH, then reinstalled it using cPanel/WHM Acronis plugin and it is readded but then shows an error message inactivity
 
Activity failed
Activity 'Deactivating ASRM' failed. Failed to find Secure Zone.
 
I think Acronis is going crazy!
 

      
                
                
                    
                                                    Tue, 12/21/2021 - 23:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

Well, I downgraded the DKMS and uninstalled the agent via SSH, then reinstalled it using cPanel/WHM Acronis plugin and it is readded but then shows an error message inactivity


No need to uninstall the agent / install via plugin etc. Here's what I do:
wget https://eu-cloud.acronis.com/download/u/baas/4.0/15.0.28559/CyberProtect_AgentForLinux_x86_64.bin
chmod +x CyberProtect_AgentForLinux_x86_64.bin
./CyberProtect_AgentForLinux_x86_64.bin
Just follow the wizard and after a couple of minutes you're done. The installer will keep all your settings, upgrade the agent, rebuilt the kernel modules and restart services.

      
                
                
                    
                                                    Wed, 12/22/2021 - 00:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks George_Fusioned  
I have tried it that way too. No matter what way I do it, the recovery points have gone and then click "Refresh" it just loads for ages and then shows an error message.
It looks like your storage setup is better than Acronis's own right now.

      
                
                
                    
                                                    Wed, 12/22/2021 - 00:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

I can confirm the Acronis cPanel plugin will now install without an issue on AlmaLinux.


 Thread needs solution <-- No, it doesn't.
 
This is resolved as confirmed by the #1 Acronis community forum expert George_Fusioned at @Ekaterina ;-)

      
                
                
                    
                                                    Wed, 12/22/2021 - 01:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

HostXNow wrote:

Well, I downgraded the DKMS and uninstalled the agent via SSH, then reinstalled it using cPanel/WHM Acronis plugin and it is readded but then shows an error message inactivity


No need to uninstall the agent / install via plugin etc. Here's what I do:
wget https://eu-cloud.acronis.com/download/u/baas/4.0/15.0.28559/CyberProtect_AgentForLinux_x86_64.bin
chmod +x CyberProtect_AgentForLinux_x86_64.bin
./CyberProtect_AgentForLinux_x86_64.bin
Just follow the wizard and after a couple of minutes you're done. The installer will keep all your settings, upgrade the agent, rebuilt the kernel modules and restart services.


I never had to do it that way but 1# turns out to be quicker and #2 seems to have bought things back to life on my end in terms of storage showing recovery points again. So seems to have done some magic somewhere
 
Thanks again George_Fusioned  

      
                
                
                    
                                                    Wed, 12/22/2021 - 01:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            False alarm, the Recovery points are still not showing correctly in the "Backup Storage" section. It is stuck on "Loading". Hopefully, it will resolve itself after some hours now that the agents have been reinstalled on each server.
I'll check it later.
Cheers!

      
                
                
                    
                                                    Wed, 12/22/2021 - 01:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

Thanks George_Fusioned  
I have tried it that way too. No matter what way I do it, the recovery points have gone and then click "Refresh" it just loads for ages and then shows an error message.
It looks like your storage setup is better than Acronis's own right now.


When you uninstall the agent, some config files usually remain on the device (they hold your device's MMSCurrentMachineID and InstanceID). So when you reinstall the agent, your device will register to the previous entry in cloud.acronis.com and not as a new box. That is unless you manually delete those conf files as well - if you did, then new backups will be saved into a new backup file (ie a different entry under "Backup Storage") and old backups won't be accessible from the WHM plugin. 
This is why I avoid uninstalling/installing the agent software via package manager (yum) in case of any issues, but instead use the command line installer as described above to reinstall the agent software on top of my existing installation/settings.
Even if the install wizard (happens sometimes) prompts me to register the device via token at the end of the installation, I just hit cancel since I know my device is actually registered. 
HostXNow wrote:

False alarm, the Recovery points are still not showing correctly in the "Backup Storage" section. It is stuck on "Loading". Hopefully, it will resolve itself after some hours now that the agents have been reinstalled on each server.
I'll check it later.
Cheers!


Have you tried restarting acronis_mms / aakore services or even the entire server?
systemctl stop acronis_mms
systemctl stop aakore
ps aux | grep acronis (get the PIDs of any acronis related processes)
kill -9 [pid]
systemctl start acronis_mms
systemctl start aakore
Wait ~10 minutes and then head over to WHM > Acronis Backup

      
                
                
                    
                                                    Wed, 12/22/2021 - 09:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

False alarm, the Recovery points are still not showing correctly in the "Backup Storage" section. It is stuck on "Loading". Hopefully, it will resolve itself after some hours now that the agents have been reinstalled on each server.
I'll check it later.
Cheers!


Also check this out: https://kb.acronis.com/content/69913
Maybe it's related to your case.

      
                
                
                    
                                                    Wed, 12/22/2021 - 10:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I did leave the config files box unchecked when running it. Still checking today, the account is a mess. Everything failed to run. It won't let me remove backups or anything. 
 
Luckily I have JetBakup running at the same time.
 
I'll just remove the account and start it again.
 
If the same issue happens again I'll drop Acronis. Because every several months or year something happens caused by an update from Acronis, then have to start again which defeats the point of using Acronis. i.e being able to keep up to 6 months retention of backups.
 
As I said, JetBackup was slower, but that was when I had 250Mbit/500Mbit connections on VPS. They now burst up to 2Gbit and using Wasabi storage is fast, especially now they have a UK location. Thank god for that, because Acronis is unreliable sometimes.

      
                
                
                    
                                                    Wed, 12/22/2021 - 11:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            For instance, I just uninstalled the agent from SSH
 
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
 
And after it completes says
 
error: package file_protector-1.1-1485 is not installed
 
It should not say that. I don't think someone there at Acronis is doing RD/QA for the software after each update.

      
                
                
                    
                                                    Wed, 12/22/2021 - 11:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            And
 
Activity failed
Activity 'Deleting backups' failed. The cloud storage is temporarily unavailable. Please try again later.
TROUBLESHOOTING
Please check your network connection or retry the operation later. For more information on network troubleshooting, click Support.
 
Nothing wrong with my server network. The issue is with Acronis.
 
What a load of nonsense. :(

      
                
                
                    
                                                    Wed, 12/22/2021 - 13:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The account started working properly again. When clicking "Refresh" it's instant. But because of issues for over 24 hrs I ended up deleting some of the data and removing some agents.
 
Unreliable.
 
Acronis really need a status page because if there is an issue with their storage or something like that customers need to be able to check instantly rather than try to fight with the thing for many hours or submit a ticket/go on the live chat which takes many hours to explain everything.

      
                
                
                    
                                                    Wed, 12/22/2021 - 14:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Are you using your own backup server or their EU1 storage?
https://kb.acronis.com/content/69928

      
                
                
                    
                                                    Thu, 12/23/2021 - 09:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

Are you using your own backup server or their EU1 storage?
https://kb.acronis.com/content/69928


Yes, I'm using their storage and that is the reason! I don't use my own storage servers as I don't want the hassle of it. Well that was the idea anyway! ;p
 
I didn't change anything and noticed the backups started working for a customers account. It must have been playing up for over a day. They should let customers know about such outages or provide a status page that can be checked easily. I'm seriously considering switching to something else if they don't.
 
How can such a massive company not have a status page or notify their customer if there is a known issue? Saves their customers trying to fix something and in most cases just make matters worse when the fix can only be done by Acronis themselves.
 
OVH have a status page
 
https://status.us.ovhcloud.com/
https://www.status-ovhcloud.com/

      
                
                
                    
                                                    Thu, 12/23/2021 - 15:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

I didn't change anything and noticed the backups started working for a customers account. It must have been playing up for over a day. They should let customers know about such outages or provide a status page that can be checked easily. I'm seriously considering switching to something else if they don't.


You can enable "Maintenance Notifications" on your partner account: https://kb.acronis.com/content/59043
You will receive email notification for such incidents then :)
(they sent out a notification regarding the EU1 incident on Tue, 21 Dec 2021 11:33 UTC)

      
                
                
                    
                                                    Fri, 12/24/2021 - 05:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

HostXNow wrote:

I didn't change anything and noticed the backups started working for a customers account. It must have been playing up for over a day. They should let customers know about such outages or provide a status page that can be checked easily. I'm seriously considering switching to something else if they don't.


You can enable "Maintenance Notifications" on your partner account: https://kb.acronis.com/content/59043
You will receive email notification for such incidents then :)
(they sent out a notification regarding the EU1 incident on Tue, 21 Dec 2021 11:33 UTC)


 Ah, that was turned off! Sure it was enabled when I signed up.
 
So I got the backups working again on some of the affected devices, but I have noticed if I add a new server and install the Acronis plugin and run backup it takes 10 minutes and incremental every day is the same at 10 minutes
Yet If continue backing up a server to the existing plan which has up to 6 months of recovery points it's taking between 3-9 hrs to complete which doesn't look right at all.
 
How can JetBackup (file-level) do incremental backup in 1 hour and 16 minutes but Acronis (block-level) is taking 7 hours and 42 minutes - something isn't right there at all

      
                
                
                    
                                                    Fri, 12/24/2021 - 16:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
