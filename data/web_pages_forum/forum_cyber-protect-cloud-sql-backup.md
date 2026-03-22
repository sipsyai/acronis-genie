# Cyber Protect Cloud SQL backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-cloud-sql-backup

## Original Post
**Author:** Unknown

Cyber Protect Cloud SQL backup

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Sven Adam
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            On 'entire machin' backup including mySQL app backup with freeze / thaw scripts placed, I receive a warning as follows:
-32603 Couldn't lock tables for instance '127.0.0.1:3306': Error 1227: Access denied; you need (at least one of) the RELOAD privilege(s) for this operation '.
Where and how do I add those privileges?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 05/18/2024 - 13:27

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
You must grant the privileges in the MySQL UI by changing the role:
Click Add User or Edit User to create or modify MySQL user accounts with predefined roles. Next, enter the required account credentials:
https://dev.mysql.com/doc/mysql-windows-excerpt/8.0/en/mysql-installer-workflow-server.html
If the user already has Admin privileges and the issue persists, please raise a ticket with our support at https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Mon, 05/20/2024 - 08:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sven Adam
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi and thanks. The relevant mysql user didn't have that privilege. Added and now works like a charm.

      
                
                
                    
                                                    Mon, 05/20/2024 - 10:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sven Adam wrote:

Hi and thanks. The relevant mysql user didn't have that privilege. Added and now works like a charm.


Hello Sven!
I am glad the issue is resolved.
Feel free to participate in the forum anytime you need assistance.
Best regards.

      
                
                
                    
                                                    Tue, 05/21/2024 - 07:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
