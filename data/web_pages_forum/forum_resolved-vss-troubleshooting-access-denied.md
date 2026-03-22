# [Resolved] VSS troubleshooting - Access Denied

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-vss-troubleshooting-access-denied

## Original Post
**Author:** Unknown

[Resolved] VSS troubleshooting - Access Denied

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello everyone,
 
I am having a problem with the backup of a Windows 2016 Standard server, the backup is completed but always displays alert with the error VSS troubleshooting Access Denied, does anyone know how I can resolve the case?
Below is the activity log:
2018-08-16T22:00:07:205-03:00 9044 I0135003A: User is running command. Command=Backup plan 'Arquivos'; User=; clientProfileID=; clientSessionID=5E5EB6CB-DB67-49E2-9AB0-11CF40017004
2018-08-16T22:00:40:094-03:00 10060 I0135003A: User is running command. Command=Backing up; User=; clientProfileID=; clientSessionID=5E5EB6CB-DB67-49E2-9AB0-11CF40017004
2018-08-16T22:00:40:290-03:00 10060 I00000000: I00000000: Backup Inclusions list:
2018-08-16T22:00:40:301-03:00 10060 I00000000: I00000000: autobackup
2018-08-16T22:00:40:313-03:00 10060 I00000000: I00000000: Gravacoes
2018-08-16T22:00:40:325-03:00 10060 I00000000: I00000000: arquivos
2018-08-16T22:00:40:347-03:00 10060 I00000000: I00000000: Archive: avfs:/online?account%3dinsidesign_dc%26provider%3dAcronis\dc.insidesigntelecom.com.br-E8AF0ADE-D990-4430-B454-57B71E35D31B-F6D29950-A27C-4C7B-9089-00EDF82D5972A
2018-08-16T22:00:41:176-03:00 10060 I00000000: Proxy setting: Enabled = 0, Host = '', port = 8080, user =
2018-08-16T22:00:41:455-03:00 10060 I00000000: I00000000: Using SecurePersistentCredentialStore.
2018-08-16T22:00:43:748-03:00 10060 I00000000: AccountID: insidesign_dc
2018-08-16T22:00:43:759-03:00 10060 I00000000: SubaccountID: 1
2018-08-16T22:00:43:771-03:00 10060 I00000000: DataStore: cluster01.insidesign.com.br
2018-08-16T22:00:44:776-03:00 10060 I00000000: Create Incremental Backup From C:\Users\administrator.INTERNO\Ubiquiti UniFi\data\backup\autobackup\...To file avfs:/online?account%3dinsidesign_dc%26computer%3d1%26provider%3dAcronis%26stream%3ddc.insidesigntelecom.com.br-E8AF0ADE-D990-4430-B454-57B71E35D31B-F6D29950-A27C-4C7B-9089-00EDF82D5972A.tibxCompression NormalExclude Files matching maskMatch criterion *&#92;System Volume Information&#92;*{3808876B-C176-4e48-B7AE-04046E6CC752}, Ask for the first media No
2018-08-16T22:01:06:581-03:00 10060 I000101FA: Locking partition C:...
2018-08-16T22:02:35:340-03:00 2876 I0135003A: User is running command. Command=VSS troubleshooting; User=; clientProfileID=; clientSessionID=5E5EB6CB-DB67-49E2-9AB0-11CF40017004
2018-08-16T22:04:16:969-03:00 10060 E00950505: Error 0x950505: An attempt to fix VSS errors has failed.
| trace level: error
| channel: tol-activity#8060457A-9A65-47E6-BDF3-7AA8A6407734
| line: 0xd0e6a7e799674295
| file: e:\235\enterprise\disk_manager\daapi1\vss_retryable_callbacker.cpp:192
| function: `anonymous-namespace'::VssCallbackStateKeeper::RunVssTroubleshooting
| $module: disk_bundle_vsa64_10330
|
| error 0x1350016: TOL: Failed to execute the command. VSS troubleshooting
| line: 0x8d165e86fb81959b
| file: e:\235\enterprise\common\tol\command\command.cpp:461
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: 401DF916-8256-400D-88C7-0786EFFA51BB
| $module: service_process_vsa64_10330
|
| error 0x1350016: TOL: Failed to execute the command. VSS troubleshooting
| line: 0x8d165e86fb81959b
| file: e:\235\enterprise\common\tol\command\command.cpp:461
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: 401DF916-8256-400D-88C7-0786EFFA51BB
| $module: disk_bundle_vsa64_10330
|
| error 0x11e000d: VSS troubleshooting failed.
| line: 0xa3507cb45b091f97
| file: e:\235\enterprise\mms\commands\analyze_vss\impl\analyze_vss_command_impl.cpp:244
| function: `anonymous-namespace'::VssAnalyzerImpl::Analyze
| $module: disk_bundle_vsa64_10330
|
| error 0x11e000d: Failed to stop service 'Cryptographic Services'.
| line: 0xa3507cb45b091fb2
| file: e:\235\enterprise\mms\commands\analyze_vss\impl\analyze_vss_command_impl.cpp:271
| function: `anonymous-namespace'::VssAnalyzerImpl::RestartServices
| $module: disk_bundle_vsa64_10330
|
| error 0xfff0: Access is denied
| line: 0xbd28fdbd64edb8f1
| file: e:\235\core\common\error.cpp:307
| function: Common::Error::AddWindowsError
| code: 0x80070005
| $module: disk_bundle_vsa64_10330
2018-08-16T22:04:16:829-03:00 2876 E0135003D: Error 0x135003d: Command has failed. Command=VSS troubleshooting;
| trace level: error
| channel: tol-activity#EEC82996-0B0E-4EF4-85AE-E41001E76A17
| line: 0x4a8728dc8a1c9583
| file: e:\235\enterprise\common\tol\gating_activity.cpp:221
| function: Tol::`anonymous-namespace'::BusinessActivityTracker::OnCompleted
| $module: service_process_vsa64_10330
|
| error 0x1350016: TOL: Failed to execute the command. VSS troubleshooting
| line: 0x8d165e86fb81959b
| file: e:\235\enterprise\common\tol\command\command.cpp:461
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: 401DF916-8256-400D-88C7-0786EFFA51BB
| $module: service_process_vsa64_10330
|
| error 0x1350016: TOL: Failed to execute the command. VSS troubleshooting
| line: 0x8d165e86fb81959b
| file: e:\235\enterprise\common\tol\command\command.cpp:461
| function: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: 401DF916-8256-400D-88C7-0786EFFA51BB
| $module: disk_bundle_vsa64_10330
|
| error 0x11e000d: VSS troubleshooting failed.
| line: 0xa3507cb45b091f97
| file: e:\235\enterprise\mms\commands\analyze_vss\impl\analyze_vss_command_impl.cpp:244
| function: `anonymous-namespace'::VssAnalyzerImpl::Analyze
| $module: disk_bundle_vsa64_10330
|
| error 0x11e000d: Failed to stop service 'Cryptographic Services'.
| line: 0xa3507cb45b091fb2
| file: e:\235\enterprise\mms\commands\analyze_vss\impl\analyze_vss_command_impl.cpp:271
| function: `anonymous-namespace'::VssAnalyzerImpl::RestartServices
| $module: disk_bundle_vsa64_10330
|
| error 0xfff0: Access is denied
| line: 0xbd28fdbd64edb8f1
| file: e:\235\core\common\error.cpp:307
| function: Common::Error::AddWindowsError
| code: 0x80070005
| $module: disk_bundle_vsa64_10330
2018-08-16T22:04:17:018-03:00 10060 I0017001A: Error 0x17001a: Failed to create a snapshot for backup.
| trace level: information
| channel: tol-activity#8060457A-9A65-47E6-BDF3-7AA8A6407734
| line: 0x616ad0806a6302f1
| file: e:\235\archive\sel_dir.cpp:1510
| function: Seldir::SelectedDir::MakeSnapshot
| Path: C:\
| $module: disk_bundle_vsa64_10330
2018-08-16T22:04:33:059-03:00 10060 I000101FA: Locking partition C:...
2018-08-16T22:05:25:396-03:00 10060 I000101FA: Locking partition D:...
2018-08-16T22:35:13:588-03:00 10060 I0135003B: Command has completed successfully. Command=Backing up;
2018-08-16T22:35:47:445-03:00 13336 I0135003A: User is running command. Command=Applying retention rules; User=; clientProfileID=; clientSessionID=5E5EB6CB-DB67-49E2-9AB0-11CF40017004
2018-08-16T22:35:48:726-03:00 13336 I00400000: Backup deletion has started.
2018-08-16T22:35:50:611-03:00 13336 I00400000: Backup deletion has successfully completed.
2018-08-16T22:35:50:667-03:00 13336 I0135003B: Command has completed successfully. Command=Applying retention rules;
2018-08-16T22:35:52:714-03:00 9044 I0135003B: Command has completed successfully. Command=Backup plan 'Arquivos';
 

