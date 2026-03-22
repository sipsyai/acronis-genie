# Uninstall Acronis Does Not Do Anything

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/uninstall-acronis-does-not-do-anything

## Original Post
**Author:** Unknown

Uninstall Acronis Does Not Do Anything

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I had installed the cPanel/WHM Acronis plugin on a server months ago and uninstalled the plugin, but I see it's still running processes /opt/acronis/bin/cyber-desktop-service --service /opt/acronis/bin/private-cloud-proxy --config private-cloud-proxy.yml /opt/acronis/bin/cred-store --aakore-control /opt/acronis/bin/feedback-collector -config config.yaml /opt/acronis/bin/acp-update-controller -e --update-controller Running /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall -a Just runs forever and doesn't even do anything!?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 05/07/2025 - 23:26

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
The --no-purge key is used when calling the protection agent uninstaller. It ensures that the association between the server, its protection plan, and the backup chain is preserved.
Please review this user guide to confirm whether the agent was actually uninstalled or if the backup plan was merely disabled:https://www.acronis.com/en-us/support/documentation/WHMCPanel/#uninstalling-plugin.html#kanchor47
If the issue persists, please contact our support team for further assistance.
Best regards.

      
                
                
                    
                                                    Thu, 05/08/2025 - 08:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
I did use
yum remove acronis-backup-cpanel
ensures that the association between the server, its protection plan, and the backup chain is preserved

Ok. But I don't want that to happen as I'm using JetBackup instead. So, how to delete Acronis? Also, I no longer have Acronis with Reseller, and I also can't contact Acronis support directly, as it's asking me for a license key.
I guess there should be an option not to use --no-purge when running
yum remove acronis-backup-cpanel

 
Regards.
Chris.

      
                
                
                    
                                                    Thu, 05/08/2025 - 11:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Smith wrote:

Hello,
I did use
yum remove acronis-backup-cpanel
ensures that the association between the server, its protection plan, and the backup chain is preserved

Ok. But I don't want that to happen as I'm using JetBackup instead. So, how to delete Acronis? Also, I no longer have Acronis with Reseller, and I also can't contact Acronis support directly, as it's asking me for a license key.
I guess there should be an option not to use --no-purge when running
yum remove acronis-backup-cpanel

 
Regards.
Chris.


Running yum remove acronis-backup-cpanel will remove the agent and all its services. After you run it, please verify whether those services are still present.
Also, check whether you have a standalone backup agent installed in addition to the plugin—uninstalling the plugin only removes the plugin itself, not the actual backup agent https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Best regards.

      
                
                
                    
                                                    Thu, 05/08/2025 - 11:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
I did run
yum remove acronis-backup-cpanel

but it didn't remove the agent and all services and that's probably why I also tried to install the agent manually and remove it manually at the time. Still, the cPanel/WHM plugin is not installed.
Yet when I try to run 
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall -a

It tries to uninstall and I can see the different processes running but it doesn't do anything. It just keeps running until I cancel the process.
So if the cPanel/WHM plugin is not installed which it isn't and let's say the agent is still installed, how do I properly uninstall it.
Can you provide installation link and steps to install it and steps to try to uninstall it again?
Also, how can I get support from Acronis ticket system if I no longer have a license with Acronis?
Regards.
Chris.

      
                
                
                    
                                                    Thu, 05/08/2025 - 12:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I just resigned upto reseller for Acronis just so I can try to install/uninstall it, but again it isn't responding
chmod u+x Cloud_AgentForLinux_x86_64.bin
./Cloud_AgentForLinux_x86_64.bin
It's just showing
/root/Cloud_AgentForLinux_x86_64.bin.inst --packages-bundle ./Cloud_AgentForLinux_x86_64.bin
and it isn't doing anything.
Install/Uninstall just hangs!?

      
                
                
                    
                                                    Thu, 05/08/2025 - 12:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Even after I install the cPanel/WHM Acronis plugin
Configuring cPanel features
Checking ports for the backup agent installation
Downloading the backup agent
Installing the required components
perl
Installing the backup agent …
The backup has been successfully enabled.
Running
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
still hangs. Years ago, when I ran

