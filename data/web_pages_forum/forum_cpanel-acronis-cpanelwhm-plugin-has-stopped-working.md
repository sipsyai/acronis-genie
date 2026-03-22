# cPanel Acronis cPanel/WHM plugin has stopped working

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cpanel-acronis-cpanelwhm-plugin-has-stopped-working

## Original Post
**Author:** Unknown

cPanel Acronis cPanel/WHM plugin has stopped working

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            It seems someone has broken something because backup and restores within the plugin have stopped working.
 
This happens on v.12.5.22750 and the new version v.12.5.22530.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/10/2020 - 16:00

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok backup started to work but if try to export a cPanel account get
 
"Failed: Archive accounts: <snipped>"

      
                
                
                    
                                                    Wed, 06/10/2020 - 16:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Error is like this
 
{
    "Command": "chroot /var/lib/Acronis/mount/1f1fe57f_0_1591805594_41 bash -c '/usr/local/cpanel/scripts/pkgacct --skiphomedir --skipdnszones --skipacctdb snipped /root/acronis_cpanel_accounts'",
    "Error": "",
    "Output": "[2020-06-10 20:05:44 +0100] pkgacct started.\n[2020-06-10 20:05:45 +0100] pkgacct version 10 - user : snipped - tarball: 1 - target mysql : default - split: 0 - incremental: 0 - homedir: 0 - mailman: 1 - backup: 0 - archive version: 4 - running with uid 0\n[2020-06-10 20:05:45 +0100] pkgacct using '/usr/local/cpanel/3rdparty/bin/pigz -6 --processes 1 --blocksize 4096 --rsyncable' to compress archives\n[2020-06-10 20:05:45 +0100] pkgacct working dir : /root/acronis_cpanel_accounts/cpmove-snipped\n[2020-06-10 20:05:45 +0100] Copying Reseller Config...[2020-06-10 20:05:45 +0100] Done\n[2020-06-10 20:05:45 +0100] Copying Suspension Info (if needed)...[2020-06-10 20:05:45 +0100] Done\n[2020-06-10 20:05:45 +0100] Copying installed SSL certificates and keys...[2020-06-10 20:05:45 +0100] Performing \u201cApacheTLS\u201d component....\n[2020-06-10 20:05:45 +0100] Completed \u201cApacheTLS\u201d component.\n[2020-06-10 20:05:45 +0100] Done\n[2020-06-10 20:05:45 +0100] Copying Domain Keys....[2020-06-10 20:05:46 +0100] Done\n[2020-06-10 20:05:46 +0100] Copying Bandwidth Data....[2020-06-10 20:05:46 +0100] Performing \u201cBandwidth\u201d component....\nSummary databases \u2026 done!\n[2020-06-10 20:05:48 +0100] Completed \u201cBandwidth\u201d component.\n[2020-06-10 20:05:48 +0100] Done\n[2020-06-10 20:05:48 +0100] Copying Mail files....[2020-06-10 20:05:48 +0100] Done\n[2020-06-10 20:05:48 +0100] Copying proftpd file....[2020-06-10 20:05:48 +0100] Done\n[2020-06-10 20:05:48 +0100] Performing \u201cLogs\u201d component....\n...log file sizes [36221 byte(s)]......snipped.org-ssl_log......snipped.org-bytes_log......snipped.org...[2020-06-10 20:05:49 +0100] Completed \u201cLogs\u201d component.\n[2020-06-10 20:05:49 +0100] Copy userdata...[2020-06-10 20:05:49 +0100] Done\n[2020-06-10 20:05:49 +0100] Copy custom virtualhost templates...[2020-06-10 20:05:49 +0100] Done\n[2020-06-10 20:05:49 +0100] Copying mailman lists and archives....Done copying mailman lists and archives.\n[2020-06-10 20:05:50 +0100] Performing \u201cCpUserFile\u201d component....\n[2020-06-10 20:05:50 +0100] Completed \u201cCpUserFile\u201d component.\n[2020-06-10 20:05:50 +0100] Copying crontab file.......[2020-06-10 20:05:50 +0100] Done\n[2020-06-10 20:05:50 +0100] Performing \u201cQuota\u201d component....\n[2020-06-10 20:05:50 +0100] Completed \u201cQuota\u201d component.\n[2020-06-10 20:05:50 +0100] Performing \u201cIntegration\u201d component....\n[2020-06-10 20:05:50 +0100] Completed \u201cIntegration\u201d component.\n[2020-06-10 20:05:50 +0100] Performing \u201cAuthnLinks\u201d component....\n[2020-06-10 20:05:50 +0100] Completed \u201cAuthnLinks\u201d component.\n[2020-06-10 20:05:50 +0100] Performing \u201cAPITokens\u201d component....\n[2020-06-10 20:05:50 +0100] Completed \u201cAPITokens\u201d component.\n[2020-06-10 20:05:50 +0100] Performing \u201cDNSSEC\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cDNSSEC\u201d component.\n[2020-06-10 20:05:51 +0100] Performing \u201cCustom\u201d component....\n[2020-06-10 20:05:51 +0100] No custom components to perform.\n[2020-06-10 20:05:51 +0100] Completed \u201cCustom\u201d component.\n[2020-06-10 20:05:51 +0100] Performing \u201cAutoSSL\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cAutoSSL\u201d component.\n[2020-06-10 20:05:51 +0100] Storing Subdomains....\n[2020-06-10 20:05:51 +0100] Done\n[2020-06-10 20:05:51 +0100] Storing Parked Domains....\n[2020-06-10 20:05:51 +0100] Done\n[2020-06-10 20:05:51 +0100] Storing Addon Domains....\n[2020-06-10 20:05:51 +0100] Performing \u201cPassword\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cPassword\u201d component.\n[2020-06-10 20:05:51 +0100] Performing \u201cDigestShadow\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cDigestShadow\u201d component.\n[2020-06-10 20:05:51 +0100] Copying shell.......[2020-06-10 20:05:51 +0100] Done\n[2020-06-10 20:05:51 +0100] Performing \u201cPublicContact\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cPublicContact\u201d component.\n[2020-06-10 20:05:51 +0100] Performing \u201cMailLimits\u201d component....\n[2020-06-10 20:05:51 +0100] Completed \u201cMailLimits\u201d component.\n[2020-06-10 20:05:51 +0100] Performing \u201cLinkedNodes\u201d component....\n[2020-06-10 20:05:53 +0100] Completed \u201cLinkedNodes\u201d component.\n[2020-06-10 20:05:53 +0100] Creating Archive ....[2020-06-10 20:05:53 +0100] Done\n[2020-06-10 20:05:53 +0100] pkgacctfile is: /root/acronis_cpanel_accounts/cpmove-snipped.tar.gz\n[2020-06-10 20:05:53 +0100] md5sum is: 4e1e5e63d3eca817805505b87efccd79\n[2020-06-10 20:05:53 +0100] \n[2020-06-10 20:05:53 +0100] size is: 155296\n[2020-06-10 20:05:54 +0100] Error while connecting to MySQL: (XID jrnw8w) The system failed to connect to the \u201cMySQL\u201d database \u201cmysql\u201d because of an error: CR_CONNECTION_ERROR (Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (111)) at /usr/local/cpanel/Cpanel/Mysql/Basic.pm line 437."
}


      
                
                
                    
                                                    Wed, 06/10/2020 - 19:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for reaching Acronis Support on Forum. I will be happy to help sharing below solution.

