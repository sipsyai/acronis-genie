# The active log sequence is empty.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/active-log-sequence-empty

## Original Post
**Author:** Unknown

The active log sequence is empty.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good morning all, We are currently having a backup failure with a VM (being backed up via the Hypervisor agent). Can anyone enlighten me as to why this error is occurring? I've included the log from the failure below. This backup has been working (incrementally) with no issues up to this point. I've searched the KB articles but can't find anything of note. Any input would be appreciated. Many thanks, Phil Whitmore The active log sequence is empty.MESSAGEThe active log sequence is empty. Additional info:------------------------ Error code: 20250646 Fields: {"$module":"mms_vsa64_15300","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"} Message: TOL: Failed to execute the command. Backup workflow ------------------------ Error code: 20250646 Fields: {"$module":"gtob_backup_command_addon_vsa64_15300","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"} Message: TOL: Failed to execute the command. Backup workflow ------------------------ Error code: 21561346 Fields: {"$module":"gtob_backup_command_addon_vsa64_15300","StepType":2,"TraceLevel":1} Message: Step 'Backup' has failed. ------------------------ Error code: 20250646 Fields: {"$module":"mms_vsa64_15300","CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0"} Message: TOL: Failed to execute the command. Tol::IsolateCommand ------------------------ Error code: 20250646 Fields: {"$module":"service_process_vsa64_15300","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"} Message: TOL: Failed to execute the command. Backing up ------------------------ Error code: 20250646 Fields: {"$module":"gtob_backup_command_addon_vsa64_15300","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"} Message: TOL: Failed to execute the command. Backing up ------------------------ Error code: 7503931 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Backup of virtual machines has failed. ------------------------ Error code: 7503950 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Not all virtual machines have been backed up. ------------------------ Error code: 7503949 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Failed to back up virtual machine 'vm3A3212B (SFTP)'. ------------------------ Error code: 7503890 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Failed to prepare for backup. ------------------------ Error code: 10551548 Fields: {"$module":"disk_bundle_vsa64_15300","account":"QNet_Acronis@qnetworks.co.uk","tenantName":"QNet_Acronis@qnetworks.co.uk"} Message: Stream name: 'vm3A3212B (SFTP)-B581AA7A-78EA-4CCA-9CF9-A1B381C15660-862C7A05-829A-41CE-A80F-FE93A4A445CBA.tibx'. ------------------------ Error code: 21561347 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Backup has failed. ------------------------ Error code: 66596 Fields: {"$module":"disk_bundle_vsa64_15300"} ------------------------ Error code: 9764877 Fields: {"$module":"disk_bundle_vsa64_15300"} Message: Failed to perform the requested operation. ------------------------ Error code: 5439582 Fields: {"$module":"hv_srv_vsa64_15300"} Message: Failed to open virtual disk file 'F:\HyperV\Clients\Virtual Machines\vm3A3212B_1_54A09E73-1BFC-4E7C-A13E-13900527075C.vhdx'. ------------------------ Error code: 3932203 Fields: {"$module":"hv_srv_vsa64_15300"} Message: The active log sequence is empty. ------------------------

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 01/13/2020 - 10:09

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
thank you for your posting! I've found similar cases with the error sequence 
Message: Failed to perform the requested operation.
Message: Failed to open virtual disk file 
Message: The active log sequence is empty.
The issue might be in fact caused by failures of snapshot processing. Agent for Hyper-V performs as a VSS requestor to create a VSS snapshot via VSS service on the Hyper-V Server. VSS service uses the Hyper-V VSS writer to quiesce the guest operating system via the Hyper-V Integration Services installed inside the guest OS during the snapshot creation. 
So I would suggest using the free Acronis VSS Doctor tool for diagnosing and repairing Volume Shadow Copy Service issues. Download links and instructions are available at https://www.acronis.com/personal/vss-diagnostic-free-tool/
Please use it both on the Hyper-V host and inside the guest OS of vm3A3212B.
Also please make sure that the Hyper-V Integration Services installed in the guest OS are functional and up-to-date.
If the issue persists, please open a support ticket for the more in-depth investigation. 

      
                
                
                    
                                                    Tue, 01/14/2020 - 08:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good afternoon Ekaterina,
 
Thanks for the quick reply - I had checked the VSS writers and restarted them via CMDline but have carried out the VSS check using the VSS Doctor application now too.
 
It did report elevated Disk I/O activity but everything else was fine.
I triggered the backup again after suspending high active services on the VM in question but it still failed with the same message.
 
Looking through the logs, the snapshot is successfully created but "non VSS" - in the end I enabled Quiesced Snapshotting on that VM (thus creating the snapshot from within the VM) and its now working.
 
I'm not sure why the previous method snapshotting from the Host has suddenly encountered issues, but it is now backing up again...
 
If it helps your development I'm more than happy to send over the logs of the failed attempts?
 
Kind regards,
 
Phil

      
                
                
                    
                                                    Tue, 01/14/2020 - 15:54
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
