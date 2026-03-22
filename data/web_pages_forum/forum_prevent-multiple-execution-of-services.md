# Prevent multiple execution of services

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/prevent-multiple-execution-services

## Original Post
**Author:** Unknown

Prevent multiple execution of services

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello support team,
when i install the Acronis Agent on an RDS server, I have already left the tray monitor in order not to reduce the performance of the server.
Is it possible to have all needed other services only run once and not by each user who is logged on the RDS?
It is about the services  "Acronis Scheduler Service Helper" and "Acronis TIP Mount Monitor".
(to understand what i mean - look at the picture)
Thanks and have a nice day

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Acronis-1.jpg

                      1.1 MB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/05/2018 - 14:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes, 
try to apply the solution from the article Multiple Instances of TimounterMonitor.exe, TrueImageMonitor.exe and schedhlp.exe Processes. It is rather old, but still should be valid. 
Please let me know, if that helped. 

      
                
                
                    
                                                    Tue, 11/06/2018 - 13:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
the solution of the article helped.Thank you for the support.

      
                
                
                    
                                                    Thu, 11/08/2018 - 11:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the update / feedback, glad the article did the trick for you.

      
                
                
                    
                                                    Thu, 11/08/2018 - 13:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
