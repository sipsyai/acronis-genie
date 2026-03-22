# Registering agent to more than one user

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/registering-agent-more-one-user

## Original Post
**Author:** Unknown

Registering agent to more than one user

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Christiaan de Wet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good day, In Acronis Cloud, a Client has a User created and agents are registered to the Acronis Cloud Console using this user. Afterwards, is is possible to create additional users for the same client and give those users access to specific backup jobs or backups created? Is it possible to register an Acronis agent to more than one user for the same client? I did some tests, and it does not seem possible as the agents aren't visible to the newly created user. Also do not want to give the user Company Administrator privileges. Thanks!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/22/2019 - 14:36

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Christiaan. 
>Is it possible to register an Acronis agent to more than one user for the same client?
No
>is it possible to create additional users for the same client and give those users access to specific backup jobs or backups created?
Unfortunately without providing the administrator access it is not possible, but you can create read-only company admin as described in Acronis Knowledge Base article below: 
https://kb.acronis.com/content/63015
End-User Company's admin can be changed to "readonly_admin" role too.
"role_id": "company_admin" --> "role_id": "readonly_admin"
 

      
                
                
                    
                                                    Tue, 12/31/2019 - 11:13
