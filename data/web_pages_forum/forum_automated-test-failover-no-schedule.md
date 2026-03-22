# Automated test failover - no schedule

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/automated-test-failover-no-schedule

## Original Post
**Author:** Unknown

Automated test failover - no schedule

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Patrick Hardy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
 
I have several standby servers in DR. I enable the Automated test failover monthly but I dont have any stats.
How to mkae sure it's working and get the actuel screenshot to validate server was able to start?
 
Automated test failover 
Schedule: Monthly
Screenshot timeout 30 min
Last start:-
Last status:-
Next start: To be defined

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/30/2024 - 19:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Patrick,
Welcome to our community.
Please review the following user guide: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#automated-test-failover.html#kanchor367
All the information regarding automated test failover is available there.
Please note that, in very rare cases, automated test failover might be skipped and not performed at the scheduled time. This is because production failover has a higher priority than automated test failover, so the hardware resources (CPU and RAM) allocated for automated test failover might be temporarily limited to ensure enough resources for a concurrent production failover.
If automated test failover is skipped for some reason, an alert will be raised.
If you face any issues with this process, please raise a ticket with our support or contact your service provider so we can investigate and assist you: https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Wed, 01/31/2024 - 17:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
