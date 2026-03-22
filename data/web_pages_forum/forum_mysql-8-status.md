# MySQL 8 status?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/mysql-8-status

## Original Post
**Author:** Unknown

MySQL 8 status?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Morris M
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I know that you do not officially support MySQL 8 yet. Why I cannot understand.
As I understand support will be fixed in dev task CI-11020 and cPanel plugin version 1.8.
But if we have to wait until second half of 2022 for this to be completed we have to find another backup solution.
We will soon convert all MySQL 5.7 servers to MySQL 8 because of many reasons.
Could you please prioritize this and give us a ETA this year?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/01/2021 - 11:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Morris,
thank you for your posting! As per the information in our internal system, implementation CI-11020 of is planned for H1 2022. I've forwarded your comment to the product team, hopefully we'll see the fix earlier than expected. 

      
                
                
                    
                                                    Thu, 11/04/2021 - 17:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Morris,
 
Is this for cPanel/WHM server? Could you not use MariaDB 10.3 or 10.5 instead? Acronis works fine on our servers running MariaDB 10.5.
 
Best,
Chris

      
                
                
                    
                                                    Fri, 11/05/2021 - 10:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            What kind of issue are you experiencing with MySQL 8?
I have cPanel servers running MySQL 8 and Acronis backs them up without an issue.

      
                
                
                    
                                                    Thu, 11/11/2021 - 09:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes, I have Acronis backing up 2 cPanel DNS only servers running MySQL 8.0 fine too.

      
                
                
                    
                                                    Thu, 11/11/2021 - 10:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Are you sure it's working fine for you? Did you ever try to restore a database? I just realized this is not working on my cpanel servers with mysql8. 
 
 

      
                
                
                    
                                                    Thu, 11/11/2021 - 17:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Morris M
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We had a ticket with Acronis and they said:
_
Official MySQL8 (backups and restores) support will come in dev task CI-11020 and cPanel plugin version 1.8 .
Aproximate ETA - the second half of 2022, possibly this will be done faster.
-
Sometimes it works, but many times it does not.
But soon we have all servers on MySQL, so Acronis is not a solution we can use when it's not officially supported.

      
                
                
                    
                                                    Mon, 01/10/2022 - 09:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Morris M
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Same goes for MariaDB 10.6 that cPanel is currently shipping with their installations. MariaDB 10.6 is not supported.
Both MariaDB 10.6 and MySQL 8 should be supported by Acronis.
For our case we currently only use MySQL 8 on new installations of cPanel and will upgrade MySQL 5.7 on the rest of the servers soon.

      
                
                
                    
                                                    Mon, 01/10/2022 - 12:09
