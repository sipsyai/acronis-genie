# Best Approach for Deploying Acronis Appliance?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/best-approach-deploying-acronis-appliance

## Original Post
**Author:** Unknown

Best Approach for Deploying Acronis Appliance?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Pawel Wojcik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a situation where I need to deploy an Acronis appliance on a server with approximately 40TB of storage. What would be the best approach in this case? Should I use Linux with a shared directory and Docker, or would Windows with shared folders be a better option?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/28/2025 - 07:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It is probably the best to have a separate VM for deploying the management server, and a separate server for storing the backups.
There is the Acronis Cyber Protect appliance (all in one), but it is CentOS based, and as this OS is end of support.
I will open another post for the future of the appliance right away.

      
                
                
                    
                                                    Tue, 06/17/2025 - 11:27
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
