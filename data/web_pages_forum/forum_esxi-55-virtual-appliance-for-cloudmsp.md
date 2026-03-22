# ESXi 5.5 Virtual Appliance for Cloud/MSP

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/esxi-55-virtual-appliance-cloudmsp

## Original Post
**Author:** Unknown

ESXi 5.5 Virtual Appliance for Cloud/MSP

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Sorry if this has been asked before. I can see there is a VA for the full version of Acronis backup, but is there one for the MSP/Cloud version?
I currently have one running on a virtual Windows server within the VCenter but am seeing some issues with it's ability to access certain hard disks. I would prefer a VA if at all possible.
Thanks
Neil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/11/2017 - 07:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Neil,
I'm afraid the Virtual Appliance for VMware is not yet available in Acronis Backup Cloud. This is planned for future versions, preliminary v.8.0.
Could you please clarify the problem with the hard disks? Is LAN-free access allowed to the Agent?

      
                
                
                    
                                                    Wed, 10/11/2017 - 08:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ah that will be it.
What is the best way then if I'm replicating a server to a different site within the same vcenter? Agents on servers on both SANS bth pointint to the VCenter? Or seperate agents for each ESXi machine rather than a single one on the VCenter

      
                
                
                    
                                                    Wed, 10/11/2017 - 09:48
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            >Agents on servers on both SANS bth pointint to the VCenter? 

That is the correct approach in case you install the agent inside a VM on these to hosts.
By default the agents will try to bind with VMs which are located on the same ESXi host as the agent (the VM inside which the agent is installed). This may not happen if there is a big disbalance between the hosts, for example 1 manages 1 VM and another 100 VMs – in this case there could be situation where agent from 2nd ESXi host tries to backup VMs from 1st ESXi host.
If Agent for VMware is installed on a physical host, there will be no automatic binding to the "closest" host, thus also no logic in which agent backs up which VM. In this case please do connect each agent to its ESXi host directly.


      
                
                
                    
                                                    Wed, 10/11/2017 - 14:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rafonso@ondacorp.com.br
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Guys,
We are using Acronis Cloud Backup for ESXi VMWare Hosts and we finded some issues when we try to do Backup in a vCenter environment.
During the installation, we passed username and password from vCenter. The installation process finished with sucess, but, when we try to do a Full Backup Plan, the error appears on our screen:
| error 0x4650: Cannot connect to the host
| line: 0xc61573f663f5d761
| file: k:\3917\enterprise\virtualware\raw\vmware\vixdisklib\vixdisklib.cpp:328
| function: `anonymous-namespace'::LibHolder::Open
| $module: esx_srv_vsa64_3917
2017-10-18 10:58:24:899 3316 E0135003D: Error 0x135003d: Command 'Backing up' has failed.
| trace level: error
| channel: tol-activity#6A56C0EB-1CEC-4BC9-B5B5-D4029ED12BFA
| line: 0x4a8728dc8a1c9534
| file: k:\3917\enterprise\common\tol\gating_activity.cpp:142
| function: Tol::`anonymous-namespace'::BusinessActivityTracker::OnCompleted
| $module: service_process_vsa64_3917
Following the complete logs in attachment.
Someone have been looked this issue?

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      428556-139349.txt

                      62.08 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 10/24/2017 - 12:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
Try to ping the IP of the ESXi host from the machine where the Agent is installed.
If a ping test is successful, check if it is possible to connect using specific ports. You can use telnet to see if you can connect to the port. The involved ports are listed under Step 4 in the following part of the documentation. 
Does the specified user account have the administrative rights on the vCenter? If not, please double check the account has all necessary privileges. 
If both ping and telnet work and the user rights meet requirements listed in the table, I'd recommend raising a support ticket for investigation. 

      
                
                
                    
                                                    Mon, 10/30/2017 - 13:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
