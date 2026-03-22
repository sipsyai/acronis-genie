# how to delete old backups from cloud

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-delete-old-backups-cloud

## Original Post
**Author:** Unknown

how to delete old backups from cloud

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nguyen Huu Duy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
             
I am using Acronis backup cloud. I want to delete the old backup file but the error can not be deleted. Is there any other way to delete this old backup file? Thank for all.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      1.png

                      14.22 KB
                  
              
                      2.png

                      11.09 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/07/2018 - 03:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nguyen Huu Duy
Welcome to that Acronis forum, I will do my best to assist you with resolving the issue you are facing.
Have you tried removing the backup from the backup management console?
From the BMC navigate to "Backups" located just under "Devices" > Click on "Backups" > The first option there should be "Cloud Storage" > On the right hand you should see all of your cloud based backups > Select the backup you want to remove > Click delete
Please note that if you are not able to see the cloud backups on the right hand side you should change the machine which to browse from located at the top of the right hand pane by simply clicking "Change" and then select the correct machine.
Deleting backups this way will generate an activity in the "Activities" section which you can monitor.
If this does not work for you please let me know by providing another screenshot of the outcome and I will continue to assist you.
Regards

      
                
                
                    
                                                    Tue, 08/07/2018 - 06:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Nguyen Huu Duy… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nguyen Huu Duy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
Thanks Jays!
I've done all the deleting (including your way of the tutorial) but still report the same error as the image (delete fail). This error occurred after I upgraded my Acronis Storage cluster and updated the agent client ver 12.5..., so the backup settings are still ok. can not understand (*..*)

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      457109-150476.png

                      55.17 KB
                  
              
                      457109-150479.png

                      52.2 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 08/07/2018 - 06:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nguyen
I am sorry to hear that the provided solution did not resolve your issue, however we can still try other methods of deleting your backups.
Will it be possible to provide me with the error log?
From the error message you receive click on "More details" then simply copy and paste the error log in your response
Regards

      
                
                
                    
                                                    Tue, 08/07/2018 - 07:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Nguyen… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nguyen Huu Duy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays!
I sent an error message
----------------------------
DATE AND TIMEAug 07, 2018, 03:08:56 PM
CODE
0x01350016+0x01350016+0x01350016+0x01350016+0x01350016+0x01350016+0x01350016+0x00A100DB+0x020B0008+0x012700CE+0x00040009
MODULE
309
MESSAGE
TOL: Failed to execute the command. Deleting recovery points

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"19926590-DC92-4835-8458-34CE45061FAD","$module":"management_server_lxa64_5544"}
Message: TOL: Failed to execute the command. Deleting recovery points
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"19926590-DC92-4835-8458-34CE45061FAD","$module":"ams_dms_lxa64_5544"}
Message: TOL: Failed to execute the command. Deleting recovery points
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"ADB12096-4F68-4B48-B2D2-23CF5B6EAC4B","$module":"mms_vsa64_10330"}
Message: TOL: Failed to execute the command. Deleting archives
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"ADB12096-4F68-4B48-B2D2-23CF5B6EAC4B","$module":"staging_command_vsa64_10330"}
Message: TOL: Failed to execute the command. Deleting archives
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"mms_vsa64_10330"}
Message: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"1ACDF6BD-769F-42B5-9C7A-1FC8B1B297E1","$module":"service_process_vsa64_10330"}
Message: TOL: Failed to execute the command. Deleting archives
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"CommandID":"1ACDF6BD-769F-42B5-9C7A-1FC8B1B297E1","$module":"staging_command_vsa64_10330"}
Message: TOL: Failed to execute the command. Deleting archives
------------------------
Error code: 219
Module: 161
LineInfo: 0x0B320396ADFE3D39
Fields: {"$module":"disk_bundle_vsa64_10330","IsReturnCode":"1"}
Message: Failed to delete the archives.
------------------------
Error code: 8
Module: 523
LineInfo: 0x93DDF24CF210E756
Fields: {"$module":"disk_bundle_vsa64_10330"}
Message: Failed to rename file '.tmp.E62EA9AE-7F93-4BA8-BB83-F5005ECF8C5E.Duynh-00062BD9-17A8-4056-95A9-55F9F1BB7616-C191CB98-F2AB-4284-A94C-7330408BC772A.xml' to 'Duynh-00062BD9-17A8-4056-95A9-55F9F1BB7616-C191CB98-F2AB-4284-A94C-7330408BC772A.xml'.
------------------------
Error code: 206
Module: 295
LineInfo: 0x8A493C8D89FD241F
Fields: {"$module":"disk_bundle_vsa64_10330"}
Message: Internal error: An invalid file object is returned.
------------------------
Error code: 9
Module: 4
LineInfo: 0x60CCAC0523AC0E6F
Fields: {"$module":"archive3_adapter_vsa64_10330","Name":"'.tmp.E62EA9AE-7F93-4BA8-BB83-F5005ECF8C5E.Duynh-00062BD9-17A8-4056-95A9-55F9F1BB7616-C191CB98-F2AB-4284-A94C-7330408BC772A.xml'' -> 'Duynh-00062BD9-17A8-4056-95A9-55F9F1BB7616-C191CB98-F2AB-4284-A94C-7330408BC772A.xml'","PcsCode":"6"}
Message: Error occurred while renaming the file.
-------------------------------------------------------------------
Other accounts have the same error when deleting or opening the old backup file.
Thank Jays!

      
                
                
                    
                                                    Tue, 08/07/2018 - 08:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nguyen
