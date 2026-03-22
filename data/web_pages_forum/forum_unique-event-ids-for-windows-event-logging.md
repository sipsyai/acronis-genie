# Unique Event ID's for Windows Event Logging

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/unique-event-ids-windows-event-logging

## Original Post
**Author:** Unknown

Unique Event ID's for Windows Event Logging

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good afternoon all,
 
We're currently experimenting with integrating Acronis Event Logging via Windows Event Viewer into a 3rd Party remote management console.
 
The issue we are having is, it appears Acronis only outputs a single Event ID of "1" regardless of the actual event that took place.
 
My question is - are (or would) Acronis looking to change this so the reported Event ID is relevant to the Event that took place?
 
I have attached a screen shot
 
Many thanks,
 
Phil

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Event Log Acronis.JPG

                      721.48 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/11/2019 - 13:32

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
Yes, currently all of our events have the Event ID of 1, which limits the possibility of parsing our events or using them with the third party software. There are plans to improve system event logging (internal ID for reference ABR-57883), I've added your feedback as a vote for this feature request. 
Thank you, 

      
                
                
                    
                                                    Tue, 02/12/2019 - 09:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks Ekaterina, that's appreciated.
 
Kind regards,
 
Phil

      
                
                
                    
                                                    Tue, 02/12/2019 - 17:35
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
