# how  to restore sql database to another machine if source machine crashed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-restore-sql-database-another-machine-if-source-machine-crashed

## Original Post
**Author:** Unknown

how  to restore sql database to another machine if source machine crashed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi folks, how i could restore a sql database to another machine if my source machine crashed ?
 
Thanks.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 01/05/2019 - 22:01

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
It's Evgeny from Acronis Service Providers Support. 
As far as I understand, you would like to know how to recover the SQL databases in a situation when the original machine is not available.
I will be glad to share the solution.
To recover SQL databases
When recovering from a database backup, click Microsoft SQL. Otherwise, skip this step.
Select the machine that originally contained the data that you want to recover.
Click Recovery.
Select a recovery point. Note that recovery points are filtered by location.
If the original machine is offline, the recovery points are not displayed. Do one of the following:
If the backup location is cloud or shared storage (i.e. other agents can access it), click Select machine, select an online machine that has Agent for SQL, and then select a recovery point.
Select a recovery point on the Backups tab.
The machine chosen for browsing in either of the above actions becomes a target machine for the SQL databases recovery.

Do one of the following:
When recovering from a database backup, click Recover SQL databases.
When recovering from an application-aware backup, click Recover > SQL databases.

Select the data that you want to recover. Double-click an instance to view the databases it contains.
If you want to recover the databases as files, click Recover as files, select a local or a network folder to save the files to, and then click Recover. Otherwise, skip this step.
Click Recover.
By default, the databases are recovered to the original ones. If the original database does not exist, it will be recreated. You can select another SQL Server instance (running on the same machine) to recover the databases to.
To recover a database as a different one to the same instance:
Click the database name.
In Recover to, select New database.
Specify the new database name.
Specify the new database path and log path. The folder you specify must not contain the original database and log files.

[Optional] To change the database state after recovery, click the database name, and then choose one of the following states:
Ready to use (RESTORE WITH RECOVERY) (default)
After the recovery completes, the database will be ready for use. Users will have full access to it. The software will roll back all uncommitted transactions of the recovered database that are stored in the transaction logs. You will not be able to recover additional transaction logs from the native Microsoft SQL backups.

Non-operational (RESTORE WITH NORECOVERY)
After the recovery completes, the database will be non-operational. Users will have no access to it. The software will keep all uncommitted transactions of the recovered database. You will be able to recover additional transaction logs from the native Microsoft SQL backups and thus reach the necessary recovery point.

Read-only (RESTORE WITH STANDBY)
After the recovery completes, users will have read-only access to the database. The software will undo any uncommitted transactions. However, it will save the undo actions in a temporary standby file so that the recovery effects can be reverted.
This value is primarily used to detect the point in time when a SQL Server error occurred.


Click Start recovery.
The recovery progress is shown on the Activities tab.
Please let me know if you have other questions.
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Mon, 01/07/2019 - 13:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    eric ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Team, 
Does Acronis backup 12.5 support point-in-time recovery for sql database. as per kb1707, point-in-time recovery support at Acronis backup version 11.x before, but its seems to be missing from 12.5, please advise.
https://kb.acronis.com/content/1707   

      
                
                
                    
                                                    Mon, 05/20/2019 - 08:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            eric ngun wrote:

Hi Team, 
Does Acronis backup 12.5 support point-in-time recovery for sql database. as per kb1707, point-in-time recovery support at Acronis backup version 11.x before, but its seems to be missing from 12.5, please advise.
https://kb.acronis.com/content/1707   


Hello Eric,
if the SQL databases are regularly backed up, then you'll be able to select any recovery point depending on how often the backup is created.  The only limitation - granular restore of SQL is not supported yet (not possible to restore individual database objects, such as tables, records, stored procedures). 

      
                
                
                    
                                                    Mon, 05/20/2019 - 13:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    eric ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
For the point in time recovery in previous version, the recovery could be done by latest backup + SQL transaction log to recovery the most latest data even. in some case, customer need to recovery in a exact time to reproduce some issue in test environment, they need to recovery data with latest SQL transaction log to get this data. but in version 12.5, this feature seems to be removed, is that right? 

      
                
                
                    
                                                    Tue, 05/21/2019 - 03:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    eric ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
Any update?

      
                
                
                    
                                                    Mon, 05/27/2019 - 08:05