Please, do the folowing:
1. Open /usr/local/cpanel/base/3rdparty/acronisbackup/python/site-packages/acronis_backup_srv/async_tasks/executors/cpanel.py
2. Find line 146: self._makedirs(path=rp_accounts_backup_tmp_dir, mode=0o600)
3. Right after it insert the following peace of code:


        dev_null = rp_root_dir + '/dev/null'
        try:
            os.mknod(dev_null)
            self.log_info("File /dev/null created.")
        except OSError as e:
            self.log_warning("Unable to create /dev/null in backup folder {}.".format(e))


4. Restart python service: /usr/local/cpanel/base/3rdparty/acronisbackup/scripts/acronis-backup-srv.sh restart
5. Check if the service is started correctly:
tail -f /usr/local/cpanel/base/3rdparty/acronisbackup/log/scripts/acronis-backup-srv.log
or
tail -f /usr/local/cpanel/base/3rdparty/acronisbackup/srv/log/main.log
6. Retry download operation and check if dbs is present.
Hope this helps.


      
                
                
                    
                                                    Tue, 06/16/2020 - 09:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ivaylo,
 
Thanks for providing the fix, but instead of me applying this to every server, I'd rather wait until you add it officially. Any idea when this will be updated? Do we need to update the agent or reinstall the cPanel Acronis plugin?
 
