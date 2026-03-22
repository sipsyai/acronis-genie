# [RESOLVED] Error codes ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/resolved-error-codes

## Original Post
**Author:** Unknown

[RESOLVED] Error codes ?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
Is  there somwhere one can check what various error codes means?
right now I have a failing system state backup and the log files dont give you must to work with.
Dont know what to look for with this info
OL: Failed to execute the command. Backing up

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_1299"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_1299"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 103
Module: 623
LineInfo: 0x94F5F955B13DDFBA
Fields: {"IsReturnCode":"1","$module":"SystemStateAgentProvider_vsa64_1299"}
Message: A generic error of System state Backuper.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/08/2015 - 09:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fredrik,
This error message is too generic and does not point to any specific root cause apart from the failing module. The reason is thus unclear for me.
Is this a full error message or just a top part of it? Please provide the full message if any.
If no additional message is available, before submitting a case to our support team you can try to localize the issue: system state backup is a file-level backup with VSS snapshot, so create a new file-level backup of any other file of comparabale size from C: volume and set the backup option of file-level snapshot to "Always create". Errors in file-level backup could then give further ideas for investigation. Also check the Windows Event log for errors at the moment of backup and provide them here.
Looking forward for additional information.
Regards,

      
                
                
                    
                                                    Tue, 12/08/2015 - 12:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            update: i changed VSS and after that it went through
hi
This is the entire error message
Error
DATE AND TIME
Dec 08, 2015, 10:33:03 AM
CODE
0x01350016+0x01350016+0x01490002+0x01350016+0x01350016+0x01350016+0x026F0067+0x02770191+0x00040017+0x00980410
MODULE
309
MESSAGE
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"mms_vsa64_1592"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"gtob_backup_command_addon_vsa64_1299"}
Message: TOL: Failed to execute the command. Backup workflow
------------------------
Error code: 2
Module: 329
LineInfo: 0x8EDC81EA38FABA3C
Fields: {"TraceLevel":"1","$module":"gtob_backup_command_addon_vsa64_1299"}
Message: Step 'Backup' has failed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"mms_vsa64_1592"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_1299"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_1299"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 103
Module: 623
LineInfo: 0x94F5F955B13DDFBA
Fields: {"IsReturnCode":"1","$module":"SystemStateAgentProvider_vsa64_1299"}
Message: A generic error of System state Backuper.
------------------------
Error code: 401
Module: 631
LineInfo: 0x9B358C6E703DE384
Fields: {"IsReturnCode":"1","$module":"SystemStateAgentProvider_vsa64_1299"}
Message: Failed to back up the system state.
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Error code: 1040
Module: 152
LineInfo: 0xA46E8D7BA5BB85F2
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message:

      
                
                
                    
                                                    Tue, 12/08/2015 - 12:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fredrik,
Thank you for the full message. This part makes it more clear:
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Program was unable to lock a file, which most probably refers to a system state file which is being backed up. This case be due to a failed or skipped snapshot. Please set the backup option File-level backup snapshot to Always create a snapshot and retry the backup.
In case this does not help and the error message does not change, please create a Procmon log during the backup and submit a support case so the support team can analyze which files cannot be locked.
Best regards,

      
                
                
                    
                                                    Tue, 12/08/2015 - 12:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the update, nice to know it helped.
Cheers,

      
                
                
                    
                                                    Tue, 12/08/2015 - 12:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Larry Vancini
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Having issues with my Acronis 2015
It boots from my USB, but can't find any drives, on my HP ZBOOK 15.
I have booted both in Legacy and UEFI ?
I get the following error event code: 0x000101F4+0X000A01FD see attached pic..
Any suggestions would be appreacited, thanks in advance

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      373537-131353.jpg

                      730.86 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 07/07/2016 - 02:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Larry,
Welcome to Acronis user forums! This forum section is dedicated to Acronis Service Provider Solutions. I'd recommend you to start a new thread in Acronis True Image 2015 section.
Thank you,

      
                
                
                    
                                                    Thu, 07/07/2016 - 11:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    wildan nasrulloh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dmitry,

