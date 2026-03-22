# Acronis Service Fails to Start on CentOS After System Crash

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-service-fails-start-centos-after-system-crash

## Original Post
**Author:** Unknown

Acronis Service Fails to Start on CentOS After System Crash

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ethan Carter
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I installed Acronis on a CentOS Linux machine, but after a system crash, the service fails to start.
When I run the command:
sudo service acronis_mms start
 
nothing happens — the service doesn't start.
Checking the status using:
sudo service acronis_mms status
 
shows that the service is stopped.
Any advice on how to troubleshoot or get it running again would be appreciated.
 


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 04/09/2025 - 09:02

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Welcome to the forum!
This likely indicates that the service is crashing or being blocked by something.
We recommend raising a support ticket with our team or your service provider, as we'll need to review the logs to determine the root cause of the issue.
Best regards,

      
                
                
                    
                                                    Wed, 04/09/2025 - 10:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ethan Carter
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for the warm welcome and the quick response.
I'll go ahead and open a support ticket so the team can take a closer look at the logs and help identify what's causing the issue. Please let me know if there’s any specific information or log files I should include when submitting the ticket.
Appreciate your support!
Best regards,
Ethan


      
                
                
                    
                                                    Wed, 04/09/2025 - 11:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ethan Carter
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            

      
                
                
                    
                                                    Wed, 04/09/2025 - 11:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ethan Carter wrote:

Hello,
Thank you for the warm welcome and the quick response.
I'll go ahead and open a support ticket so the team can take a closer look at the logs and help identify what's causing the issue. Please let me know if there’s any specific information or log files I should include when submitting the ticket.
Appreciate your support!
Best regards,
Ethan



Hello!
The team usually requests the system report and debug logs https://care.acronis.com/s/article/69532-Acronis-Cyber-Protect-Cloud-ho…
Best regards.

      
                
                
                    
                                                    Thu, 04/10/2025 - 09:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
