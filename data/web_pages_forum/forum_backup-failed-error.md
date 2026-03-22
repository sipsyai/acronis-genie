# Backup failed error

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-failed-error

## Original Post
**Author:** Unknown

Backup failed error

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Amir Gh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I habe a problem with Acronis cloud.
In Brief, add a storage to Acronis console through Acronis Gateway and now I'm trying to backup office 365 or a file for test, but I get a error as you can see below.
Could you please direct me, how can to fix it?
Code
0x01350016+0x01350016+0x026F0067+0x00A100D4+0x02710001+0x02720136+0x02720133
Module
309
Message
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_3917"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_3917"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 103
Module: 623
LineInfo: 0x94F5F955B13DDE83
Fields: {"IsReturnCode":"1","$module":"arx_agent_fork_vsa64_3917"}
Message: A generic error of Microsoft Exchange backup component.
------------------------
Error code: 212
Module: 161
LineInfo: 0x0B320396ADFE3EA3
Fields: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_3917"}
Message: Failed to find archive 'xx@yy.com_mailbox_C0649180-EA04-4D22-9FF6-3EA4FA1DB4BDA'.
------------------------
Error code: 1
Module: 625
LineInfo: 0x6592A83AA4AE5CDD
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Failed to discover the front-end server that serves your account.
------------------------
Error code: 310
Module: 626
LineInfo: 0x16ACA2F42BFBE33A
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: The certification server is unavailable.
------------------------
Error code: 307
Module: 626
LineInfo: 0x50E61E3E2E723B45
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Internal error: Registration server call has failed with the following error: 'The certificate authority is not found.'.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 03/06/2017 - 21:37

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Amir!
 
Thanks for contacting Acronis Support.
My name is Evgeny, I am from Acronis Service Providers Support.
As far as I understand you have configured the Acronis Storage gateway and the backups of Office 365 mailbox fails with an error related to the registration server.
The issue is not wide-spread, so we will need to investigate the root cause.
I have created a support ticket for you and involved the DCO team to resolve this.
The ticket number is 02933642 for your reference.
Will get back to you within the ticket to work on the issue.
Warm regards,
Evgeny Ryuntyu
Acronis Service Providers Support

      
                
                
                    
                                                    Thu, 03/09/2017 - 15:25
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ian Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Has this problem been fixed yet??
I have the same issue I think.

      
                
                
                    
                                                    Tue, 03/28/2017 - 15:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    William Osterberg
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
I have been using True Image 2017 to back up some files to Cloud successfully for a few months now.  However, recent weekly backups have now failed and there appears to be a problem with connecting to the designated IP address:  185.151.160.38   I simply get a message that the backup failed and I could not connect.  I know of no change to my laptop that might explain this.  Note I have just now updated my version of True Image.
Any help would be appreciated.
William
 
 

      
                
                
                    
                                                    Wed, 03/29/2017 - 21:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Ian and William, 
Thank you for your postings! This particular forum is for a Cloud-based business solution named Acronis Backup Cloud. Please open a new topic in the Acronis True Image 2017 Forum if you want to try to persue this further with the user community, but you would be best advised to open a Support Case directly with Acronis Support for this issue given that it's related to Cloud storage and only Acronis support can check the status of your cloud account.
Thank you, 

      
                
                
                    
                                                    Mon, 04/03/2017 - 12:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris H
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Error code 0x01350016+0x01350016+0x00A100D4+0x0040002E+0x0004000F
I receive the above Error when trying to back up my AD Server. Out of 18 Servers this is the only one with this issue. I have tried setting the backup location to the IP Address and that results in the same error. Logon information for the folder location is corrcet since all other servers backing up to this same location have no issue. Log file can be provided to Support if needed but CANNOT be posted due to confidentiality.
Additional info: (IP, User and Server Information was Redacted)
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
Message: Failed to find archive 'XXXX-AD.XX.XXXXX.org-FFE6A3BF-CC32-4CF6-93C9-875A961930F0-54803CB9-9CAC-4B2F-A312-538A03ED30BFA'.
------------------------
Error code: 46
Module: 64
LineInfo: 0x97675718D2B52D1F
Fields: {"user":"ad\\XXXXXX","$module":"disk_bundle_vsa64_3917","path":"\\\\172.xxx.xxx.xxx\\backup\\"}
Message: Failed to open the backup location.
------------------------
Error code: 15
Module: 4
LineInfo: 0xF35F747B3B21FAA5
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Canceled.

      
                
                
                    
                                                    Tue, 04/11/2017 - 22:45