I have same issue with below error. But i cannot find option "the backup option File-level backup snapshot
 
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"mms_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"agent_protection_addon_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE31
Fields: {"$module":"agent_protection_addon_vsa64_16363"}
Message: Failed to execute the command.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB713
Fields: {"$module":"agent_protection_addon_vsa64_16363","FailCount":"2"}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"service_process_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"gtob_backup_command_addon_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 3
Module: 143
LineInfo: 0x1CD98AAE889424F5
Fields: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_16363"}
Message: The running task has been canceled.
------------------------
Error code: 1061
Module: 1
LineInfo: 0xB43E776571144E10
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message:
------------------------
Error code: 1060
Module: 1
LineInfo: 0xB43E776571144DF0
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Failed to commit operations.
------------------------
Error code: 34
Module: 7
LineInfo: 0x2CBDD167CBCA9503
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Operation canceled.
 
Dmitry Zelensky wrote:

Hi Fredrik,
Thank you for the full message. This part makes it more clear:
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Program was unable to lock a file, which most probably refers to a system state file which is being backed up. This case be due to a failed or skipped snapshot. Please set the backup option File-level backup snapshot to Always create a snapshot and retry the backup.
In case this does not help and the error message does not change, please create a Procmon log during the backup and submit a support case so the support team can analyze which files cannot be locked.
Best regards,



      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      647417-479161.zip

                      2.92 KB
                  
              
                      647417-479164.jpg

                      363.58 KB
                  
              
                      647417-479167.jpg

                      273.04 KB
                  
              
                      647417-479170.jpg

                      309.59 KB
                  
              
                      647417-479173.jpg

                      374.3 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 03/25/2025 - 05:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            wildan nasrulloh wrote:

Hi Dmitry,

I have same issue with below error. But i cannot find option "the backup option File-level backup snapshot
 
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"mms_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"agent_protection_addon_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE31
Fields: {"$module":"agent_protection_addon_vsa64_16363"}
Message: Failed to execute the command.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB713
Fields: {"$module":"agent_protection_addon_vsa64_16363","FailCount":"2"}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"service_process_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"gtob_backup_command_addon_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 3
Module: 143
LineInfo: 0x1CD98AAE889424F5
Fields: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_16363"}
Message: The running task has been canceled.
------------------------
Error code: 1061
Module: 1
LineInfo: 0xB43E776571144E10
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message:
------------------------
Error code: 1060
Module: 1
LineInfo: 0xB43E776571144DF0
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Failed to commit operations.
------------------------
Error code: 34
Module: 7
LineInfo: 0x2CBDD167CBCA9503
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Operation canceled.
 
Dmitry Zelensky wrote:

Hi Fredrik,
Thank you for the full message. This part makes it more clear:
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Program was unable to lock a file, which most probably refers to a system state file which is being backed up. This case be due to a failed or skipped snapshot. Please set the backup option File-level backup snapshot to Always create a snapshot and retry the backup.
In case this does not help and the error message does not change, please create a Procmon log during the backup and submit a support case so the support team can analyze which files cannot be locked.
Best regards,




Hello!
That reveals that something is locked, either the files you want to backup or the location so the snapshot can't be taken.
You need to review all of that. You can also try to disable the VSS as a test in the backup options of that plan.
 Best regards.

      
                
                
                    
                                                    Tue, 03/25/2025 - 13:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    wildan nasrulloh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose P. Magalhaes wrote:

wildan nasrulloh wrote:

Hi Dmitry,

I have same issue with below error. But i cannot find option "the backup option File-level backup snapshot
 
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"mms_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"agent_protection_addon_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE31
Fields: {"$module":"agent_protection_addon_vsa64_16363"}
Message: Failed to execute the command.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB713
Fields: {"$module":"agent_protection_addon_vsa64_16363","FailCount":"2"}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"service_process_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"gtob_backup_command_addon_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 3
Module: 143
LineInfo: 0x1CD98AAE889424F5
Fields: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_16363"}
Message: The running task has been canceled.
------------------------
Error code: 1061
Module: 1
LineInfo: 0xB43E776571144E10
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message:
------------------------
Error code: 1060
Module: 1
LineInfo: 0xB43E776571144DF0
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Failed to commit operations.
------------------------
Error code: 34
Module: 7
LineInfo: 0x2CBDD167CBCA9503
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Operation canceled.
 
