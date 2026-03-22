# Create plan with encryption (API)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/create-plan-encryption-api

## Original Post
**Author:** Unknown

Create plan with encryption (API)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Patrick van Gortel
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I am trying to create a backup protection plan using the Acronis API. I'm able to create a protection plan without an encryption key but can't find any info on how to create a protection plan with an encryption key.
Any help would be appreciated,
 
Patrick

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/07/2025 - 13:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Patrick,
Welcome to the forum.
To properly set up archive encryption when creating a protection plan via the API, you must first create a credentials object in the credentials store and use the ID of the credentials object in the "password" field.
For more details, please refer to the following link: Credentials Object Structure
Best regards.

      
                
                
                    
                                                    Mon, 02/10/2025 - 09:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
