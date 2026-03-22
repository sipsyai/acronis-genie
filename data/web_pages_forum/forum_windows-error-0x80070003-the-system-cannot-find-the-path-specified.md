# Windows error: (0x80070003) The system cannot find the path specified

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/windows-error-0x80070003-system-cannot-find-path-specified

## Original Post
**Author:** Unknown

Windows error: (0x80070003) The system cannot find the path specified

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Shabin Suresh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi Team,
We have a V
Windows Hyper-V Server, nowadays this is the error coming. Kindly advise for a solution.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Acronic_Error.png

                      52.91 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Sat, 09/23/2023 - 05:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Welcome to the forum!
The error you mentioned seems to be related to the following KB: https://kb.acronis.com/content/65553.
Please apply all the solutions specified there and follow the troubleshooting steps. The error appears to be connected with the storage where you store your backups; it could be due to connection issues or problems with the storage itself. To further diagnose this, you can run a CHKDSK on the storage, which you can learn more about here: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk?tabs=event-viewer
Additionally, as a test, try editing the backup plan and check if you can select the destination. If you can't, it indicates that the agent can't connect, and you should troubleshoot for local network issues.
If the issue persists after applying all the solutions from the KB and performing these tests, please consider opening a support ticket with us or contacting your Service Provider to do so: https://kb.acronis.com/content/8153
Thanks in advance!

      
                
                
                    
                                                    Mon, 09/25/2023 - 10:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
