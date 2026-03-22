# Probleme mit SQL Backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/probleme-mit-sql-backup

## Original Post
**Author:** Unknown

Probleme mit SQL Backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo, jemand eine Idee?
 
Restore of database 'master' (SQL Server instance: 'MICROSOFT##SSEE') to the point of failure may become unavailable.
42000 (33003): [Microsoft][ODBC SQL Server Driver][SQL Server]DDL statement is not allowed.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/20/2018 - 09:07

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Oliver,
It's Evgeny from Acronis Service Provider Support. 
 
The issue appeared as there were warnings during backup.
We are running SQL statement 'CREATE TABLE during backup to make backup/log truncation pair consistent. We create transaction, create table and hold it until backup finished.
To avoid warning either give user sufficient rights to create table or turn off log truncation. In the latter case automatic log truncation can be accomplished by switching database recovery model to 'SIMPLE'.
1.
Turn off log truncation in backup plan options 
2.
Go to Microsoft SQL Server Management Studio and change Recovery Model to Simple in database properties
 
Please let me know if this helps you resolve the issue.
Otherwise please reach out to our Support team.
 
Best Regards,
Evgeny Ryuntyu | Senior Support Engineer
Acronis 

      
                
                
                    
                                                    Wed, 03/21/2018 - 09:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Zarif moore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, Here I would like to refer an excellent third party software, Kernel for SQL Recovery software. The software is capable to resolve all kind of issues related to SQL server.

      
                
                
                    
                                                    Fri, 06/22/2018 - 09:30
