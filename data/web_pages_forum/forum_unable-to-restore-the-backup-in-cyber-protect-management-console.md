# Unable to restore the backup in Cyber Protect Management Console.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/unable-restore-backup-cyber-protect-management-console

## Original Post
**Author:** Unknown

Unable to restore the backup in Cyber Protect Management Console.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Himanshu Dwivedi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello ,
 
I am using Cyber Protect Management Console on Prem Setup and some of machine are getting backed up. Customer want to see the restoration process on their fresh machine. What all the things are to be there kn new system.
 
I tried to restore the Full backup in one of the PC usign ISO media builder, and restoration  is also getting successful, but As I am booting from the Disk it is showing files missing. Not sure why. Does that PC disk need to be formatted or the recovery image do by itself. Need better suggestion on this.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 04/10/2025 - 13:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
The restored disk may become unbootable if certain drivers required for the target hardware are missing.
If you are restoring to a machine with different hardware, we recommend using Acronis Universal Restore:

Acronis Universal Restore – Overview


Restoring to dissimilar hardware with Universal Restore

Please ensure that the restored system is set to boot in the same mode (UEFI or Legacy BIOS) as the original system. A mismatch in boot mode may lead to errors or missing boot files.
Boot Loader Recovery: In some cases—particularly with Windows—you might need to perform a startup repair using the Windows installation media after restoring the image.
Additionally, you may need to manually install specific drivers to ensure full hardware compatibility.
If the issue persists, we recommend contacting our support team for further assistance, as such cases may require deeper analysis.
Best regards,

      
                
                
                    
                                                    Fri, 04/11/2025 - 14:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Himanshu Dwivedi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Suppose if I recover the MBR and C drive and the windows was unable to boot so From where to get HAL.DLL file? As I can see that MBR is recovered but the system is booting in UEFI and does not show the HDD to boot.

      
                
                
                    
                                                    Fri, 04/11/2025 - 16:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Himanshu Dwivedi wrote:

Suppose if I recover the MBR and C drive and the windows was unable to boot so From where to get HAL.DLL file? As I can see that MBR is recovered but the system is booting in UEFI and does not show the HDD to boot.


Hello!
Maybe there was an issue with missing drivers or errors with the disk/file system.
Retry the process and recreate the bootable media making sure everything is added. Make sure you follow the documentation.
Option 1: Match Boot Mode to Disk Format

If you restored an MBR-based backup, go into your BIOS/UEFI settings:

Enable Legacy Boot / CSM.


Disable Secure Boot (UEFI only).


Make sure the drive is set as the primary boot device.



If you're in UEFI-only mode, your system may expect a GPT + EFI partition instead of MBR. In that case:

Either reconfigure BIOS to legacy mode,


Or convert the disk to GPT and install an EFI bootloader (not trivial).


Option 2: Repair Boot Files
Boot from a Windows installation media and:

Choose "Repair your computer" → "Troubleshoot" → "Command Prompt".


Run:

 cmd
bootrec /fixmbr bootrec /fixboot bootrec /scanos bootrec /rebuildbcd 


If you're in UEFI mode, these may not apply. You’d need to rebuild the EFI partition using:

 cmd
bcdboot C:\Windows /l en-us /s S: /f UEFI

If the issue persists, kindly raise a ticket with the team, because this needs to be reviewed by team.
Best regards.

      
                
                
                    
                                                    Mon, 04/14/2025 - 12:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
