# How to fix error the specified host is managed by another agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-fix-error-specified-host-managed-another-agent

## Original Post
**Author:** Unknown

How to fix error the specified host is managed by another agent

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cao Hung
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Master,
I would like to ask, why i can't do recover my backup to virtual machine..
I want to restore a backup from the old device to the new device and get an error"the specified host is managed by another agent only virtual machines whose backups are located in the cloud storage or on a network share can be recovered to a host managed by another agent" 
Code 15100
Thanks and Regards,

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/09/2024 - 07:23

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Cao,
Welcome to the forum!
The message indicates that you're browsing the backups (recovery points) from an agent that doesn't have access to the target ESXi host. To ensure that the correct agent is selected, go to the "Backups" section of the web console UI, then select the backup location and perform the recovery from there. Avoid checking the recovery points from the "Recovery" tab in the "Devices" section while selecting the VM. Note that if the backup location is a local folder on one of the agents (for example, Locally Attached Storage), you won’t be able to recover to another ESXi host. The backup must be located on a network share. You can share the location and then add it as a new one from the "Backups" section.
If you encounter any issues during the process, please contact our support at https://kb.acronis.com/content/8153 or reach out to your service provider.
Best regards.

      
                
                
                    
                                                    Fri, 08/09/2024 - 10:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
