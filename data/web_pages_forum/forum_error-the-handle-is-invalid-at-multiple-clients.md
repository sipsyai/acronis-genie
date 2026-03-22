# Error - "The handle is invalid" at multiple clients

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-handle-invalid-multiple-clients

## Original Post
**Author:** Unknown

Error - "The handle is invalid" at multiple clients

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Christiaan de Wet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good day Forum!
Starting on January 9 2019, we are experiencing failed backups over multiple clients with the following error:
Windows error: (0x80070006) The handle is invalid 
I have tried updating the agents to resolve the issue, but this does not seem to be working.
Is this a known problem? Is anyone else experiencing this?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/15/2019 - 15:49

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christiaan de Wet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The issue has been resolved.
In our case it was due to Windows Updates, KB4480970, that broke SMB on our backup storage.
Uninstalling this resolved the issue.

      
                
                
                    
                                                    Tue, 01/15/2019 - 21:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Christiaan,  thank you for the update and sharing the information of how you resolved this issue which will be of value for other users.

      
                
                
                    
                                                    Tue, 01/29/2019 - 13:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