/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall

 
It would load the installation screen instantly, so I know something isn't right with it. One of the reasons I stopped using Acronis was that there were issues with the cPanel/WHM plugin, which would stop restoring accounts/data every so often due to various problems, and I had to spend way too much time going back and forth with support. Sometimes, the problems occur when Acronis updates the agent.
It installs fine, but you can't completely uninstall Acronis if you want to; it says everything. Why make things easy when you can make it complicated, eh?
I want to be able to completely uninstall it from the server, including all of its Acronis configurations. Once that is done, I will try to use Acronis to backup again with a new plan and hopefully restore it properly. If it does, I'll continue using it as a secondary backup.
Regards.
Chris.
 

      
                
                
                    
                                                    Thu, 05/08/2025 - 12:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If I uninstall cPanel/WHM plugin
yum remove acronis-backup-cpanel
This system is receiving updates from CloudLinux Network server.
Dependencies resolved.
==============================================================================================================================================================================
 Package                                        Architecture                    Version                                 Repository                                       Size
==============================================================================================================================================================================
Removing:
 acronis-backup-cpanel                          x86_64                          1.8.5-882.el7                           @acronis-cpanel-stable                           87 M
Transaction Summary
==============================================================================================================================================================================
Remove  1 Package
Freed space: 87 M
Is this ok [y/N]: y
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                      1/1
  Running scriptlet: acronis-backup-cpanel-1.8.5-882.el7.x86_64                                                                                                           1/1
Detecting OS type and version ...
Unregistering plugin...
Uninstalling plugin for cPanel...
Plugin uninstalled ok
Plugin has been uninstalled for cPanel
Unregistering plugin in WHM...
acronisbackup unregistered
Plugin has been unregistered in WHM
Removing plugins feature, if exists...
Acronis Backup feature '/usr/local/cpanel/whostmgr/addonfeatures/acronisbackup_reseller' has been removed.
Plugin has been successfully uninstalled
  Erasing          : acronis-backup-cpanel-1.8.5-882.el7.x86_64                                                                                                           1/1
  Running scriptlet: acronis-backup-cpanel-1.8.5-882.el7.x86_64                                                                                                           1/1
  Verifying        : acronis-backup-cpanel-1.8.5-882.el7.x86_64                                                                                                           1/1
Removed:
  acronis-backup-cpanel-1.8.5-882.el7.x86_64
Complete!
 
It still shows the server in Acronis control panel console. So running that didn't remove the agent. It doesn't work properly!?
Regards.
Chris.

      
                
                
                    
                                                    Thu, 05/08/2025 - 12:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
Remove Remaining Files and Directories
Note: Once executed, this action is irreversible and will permanently delete the files.
After stopping the related processes, remove the Acronis files to prevent them from restarting. The main directory appears to be /opt/acronis. You can delete it using the following command:
bash
sudo rm -rf /opt/acronis 
To ensure all changes take effect and no residual processes remain, please reboot the server.
If the issue persists, kindly contact your previous service provider and inform them. Such issues should be escalated. While it's rare, problems with uninstallation can occur. If this were on Windows, it would be easier to resolve using the cleanup tool.
Best regards,

      
                
                
                    
                                                    Thu, 05/08/2025 - 14:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I did sudo
rm -rf /opt/acronis

I then killed the running processes. They didn't come back. 
 
But I also noticed some processes still running from /usr/lib/Acronis
So I did the same for that

sudo rm -rf /usr/lib/Acronis
and then killed the processes. They didn't restart automatically. All good there.
Then I thought I'd try to rerun the installer
chmod u+x Cloud_AgentForLinux_x86_64.bin
./Cloud_AgentForLinux_x86_64.bin

 
But again, it just hangs. I see it did create the directory
/opt/acronis

I went to
/opt/acronis/var/log/aakore

and it has the file
aakore.http.proxy.cyber-desktop-service.log

In the file, it has
 
