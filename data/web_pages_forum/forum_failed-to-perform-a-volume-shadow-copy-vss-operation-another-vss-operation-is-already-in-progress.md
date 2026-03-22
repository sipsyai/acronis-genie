# Failed to perform a Volume Shadow Copy (VSS) operation. Another VSS operation is already in progress.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/failed-perform-volume-shadow-copy-vss-operation-another-vss-operation-already-progress

## Original Post
**Author:** Unknown

Failed to perform a Volume Shadow Copy (VSS) operation. Another VSS operation is already in progress.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello team,
I'm facing an issue with a client where their backup plan shows the message:
"Failed to perform a Volume Shadow Copy (VSS) operation. Another VSS operation is already in progress."
Is it possible to resolve this issue without disabling VSS? It states that another VSS operation is already in progress, but it’s the only one running.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/11/2024 - 13:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
I would advise you to review the following KB and check if it can be applied to the situation: https://care.acronis.com/s/article/68822-Acronis-Cyber-Protect-Cloud-backup-of-Hyper-V-virtual-machine-fails-with-the-error-message-Another-shadow-copy-creation-is-already-in-progress?language=en_US
You could also try running the VSS Doctor on the respective machine and check the output of the report. At the bottom, it will list all the errors detected: https://www.acronis.com/en-gb/products/vss-doctor/
In the host, check the status of the writers: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin-list-writers
If any writers show an error status, the client will need to fix it, as those errors will continue to be triggered otherwise.
In the VM, manually create and delete a snapshot. If there is an error, the VM tools are probably broken and need to be fixed.
Re-scheduling the backups with a more distant time frame may also help, giving the system time to create and delete the snapshots properly.
If the issue persists after executing all those steps and no issues are detected, please raise a ticket with the team or contact your MSP to do so: https://support.acronis.com/
Best regards.

      
                
                
                    
                                                    Mon, 11/11/2024 - 14:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Paolo Bagnoli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello
this are my tests:
Disabled VSS same problem
Error handing: is enabled (9 retry every 30 minutes) but it retry 2 times (in 2 minutes) and try no further
VSS Doctor: the only error is this:
	Name: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
	DeviceId: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
	Size: 548 MB
	Available: 125 MB
	Minimum: 320 MB
	IsOk: False
	Description: Free space is below required minimum
	IsMounted: False
	But this is the System Reserved partition and I can't modify it
vssadmin list writers all ok
No problem with take snapshot 
If i take a vss point no problem it works
scheduled backup in another time
My best regards

      
                
                
                    
                                                    Fri, 11/22/2024 - 14:02
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Paolo Bagnoli wrote:

Hello
this are my tests:
Disabled VSS same problem
Error handing: is enabled (9 retry every 30 minutes) but it retry 2 times (in 2 minutes) and try no further
VSS Doctor: the only error is this:
	Name: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
	DeviceId: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
	Size: 548 MB
	Available: 125 MB
	Minimum: 320 MB
	IsOk: False
	Description: Free space is below required minimum
	IsMounted: False
	But this is the System Reserved partition and I can't modify it
vssadmin list writers all ok
No problem with take snapshot 
If i take a vss point no problem it works
scheduled backup in another time
My best regards


Hello!
This indicates an issue with the shadow storage.
To resolve it, you may need to increase the shadow storage size following Microsoft's instructions:
Volume Shadow Copy Service Overview
Resize Shadow Storage Using vssadmin
As a test, you could also try disabling VSS in the backup plan. However, please note that SQL backups require VSS to function, so this option may not be suitable if you're working with SQL databases.
Best regards.

      
                
                
                    
                                                    Fri, 11/22/2024 - 17:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
