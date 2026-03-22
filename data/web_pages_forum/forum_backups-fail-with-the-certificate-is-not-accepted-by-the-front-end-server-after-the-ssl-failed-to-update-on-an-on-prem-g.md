# Backups Fail with "The certificate is not accepted by the front-end server." after the SSL failed to update on an on-prem GW

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backups-fail-certificate-not-accepted-front-end-server-after-ssl

## Original Post
**Author:** Unknown

Backups Fail with "The certificate is not accepted by the front-end server." after the SSL failed to update on an on-prem GW

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    RB
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello everyone,
We ran into an intresting problem that I am thinking others may have seen.  
We use Acronis Cloud backup via Kaseya and it sounds like we have a unique situation.  
A month ago, I built two gateway servers.  These servers have been working great, until two days ago, which was exactly a month after they were built.  
The problem we ran into is defined here - https://kb.acronis.com/content/57417
The work-around updated the dates on the SSL certs and looked like we were back in business, nope.  All backups on the on two servers fail.  
 
I ran a re-registration of the clients to see if this helped, nope. 
I ran a port connection test - all good.  
 
Here is the latest log for one of the machines (all 130 others are similar)- 
Error
DATE AND TIME
Apr 27, 2017, 11:03:11 PM
MODULE
309
MESSAGE

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"service_process_vsa64_3917","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"gtob_backup_command_addon_vsa64_3917","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 212
Module: 161
LineInfo: 0x0B320396ADFE3EA3
Fields: {"$module":"disk_bundle_vsa64_3917","IsReturnCode":"1"}
Message: Failed to find archive 'redacted'.
------------------------
Error code: 16
Module: 515
LineInfo: 0xDF3CBAD70699540B
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Failed to renew certificate, reason is "server doesn't trust our certificate (unknown ca)"
------------------------
Error code: 3
Module: 625
LineInfo: 0x6592A83AA4AE5D21
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: The certificate is not accepted by the front-end server. The server address has been probably changed. Please retry the operation.
 
 
Has anyone worked through this with Gateway servers before?  Any tips as to what to check into?
Thank you!
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/28/2017 - 13:38

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello RB,
 
My name is Evgeny, I am from Acronis Service Providers Support.
As far as I understand you have faced two issues with backups of some VMs by Acronis Backup Cloud v6.1. 
I will be glad to assist you!
Unfortunately you have not provided your backup account, so I am unable to check the errors from the console and download the system report from the affected Agent machine. The exact cause needs to be narrowed down first.
In order to investigate root cause of the issue, please send an email at mspsupport@acronis.com while providing the account name, the Customer's company name and the affected server. 
A new ticket will be generated and we will take over to assist you further. 
 
Warm Regards,
Evgeny Ryuntyu
Senior Support Specialist – Service Provider Support team | Acronis
Office: +1 781 79 14 486

      
                
                
                    
                                                    Fri, 04/28/2017 - 15:34
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RB
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sure thing!  Emailing now. 
 
 

      
                
                
                    
                                                    Fri, 04/28/2017 - 15:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RB
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So I have continued troubleshooting and have done the following - 
Existing agent that fails - 
Rebooted servers
Checked connectivity
Reregister
Rebooted client/agent
 Same errors.  Cannot trust the certs
 
On a new client that has never had Backup - 
Installed.  No errors
Re-registered.  Probably did not need to but I wanted to verify.
Machine shows up in Acronis portal
Attempt to schedule a simple backup of one file
Fails due to the same cert errors.

 
It seems like there should be a method/process/script/manual procedure to ensure the certs in use on the server are what is expected by the agent and vise versa, but I am not familar enough with the inner workings of the SSL configs on either side.  
Has anyone else worked through rebuilding the certs between the clients and the servers?  

      
                
                
                    
                                                    Mon, 05/01/2017 - 14:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Reto Bättig
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello 
Same error here on two different servers. Both Centos 7 and both are Acronis Gateway Servers on which we store some data.
We had this error last week at one of the servers. I wasnt able to fix the error. I registered and rebooted the server multiple times, but the error message still apears. One day later the error disappeared - I dont knew why. 
Today i installed a new client, which stores his data on the second server. When i wanna access the cloud storage i get the same error message "he certificate is not accepted by the front-end server". Then i again registred the Server againt and rebooted the device. The error still apears...
Already an edit while im writing this: 10 minutes later the error message doesent apper anymore. I think maybe you can really "fix" the error when you register the Gateway Server new. But after this it always need some time..
 

      
                
                
                    
                                                    Wed, 05/10/2017 - 08:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RB
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            By chance, did your servers just turn 1 month old since install?  Our cert after install was for a month.  After re-reg, it looks like it is good for a year.  I added chron jobs to re-run the command again in 11 months and then every 12 months after that to avoid the failed ssl update in the future.
 
I was able to re-register the servers again, but with the port specified to the port we are using.  We use two different ports for incoming servers to share the IP/bandwidth of our primary connection so this created some confustion with the re-register command.  
 
Also learned that the variables the command needs are directly tied to the storage config at baas.acronis.com so make sure the command has the right url:port, user name, and UID for the storage.  
 
On top of this, I was told by Acronis Support that the gateway servers are basically EOL and we should move to their on-prem cloud with Acronis Storage 2.0.   I have built this in a test env, but the overhead of the needed number of machines can be daunting for a small shop.  

      
                
                
                    
                                                    Wed, 05/10/2017 - 13:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RB
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Two more things I needed to do -
On the client, I scrioted a deletion of the "default" folder where the cert is instaled.  
Then we scripted re-registering the clients.  The "Default" folder was rebuilt automatically when re-registering the clients.
I am not 100% sure if this was needed, but it seemed to help.
 

      
                
                
                    
                                                    Wed, 05/10/2017 - 13:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Net Admins
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            did you fix the problem finally? I've tried to reinstall and rebuild the gateway server using the same dataset and same serverid, but it still popped up the same 3917 error.
 
The certificate is not accepted by the front-end server. The server address has been probably changed. Please retry the operation.
DATE AND TIMEJul 24, 2017, 10:54:09 AM
CODE0x015B0010+0x00A100C9+0x02030010+0x02710003
MODULE347
MESSAGEFailed to access the backups.
Additional info:------------------------
Error code: 16
Module: 347
LineInfo: 0xDC03ECC21410E659
Fields: {"$module":"dms_provider_vsa64_3917"}
Message: Failed to access the backups.
------------------------
Error code: 201
Module: 161
LineInfo: 0x0B320396ADFE4224
Fields: {"$module":"disk_bundle_vsa64_3917","IsReturnCode":"1"}
Message: Failed to get information about the archives.
------------------------
Error code: 16
Module: 515
LineInfo: 0xDF3CBAD70699540B
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Failed to renew certificate, reason is "server doesn't trust our certificate (unknown ca)"
------------------------
Error code: 3
Module: 625
LineInfo: 0x6592A83AA4AE5D21
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: The certificate is not accepted by the front-end server. The server address has been probably changed. Please retry the operation.

      
                
                
                    
                                                    Mon, 07/24/2017 - 03:08
