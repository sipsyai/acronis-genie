# Questions about "File Sync & Share "

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/questions-about-file-sync-share

## Original Post
**Author:** Unknown

Questions about "File Sync & Share "

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is there a way to download file directly from link of shared file from linux server cli? For now the only workaround I found is open the link (...eu2-cloud . acronis . com/fc/t/...) in browser of other device with gui, copy the temp. direct link "generate" inside the page and download from linux with:
wget --user-agent=Mozilla --content-disposition -E -c  "...eu2-cloud . acronis . com/fc/node_share_links/download?id=...&token=..."
Another thing: it would be good to have the possibility to have links without expiration, at the moment they always have a time limit that can be set no more than 1 year (this to be added as a feature request if possible please)
Thanks for any reply and sorry for my bad english.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 09/07/2020 - 09:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Victor Batraev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Emilio,
You can download files using API. Please check API reference for details: https://developer.acronis.com/doc/files/v1/reference/index#/http/getting-started

      
                
                
                    
                                                    Mon, 09/07/2020 - 10:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Victor Batraev

Lead Product Manager | Acronis

            
                            
                Products: 
                Acronis Cyber Platform

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Victor Batraev wrote:

Hi Emilio,
You can download files using API. Please check API reference for details: https://developer.acronis.com/doc/files/v1/reference/index#/http/getting-started


FYI, getting the ability to create a separate plan for validation has been requested under the number RM-49. 
I didn't get an ETA on it, though.

      
                
                
                    
                                                    Fri, 01/29/2021 - 09:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
