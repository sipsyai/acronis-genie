# SOLVED: Access is denied

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/solved-access-denied

## Original Post
**Author:** Unknown

SOLVED: Access is denied

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Palomares
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I have some customers which backup to Acronis cloud that suddenly the backups fails with 'Access is denied' error.
Also, when trying to refresh the backup list, it ask for credentials for folder '/' but we don't have such credentials (it seems these are the cloud credentials, which we didn't manage).
How can we proceed?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/14/2022 - 09:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Palomares
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
The issue has been resolved by removing the certificates on the clients. I followed this kb: https://kb.acronis.com/content/60082
But be aware that you cannot remove the certificate with the acronis services running, you have to stop all processes (there's one you cannot stop, just ignore it), then remove the certificates and restart the processes.
After that, wait a few minutes and try to refresh the backup storage on the console, selecting the affected client, and the certificates will regenerate and the backup will be working correctly.

      
                
                
                    
                                                    Fri, 07/15/2022 - 09:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I believe this KB article describes this issue and the workaround you posted: https://kb.acronis.com/content/67790
 

      
                
                
                    
                                                    Fri, 07/15/2022 - 13:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear David Palomares,
Thank you very much for sharing the solution.

      
                
                
                    
                                                    Tue, 09/20/2022 - 13:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
