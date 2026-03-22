# Unable to register with on prem system

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/unable-register-prem-system

## Original Post
**Author:** Unknown

Unable to register with on prem system

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    ej
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
We are new to Acronis and thus far have been using the Cyber Protect Cloud portal.
As there are features only available in the "on-prem" version, we have installed this (on linux).
The problem we are having is that we are unable to register a device against it.
 
I have installed the Agent on a Windows laptop, and tried manually registering it on the command line, using the correct hostname (for our on-prem system) and with a sufficiently entitled user.
All firewall ports between the device and management server are open, but nothing happens.
The command exits without an error, and if I watch net traffic on the management server, I can see activity (so I know the laptop "talks" to our on-prem server).
But nothing... no new device is registered.
 
I have gone through the knowledgebase, but this problem doesn't appear to be addressed.
 
Any tips?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/03/2021 - 14:45

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello 
thank you for your posting! I'd start with the troubleshooting steps outlined in 63130: Acronis Cyber Protect Cloud: troubleshooting Agent registration issues and shall the issue persist, open a support ticket for investigation. We'd need to examine the Agent's logs to see the real cause for the issue.

      
                
                
                    
                                                    Mon, 05/10/2021 - 10:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
