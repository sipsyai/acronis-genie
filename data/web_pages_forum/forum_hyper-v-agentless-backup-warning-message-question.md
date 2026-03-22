# Hyper-V Agentless backup - Warning message question

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/hyper-v-agentless-backup-warning-message-question

## Original Post
**Author:** Unknown

Hyper-V Agentless backup - Warning message question

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good evening all,
 
Whilst running a backup on a VM (which runs onsite MS Exchange for our customer), we had the following Warning Message:
 
Failed to obtain descriptions of class '\\MCI-HV2\root\virtualization\v2:Msvm_VirtualEthernetSwitch.CreationClassName="Msvm_VirtualEthernetSwitch",Name="E6D1381B-3071-4C65-A381-D7767FC965D7"'.
Windows error: (0x80041002) Failed to obtain descriptions of class '\\MCI-HV2\root\virtualization\v2:Msvm_VirtualEthernetSwitch.CreationClassName="Msvm_VirtualEthernetSwitch",Name="E6D1381B-3071-4C65-A381-D7767FC965D7"'.
 
I can read enough into this to see that the Virtual Switch Config may not be getting captured? But I'd appreciate any insight as to what may be causing this if that is possible from the above output?
 
Kind regards,
 
Phil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/12/2019 - 17:38

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
There was a discussion on a similar problem: backup of a virtual machine was failing with the same error message after migrating this machine from one host to another through Live Migration feature. There the user was able to solve the problem with removing two network interfaces of problematic VM and adding new ones using Failover Cluster Manager. After this operation backup succeeded. 
Another user mentioned that re-adding the network adapter helped.
If the issue still persists, I'd recommend raising a support ticket for investigation. 

      
                
                
                    
                                                    Tue, 02/19/2019 - 13:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
 
Many thanks for the feedback - we will investigate this further and post our findings if we can identify what fixes the issue.
 
Kind regards,
 
Phil

      
                
                
                    
                                                    Thu, 02/21/2019 - 17:03
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
