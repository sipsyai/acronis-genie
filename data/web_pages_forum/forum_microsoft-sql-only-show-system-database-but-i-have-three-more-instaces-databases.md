# Microsoft Sql only show System Database but I have three more instaces databases

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/microsoft-sql-only-show-system-database-i-have-three-more-instaces-databases

## Original Post
**Author:** Unknown

Microsoft Sql only show System Database but I have three more instaces databases

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I installed acronis backup cloud in my server but  the agent doesn't show all instances , show only the system database

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      database_show.jpg

                      32.03 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/31/2018 - 20:29

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi!
I'd start with checking the user rights. A user account specified for access to SQL must be a member of the Backup Operators or Administrators group on the machine in question and have a sysadmin role on each of the protected instances. The same is valid for a user who runs the SQL writer for VSS. Make sure it is turned on and has the above privileges. 
 

      
                
                
                    
                                                    Wed, 08/01/2018 - 11:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    KISAMIZU
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I the same problem has occurred now.
can fix this problem
1) Open "service.msc"
2) select "SQL Server VSS Writer" and open properties
3) select "login" tab
4) select "account" and input SQL login account
5) Reboot Server
can look other SQL Databases!
Try and please write your result!

      
                
                
                    
                                                    Fri, 10/12/2018 - 08:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sibi Mathew
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks mate.. It's working beautifully.. 
KISAMIZU wrote:

I the same problem has occurred now.
can fix this problem
1) Open "service.msc"
2) select "SQL Server VSS Writer" and open properties
3) select "login" tab
4) select "account" and input SQL login account
5) Reboot Server
can look other SQL Databases!
Try and please write your result!



      
                
                
                    
                                                    Wed, 11/07/2018 - 14:04
