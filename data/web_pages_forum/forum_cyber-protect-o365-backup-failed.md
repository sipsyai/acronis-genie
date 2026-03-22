# Cyber protect O365 backup failed.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-o365-backup-failed

## Original Post
**Author:** Unknown

Cyber protect O365 backup failed. 

        
  



    
  


  
          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Leonid Kutepov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey guys, I'm using strato backup based on acronis, I'm trying to backup office 365 mailboxes and sharepoint sites.
I followed the instruction, added organization, check that azure app was created with necessary permission but when I'm trying to backup test mailbox, I got an error.
Cannot back up Microsoft 365 mailbox item 'Id: ***sometoken***= CreatedOn: somedate T14:25:04Z' in folder 'mymail@mycompany.com Calendar/United States holidays': 'context deadline exceeded (Client.Timeout exceeded while awaiting headers)'

I guess that it is not enough some permission, but which exactly I can't find.
Any help is appreciated.
Thank you.
Leonid

      
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/02/2024 - 12:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Melis Freag
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 30
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The error message you’re encountering, ‘context deadline exceeded (Client.Timeout exceeded while awaiting headers)’, typically indicates a timeout issue. This can occur when a service takes too long to respond, often due to network latency or a service being overloaded.

      
                
                
                    
                                                    Tue, 05/07/2024 - 20:56
