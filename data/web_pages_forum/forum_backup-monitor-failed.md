# Backup Monitor Failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-monitor-failed

## Original Post
**Author:** Unknown

Backup Monitor Failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We installed a web server on port 80 on one of our servers but since then the Backup Monitor has failed.
I've just tried upgrading it but am seeing the same problem.
I would reinstall, but I don't want to lose the file retention on this job.
Any ideas great appreciated.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/09/2017 - 09:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tried running the port checker tool and it reports everything as fine
Starting verification for  DC-LIVE-GUST02 on 1510226565

Verifying connection to Front End Servers
Performing Name Resolution for: cloud-fes-eu1.acronis.com...SUCCESS!
Verifying connection to 62.138.203.218 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.218 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.219 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.219 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.217 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.217 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.213 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.213 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.216 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.216 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.220 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.220 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.212 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.212 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.215 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.215 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 62.138.203.214 on port 44445...SUCCESS!
Verifying connection stability to  62.138.203.214 on port 44445...
Connection was verified. Packets Success rate 50/50 
Verifying connection to Registration Servers
Performing Name Resolution for: cloud-rs-eu1.acronis.com...SUCCESS!
Verifying connection to 85.25.240.132 on port 55556...SUCCESS!
Verifying connection stability to  85.25.240.132 on port 55556...
Connection was verified. Packets Success rate 50/50 
Verifying connection to RPC Servers
Performing Name Resolution for: web-api-tih.acronis.com...SUCCESS!
Performing Name Resolution for: web-api-vmp.acronis.com...SUCCESS!
Performing Name Resolution for: web-api-tie.acronis.com...SUCCESS!
Verifying connection to 69.20.59.84 on port 443...SUCCESS!
Verifying connection stability to  69.20.59.84 on port 443...
Connection was verified. Packets Success rate 50/50 
Verifying connection to 69.20.59.83 on port 443...SUCCESS!
Verifying connection stability to  69.20.59.83 on port 443...
Connection was verified. Packets Success rate 50/50 
 
 

      
                
                
                    
                                                    Thu, 11/09/2017 - 11:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Now resolved. It was a Trial customer. Set to Production. I guess the trial period had expired?

      
                
                
                    
                                                    Thu, 11/09/2017 - 11:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Neil,
I'd report the issue to the support team by sending an email to mspsupport@acronis.com. Only Service Provider Support team can check the status of your account.
 
Thank you!

      
                
                
                    
                                                    Tue, 11/14/2017 - 11:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
