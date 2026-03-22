# Long-term backup storage solution?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/long-term-backup-storage-solution

## Original Post
**Author:** Unknown

Long-term backup storage solution?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Is there any kind of storage available to use to store data for long term?
Acronis standard storage is very usefull for data that has a "live" state and is recently accesed or created, but there is another kind of data that is never changed once it has been backed up. It would be very helpfull to have any option to "archive" that kind of data to a some "cold storage" less priced.
Is there any way to do this with Acronis actually?
 
Thank you.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/06/2024 - 21:58

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
That's complicated because the Acronis Cyber Protect Cloud requires network connections, as the management server runs in the data center and not on-premise, so cold storage is not possible.
You could try changing the retention rules for certain backups to keep them for a longer term: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#retention-rules.html#kanchor691
You can also check the immutable storage feature, where deleted backups are archived according to your retention rules: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#immutable-storage.html#kanchor600
Best regards.

      
                
                
                    
                                                    Fri, 06/07/2024 - 12:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