Thanks,
Chris

      
                
                
                    
                                                    Tue, 06/16/2020 - 09:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
Thank you for you reply.
Which version of cPanel's Acronis plugin are you currently with? This workaround should be included into bugfix release of cPanel's Acronis plugin 1.4 build 312. We released earlier this month version 1.4.
Thank you.

      
                
                
                    
                                                    Tue, 06/16/2020 - 22:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ivaylo Tsvetkov wrote:

Hello Chris,
Thank you for you reply.
Which version of cPanel's Acronis plugin are you currently with? This workaround should be included into bugfix release of cPanel's Acronis plugin 1.4 build 312. We released earlier this month version 1.4.
Thank you.


For me, it shows
 
Version 1.4.320 so guess a later version 

      
                
                
                    
                                                    Wed, 06/17/2020 - 10:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
In this case we should forward this reappearing issue to RnD Support, but normal workflow requires opening an Acronis Support case so we can escalate to RnD. Please open a new Support case, provide your Acronis account login and DC, share the same description, the version and complete set of plugin logs: https://kb.acronis.com/content/61940
The Download logs button is available in Acronis Backup plugin dashboards like shown in the images on the KB article.
In order to get a fix RnD should investigate your case scenario and find new root cause of this issue.
And additionally I need to ask, have you tried the suggested workaround at least on one server, does is still helps fixing this issue, it will be useful to share results with RnD in case it is not working on the latest version.
Thank you.

      
                
                
                    
                                                    Wed, 06/17/2020 - 13:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I found the issue I was describing
Hi,
I found the problem. Archive/Restore full cPanel account does not work if there are no MySQL database/users in the cPanel account i.e if the cPanel account is only hosting an HTML website with no MySQL database then the Archive/Restore will fail.
Archive/Restore works fine for all sites that use MySQL DBs.
Kind regards,
Chris

I let Acronis support team know about it. So hopefully they can fix it.

      
                
                
                    
                                                    Wed, 06/24/2020 - 19:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ps because of the above issue, I'm now running Acronis/JetBackup side-by-side. Just to be sure. Cost an extra $40-50/month to run but worth it.

      
                
                
                    
                                                    Wed, 06/24/2020 - 19:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maksim Emelianov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey, HostXNow, was you able to resolve the problem?

      
                
                
                    
                                                    Fri, 02/12/2021 - 07:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Abdul-Aziz Arnold
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
I experienced the exact same issue. And this is what occurred and how I fixed it.
A customer's account was terminated and we had to restore the whole account from WHM plugin of Acronis
When we selected and clicked Recover it went through but failed due to the same error above.
The steps to solve this was the following.
1. Restore the whole account excluding the abs by selecting the option: skip databases
2. Once done as it successfully completed we logged into the cPanel account of this restored account and used the Acronis cPanel plugin to restore the databases which funny enough worked.
I decided to try this technique a few times by terminating our test accounts and retry and every time the same occurrence and the same solution as described above seemed to work.
Very strange but at least we have a workaround for now without editing any code.
Note we are on the latest Acronis agent version as of today.  Just FYI.

      
                
                
                    
                                                    Sat, 11/13/2021 - 11:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best Web Hosting Provider in South Africa - cPanel, Plesk and Acronis

Wordpress Hosting - Website Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Abdul-Aziz Arnold thank you for taking the time to share your experience with the community! 

      
                
                
                    
                                                    Tue, 11/16/2021 - 08:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
