# Issue with WHMCS module after upgrading to v2.2.0-175

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/issue-whmcs-module-after-upgrading-v220-175

## Original Post
**Author:** Unknown

Issue with WHMCS module after upgrading to v2.2.0-175

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
Has anyone whose using the Acronis Cyber Cloud WHMCS module upgraded to v2.2.0-175?
I upgraded the module yesterday (I'm running WHMCS 7.10.2) and right after replacing the files, I started receiving a cron email every 5 minutes as shown below:

Console Tool

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  help                    Displays help for a command
  list                    Lists commands
 usage-report
  usage-report:erase      Command for usage reports erasing, keeping only reports for last "2" days.
  usage-report:flushall   Command for usage report flushing.
  usage-report:master     Usage report aggregation master command.
  usage-report:metrics    Command for metrics fetching.
  usage-report:process    Command for usage report processing.
  usage-report:view-list  Command for usage report listing.
X-Powered-By: PHP/7.3.23
Content-Type: text/html; charset=utf-8
Set-Cookie: WHMCS5tRbx3LY=f513f0e5d2f6xa5982; path=/; secure; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache

Console Tool

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  help                    Displays help for a command
  list                    Lists commands
 usage-report
  usage-report:erase      Command for usage reports erasing, keeping only reports for last "2" days.
  usage-report:flushall   Command for usage report flushing.
  usage-report:master     Usage report aggregation master command.
  usage-report:metrics    Command for metrics fetching.
  usage-report:process    Command for usage report processing.
  usage-report:view-list  Command for usage report listing.
X-Powered-By: PHP/7.3.23
Content-Type: text/html; charset=utf-8
Set-Cookie: WHMCS5tRx3LY=bbb53eb78xb66153; path=/; secure; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache

Thanks,
George

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/20/2020 - 07:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello George,
I checked with our WHMCS module's Dev and I can see he replied to you on this topic to same post on GitHub. Link to post: https://github.com/acronis/acronis-cyber-cloud-whmcs/issues/4#issuecomm…
Our Devs are aware of this issue already and they will be looking into it to find the root cause and proper solution. Please, feel free to reply on your comments with our Dev in GitHub. I can post here the final solution when we have it.
Thank you!

      
                
                
                    
                                                    Tue, 10/20/2020 - 12:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you, indeed Martin got back to me via Github. For now we've disabled the cron jobs until there's a fix for this issue.

      
                
                
                    
                                                    Tue, 10/20/2020 - 14:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey George,
I was thinking about whether there was a new update of the plugin because I was waiting for them to readd the auto-login button back so admin can log in to customer account automatically from within WHMCS. Saves the hassle of having to enter their username and password manually.
Also, because they removed that auto-login I'm no longer able to set up the account on customers behalf. Instead, I have to wait for the customer to activate the account using the activation link that is sent to the customers' email, and then the customer has to provide ME with the login details. That's not that good for providers who offer managed Acronis Backups.
Anyway, you saved me the hassle of upgrading and having this annoying bug I'm sure.
Hopefully, they can get it fixed for you asap.

      
                
                
                    
                                                    Wed, 10/21/2020 - 05:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Posting cron jobs emails issue's temporary solution.
Temporarily disable the daily usage fetching cron jobs in file [whmcs_path]/includes/hooks/acroniscloud.php and comment the two cron job hooks:
$hooks = [
    'ServerAdd',
    'ServerDelete',
    'ServerEdit',
    'ClientEdit',
    'ProductEdit',
    'ServiceDelete',
    'AdminAreaHeaderOutput',
    'ClientAreaHeaderOutput',
    'OrderProductUpgradeOverride',
    'AfterModuleChangePackageFailed',
//    'AfterCronJob',
//    'DailyCronJob'
];
We will further investigate this issue, as the feature shouldn't be running in case of usage report is being disabled.

      
                
                
                    
                                                    Wed, 10/21/2020 - 09:06
                                                                            
                                
                            
                                            
                                            
    
                    
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
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello HostXNow,
Latest module version is v2.2.0-175, it can be downloaded from WHMCS Marketplace:https://marketplace.whmcs.com/product/1246-acronis-cyber-cloud
Auto-login from Client area to Acronis Cyber Cloud console is not yet supported.
It was previously disabled/removed for Security reasons, and not yet approved to be implemented back.
You may find reference into our product manual under "10 Known issues and limitations" chapter: https://download.acronis.com/pdf/WHMCS_Integration_Manual_en-US.pdf
Thank you.

      
                
                
                    
                                                    Wed, 10/21/2020 - 09:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            HostXNow wrote:

Also, because they removed that auto-login I'm no longer able to set up the account on customers behalf. Instead, I have to wait for the customer to activate the account using the activation link that is sent to the customers' email, and then the customer has to provide ME with the login details. That's not that good for providers who offer managed Acronis Backups.


This is still possible but requires a small change in the config.yaml file: https://kb.acronis.com/content/63533

      
                
                
                    
                                                    Wed, 10/21/2020 - 09:35
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you @Ivaylo Tsvetkov and @George_Fusioned.

      
                
                
                    
                                                    Wed, 10/21/2020 - 15:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
