# Adding a Device replaces a Device

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/adding-device-replaces-device

## Original Post
**Author:** Unknown

Adding a Device replaces a Device

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            My issue is like this one but for ACP 16:https://forum.acronis.com/forum/acronis-cyber-backup-125-forum/pc-remov…
I had Device1 setup with agent and protection plans configured and applied. 
Device2, would not be discovered by Acronis Cyber Protect in the web console. So I ran the agent installation.
Now Device2 has effectively replaced Device1 throughout my Acronis Cyber Protect web console configurations.
Device1 is missing. Device2 has taken its place.
When you check the inventory hardware of the Device2, the hardware listed is that for Device1.
I'm just wondering what the approved solution is before I start regedit.
Thank you for reading,
RW
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/03/2024 - 17:48

                                                          
                                                            
                                                                                        
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to our forum.
That issue is not expected in ACP16.
I have reported the situation to our team. You will receive an email as soon as possible so we can begin troubleshooting.
Feel free to update the thread if you have any new information.
Best regards.

      
                
                
                    
                                                    Wed, 12/04/2024 - 11:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for kind greetings. 
Acronis support was able to resolve. 
This link article was initially provided and may be of some assistance.
How-to-change-MMScurrentMachineID-and-InstanceID
I was able to follow the instructions, generate the guids, and execute the python script as directed. The directions are slightly incomplete. To run acrosh you will need to be in the bin directory under PyShell
C:\Program Files\BackupClient\PyShell\bin

Once I executed the script I got an error:
Traceback (most recent call last):
  File "c:\temp\change_machine_id.py", line 15, in <module>
    import acrort

Support and I were unable to resolve this and they had me try to change the machine id with regedit. 
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings\MachineManager
Put the two guids in InstanceID and MMSCurrentMachineID 
Then Restart the Acronis Core service
The full instructions look like
Remove Device2 agent from Device2. However you can. From the web console or directly on the box.
Install the Agent on Device2 without Registering.
Change the IDs in windows REGEDIT as outlined above.
Restart Acronis Core Windows Service
Register Device2. 

Device1 and Device2 should exist in Devices listing on web console.
-RW

      
                
                
                    
                                                    Wed, 12/04/2024 - 22:24
                                                                            
                                
                            
                                            
                                            
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            RW Smith wrote:

Thank you for kind greetings. 
Acronis support was able to resolve. 
This link article was initially provided and may be of some assistance.
How-to-change-MMScurrentMachineID-and-InstanceID
I was able to follow the instructions, generate the guids, and execute the python script as directed. The directions are slightly incomplete. To run acrosh you will need to be in the bin directory under PyShell
C:\Program Files\BackupClient\PyShell\bin

Once I executed the script I got an error:
Traceback (most recent call last):
  File "c:\temp\change_machine_id.py", line 15, in <module>
    import acrort

Support and I were unable to resolve this and they had me try to change the machine id with regedit. 
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings\MachineManager
Put the two guids in InstanceID and MMSCurrentMachineID 
Then Restart the Acronis Core service
The full instructions look like
Remove Device2 agent from Device2. However you can. From the web console or directly on the box.
Install the Agent on Device2 without Registering.
Change the IDs in windows REGEDIT as outlined above.
Restart Acronis Core Windows Service
Register Device2. 

Device1 and Device2 should exist in Devices listing on web console.
-RW


Hello!
Thank you for updating the thread.
The information may be useful for other users.
Best regards.

      
                
                
                    
                                                    Thu, 12/05/2024 - 06:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