{"time":"2025-05-08T15:50:56.133+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633229,"remote_address":"127.0.0.1:55938","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:50:56.133+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633229,"remote_address":"127.0.0.1:55938","user_agent":"","auth_method":"Bearer","from":"local"}
{"time":"2025-05-08T15:50:57.134+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633239,"remote_address":"127.0.0.1:56068","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:50:57.134+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633239,"remote_address":"127.0.0.1:56068","user_agent":"","auth_method":"Bearer","from":"local"}
{"time":"2025-05-08T15:50:59.135+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633240,"remote_address":"127.0.0.1:55262","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:50:59.135+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633240,"remote_address":"127.0.0.1:55262","user_agent":"","auth_method":"Bearer","from":"local"}
{"time":"2025-05-08T15:51:03.141+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633241,"remote_address":"127.0.0.1:55272","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:51:03.141+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633241,"remote_address":"127.0.0.1:55272","user_agent":"","auth_method":"Bearer","from":"local"}
{"time":"2025-05-08T15:51:11.143+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633244,"remote_address":"127.0.0.1:45478","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:51:11.143+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633244,"remote_address":"127.0.0.1:45478","user_agent":"","auth_method":"Bearer","from":"local"}
{"time":"2025-05-08T15:51:27.144+01:00","level":"error","msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: cyber-desktop-service unit is offline","request_id":1746708037292633254,"remote_address":"127.0.0.1:56458","user_agent":"","auth_method":"Bearer","from":"local","subject":"atp-agent"}
{"time":"2025-05-08T15:51:27.144+01:00","level":"info" ,"msg":"GET /api/cyber-desktop-service/v1/getpolicystatus: proxy finished: status code 502, response {\"domain\":\"AGENT_CORE\",\"code\":\"BAD_GATEWAY\",\"debug\":{\"msg\":\"cyber-desktop-service unit is offline\"}}, content length 100","request_id":1746708037292633254,"remote_address":"127.0.0.1:56458","user_agent":"","auth_method":"Bearer","from":"local"}

Still, it just runs the installer and hangs like that. It doesn't do anything more than try to use resources to run it, but it doesn't do anything.
It isn't just the server I'm testing on. The same happens even on the new test servers I create.
 
 

      
                
                
                    
                                                    Thu, 05/08/2025 - 15:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So I install cPanel/WHM Acronis and click "Run now", which fails with (see attached text file).
I don't quite understand Acronis. It worked flawlessly when I first used it with cPanel/WHM at launch. However, over the years, I’ve encountered more and more issues. Interestingly, others don’t seem to notice as many problems. Strangely, I experience odd issues when installing or uninstalling it and backing up and restoring data. 
Having been involved in web hosting for over 15 years and considering myself quite tech-savvy, these issues are especially perplexing. Due to the ongoing problems, I eventually decided to stick with the cPanel/WHM backup system and JetBackup. Now, I transfer data to a remote server via SSH/rsync, which works without issues.
I guess Acronis isn't the right fit for me!
 
I added text file, but it doesn't show in the post afterwards. I give up lol!
Regards,  
Chris.

      
                
                
                    
                                                    Thu, 05/08/2025 - 15:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If Acronis want to check logs for the Acronis that I was using, it is WF3FE1396.

      
                
                
                    
                                                    Thu, 05/08/2025 - 15:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is the error that it shows when try to backup using cPanel/WHM plugin. I had to add log to codefile as this forum shows nginx error if I try to put the code here
