# Problem during instalation Acronis Backup on WS2012

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/problem-during-instalation-acronis-backup-ws2012

## Original Post
**Author:** Unknown

Problem during instalation Acronis Backup on WS2012

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lukas Bartakovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
i have problem during instalation of Acronis Backup Cloud Agent on Windows Server 2012 R2 as shown on screen bellow.
It says something like this:
This computer is domain controller. Please use existing domain user account with permision "Sign as a service" otherwise the agent service cannot be started.
Error: Inserted account doesnt exist"
But the account PetrHanka does exist, and also has administrator rigths.
 
Could you guide me please, how to solve this issue?
Thank you
Lukas
 
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      screen_instal.jpg

                      141.49 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/31/2017 - 12:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Lukas,
Thank you for your posting! Have you tried to specify the account in a form Domain\User? I'd also suggest testing a new user account for the Agent. Create a domain user account (member of Domain Administrators and Backup Operators with privileges Log on as a service). Then proceed with the instructions from the following article. If the issue persists, please contact Acronis support team.
Thank you, 

      
                
                
                    
                                                    Thu, 02/02/2017 - 11:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
