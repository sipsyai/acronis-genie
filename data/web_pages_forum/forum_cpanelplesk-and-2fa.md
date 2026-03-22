# cPanel/Plesk and 2FA

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cpanelplesk-and-2fa

## Original Post
**Author:** Unknown

cPanel/Plesk and 2FA

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
The current docs for installing the cPanel and Plesk plugins say that if the Acronis user account uses 2FA then you need to install using a registration token, but as we know this now doesn't work and any servers that used registration tokens with Plesk/cPanel had to be re-logged in with a username and password, but 2FA blocks this.
The docs are inconsistent with each other.
What is the plan with regards to 2FA and cPanel/Plesk? This is a must have feature to pass any sort of compliance.
Thanks,
Karl

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/11/2022 - 09:57

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Karl Austin,
Thank you for reaching out. We have forwarded your question to a dedicated support engineer who will review and respond soon.

      
                
                
                    
                                                    Mon, 11/14/2022 - 17:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Thomas Fisinger
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Is there already a solution for this? I think i have the same problem.
      
                
                
                    
                                                    Sun, 01/15/2023 - 16:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Thomas,
thank you for your posting! Here is an update on the raised topic: 
Due to the security improvements introduced in the C22.07 release it's necessary to generate a service user. In order to register the agent please provide credentials to the Acronis account under which the protection agent is registered in Acronis Cyber Protect Cloud as described in the article: https://kb.acronis.com/content/70937
The accounts with the enabled 2FA cannot be used with the WHM user interface and create_api_client.py script. 
Also, we are planning to introduce the new mechanism to simplify the authentication procedure. The ID of the fix: CI-20591 which should be released with cPanel 1.7 update, but no ETA at the moment.
Please let me know, if there are any questions.

      
                
                
                    
                                                    Tue, 01/17/2023 - 15:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
