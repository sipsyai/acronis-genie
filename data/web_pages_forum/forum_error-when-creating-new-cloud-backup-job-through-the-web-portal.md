# Error when creating new cloud backup job through the web portal

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-when-creating-new-cloud-backup-job-through-web-portal

## Original Post
**Author:** Unknown

Error when creating new cloud backup job through the web portal

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            While trying to create a new backup job through the web portal I receive the error:
HTTP error: GET on 'http://accountsrv.service.consul/api/1/users/122841/' failed with code 500.
Error code 0x02910012
 
Additional info:
------------------------
Error code: 18
Module: 657
LineInfo: 0x57D76ED4D7C6DB91
Fields: {"$module":"ams_core_protection_addon_lxa64_5193"}
Message: HTTP error: GET on 'http://accountsrv.service.consul/api/1/users/122841/' failed with code 500.
 
 
I am receiving this for all of our clients. I am not too familiar with the URI accountsrv.service.consul as it is not pingable and doesn't resolve to anything. Is anyone else seeing anything like this?
 
Update: It seems I am unable to adjust the schedules from the Webportal as well, although I can still configure the settings.
 
Also unable to log into any of my client's groups directly because I receive this error:
 
An error occurred during the application initialization.
Additional info is:
500 : INTERNAL SERVER ERROR : https://us-baas.acronis.com/bc/api/ams/session?_dc=1506968770519


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 10/02/2017 - 17:34

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello David,
My name is Eugene.
I'm from Acronis Service Provider Support team.
I checked our internal notes and found that issue is caused by the fact that account has multiple email addreses for notifications.
Solution is to change to single email.
The behavior is addressed in future Acronis Backup Cloud releases.
---
Best Regards,
Eugene Tanasiev

      
                
                
                    
                                                    Mon, 10/02/2017 - 23:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you, Eugene. That seems to have fixed the issue.

      
                
                
                    
                                                    Thu, 10/05/2017 - 12:30
