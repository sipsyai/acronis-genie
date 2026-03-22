# m365 license seats do not match with acronis billing seats

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/m365-license-seats-do-not-match-acronis-billing-seats

## Original Post
**Author:** Unknown

m365 license seats do not match with acronis billing seats

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jovica Zivkovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear all,
I need advice regarding strange invoice billings from Acronis.
Our licensing plan is per workload, so all our licensed M365 users are included in the backup.
A few months ago we removed M365 licenses from a dozen users, but Acronis is still billing them with the explanation that they still have access to some SharePoint sites and have some type of hidden OneDrive.
Is this a feature or a bug? 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/03/2023 - 14:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jovica,
Thank you for contacting us.
Regarding the situation you just mentioned, it may be an expected behavior. Please refer to the following KB: https://kb.acronis.com/content/71732.
If you are backing up a SharePoint or Teams site, each user that has access to the site will be counted, even if this user is not protected separately (such as a mailbox or OneDrive). Seats will also be taken if the user has OneDrive or a personal mailbox: https://kb.acronis.com/content/69686.
If you believe this is not the case, please raise a ticket with our support or request your Service Provider to do so, providing screenshots of the incorrect counting from your O365 management account, comparing them to the backup console: https://kb.acronis.com/content/8153.
Thanks in advance!

      
                
                
                    
                                                    Mon, 11/06/2023 - 10:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
