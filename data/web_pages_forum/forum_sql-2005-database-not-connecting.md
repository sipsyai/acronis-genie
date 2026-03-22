# sql 2005 database not connecting

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-2005-database-not-connecting

## Original Post
**Author:** Unknown

sql 2005 database not connecting

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    murat caglar
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, we are using cloud backup.When we click on the sql server and click on the server name, we get an error.It does not ask for the password.Sql version 2005 sp3.thanks

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      11.JPG

                      14.9 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Sat, 07/14/2018 - 13:34

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
I'd check the list of assigned privileges of a user account specified for access to SQL. It must be a member of the Backup Operators or Administrators group on the machine in question and have a sysadmin role on each of the protected instances. The same is valid for a user who runs the SQL writer for VSS. Make sure it is turned on and has the above privileges. 
If the issue persists, please raise a support ticket.

      
                
                
                    
                                                    Wed, 08/01/2018 - 12:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
