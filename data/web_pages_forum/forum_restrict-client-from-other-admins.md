# Restrict Client from other Admins

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/restrict-client-other-admins

## Original Post
**Author:** Unknown

Restrict Client from other Admins

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Naushad Mohammed
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
We have 3 admins who manage all the backups for all clients from the cyber protect portal.
i want to create a backup for myself ( own computer & google workspace backup) and other admins should not have access to this, but only me.
I am the company administrator for cyber protect.
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/29/2022 - 05:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kristian Popov
                            

                            
                    
                        Acronis Support Engineer
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 19
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Naushad,
If the other 3 admins have the Administrator role enabled for their account, this means that they will have access to all the backups within the console.
There is an option for "Read-only administrator" role, which provides read-only access to all objects of the Cyber Protection service but this will eliminate the possibility for the admins to control the backups.
With that said, if you add your machine under a tenant where there are other machines being backed up, the admins who take care of those machines and backups will have access to yours as well.
More information on user roles can be found here https://www.acronis.com/en-us/support/documentation/AcronisCyberCloud/#…

      
                
                
                    
                                                    Wed, 08/03/2022 - 11:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Kristian Popov | Acronis Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Naushad Mohammed,
Can you please tell us was the problem resolved? If yes, what helped it?

      
                
                
                    
                                                    Tue, 09/20/2022 - 13:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Naushad Mohammed
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
making others read only will not work for our job tasks.
what if i recreate all clients as a sub account and then add the other 2 admins only for them, will it work? 

      
                
                
                    
                                                    Tue, 09/27/2022 - 18:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Naushad Mohammed
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            making the other 2 admins ready only won't be possible for the tasks to be performed.
 
what i create all clients as sub-account and then move the other 2 admins to manage those sub-accounts only, will it work?

      
                
                
                    
                                                    Tue, 09/27/2022 - 18:18
