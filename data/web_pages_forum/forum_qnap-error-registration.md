# qnap error registration

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/qnap-error-registration

## Original Post
**Author:** Unknown

qnap error registration

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Alessandro Giovannelli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            i have done all things to do in the pdf for istall the agent acronis in the cvber cloud but when execute the command not register the device.can you help me

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      error.jpeg

                      134.26 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Sun, 11/05/2023 - 08:41

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum!
Please ensure that you follow all the steps one by one in this KB article to create the docking station: https://kb.acronis.com/content/62826.
Next, download the following agent and try to install and register it again: https://dl.managed-protection.com/u/baas/4.0/15.0.36119/CyberProtect_AgentForLinux_x86_64.bin.
Also, please note that you need to register the agent using the correct token for Acronis Cyber Protect Cloud/Acronis Cyber Protect 15 in "cloud management" mode:
 
sudo docker exec -it [container name or ID] /usr/lib/Acronis/RegisterAgentTool/RegisterAgent -a https://[Datacenter URL] --token [Registration token] -o register -t [type of registration: local or cloud] 
For example:

 sudo docker exec -it acronis_agent1 /usr/lib/Acronis/RegisterAgentTool/RegisterAgent -a https://eu2-cloud.acronis.com --token 241C-C614-40F6 -o register -t cloud 
(If your datacenter is EU1 or EU8, etc., you must replace the URL with the correct one).
If the issue persists, please ensure that all the required ports are open on the device running the connection tool: https://kb.acronis.com/content/47678 (if the output detects closed ports/IPs, you must open them).
If the issue still persists, please raise a ticket with our support at https://kb.acronis.com/content/8153.
Thank you.

      
                
                
                    
                                                    Mon, 11/06/2023 - 10:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
