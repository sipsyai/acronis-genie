# Sql backup warning Error 0x57002b: Failed to find the full backup of database 'Teste'

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/sql-backup-warning-error-0x57002b-failed-find-full-backup-database-teste

## Original Post
**Author:** Unknown

Sql backup warning Error 0x57002b: Failed to find the full backup of database 'Teste'

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Error 0x57002b: Failed to find the full backup of database 'Teste'.
| trace level: warning
| channel: tol-activity#66B3A433-E35A-4D5D-B364-6097DD24F881
| line: 0xb19b368b2754d7b9
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:2385
| function: OdbcDbServiceImpl::DatabaseHasFullBackup
| $module: ArsAgentProvider_vsa64_10790
|
| error 0x570010: Failed to execute SQL statement 'select * from msdb.dbo.backupset where database_name=N'Teste' AND is_copy_only=0'.
| line: 0xb19b368b2754d2e3
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:1147
| function: OdbcDbServiceImpl::QueryResultImpl::Create
| $module: ArsAgentProvider_vsa64_10790
|
| error 0x570800: 01000 (926): [Microsoft][ODBC SQL Server Driver][SQL Server]Database 'msdb' cannot be opened. It has been marked SUSPECT by recovery. See the SQL Server errorlog for more information.
| line: 0xb19b368b2754d2e4
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:1148
| function: OdbcDbServiceImpl::QueryResultImpl::Create
| $module: ArsAgentProvider_vsa64_10790
2018-10-26T12:51:49:730-02:00 5616 I00000000: TruncateLogOf: Teste start making fake database backup
2018-10-26T12:51:52:402-02:00 5616 I00000000: TruncateLogOf: Teste done making fake database backup
2018-10-26T12:52:00:418-02:00 5616 W0057002B: Error 0x57002b: Failed to find the full backup of database 'Teste'.
| trace level: warning
| channel: tol-activity#66B3A433-E35A-4D5D-B364-6097DD24F881
| line: 0xb19b368b2754d7b9
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:2385
| function: OdbcDbServiceImpl::DatabaseHasFullBackup
| $module: ArsAgentProvider_vsa64_10790
|
| error 0x570010: Failed to execute SQL statement 'select * from msdb.dbo.backupset where database_name=N'Teste' AND is_copy_only=0'.
| line: 0xb19b368b2754d2e3
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:1147
| function: OdbcDbServiceImpl::QueryResultImpl::Create
| $module: ArsAgentProvider_vsa64_10790
|
| error 0x570800: 01000 (926): [Microsoft][ODBC SQL Server Driver][SQL Server]Database 'msdb' cannot be opened. It has been marked SUSPECT by recovery. See the SQL Server errorlog for more information.
| line: 0xb19b368b2754d2e4
| file: e:\257\enterprise\applications\mssql\archiver\sqldmo_provider\impl\db_service_odbc_impl.cpp:1148
| function: OdbcDbServiceImpl::QueryResultImpl::Create
| $module: ArsAgentProvider_vsa64_10790
2018-10-26T12:52:00:419-02:00 5616 I00570000: Cannot truncate the transaction logs of database 'Teste' because the database has never been backed up by Microsoft SQL Server.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/26/2018 - 23:44

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hi!
 
As I understood, SQL DB backups are not successful.
 
The log that you have pasted indicates issues with the initial stages of the backup job - making a snapshot of the databases.
Acronis uses Microsoft VSS and native SQL queries to prepare the data to be backed up.
Error message that are observed look like the are generated by Windows and the SQL Server himself.
I would advise you to check the following point:
 1. when you were first setting up the SQL backup, you specified a user - ensure that this user still has sysadmin roles of the instances
 2. ensure the NT Authority\System user is also a sysadmin - it runs the VSS requests
 3. ensure that the user that the Acronis Managed Machine service log on to Windows as has proper privileges -> https://kb.acronis.com/content/56202
 
Send the screenshots here with proofs in case issue still occurs. Share the login name in PM so I could involve support team.

      
                
                
                    
                                                    Tue, 10/30/2018 - 15:22
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
