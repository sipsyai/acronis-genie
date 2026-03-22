# Operation canceled by user

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/operation-canceled-user

## Original Post
**Author:** Unknown

Operation canceled by user

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
We started to roll out Acronis Cloud Backup on all our cpanel webservers. It works quite well, but on a few servers we always get the following message:
Backup failed:
Operation canceled by user
I have already a ticket with the support open since a few days and sent also all the logs and gave access to the server, but it looks like they can't find the reason for this problem.
We don't use any process killer, and also don't restart the backup service on the webserver.
Is this a known problem, and maybe someone even know the solution? Or am I really the only Acronis customer with this problem?
Regards
Michael
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 05/18/2018 - 18:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Michael,
thank you for your posting! Operation canceled by user is a very generic message, the root cause should be reflected in the log files. I've found the related support ticket, seems that the investigation is pending the access credentials to your end. Could you please provide the new access details to the support engineers. Thank you for your time and co-operation! 

      
                
                
                    
                                                    Tue, 05/22/2018 - 08:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina
I sent the login details already to Cloudlinux who will forward them to you. I hope you can find the reason for this problem. We have now already 3 servers with the same problem.
Regards
Michael

      
                
                
                    
                                                    Tue, 05/22/2018 - 09:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you! As per the records in the support ticket, our engineers has shared the outcome of the investigation. Please let us know, if this helped. 

      
                
                
                    
                                                    Thu, 05/24/2018 - 07:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina
Yes, thanks a lot, the problem is solved. Disabling the mysql freeze solves the problem.
Regards
Michael

      
                
                
                    
                                                    Wed, 05/30/2018 - 06:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Great, thank you for the update\feedback! 

      
                
                
                    
                                                    Fri, 06/01/2018 - 08:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
