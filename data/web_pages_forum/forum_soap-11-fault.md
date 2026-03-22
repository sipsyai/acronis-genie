# SOAP 1.1 Fault

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/soap-11-fault

## Original Post
**Author:** Unknown

SOAP 1.1 Fault

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I got this error when i try to backup one of my account. Can you help ?
SOAP 1.1 fault: SOAP-ENV:Client[no subcode]
"A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.
"
Detail: connect failed in tcp_connect()
It's an ESXi agent
Thanks,

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/24/2016 - 08:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kevin,
Thank you for your posting! "SOAP 1.1 fault: SOAP-ENV:Client[no subcode] Detail: connect failed in tcp_connect()" is a general communication error. The issue is that the Agent for VMware is unable to connect to https://[hostname_or_IP]/sdk address, i.e. to the specified ESX(i) host or the vCenter. Please make sure that the specified ESX(i) host/vCenter is accessible through the network interfaces available to Acronis Agent (via 'ping' command for example). If the issue perists, I would recommend to raise a support ticket.
Thank you,

      
                
                
                    
                                                    Mon, 06/27/2016 - 14:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