Thank you for providing me with the logs,
Based on the screenshots and error log which you have provided me I would recommend that you try the following solutions:
Ensure you are on the latest agent version which should be 12.5.10330
1. Stop all Acronis services and programs on your system (The machine of which you are trying to delete the backups)
The services should be:
Acronis Managed Machine Service
Acronis Remote Agent Service
Acronis Scheduler2 Service
Acronis Active Protection Service
 Then under task manager > Details (End the following)
I know of the following but just check if their are any other relating to Acronis:
MmsMonitor.exe
service_process.exe
tib_mounter_service.
And sometimes you will see a process/service.exe pertaining to Acronis
Once all of the above is done then attempt to delete the backups again.
2. Then you can also attempt the following and actually does not require you to do anything
I reviewed your error log and found the following there are references to cloud based backup computer being unavailable and data locked. Locked data occurs when data requested to be backed up is in progress and operation has not yet completed.  The resolution is to give the backup process time to complete and try to remove the backup archives again at a later time.  This can occur if the delete request happens shortly after the backup request is started or completed. I would recommend allowing 5-10 minutes after backup has completed.
To confirm the above step ensure that there are no running backup tasks on the machine you are trying to delete backups for, and double check in activities to ensure no running activities are present in the backup management console.
If any running backup tasks are found please allow them to complete them and then proceed with trying to delete the backups. If there are stuck tasks please also let me know 
I hope the above resolves your issue.
Regards

      
                
                
                    
                                                    Tue, 08/07/2018 - 11:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Nguyen… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nguyen Huu Duy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays!
Thank you for troubleshooting support. Through this incident I have also learned more experience.
Again thank you!

      
                
                
                    
                                                    Wed, 08/08/2018 - 07:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nguyen
Always a pleasure to assist, if I may ask have you resolved your issues?
Please do not hesitate to respond should you require any additional assistance.
Regards

      
                
                
                    
                                                    Wed, 08/08/2018 - 12:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hi Nguyen… by Jays
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nguyen Huu Duy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
Hi Jays.
During the process of building and operating the Acronis Storage system, two problems have occurred.
1. During the system test, I installed the client agent on the PC and performed a backup, then uninstalled the client agent without deleting the backups before removing the agent. Then I installed a new agent for demo. So when doing the delete the old backup system error.
2. Recently, I made the Acronis Storage auto-upgrade to the latest version and client agent to the latest version. I then receive a message from all client agents that fail backup. I have searched on google for fix but still can not fix failed backup so I revoke on old backup plan and create new backup plan (currently new backup plan ok).
I followed your instructions but still did not. Finally, I have to remove the agent and delete the client account, the system will delete the backup errors (this fix is ​​bad).
I still do not know the exact cause of 1 or 2, can you explain me understand?
Thank you very much!

      
                
                
                    
                                                    Thu, 08/09/2018 - 02:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Nguyen
With point 1 did you select remove configuration and logs when you uninstalled the agent? Generally it should not cause a problem if you register the agent again to the same machine as uninstalling does not remove or affect backups.
With poinf 2 what did the backup fail with? Do you have a log you can provide?
I also run my own Acronis Storage 2.4 and did the latest node update and all agents are on the latest version and everything is running okay.
Can you advise to the following:
What version of storage were you on before you did the upgrade?
What type of storage do you use?
Regards

      
                
                
                    
                                                    Fri, 08/10/2018 - 05:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
