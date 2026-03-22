# Cyber Protect Cloud Agent automatic update fails

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-cloud-agent-automatic-update-fails

## Original Post
**Author:** Unknown

Cyber Protect Cloud Agent automatic update fails

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have 3 VMs running Windows Server 2022 and always seem to have a problem with at least one of them when Acronis Cyber Protect Cloud tries to update the agent.
"Task timeout expired. The agent that is responsible for processing the task is not accessible"
Also, when this happens, Remote Desktop service stops responding so I can't access the server and try to manually install. Each time this happens we have to schedule downtime to restart the VM.
Has anyone experienced this? Does anyone have a solution? Thanks in advance

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/11/2023 - 14:25

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dustin!
Please note that this issue used to happen with old builds of the agent. If you use an old version please try to update the agents manually one by one.
As alternative, Please try the following workaround 
Stop Acronis Agent Core service (this will also automatically stop Acronis Managed Machine Service);
Stop Acronis Update Controller service
Wait for a few minutes.
Start aakore service (Acronis Agent Core Service)
Start mms service (Acronis Managed Machine Service)
Start Acronis Update Controller service
If the issue persists, please raise a ticket with our support at https://kb.acronis.com/content/8153 .
Best regards.

      
                
                
                    
                                                    Wed, 10/11/2023 - 14:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dustin Bunyan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks Jose. We restarted the whole server and it made no difference. On further investigation it looks like maybe Acronis has reset the firewall rules to default. The Remote Desktop rules were disabled, and a custom database rule that was there before, was completely missing. We'll log a support ticket.

      
                
                
                    
                                                    Mon, 10/16/2023 - 10:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dustin Bunyan wrote:

Thanks Jose. We restarted the whole server and it made no difference. On further investigation it looks like maybe Acronis has reset the firewall rules to default. The Remote Desktop rules were disabled, and a custom database rule that was there before, was completely missing. We'll log a support ticket.


Thanks for the information.
Please update the thread with the solution provided by our support. This may help the other users.
Best regards. 

      
                
                
                    
                                                    Mon, 10/16/2023 - 13:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