Can anybody help me?
 
 
thanks

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/17/2018 - 11:55

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi tvieira
I would recommend that you start off with using the Acronis vss Doctor which you can download from here:
https://www.acronis.com/ja-jp/personal/vss-diagnostic-free-tool/
The tool will help you to identify possible vss related issues and remediate them.
Regards
 

      
                
                
                    
                                                    Fri, 08/17/2018 - 13:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @Jays, thanks for the reply
 
I am putting the images of the errors that the tool showed.
 
Can you help me how can I solve it?
 
thanks

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      458137-150970.png

                      136.99 KB
                  
              
                      458137-150973.png

                      168.91 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 08/17/2018 - 14:04
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi tvieira
Unfortunately there is not much you can do regarding disk IO besides adding additional resources to the machine.
What I would suggest you do is as follows:
1. For testing purposes disable VSS aware backup and run the backup again, if the backup is successful but with a warning of non time consistent VSS snapshot ( Or similar warning) then proceed to step 2 but if the backup fails please send me the backup activity log
*To disable VSS: Backup Management Console > Select the machine you are having issues with > Backups > Backup options > Volume Shadow Copy Service = OFF
2. Schedule the backup for a time which the machine will not be busy (For example after work hours or before work hours)
Then lastly if non of the above works please check what backup format your backup is using:
Backups > Backup options > Backup Format
If the backup is set to Automatic selection this can mean that you are using an old backup format, to check this you need to know if the backup was created prior to version 7.7 of Acronis Backup Cloud and you can check in the console:
Under devices > Backups > Select the backup > And select details, you will then see Backup format. If this says version 12 then you are on the latest version. If not please advise what it says?
I have noticed in my own environment that the latest backup format using the .tibx format has much less issues with VSS.
Regards

      
                
                
                    
                                                    Mon, 08/20/2018 - 06:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    mark williams
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hi tvieira
This issue occurs when using a 3rd party backup program that utilizes Windows VSS (Volume Shadow Service) and has its own requestor.
It looks like the requestor (the backup application) does not allow system writer to call back into their process and hence generates the error in the application log.

