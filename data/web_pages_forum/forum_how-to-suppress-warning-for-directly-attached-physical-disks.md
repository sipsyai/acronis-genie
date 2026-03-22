# How to suppress warning for directly attached physical disks?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-suppress-warning-directly-attached-physical-disks

## Original Post
**Author:** Unknown

How to suppress warning for directly attached physical disks?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Anonymous
                            

                            
                    
                        Beginner
                    
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have a VM which has an attached physical disk. Every day, we get the following warnings. How can we suppress these?
Activity 'Preparing for backup of virtual machine' succeeded with the following warning: 'There are directly attached physical disks. The disks will not be backed up while backing up the virtual machine.'
Activity 'Configuring existing virtual machine' succeeded with the following warning: 'Secure Boot has been disabled in the recovered virtual machine. If required, enable it manually.'


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/16/2024 - 21:26

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Scott,
Usually, the first warning appears when a drive from the host is attached directly to the VM. If that's the case, the workaround is to install an agent inside each VM instead of executing agentless backups.
Regarding the second warning, disabling secure boot during recovery is done intentionally to guarantee proper VM boot-up, so it is expected behavior for protection purposes.
Solution: follow the recommendation described in the warning or disable secure boot before the next backup.
If you have any queries, please contact the team so we can troubleshoot the issue further: https://kb.acronis.com/content/8153
Best regards.
 

      
                
                
                    
                                                    Wed, 07/17/2024 - 09:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Anonymous
                            

                            
                    
                        Beginner
                    
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
 Thanks for the quick response.

workaround is to install an agent inside each VM instead of executing agentless backups.


What are the consequences of this, if any? Performance?
Regarding the second warning, disabling secure boot during recovery is done intentionally to guarantee proper VM boot-up, so it is expected behavior for protection purposes.
Solution: follow the recommendation described in the warning or disable secure boot before the next backup.

This is a VM that was recovered from a backup. I have since enabled secure boot. But the warning still shows up every day. All the other VMs have secure boot enabled and do not throw this warning, so I'm a bit confused by your statement.
To state this another way, we were not receiving this warning at all and all the VMs had Secure Boot enabled. I then did a restore on one of the VMs and it did disable secure boot, as stated, but even since reenabling it I'm still getting the warning.

      
                
                
                    
                                                    Wed, 07/17/2024 - 12:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Scott Beeson wrote:

 
 Thanks for the quick response.

workaround is to install an agent inside each VM instead of executing agentless backups.


What are the consequences of this, if any? Performance?
Regarding the second warning, disabling secure boot during recovery is done intentionally to guarantee proper VM boot-up, so it is expected behavior for protection purposes.
Solution: follow the recommendation described in the warning or disable secure boot before the next backup.

This is a VM that was recovered from a backup. I have since enabled secure boot. But the warning still shows up every day. All the other VMs have secure boot enabled and do not throw this warning, so I'm a bit confused by your statement.
To state this another way, we were not receiving this warning at all and all the VMs had Secure Boot enabled. I then did a restore on one of the VMs and it did disable secure boot, as stated, but even since reenabling it I'm still getting the warning.


Hello!
I wouldn't say there would be any consequence apart from the fact that you need to install an agent inside the VM and start a new backup file.
Regarding the second warning, that's not expected. I've seen a known issue in an older version of the product for that error, but this one doesn't present it. I suggest you raise a ticket with the support team or contact your MSP to do it, as that would require an internal investigation. https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Wed, 07/17/2024 - 16:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Anonymous
                            

                            
                    
                        Beginner
                    
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks.

      
                
                
                    
                                                    Wed, 07/17/2024 - 16:21
