# Expired proxy  error during installation

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/expired-proxy-error-during-installation

## Original Post
**Author:** Unknown

Expired proxy  error during installation

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jopit
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
During the installation of the Acronis Cyber Protect agent, an error appears about an expired proxy. Indeed, an encrypted communication software uses proxy setting that conflict with the Acronis agent. Is there any parameter to set to bypass this proxy?
Thanks in advence

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/12/2023 - 08:23

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi jopit,
Proxy must be configured to allow all Acronis ports, not only the default 443. If there is a proxy server in the network, test connection to Acronis servers using telnet: required IP addresses and ports can be found in Acronis Cyber Protect Cloud: access ports and hostnames.
Please refer to https://kb.acronis.com/content/47678 for more details. If the issue still persists, I'd recommend raising a support ticket, so that our engineers can examine the configuration. 

      
                
                
                    
                                                    Fri, 01/13/2023 - 11:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
