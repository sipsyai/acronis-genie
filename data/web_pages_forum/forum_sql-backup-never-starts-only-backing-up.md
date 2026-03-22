# sql backup never starts only backing up

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-backup-never-starts-only-backing

## Original Post
**Author:** Unknown

sql backup never starts only backing up

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            my job sql database have status , backing up but never starts. When i try to stop it doesnt stop. 
 
thanks

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      errosql.jpg

                      167.85 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/25/2018 - 16:14

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey there!
 
Most likely reason is that the necessary ports are blocked.
Check against the followin article to see which ones must by open -> https://kb.acronis.com/content/47189
Test the connection using the Connection Verification Tool (reference article -> https://kb.acronis.com/content/47678) and share the output here. Note that if you have strict firewall rules with Deep Packet Inspection, normal connection would go in and out just find, while SSL connection would be intercepted.
 

      
                
                
                    
                                                    Tue, 10/30/2018 - 15:25
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
