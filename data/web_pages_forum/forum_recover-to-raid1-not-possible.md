# Recover to RAID1 - not possible

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/recover-raid1-not-possible

## Original Post
**Author:** Unknown

Recover to RAID1 - not possible

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andreas Grüll
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
i have a Highpoint SSD7502 NVMe RAID Controller setup. The two SSDs are configured as RAID1. Backing up the machine with Cyber Protect Cloud works well. I only do full backups. 
The goal is to recover the whole disk. But this doesn't work, because  "Recovery Bootable Media" doesn't recognize the RAID1. I believe I had to add the Highpoint RAID drivers, but I don't know how. 
Can you help me please?
 
 
 
 
 
 
 
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/20/2023 - 11:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to our forum.
You could create a WinPE bootable media for that propose.
Please check this KB, on the topic number 19 there are the instructions: https://kb.acronis.com/content/59611
Feel free to contact our support if you have any questions: https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Wed, 12/20/2023 - 15:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andreas Grüll
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The creation of a bootable media with integrated Highpoint RAID drivers was successful. Thanks for the link. 
 
The recover process is weird:
1. When trying to recover from the Backup Harddisk directly to the Highpoint RAID1 drive then the destination drive ist greyed out. I can't select it. When attaching a second SATA drive to the system (this drive is empty and has nothing to to with the recovery process), then I can select the Highpoint RAID as destination. 
 
2. The biggest problem is: After the recovery finished the OS is not booting. A bluescreen with inaccessible boot device appears. But it's exactly the same hardware. Nothing changed since Backup. 
 
 

      
                
                
                    
                                                    Thu, 12/21/2023 - 09:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andreas Grüll wrote:

The creation of a bootable media with integrated Highpoint RAID drivers was successful. Thanks for the link. 
 
The recover process is weird:
1. When trying to recover from the Backup Harddisk directly to the Highpoint RAID1 drive then the destination drive ist greyed out. I can't select it. When attaching a second SATA drive to the system (this drive is empty and has nothing to to with the recovery process), then I can select the Highpoint RAID as destination. 
 
2. The biggest problem is: After the recovery finished the OS is not booting. A bluescreen with inaccessible boot device appears. But it's exactly the same hardware. Nothing changed since Backup. 
 
 


Hello!
Incorrect configuration in the BIOS or UEFI settings can be one of the causes of the "inaccessible boot device" error, preventing the OS boot device. Ensure that the BIOS settings are correctly configured to avoid any serious errors.
Corrupted or damaged drivers, especially storage device drivers, can trigger this error.
Attempt to boot into Safe Mode. If successful, it may indicate a driver or software issue. You can then troubleshoot and update drivers or uninstall recent updates.
You can also boot from the Windows installation media and run the automatic repair option. This can resolve common boot problems.
After recovery, the boot configuration might need adjustment. Boot into the Windows Recovery Environment or use the Windows installation media to access the Command Prompt and rebuild the boot configuration.
bootrec /rebuildbcd
If the issue persists, please raise a ticket with the team because this needs an investigation.
Best regards.
 

      
                
                
                    
                                                    Thu, 12/21/2023 - 14:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
