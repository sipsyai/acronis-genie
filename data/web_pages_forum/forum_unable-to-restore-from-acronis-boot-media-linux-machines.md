# Unable to restore from acronis boot media - Linux machines

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/unable-restore-acronis-boot-media-linux-machines

## Original Post
**Author:** Unknown

Unable to restore from acronis boot media - Linux machines

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Scantec Informatica Lda
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
We have this issue when trying to restore from boot media iso: When we try to restore a Linux based machine backup from local storage the machine resets at the point - while loading information about backed-up data.
 
If we try to restore a Windows based machine the issue doesn't happen.

 
We tried this with different hardware/hypervisors, the issue is the same (only happens with Linux backups).
 
We tested with current boot media iso and previous stable.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/13/2025 - 15:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
If you are using different kernel versions on the Linux backups, check for any known issues with the specific kernel version and Acronis boot media compatibility.
Even though you've tested both the current and previous stable boot media ISOs, I recommend double-checking if there are any firmware or bootloader updates available for the specific Linux distributions you are backing up. Sometimes, Linux kernels or certain configurations might cause issues with the boot media.
Verify that the file systems on the Linux-based machines are compatible with Acronis’ boot media and restore environment.
Try adding or modifying boot parameters in the bootloader (GRUB or equivalent) to see if this helps.
If the issue persists after testing all that, please raise a ticket with our support or with your MSP because that must be investigate https://kb.acronis.com/content/8153?_gl=1*1oklsvh*_gcl_au*MTg4ODYwNDM5N….. 
Best regards.

      
                
                
                    
                                                    Wed, 05/14/2025 - 01:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Scantec Informatica Lda
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
Kernel versions are the supported current kernel versions for Debian 12 and Debian 11 (two different machines I tested). Both systems are updated, no firmware/bootloader updates pending.
Filesystem is compatible - ext4 on both systems
I'll open a ticket with support.
 
Thanks,
 
Best regards

      
                
                
                    
                                                    Wed, 05/14/2025 - 10:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Scantec Informatica Lda wrote:

Hello,
 
Kernel versions are the supported current kernel versions for Debian 12 and Debian 11 (two different machines I tested). Both systems are updated, no firmware/bootloader updates pending.
Filesystem is compatible - ext4 on both systems
I'll open a ticket with support.
 
Thanks,
 
Best regards


Hello!
Feel free to update the thread if you have any questions or with the solution provided by our support.
Thanks!

      
                
                
                    
                                                    Wed, 05/14/2025 - 11:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
