# SQL Backup Confusion

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/sql-backup-confusion

## Original Post
**Author:** Unknown

SQL Backup Confusion

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Brian Juhl
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all
Running Cyber Protect Cloud im a bit confused as to how to configere SQL Backup.
So a few questions i hope anyone can answer or confirm.
1. When running entire machine backup, i can add SQL as application aware backup.
But when doing Disk/Volume og Folder/Files this is not an option. But from my test it seems to work fine, and in sql log i can see it registers backup.
So is all backup types application aware, even if you cant control it in settings?
2. When using backup type MS SQL, then i can only recover as files to a sql server with sql and sql agent installed, even if i only want database files and no attach. But when recovering from entire machine backup, i can recover to any client. Is this by design?
3. Then the question comes about setup.
Today i run an entire server backup a day (sql aware), and sql backup every hour.
But should i instead just run entire server backup (or disk/folder) every hour, giving me better recovery options.
Or what is the recommend solution?
Is there an overhead of running entire machine every hour.
Hope you have some input. Thanks.
Best regards. Brian
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 12/12/2024 - 08:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Entire machine backups (full backups) are required for application-aware backup. You can review the prerequisites in the Acronis Documentation. Without application-aware settings, the full machine (including SQL) will be backed up, but recovery options are more limited. For further details, refer to the Application-Aware Backup Guide.
Recovery from entire machine backups can be performed on any system with an agent or bootable media, including SQL databases. Application-aware backups allow recovery to:
Original instance
Another instance
Original database
New database
For SQL databases, dedicated backups are recommended for quick recovery, granular restore etc.. Contact Acronis Support for personalized guidance.
Best regards.

      
                
                
                    
                                                    Thu, 12/12/2024 - 09:16
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brian Juhl
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jose
Thanks for the answer, but it dosent really answer my questions.
1. Is Disk/Volumes and Folder backup also application aware, my tests say yes?
I now they can only be restored as files and thats fine, but can you count on the integrity of the database?
2. I guess is by design, but funny you cant restore as files with out SQL agent.
3. Is my setup ok, og could i just run the entire machine backup each hour instead.
Also you mention faster recovery with sql backup. My experience is that using files recovery from an entire machin backup is 3 times as fast than sql restore to files. Ending up with same files.

      
                
                
                    
                                                    Thu, 12/12/2024 - 10:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Brian Juhl wrote:

Hi Jose
Thanks for the answer, but it dosent really answer my questions.
1. Is Disk/Volumes and Folder backup also application aware, my tests say yes?
I now they can only be restored as files and thats fine, but can you count on the integrity of the database?
2. I guess is by design, but funny you cant restore as files with out SQL agent.
3. Is my setup ok, og could i just run the entire machine backup each hour instead.
Also you mention faster recovery with sql backup. My experience is that using files recovery from an entire machin backup is 3 times as fast than sql restore to files. Ending up with same files.


1- Application-aware backups are only supported with full machine backups. File or disk backups can include databases, but they don't ensure integrity. A dedicated SQL agent or application-aware backup is required for full protection.
2- This behavior is by design.
3- If recovering databases as files is acceptable for your needs, it will work, but integrity won't be guaranteed so you need to be careful to ensure the integrity of the backups.
The user guides I provided above explain most of this in detail. Please review your needs, and if recovering DBs as files works for you, that’s fine.

      
                
                
                    
                                                    Thu, 12/12/2024 - 10:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brian Juhl
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Im gonne stick with Entire Backup with SQL, and then SQL Backups every hour or 15 min. as a second protection plan. Then all should be good.
Thanks Jose

      
                
                
                    
                                                    Thu, 12/12/2024 - 11:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Brian Juhl wrote:

Im gonne stick with Entire Backup with SQL, and then SQL Backups every hour or 15 min. as a second protection plan. Then all should be good.
Thanks Jose


You are welcome! 

      
                
                
                    
                                                    Thu, 12/12/2024 - 12:08
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
