# "Failed to create a snapshot for backup" since agent 24.1 37279

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/failed-create-snapshot-backup-agent-241-37279

## Original Post
**Author:** Unknown

"Failed to create a snapshot for backup" since agent 24.1 37279

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Matt R
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            As title, everything was working fine until the agent auto-updated to 24.1 37279 and since then it always fails with the error:
Failed to create a snapshot for backup.
Failed to find a partition. Path '/'.
The partition snapshot will not be created.
System is Debian Linux

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/12/2024 - 15:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to our community.
The issue may be related to the SnapAPI kernel module.
I would advise you to reboot the device.
If the issue persists, kindly raise a ticket with our support so we can investigate the issue at https://kb.acronis.com/content/8153.
Thanks in advance!

      
                
                
                    
                                                    Tue, 03/12/2024 - 15:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Matt R
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fixed in 24.3.37719

      
                
                
                    
                                                    Sun, 04/21/2024 - 12:25
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Matt R wrote:

Fixed in 24.3.37719


Hello Matt,
Thank you for updating the thread.
This information may be useful to other users.
Best regards.

      
                
                
                    
                                                    Mon, 04/22/2024 - 10:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