Dmitry Zelensky wrote:

Hi Fredrik,
Thank you for the full message. This part makes it more clear:
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Program was unable to lock a file, which most probably refers to a system state file which is being backed up. This case be due to a failed or skipped snapshot. Please set the backup option File-level backup snapshot to Always create a snapshot and retry the backup.
In case this does not help and the error message does not change, please create a Procmon log during the backup and submit a support case so the support team can analyze which files cannot be locked.
Best regards,




Hello!
That reveals that something is locked, either the files you want to backup or the location so the snapshot can't be taken.
You need to review all of that. You can also try to disable the VSS as a test in the backup options of that plan.
 Best regards.
 
Hello Jose,
I am not sure which part is causing the Disk to not be able to be backup. Is there a common reason why backup fails?
I have tried to backup with VSS On and VSS Off but still Backup Failed.
 
Best regards,
wildan



      
                
                
                    
                                                    Wed, 03/26/2025 - 02:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            wildan nasrulloh wrote:

Jose P. Magalhaes wrote:

wildan nasrulloh wrote:

Hi Dmitry,

I have same issue with below error. But i cannot find option "the backup option File-level backup snapshot
 
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"mms_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"agent_protection_addon_vsa64_16363","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Backup plan 'Disks/volumes to \\192.168.6.143\SBR\SBR SERVER\ (4)'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE31
Fields: {"$module":"agent_protection_addon_vsa64_16363"}
Message: Failed to execute the command.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB713
Fields: {"$module":"agent_protection_addon_vsa64_16363","FailCount":"2"}
Message: 2 activities have not succeeded. One of them is displayed.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"service_process_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819597
Fields: {"$module":"gtob_backup_command_addon_vsa64_16363","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 3
Module: 143
LineInfo: 0x1CD98AAE889424F5
Fields: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_16363"}
Message: The running task has been canceled.
------------------------
Error code: 1061
Module: 1
LineInfo: 0xB43E776571144E10
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message:
------------------------
Error code: 1060
Module: 1
LineInfo: 0xB43E776571144DF0
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Failed to commit operations.
------------------------
Error code: 34
Module: 7
LineInfo: 0x2CBDD167CBCA9503
Fields: {"$module":"disk_bundle_vsa64_16363"}
Message: Operation canceled.
 
Dmitry Zelensky wrote:

Hi Fredrik,
Thank you for the full message. This part makes it more clear:
------------------------
Error code: 23
Module: 4
LineInfo: 0x5E37827EF93FC21B
Fields: {"$module":"disk_bundle_vsa64_1299"}
Message: Failed to lock the file.
------------------------
Program was unable to lock a file, which most probably refers to a system state file which is being backed up. This case be due to a failed or skipped snapshot. Please set the backup option File-level backup snapshot to Always create a snapshot and retry the backup.
In case this does not help and the error message does not change, please create a Procmon log during the backup and submit a support case so the support team can analyze which files cannot be locked.
Best regards,




Hello!
That reveals that something is locked, either the files you want to backup or the location so the snapshot can't be taken.
You need to review all of that. You can also try to disable the VSS as a test in the backup options of that plan.
 Best regards.
 
Hello Jose,
I am not sure which part is causing the Disk to not be able to be backup. Is there a common reason why backup fails?
I have tried to backup with VSS On and VSS Off but still Backup Failed.
 
Best regards,
wildan




Hello!
The issue isn’t necessarily with the disk you are backing up—it could also be related to the storage location. If the backup agent cannot access it, the error may occur.
If the backup file is stored on a NAS, ensure it is accessible and that no other program is using it. Restarting the NAS might also help to see if backups run smoothly afterward.
This error can also appear when backing up cloud applications like O365 if the folder is locked by the program, preventing the backup agent from running.
In summary, there is no single workaround or solution, as it depends on the specific client environment.
If the issue persists, please contact our support or your Service Provider so we can troubleshoot it.
Best regards.

      
                
                
                    
                                                    Wed, 03/26/2025 - 07:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
