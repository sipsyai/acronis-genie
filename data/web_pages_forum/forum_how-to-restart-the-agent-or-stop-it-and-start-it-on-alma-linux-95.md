# How to restart the agent (or stop it and start it) on Alma Linux 9.5?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/how-restart-agent-or-stop-it-and-start-it-alma-linux-95

## Original Post
**Author:** Unknown

How to restart the agent (or stop it and start it) on Alma Linux 9.5?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Justin Wyllie
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am trying;
service acronis_mms start
This gives: 

Redirecting to /bin/systemctl start acronis_mms.service
 
But when i do ps aux | grep acronis 
I see all the processes still running.
Thank you
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/07/2024 - 14:59

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
What is the ultimate goal of your actions? Are you looking to simply start and stop the services manually? Is the issue that the MMS doesn’t work when you stop it? Is the machine a regular agent or the management server itself?
What is the exact version of the product you’re using? Please note that Acronis Cyber Protect 16 does not support Alma Linux 9.5. You can find more information here: Acronis Cyber Protect Documentation.
Best regards.
 

      
                
                
                    
                                                    Mon, 12/09/2024 - 07:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