https : // codefile .io /f/gqHqinW9xX
I was testing on a decent spec VPS that just hosts very low resource website and MySQL usage is very low. Server load is very low. It shows now
19:59:56 up 1 day, 3:41, 0 users, load average: 0.00, 0.00, 0.00
Also, it's just cPanel and LiteSpeed running. CloudLinux/MySQL governor is NOT running. Shouldn't be anything killing anything.
I'm running
OS
AlmaLinux v9.5.0 STANDARD kvm
cPanel Version
126.0.16
mariadb: 11.4
Server Load 0.007812 (3 CPUs)
Memory Used 41.64% (1,185,076 of 2,845,780)
Swap Used 11.54% (30,132 of 261,096)
What's odd is the Acronis protection plan used to run fine years ago when using it i.e could uninstall the Acronis backup plugin and it would also uninstall the agent from Acronis backup cloud console. Then if reinstalled the plugin and reconfigured with the same Acronis account details it would continue the backup as hostname.domain.com
Now each time you do it it keeps renaming the protection plan name i.e
hostname.domain.com
hostname.domain.com (1)
hostname.domain.com (2)
hostname.domain.com (3)
Even if you uninstall the plugin from the server and remove the Acronis directories from the server.
Acronis must have changed something in some recent versions but it acts very weird now.
You could also used to run
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
Whether Acronis was installed using cPanel/WHM plugin or even if agent was installed directly without using cPanel plugin, it would show options if you wanted to reinstall the agent but leave configurations intact or completely remove them. When running /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall, it doesn't show the screen (used to load in about 1-3 seconds). I've tried leaving it running for 15 minutes, and it doesn't do anything other than use resources to try to load it but doesn't show the screen.
I noticed the same on existing VPS/dedicated servers and new ones running different combos, i.e cPanel on its own or even full Shared/Reseller dev setup with all of the usual software installed, cPanel, CloudLinux, Imunify360 etc.
So, yeah, I don't know what Acronis changed, but it doesn't work like it used to when I first started using it many years ago.

      
                
                
                    
                                                    Fri, 05/16/2025 - 09:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Smith wrote:

This is the error that it shows when try to backup using cPanel/WHM plugin. I had to add log to codefile as this forum shows nginx error if I try to put the code here
https : // codefile .io /f/gqHqinW9xX
I was testing on a decent spec VPS that just hosts very low resource website and MySQL usage is very low. Server load is very low. It shows now
19:59:56 up 1 day, 3:41, 0 users, load average: 0.00, 0.00, 0.00
Also, it's just cPanel and LiteSpeed running. CloudLinux/MySQL governor is NOT running. Shouldn't be anything killing anything.
I'm running
OS
AlmaLinux v9.5.0 STANDARD kvm
cPanel Version
126.0.16
mariadb: 11.4
Server Load 0.007812 (3 CPUs)
Memory Used 41.64% (1,185,076 of 2,845,780)
Swap Used 11.54% (30,132 of 261,096)
What's odd is the Acronis protection plan used to run fine years ago when using it i.e could uninstall the Acronis backup plugin and it would also uninstall the agent from Acronis backup cloud console. Then if reinstalled the plugin and reconfigured with the same Acronis account details it would continue the backup as hostname.domain.com
Now each time you do it it keeps renaming the protection plan name i.e
hostname.domain.com
hostname.domain.com (1)
hostname.domain.com (2)
hostname.domain.com (3)
Even if you uninstall the plugin from the server and remove the Acronis directories from the server.
Acronis must have changed something in some recent versions but it acts very weird now.
You could also used to run
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
Whether Acronis was installed using cPanel/WHM plugin or even if agent was installed directly without using cPanel plugin, it would show options if you wanted to reinstall the agent but leave configurations intact or completely remove them. When running /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall, it doesn't show the screen (used to load in about 1-3 seconds). I've tried leaving it running for 15 minutes, and it doesn't do anything other than use resources to try to load it but doesn't show the screen.
I noticed the same on existing VPS/dedicated servers and new ones running different combos, i.e cPanel on its own or even full Shared/Reseller dev setup with all of the usual software installed, cPanel, CloudLinux, Imunify360 etc.
So, yeah, I don't know what Acronis changed, but it doesn't work like it used to when I first started using it many years ago.


Hello Chris,
The Acronis Cyber Protect Cloud agent and the plugin integration agent are separate components — they serve different purposes and are not directly connected. We do not manage third-party platforms like cPanel, and there has never been a direct integration between them. Uninstalling one will not uninstall the other.
As mentioned above, a proper investigation is required. You should contact your MSP so they can open a support ticket with us. This is essential for us to analyze the issue in detail, especially when third-party tools are involved. Unfortunately, it’s not possible to resolve such cases via the forum.
Best regards.

      
                
                
                    
                                                    Fri, 05/16/2025 - 12:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
