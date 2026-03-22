# Run VM error when authenticating to Windows share

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/run-vm-error-when-authenticating-windows-share

## Original Post
**Author:** Unknown

Run VM error when authenticating to Windows share

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Philip Rabensteine
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello all!
A colleague and I have been attempting to get a live version of a virtual machine, Windows Server 2012R2, running from a backup stored on a local windows (SMB) file share on a standalone windows server 2016 host. The 2012 VM is running on top of an ESXi cluster and we have it protected using the Acronis Backup Cloud "VMWare ESXi" virtualization host agent.
It's backing up to the windows share just fine. We also have the acronis HyperV agent installed on the windows server 2016 host. However when I attempt to take one of those backups and "Run as VM" from the windows share, on the windows 2016 host using HyperV, I am prompted to Specify credentials for the windows share. After supplying these the prompt returns an error - "The credentials for '//<ourwindowsserverIPaddress>/vmbackups/' are incorrect."
We have double checked credentials from accessing windows share from our workstations, and the server settings for the share locally. Everything appears to be functional in order to access this share with the same user we are attempting to supply to Acronis for running the VM. 
We believe this is an authentication issue. We have found a functional work around by taking a backup of the windows 2016 share to Acronis Cloud. We are then able to see the backup files for the ESXi backup deposited there. After selecting the backup(for 2012VM), we are able to successfully "Run VM" on the 2016 HyperV host choosing default settings along the way after ensuring that we had the HyperV host chosen as the Target host, and supplied a VM name. This spun up (it did take quite a while) and is now running. 
Is there a known issue with SMB authentication when trying to do a live test restore? Are there any pointers for what we may be missing? We would ideally like to just be able to do these live server tests without having to backup the windows share additionally. 
Thanks,
Philip

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/20/2019 - 20:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Philip Rabensteine
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I had to move this as I posted it to the wrong Forum landing place. Sorry in advance admins!!! Thank you for your help! :)

      
                
                
                    
                                                    Wed, 03/20/2019 - 20:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Philip and welcome to our forums!
 
As I understand, you have a VMware VM backed up to a network share.
Then you want to run such a VM from it's backup archive to a Hyper-V server as another VM.
 
You described the scenario pretty well and there are no known issues with authentication like that.
It has to be noted, just for the sake of clarity, that, if I got the scenario correctly, when Backup up this VM, it's the agent for VMware machine that accesses the network share, while when Recovering the VM, it's the Hyper-V machine that connects to the share. - perhaps a connection limit on the share was exceeded or a user was not recognised.
 
In general, I would advise you to submit a ticket to us with information about the user and exact example of such behavior.
When seeing an error in the GUI of the Backup Console, click "Details" button to expand the error message - be sure to copy and paste that when submitting a ticket.
 

      
                
                
                    
                                                    Mon, 03/25/2019 - 16:53
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Philip Rabensteine
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Fedor!
Thank you for your reply. 
Yes, you understand the scenario correctly indeed. I was wondering about connection limits, or perhaps an authentication lock-out due to typo. 
We just ran through testing this again after giving it a break for several days with a reboot of the 2016 host in between. At this time we're still getting the error - See attached png.

Interestingly enough there's no "Details" button present to expand this particular error message. Additionally we did verify share authentication was working from the server and from a workstation. 
I will proceed with a support ticket. Thanks again for your help! If we find a resolve with support I'll be sure to update this thread.
Philip

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      493831-165880.PNG

                      14.33 KB
                  
          
    

                    
    
                
                
                    
                                                    Thu, 03/28/2019 - 13:19
