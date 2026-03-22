# Activity succeeded with warnings - Production checkpoints cannot be created

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/activity-succeeded-warnings-production-checkpoints-cannot-be-created

## Original Post
**Author:** Unknown

Activity succeeded with warnings - Production checkpoints cannot be created

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andreas Johansson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
 
I get an error every night during backup. I have been in contact with support x number of times but they can't do much. Dissatisfied with their support.
 
Activity 'Creating application-consistent (VSS) hypervisor snapshot' succeeded with the following warning: 'Creation of the virtual machine checkpoint failed on Hyper-V host level with a Microsoft-specific error. Windows error: The task has completed with errors.'
This from event viewer:
Production checkpoints cannot be created for 'BSUbuntu-Monitoring'. (Virtual machine ID 0FE84595-C99E-4F88-8163-9436B1C5DCBB)
Checkpoint operation for 'BSUbuntu-Monitoring' failed. (Virtual machine ID 0FE84595-C99E-4F88-8163-9436B1C5DCBB)
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/25/2024 - 10:57

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Andreas!
Did you check the native tools of Hyper-V? If they are damaged, we can't fix them because they are a Microsoft product.
Manually go to that VM and create and delete a snapshot. If there are errors, it means the native tools of the VM are somehow damaged and must be fixed: https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/use…
Also, consider disabling VSS in the backup plan options as a test and run a backup: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
Best regards.

      
                
                
                    
                                                    Tue, 06/25/2024 - 11:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andreas Johansson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks a lot, turning off VSS in Acronis helped. Support should be able to say that at once.
I think.  

But what are the disadvantages of having VSS turned off, will I notice any difference? 

      
                
                
                    
                                                    Tue, 06/25/2024 - 12:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andreas Johansson wrote:

Thanks a lot, turning off VSS in Acronis helped. Support should be able to say that at once.
I think.  

But what are the disadvantages of having VSS turned off, will I notice any difference? 


Hello,
Note that the snapshots should be set as Standard in the hypervisor.
The virtual disk files are stored in the D:\Hyper-V\Virtual hard disks folder. You need to ensure that Hyper-V has sufficient permissions to access the necessary data.
The system account that Hyper-V is running must have read and write permissions for the folder containing virtual disks and snapshot files. If you see an identifier instead of a user or group name in the folder properties, the permissions may be incorrect. If permissions are correct, check that you have enough free storage space to perform operations with Hyper-V checkpoints.
Also, try the following steps to fix the issue:
Make sure that Hyper-V Integration Services are installed in the guest operating system (OS).
Open VM settings.
Click Integration Services in the Management section.
Select/Deselect the Backup (volume checkpoint) option. The deselected option is used for crash-consistent checkpoints, and the selected option is used for application-consistent checkpoints (the VSS signal is passed to a guest OS). If there is an issue with the VSS writer, disabling this option can be helpful. Select the Guest Services option.
Reboot the VM and retry the backup.
Regarding disabling VSS in the backup plan, it's not a fix but a workaround when the native tools of a VM won't work. If you don't have any SQL plan enabled in that VM, I would say there's no problem running a backup with it disabled, there's no visible changes. The only issue is that without VSS, the backup won't ensure application-consistent snapshots. This is crucial for databases and other transactional applications that rely on VSS to maintain data integrity during backups
Best regards.
Best regards.

      
                
                
                    
                                                    Tue, 06/25/2024 - 12:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
