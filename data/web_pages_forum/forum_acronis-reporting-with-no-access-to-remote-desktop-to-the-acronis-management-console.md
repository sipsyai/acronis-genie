# Acronis Reporting with no access to Remote Desktop to the Acronis Management Console

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-reporting-no-access-remote-desktop-acronis-management-console

## Original Post
**Author:** Unknown

Acronis Reporting with no access to Remote Desktop to the Acronis Management Console

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ludhi Sidikpramana
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Does anyone out there know how to send all the Acronis Reporting on email without Remote Desktop to the Management Console nor open a link to the server as most of the email recipient has no login access to the management console.
Also, we just need those VMs that under Protection only and do not need the rest, for example (see below)
Acronis Report:
VM1 Backup Successfully or some sort
VM2 Backup Failed or some sort ...
VM3 Backup Successfully but with warning or alert or some sort
VM4 Some other basic reporting message ....
....
....
 
I got the emailing part is working so SMTP server set up is working, it just sending only a link to remote desktop to the Management Console.  I was wondering if anyone has done customizing the report so we don't have to Remote Desktop in to the Acronis Management Console just to see the reporting but email just the relevant message to everyone on the list.
 
Thanks

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/14/2024 - 14:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
As far as I can see, you joined a remote session with the team to guide you through the process.
To configure email notifications for the activities of the backup plan included on those machines, you should follow this user guide and add the emails of the users: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_15/#email-notifications-52471.html#kanchor155
Note that it's not possible to create notifications or emails for just one random machine, for example. You either receive them for a specific backup plan or for all the machines added in the console.
For reports, this is what must be followed: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_15/#reports.html
If you have any questions, please follow up with the team in the ticket.
Best regards.

      
                
                
                    
                                                    Fri, 06/14/2024 - 16:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
