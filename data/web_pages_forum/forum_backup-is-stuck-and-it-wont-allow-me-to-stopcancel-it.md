# Backup Is Stuck and it won't allow me to stop/cancel it

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-stuck-and-it-wont-allow-me-stopcancel-it

## Original Post
**Author:** Unknown

Backup Is Stuck and it won't allow me to stop/cancel it

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cheyenne Beard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a backup that has been running for 146 hours and when I attempt to stop or cancel the plan it does nothing. It doesn't give an error message; it just doesn't do anything at all. The backup is a SQL DB only backup set to backup 4 individual DB's. 
I was able to cancel the backups individually on the DB's but the plan is still stuck at 100%. On the server the Acronis Cyber Protect Monitor process had spiked and caused my memory to stay at 96% so I restarted the service, and that fixed the spike, but the backup job still is stuck. 
I also selected the "stop all backups" option in Acronis Cyber Protect and it didn't resolve the issue. All of the backups on this server are failing because of this. Any assistance is greatly appreciated.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 06/07/2024 - 14:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
To cancel it, I suggest you restart the services in the Task Manager, kill them in the Command Prompt, or reboot the machine (for example, restart the service mms.exe as it's the main one).
Please note that even if you restart the services, it can happen that the console still displays that a backup is running (even if this information is incorrect). If that's the case, please raise a ticket with the team or contact your service provider so we can help with the issue: https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Fri, 06/07/2024 - 18:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
