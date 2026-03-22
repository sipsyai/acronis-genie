# MS SQL Backup Failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/ms-sql-backup-failed

## Original Post
**Author:** Unknown

MS SQL Backup Failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jason Garland
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Does anyone know what this means and how to fix it?
Failed to create the shadow copy of volume '\\?\Volume{60f21b03-f144-11e1-ae59-00155d890e47}\'.
Date and time
Code
Module
349
Message
Failed to create the shadow copy of volume '\\?\Volume{60f21b03-f144-11e1-ae59-00155d890e47}\'.
Additional info:
------------------------
Error code: 1802
Module: 349
LineInfo: 0x8A9F7BA9E74D6F1F
Fields: {"$module":"ArsDbBackupProvider64_vsa64_1621"}
Message: Failed to create the shadow copy of volume '\\?\Volume{60f21b03-f144-11e1-ae59-00155d890e47}\'.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/10/2016 - 22:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jason,
Thank you for posting your question here.
To protect MS SQL databases Acronis Backup Cloud uses Microsoft Volume Shadow Copy Service (VSS) to create a snapshot of the volumes where the application is installed. This way we guarantee that application is backed up in a consistent way. However in case Microsoft VSS fails to perform the snapshot, we return the error above.
MS VSS may fail due to various reasons, starting from insufficient shadow copy storage space, to incorrect functioning of the MS SQL VSS writer. The latter is essential for protecting MS SQL. You can track down the root cause by starting analyzing the Windows Event Logs for VSS errors, and proceeding to verifying the VSS service and MS SQL VSS writer with DiskShadow tool.
Should you have issues with troubleshooting, please first update the agent to the latest version, then collect the output of DiskShadow tool and contact our Support team, or post the Windows Event Log VSS errors together with the DiskShadow output in this thread.
Also please post the full error message stack here (if available) to make sure it contains no other valuable details.
Let me know if you have any questions.
Best regards,

      
                
                
                    
                                                    Mon, 03/14/2016 - 14:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    xavi pirlo
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            When you use a backup statement to try to back up a database in Microsoft SQL Server 2008, in Microsoft SQL Server 2008 R2 or in Microsoft SQL Server 2012, the operation fails if the following conditions are true:
You have enabled change tracking on the database.
The database has been recovered at least one time after change tracking was enabled.
Additionally, the following error is logged in the SQL Server error log:
<Date><Time> <spid> Error: 2601, Severity: 14, State: 1. 
<Date><Time> <spid> Cannot insert duplicate key row in object 'sys.syscommittab' with unique index '<Index Name>'. 
<Date><Time> <spid> Error: 3999, Severity: 17, State: 1.
<Date><Time> <spid> Failed to flush the commit table to disk in dbid <Database ID> due to error 2601. Check the errorlog for more information.

      
                
                
                    
                                                    Thu, 03/17/2016 - 05:55
                                                                            
                                
                            
                                            
                                            
    
                    
                hadoop training in chennai | informatica training in chennai | hadoop training in chennai | aws training in chennai

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello xavi pirlo,
Thank you for your posting! This issue has not been documented in our internal system yet. I would recommend to raise a support ticket.
Thank you,

      
                
                
                    
                                                    Mon, 03/28/2016 - 08:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mohamed Ibrahim
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            At the point when you utilize a reinforcement proclamation to attempt to back up a database in Microsoft SQL Server 2008, in Microsoft SQL Server 2008 R2 or in Microsoft SQL Server 2012, the activity falls flat if the accompanying conditions are valid: 
You have empowered change following on the database. 
The database has been recouped in any event one time after change following was empowered. 
Moreover, the accompanying mistake is signed in the SQL Server blunder log: 
<Date><Time> <spid> Error: 2601, Severity: 14, State: 1. 
<Date><Time> <spid> Cannot embed copy key column in object 'sys.syscommittab' with novel list '<Index Name>'. 
<Date><Time> <spid> Error: 3999, Severity: 17, State: 1. 
<Date><Time> <spid> Failed to flush the submit table to plate in dbid <Database ID> because of mistake 2601. Check the errorlog for more data.

      
                
                
                    
                                                    Tue, 07/28/2020 - 07:02
                                                                            
                                
                            
                                            
                                            
    
                    
                AWS Training in Chennai | SAP Training in Chennai | Networking Training in Chennai | QTP Training in Chennai
