# Hypervisor level backup & targeted host

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/hypervisor-level-backup-targeted-host

## Original Post
**Author:** Unknown

Hypervisor level backup & targeted host

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good afternoon all,
We currently have a situation wherein we have 2 "live" HyperV Hosts and 1 "Replica" Host.
All 3 Hosts have the HyperV agent installed.
We have been backing up with a plan created to capture the VM's on the Replica Host from a Hypervisor level.
Now, in the past we have seen the situation where if one Host is removed, the backup will automatically repoint at the identical VM on a seperate Host (I guess due to the WMI ID being the same on the VM).
My question is twofold:
1. Is there any way of forcing the backup plan to target a specific Host?
2. I have tried turning off the Acronis services on the Host I don't want to back up from and the Host has gone dark on the management portal - but I've lost the ability to manually trigger that backup now - will it automatically repoint at the backup runtime?
Many thanks for your help,
Phil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/01/2019 - 11:49

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
thank you for posting on Acronis forums!
The root cause of the behavior you see is that Acronis Backup identifies (and distinguishes between them) the Hyper-V VMs using WMI ID which is identical for original VM and it's replica created natively by Hyper-V.
In Acronis Backup 12.5 Update 4, there was a new identification method added, which allows handling these scenarios.
If you are already using Update 4 and still experience this issue, please contact Acronis Support Team for further assistance with the issue (the root cause might be different in your case).

      
                
                
                    
                                                    Fri, 11/01/2019 - 14:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             Hi Maria,
 
Thanks for your response, I think this may have been posted in the wrong forum? We're using Acronis Cyber Cloud - shall I just repost there or can you move this post?
 
Kind regards,
 
Phil
Maria Belinskaya wrote:

Hello Phil,
thank you for posting on Acronis forums!
The root cause of the behavior you see is that Acronis Backup identifies (and distinguishes between them) the Hyper-V VMs using WMI ID which is identical for original VM and it's replica created natively by Hyper-V.
In Acronis Backup 12.5 Update 4, there was a new identification method added, which allows handling these scenarios.
If you are already using Update 4 and still experience this issue, please contact Acronis Support Team for further assistance with the issue (the root cause might be different in your case).



      
                
                
                    
                                                    Fri, 11/01/2019 - 15:10
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
sorry for the delayed response! I've clarified your question with the dedicated team and here their reply
The main difficulty with Hyper-V replicas stems from the fact that both original and replicated Virtual Machine will have same UUID. For this reason, Acronis Agent for Hyper-V has no way of distinguishing between the original and replicated machines which might cause issues with machine detection. 
A new feature that would allow correct identification of Agentless (Agent is not inside VM) virtual machines is in development.
In the meantime, you may want installing the Agent inside the virtual machine that would be replicated and backing it up like any other machine with Agent installed inside of it. This way, there won't be any issues caused by duplicate entries. 
Also, generally,  in case of clustered VM hosts environment:
VMs might migrate from one node to another for a different reasons (node unavailability, load balancing). Therefore in this case it's recommended to install and Agent for Backup on each node to cover all the VMs hosted on it.
The Agent for Hyper-V is designed in such a way that it uses the information from the installation of Hyper-V.
Within a Clustered environment we need to make sure the Agents for Hyper-V are installed on the nodes and they access the same information using the WMI. 

      
                
                
                    
                                                    Tue, 11/12/2019 - 16:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
