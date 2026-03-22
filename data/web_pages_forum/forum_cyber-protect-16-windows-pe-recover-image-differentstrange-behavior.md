# Cyber Protect 16 - Windows PE recover image different/strange behavior

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/cyber-protect-16-windows-pe-recover-image-differentstrange-behavior

## Original Post
**Author:** Unknown

Cyber Protect 16 - Windows PE recover image different/strange behavior

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jens T
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I noticed a different / strange behavior on restoring an image with acrocmd on Windows PE - "Offline".
Acronis Cyber Protect 16 (16.4.40354)
Problem: 
At about 87% the process seems to slow down and finally a message is displayed that a reboot is required, which I can reboot or cancel. The whole process is done via acrocmd (recover disk --loc=x --arc=x --nt_signature=backup --oss_numbers=false --disk=a --target_disk=a --progress). 
 
This problem appears on the Windows PE I build based on Windows 11 (Build 26100). The integration of Acronis acrocmd works fine. I can create images and also can restore images which are fully functional (boot into restored Windows) if I confirm the message with reboot AND also when I choose cancel! 
If I choose cancel for the reboot request, there is an error message printed in the command line that the Acronis Activity was canceled. Also is the Activity listed as Canceled, when I check the activities via acrocmd list activities. 
While I'm automating the restore process I need to get a "Completed successfully" to continue my script. 
 
Countercheck:
As a countercheck, I then performed the same test with an Windows PE build by Acronis Bootable Media Builder. Bootable media type is Windows PE (64-bit) and Create WinPE automatically.
With this Windows PE Version, also based on Windows 11 Build 26100, I performed the same restore command with the same image file from the same source location. But this time acrocmd completed the restore without a "required reboot" message.
 
What am I overlooking?
 
br
jens

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/10/2026 - 18:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jens!
Welcome to the forum.
You are most likely seeing this because of differences between your custom WinPE build and the WinPE created with the Acronis Bootable Media Builder.
In your own WinPE (built from Windows 11 ADK), some Acronis storage integration components (e.g., SnapAPI / storage filters used by Acronis media) are not fully integrated. Because of that, when the restore reaches the final stage (~87%) and the disk signature / partition table is updated, the Windows PE storage stack may flag that a reboot is required to refresh the disk state.
In the WinPE generated by Acronis Bootable Media Builder, these components are injected automatically, so the disk refresh is handled internally and acrocmd finishes with “Completed successfully” without prompting for reboot.
Since you confirmed that the restored system boots correctly even when selecting Cancel, the restore itself is already complete — the reboot request is just coming from the WinPE environment.
In practice, for automated workflows the safest approach is either:

use the Acronis-built WinPE media, or


allow/trigger an automatic reboot after the restore step.

Best regards.

      
                
                
                    
                                                    Wed, 03/11/2026 - 05:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
