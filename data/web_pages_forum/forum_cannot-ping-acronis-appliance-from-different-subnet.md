# Cannot ping Acronis appliance from different subnet

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cannot-ping-acronis-appliance-different-subnet

## Original Post
**Author:** Unknown

Cannot ping Acronis appliance from different subnet

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    whoami
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello everyone,
 
We recently acquired an Acronis Cyber Protect Cloud device. We also have a test server (hyper-v) that is on a different subnet in our network. I tried restoring a backup to that test server from the acronis cloud portal, but the restore failed. I also cannot ping the NAS device (both using FQDN and IP) from my test server.
I confirmed that our firewall is allowing the packets between each subnet. I believe there may be something configured on the Acronis device that is rejecting connections from outside its own subnet. I am able to ping and connect to the backup's network share when I'm on the same subnet.
I also made sure I could connect to other devices from my test server that are on the same subnet as the Acronis device. The issue seems to be on the Acronis device, I believe.
 
Any ideas on how to fix this?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/09/2023 - 16:54

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Whoami.
Welcome to the forum.
Please run the Connection tool in the machine where those network issues are happening: https://kb.acronis.com/content/47678
If the outputs reveals some error you should open the respective port/IP otherwise the recovery will fail.
When doing recovery/restore with reboot, there are sometimes unexpected imports/inheritance/discovery of DNS and IP settings, which do not match the target machine's/agent's network environment. This is one of the reasons why it's usually best to use the Bootable Media (ISO, can be flashed onto a USB stick as well, of course) -- either the standard/default Linux-based one (which is directly downloadable from your tenant's web console, from the same place where you donwload the agent installers), or the WinPE-based one which you can build via the Builder tool (and customize network settings as well, if you wish) -- that way there is full control of network settings: nothing gets inherited from anywhere, and the operator can select either atomic DHCP or set IPs/DNS servers manually, as appropriate for the target environment/network.
For bare-metal recovery, using the Bootable Media is often the most flexible and most straightforward way of doing such restores.
 Bootable media is covered quite extensively in the User Guide sections at https://www.acronis.com/en-us/support/documentation/CyberProtectionServ… .
Awaiting your feedback about the network evironments/what this DNS IP is.
Thanks in advance!

      
                
                
                    
                                                    Wed, 05/10/2023 - 07:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