Check if the Volume Shadow Copy service is running on your computer or not.
To check for the same,
Click ‘Start’, type ‘services.msc’ and hit Enter.
 Locate “Volume Shadow Copy” and check if the service is started.
If not ‘Start’ the service.

If the issue persists, you may have to make some changes in the registry.
 The following example grants access to the "MyDomain\MyUser" account:
Click on Start, type regedit in the search box.
 On the Registry Editor window, navigate to the below location:
HKEY_LOCAL_MACHINE>SYSTEM>CurrentControlSet>Services>VSS>VssAccessControl <--- ADD KEY
MyDomain\MyUser = 1 <- ADD VALUE
Important: This section, method, or task contains steps that tell you how to modify the registry. However,
serious problems might occur if you modify the registry incorrectly. Therefore, make sure that you follow these steps carefully. For added protection, back up the registry before you modify it. Then, you can restore the registry if a problem occurs. For more information about how to back 
If you still come across the issue, to troubleshoot the error condition, you first need to determine what caused it by using the VssAdmin command line tool. After determining the cause of the error condition, follow the steps indicated for each possible cause.

      
                
                
                    
                                                    Mon, 09/03/2018 - 12:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the answers, I disabled VSS in the backup and it is doing the backups normally.
 
 
 
thanks

      
                
                
                    
                                                    Mon, 09/03/2018 - 14:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted
