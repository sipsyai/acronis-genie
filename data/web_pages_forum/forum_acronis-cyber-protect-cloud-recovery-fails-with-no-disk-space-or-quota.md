# Acronis Cyber Protect Cloud: Recovery fails with "No disk space or quota"

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/acronis-cyber-protect-cloud-recovery-fails-no-disk-space-or-quota

## Original Post
**Author:** Unknown

Acronis Cyber Protect Cloud: Recovery fails with "No disk space or quota"

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Vincent Duvernet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I'm extremely frustrated by the difficulty I'm having restoring a backup and having to spend my entire weekend on it.
To summarize, I need to restore 1.5 TB of data to a new server on a blank 2x4TB RAID1 array (verified with MiniTool Partition Wizard).
The restoration consistently fails with the message "Acronis Cyber ​​Protect Cloud: Recovery fails with "No disk space or quota"".
I found this KB article that addresses the problem:
https://care.acronis.com/s/article/68475-Acronis-Cyber-Protect-Cloud-Re…
But it seems just as buggy as the rest.
I formatted a 1TB external drive as NTFS and followed the procedure, yet the MKLINK command returns "incorrect function". If I try the other switches, I get different error messages.
If anyone has a brilliant idea, I'm all ears because right now I'm trying to restore the data by directly copying it from server to server.
Thanks,
Vincent

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/13/2025 - 10:03

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                TrueImage 2014,2018,2021
CyberBackup
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Vincent,
Based on what you described, this does not appear to be an Acronis Cyber Protect Cloud scenario.
If you are using Acronis Cyber Protect 15 / 16 / 17 (on-premises) and restoring to a local RAID volume, the KB you referenced does not apply, as it is specific to Cyber Protect Cloud agents and their temporary storage handling.
For on-prem products, the “No disk space or quota” error during recovery is most commonly related to one of the following:

Temporary / staging storage

During recovery, Acronis requires additional temporary space (often close to the size of the backup).


The default temp location is usually on the system drive.


Even if the target RAID has enough free space, the restore can fail if the temp path does not.



Target disk layout

Ensure the RAID volume is fully initialized, partitioned, and visible to Windows with sufficient free space.


Verify that the correct target disk/volume is selected in the recovery wizard.



Permissions / security software

Antivirus or security software may block temporary files created during restore.


Ensure the restore is performed with administrative privileges and that SYSTEM has access to the temp location.


The MKLINK workaround described in the Cloud KB is not supported for on-prem Cyber Protect and may fail or cause additional issues, which explains the “incorrect function” error you are seeing.
At this point, since you’ve already spent significant time troubleshooting, I strongly recommend contacting Acronis Support so they can review logs and confirm the exact cause:
https://support.acronis.com/
When opening the case, please include:

Exact product name and build (ACP 15 or 16)


Screenshot of the target disk layout


Recovery logs (if available)

This will allow them to provide precise guidance for your configuration.
Best regards,
José

      
                
                
                    
                                                    Sat, 12/13/2025 - 17:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
