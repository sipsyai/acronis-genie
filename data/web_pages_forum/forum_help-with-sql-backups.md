# Help With SQL Backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/help-sql-backups

## Original Post
**Author:** Unknown

Help With SQL Backups

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cheyenne Beard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a couple of questions regarding some issues I have been having with getting my SQL backups set up correctly.
I am trying to create a protection plan for a variety servers and their DB's. The owner of the servers would like to have the transaction logs backed up hourly while backing up the full DB daily. Is there a way to only backup the transaction logs? 
Another question that one of our SQL vendors had asked is that the application aware backups show that they are backing up to NULL. Is this normal? And are those full backups?
We are currently using Acronis Cyber Protect for our backup infrastructure. Any Assistance is greatly appreciated.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/06/2024 - 19:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Cheyenne,
When you run an application-aware backup, log truncation is enabled by default: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#log-truncation.html?Highlight=sql%20logs
When this option is enabled, a database can be recovered only to the point in time of a backup created by this software. Disable this option if you back up transaction logs using the native backup engine of Microsoft SQL Server. You will then be able to apply the transaction logs after a recovery and thus recover a database to any point in time.
To determine if a backup is full or not, check the schedule and the backup configuration. For example, if they selected "always full," it is expected to always be a full backup. Otherwise, it won't be: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#backup-schemes.html
Best regards.

      
                
                
                    
                                                    Fri, 06/07/2024 - 12:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Cheyenne Beard
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose Pedro Magalhaes wrote:

Hello Cheyenne,
When you run an application-aware backup, log truncation is enabled by default: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#log-truncation.html?Highlight=sql%20logs
When this option is enabled, a database can be recovered only to the point in time of a backup created by this software. Disable this option if you back up transaction logs using the native backup engine of Microsoft SQL Server. You will then be able to apply the transaction logs after a recovery and thus recover a database to any point in time.
To determine if a backup is full or not, check the schedule and the backup configuration. For example, if they selected "always full," it is expected to always be a full backup. Otherwise, it won't be: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#backup-schemes.html
Best regards.
 
Thank You Jose,
 
Is there a way for Acronis to backup the transaction logs separately? As an Example:
One protection plan backing up the OS of the VM weekly
One protection backing up the DB daily, and the transaction logs hourly
Also, if it is possible to back up the transaction logs separately from the DB using Acronis, I'm assuming this would cause stuns each hour since it uses VSS?
We need to have Acronis truncating the logs after backup since the logs fill up quickly on certain machines. If this is the case would you recommend us use a combination of Acronis DB backups (with truncation enabled) and SQL native backups for the transaction logs? 
 
 
 



      
                
                
                    
                                                    Fri, 06/07/2024 - 13:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Cheyenne Beard wrote:

Jose Pedro Magalhaes wrote:

Hello Cheyenne,
When you run an application-aware backup, log truncation is enabled by default: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#log-truncation.html?Highlight=sql%20logs
When this option is enabled, a database can be recovered only to the point in time of a backup created by this software. Disable this option if you back up transaction logs using the native backup engine of Microsoft SQL Server. You will then be able to apply the transaction logs after a recovery and thus recover a database to any point in time.
To determine if a backup is full or not, check the schedule and the backup configuration. For example, if they selected "always full," it is expected to always be a full backup. Otherwise, it won't be: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#backup-schemes.html
Best regards.
 
Thank You Jose,
 
Is there a way for Acronis to backup the transaction logs separately? As an Example:
One protection plan backing up the OS of the VM weekly
One protection backing up the DB daily, and the transaction logs hourly
Also, if it is possible to back up the transaction logs separately from the DB using Acronis, I'm assuming this would cause stuns each hour since it uses VSS?
We need to have Acronis truncating the logs after backup since the logs fill up quickly on certain machines. If this is the case would you recommend us use a combination of Acronis DB backups (with truncation enabled) and SQL native backups for the transaction logs? 
 
 
 




Hello!
The application-aware backup is intended to back up the database. We don't offer any service to back up just the logs because most clients want them to be truncated to avoid accumulating huge amounts of storage.
You could try, for example, creating a new files/folders backup plan and selecting the path where the logs are stored to see if that works. A full backup of the machine would also save the entire SQL database and the respective logs.
Best regards.

      
                
                
                    
                                                    Fri, 06/07/2024 - 18:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
