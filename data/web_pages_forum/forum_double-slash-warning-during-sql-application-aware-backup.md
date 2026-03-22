# Double Slash Warning during SQL Application Aware Backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/double-slash-warning-during-sql-application-aware-backup

## Original Post
**Author:** Unknown

Double Slash Warning during SQL Application Aware Backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Christiaan de Wet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am receiving similar warnings on multiple of my clients's backups:
Activity 'Preparing for application backup' succeeded with the following warning: ' Database name: 'XXXXXXXXX' Database logical file name: 'XXXXX_log' Incorrect value: 'F:\Logs\\XXXXXXX.LDF' Error: A double slash in the path. To remove the double slash, run the T-SQL command: ALTER DATABASE MODIFY FILE '
When I access the database using SQL Management Studio I can confirm that there are no double slashes as stated in the warning.
They are all running Acronis Agent 12.5.10170.
Is this a known issue or am I missing something?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/13/2018 - 13:57

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    h4wtd0gz
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Also experiencing the same issue. Again no double slash showing up in SQL Studio

      
                
                
                    
                                                    Tue, 07/17/2018 - 06:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello everyone!
 
We're working on fixing this issue in the code, however, may I suggest couple of workarounds?
 
Option 1:
1. Open SQL Server Management Studio (make sure that SSMS version matches the version of SQL instance running on the machine)
2. Run the following query to get the list of database names and locations:
use <database_name>
select * from sys.database_files 
3. In the output, find the database that is mentioned in the warning
4. Run the following command to modify physical path to the file:
ALTER DATABASE <database name>
MODIFY FILE (NAME = '<logical name>', FILENAME='<path to file>');
where
<database name> is the name of the database that is mentioned in the error, no changes needed
<logical name> is the logical name of the file mentioned in the error, no changes needed
<path to file> is the full path to the file that is mentioned in the error, without double slashes or extra spaces at the end 
 
Option 2
1. Open SQL Management Studio
2. Detach the database and put it offline
3. Reattach the database 
 
Please let me know if this imposes any difficulties or, otherwise, does lead you to successful backup!

      
                
                
                    
                                                    Tue, 07/17/2018 - 07:46
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Christiaan de Wet
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the feedback Fedor!
There are a lot of clients this is happening to and we do not want to access all of their databases for this issue.
We will rather wait until the issue has been resolved with an agent update.
One comment though...
Should the statement:
MODIFY FILE (NAME = '<logical name>', FILE='<path to file>');
not be
MODIFY FILE (NAME = <logical name>, FILENAME='<path to file>'); ?

      
                
                
                    
                                                    Fri, 07/20/2018 - 19:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Cristiaan, you are right, my mistake, I found proof in https://docs.microsoft.com/en-us/sql/relational-databases/databases/mov…
 
We also published an article about this issue.
https://kb.acronis.com/content/61548
 
p.s. I edited my original comment to reflect the proper cmdlet.
p.p.s. The agent-based fix is targeted ~autumn this year.

      
                
                
                    
                                                    Mon, 07/23/2018 - 07:51
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
