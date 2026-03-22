# Test Restore

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/test-restore

## Original Post
**Author:** Unknown

Test Restore

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi All
I have 3 Windows Server VMs hosted on Citrix and backed up using the standard Acronis Windows agent.
I need to perform test restores to another device, e.g. Hyper-V on my workstation. What is the best way to do this without bringing duplicate machines onto our network?
I have downloaded Bootable Media and got it running in Hyper-V. Is it safe to use the registration token, or will I end up with duplicate machines in the Acronis console? Also, the bootable agent needs network connectivity to do the restore so I can't do a completely offline restore
Any advice or links to a process to achieve this would be greatly appreciated. Thanks.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/24/2024 - 12:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dustin,
Welcome to our community.
Acronis Cyber Protect Cloud has the management server in the cloud, making it impossible to execute recovery offline.
With that said, if you have a Windows agent installed inside each VM, you can recover directly from there. The machine won't be replicated.
You can recover those VMs following this user guide: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#virtual-machine-recovering.html#kanchor351
The duplication of those VMs will only happen under these scenarios: https://kb.acronis.com/content/67774
As for Hyper-V, the process is slightly different. If you are executing an agentless backup (meaning without an agent inside each VM), I advise you to take a look at the following documentation:

https://kb.acronis.com/content/16577


https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#recovering-disks-by-using-bootable-media.html#kanchor10

Feel free to contact our support at https://kb.acronis.com/content/8153 if you have any questions.
Best regards.

      
                
                
                    
                                                    Wed, 01/24/2024 - 14:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the response Jose. Unfortunately I may have not explained myself fully. I want to be able to restore a Citrix VM backup (using Windows Agent), onto Hyper-V, or even a physical machine. For disaster recovery purposes, I don't want it restored back onto Citrix. What would happen in this scenario if I try to restore to a different location, a machine that already exists in Cyber Protect Cloud? Can I restore offline with no network connection?

      
                
                
                    
                                                    Wed, 01/24/2024 - 15:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dustin Bunyan wrote:

Thanks for the response Jose. Unfortunately I may have not explained myself fully. I want to be able to restore a Citrix VM backup (using Windows Agent), onto Hyper-V, or even a physical machine. For disaster recovery purposes, I don't want it restored back onto Citrix. What would happen in this scenario if I try to restore to a different location, a machine that already exists in Cyber Protect Cloud? Can I restore offline with no network connection?


Hello! This product doesn't work offline; a network connection is a prerequisite. The management server is centralized in the cloud, and without it, the recovery can't be done. If you have the VM with the agent for Windows, you can recover it on a new VM or physical machine without problems as long as you have a network.
There are different ways to do it. You can do it from the console, bootable media, or even create a new VM from scratch, install a Windows agent in there, and recover the Centrix VM back to it from the console.
Best regards.

      
                
                
                    
                                                    Wed, 01/24/2024 - 15:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks Jose. So what happens in the Acronis Cloud console when the duplicate machine checks in? Will it not get confused?

      
                
                
                    
                                                    Wed, 01/24/2024 - 16:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dustin Bunyan wrote:

Thanks Jose. So what happens in the Acronis Cloud console when the duplicate machine checks in? Will it not get confused?


Hello!
That shouldn't create problems as long as you don't schedule backups for that same machine in 2 backup plans at the same hour for example.
Best regards.
 

      
                
                
                    
                                                    Thu, 01/25/2024 - 14:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks Jose.
So the solution to performing a test restore of a Citrix hosted Windows VM onto Hyper-V was as follows:
Download bootable media iso and generate a registration token
In Hyper-V, create 2 virtual switches - one configured as External, and the other as Private
Create a new VM, with Secure Boot Disabled, and connected to the virtual switch configured as External.
Configure the VM to use a VLAN ID of an isolated test VLAN configured on your main network. This is just in case you accidentally bring a duplicate machine online on your network.
Set the VM to install from DVD image and specify the downloaded Acronis bootable media iso.
Connect and start the VM, check you have an IP address, then register the media using the registration token.
Select the latest backup, and check all volumes including the MBR. Click OK to begin recovery.
Once complete, and before restarting the VM, change the VM to use the Private switch so it can no longer contact any cloud services which may affect the existing server due to a duplicate server coming online.
Restart the VM
 

      
                
                
                    
                                                    Thu, 02/01/2024 - 10:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dustin Bunyan wrote:

Thanks Jose.
So the solution to performing a test restore of a Citrix hosted Windows VM onto Hyper-V was as follows:
Download bootable media iso and generate a registration token
In Hyper-V, create 2 virtual switches - one configured as External, and the other as Private
Create a new VM, with Secure Boot Disabled, and connected to the virtual switch configured as External.
Configure the VM to use a VLAN ID of an isolated test VLAN configured on your main network. This is just in case you accidentally bring a duplicate machine online on your network.
Set the VM to install from DVD image and specify the downloaded Acronis bootable media iso.
Connect and start the VM, check you have an IP address, then register the media using the registration token.
Select the latest backup, and check all volumes including the MBR. Click OK to begin recovery.
Once complete, and before restarting the VM, change the VM to use the Private switch so it can no longer contact any cloud services which may affect the existing server due to a duplicate server coming online.
Restart the VM
 


Hello Dustin!
Thanks for sharing what helped to execute the recovery fix.
This may help other users.
Best regards.
 

      
                
                
                    
                                                    Thu, 02/01/2024 - 10:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
