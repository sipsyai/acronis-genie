# Backup SQL database

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-sql-database

## Original Post
**Author:** Unknown

Backup SQL database

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi guys!
The most importand data in our customers is their SQL databases. Now we are using SQL's backup with plans and taking in the local disk .bak files from SQL database.
One reason that we choose to use Acronis Cloud was that have SQL backup application.
I tested also in cloud and also in local network via NAS to take back-up and i noticed that it is taking the .mdf & .ldf files.
The problem is that when SQL service is running if it took the mdf & .ldf files is useless because they are in use from SQL service, so when i'm trying to attach the files in SQL is int possible, and i got error.
Also i tried via Application backup from whole machine and i noticed that did the same, its coppied mdf & .ldf files!
Is there any whey to take SQL back-up? One way i'm thinking is with post coammnd one command to take down the SQL service before back-up and one command after back-up to run the SQL service.
Is there any other way?
 
Thanks in advanced.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/22/2018 - 09:14

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have update about that.
I did mistake its working fine! The problem was with version of database backup. If i use backup format 11 i can restore it in SQL 2012 and after, if i use backup format 12 i can restore it in SQL 2014 and after.
The question is what about SQL 2008? It does'nt work there. Is there any solution about that?

      
                
                
                    
                                                    Mon, 11/26/2018 - 08:20
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Stilianos,
Stopping the databases before backup and resuming after is one of the possible ways to secure the consistent copy of sql, but it's mostly recommended as a workaround in case you have issues with the Volume Shadow Copy service (VSS) or applications that are not compatible with VSS.  
In all other cases the files are backed up with the help of the VSS Writers that allow creating consistent copies of running MS applications such as SQL, Exchange or AD. You can either use Application backup option in the plan, or create a separate plan for SQL databases only, see Protecting applications. 
 

      
                
                
                    
                                                    Mon, 11/26/2018 - 09:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes Ekaterina i noticed that its ok with VSS. The only problem now is SQL 2008r2. Im backing up 2008r2 database with acronis and when im going to restore it to 2008r2 back again says
"The database cannot be opened because it is version 706 (this with back up format 11 and with 12 says 782). This server supports version 661 and earlier. A downgrade path  is not supported." 
 Some of our customers have SQL 2008R2 and we are sad about that.
Is there any solution about 2008r2 databases?

      
                
                
                    
                                                    Mon, 11/26/2018 - 10:14
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Stilianos,
according to the third-party forums, this error message means the database file in the backup and the target databases actually have different versions, e.g. the older server can't support the newer database format. 
https://forums.asp.net/t/1934100.aspx?Getting+error+cannot+be+opened+because+it+is+version+706
https://www.sqlservercentral.com/Forums/Topic1621506-391-1.aspx
As far as I understand, 706 corresponds to SQL Server 2012 and 661 to SQL Server 2008R2

      
                
                
                    
                                                    Tue, 12/04/2018 - 14:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes thats right, but my problem is that im backing up 2008r2 database with acronis and when i want to restore it to 2008r2 again says this message. Its like Acronis transformate my database to newer version! So icant use acronis cloud backup to our clients because many of them have 2008r2!
Is there any solution about that?

      
                
                
                    
                                                    Fri, 12/07/2018 - 09:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Stilianos,
I'm not aware of any cases, where the version of the databases in the backup has been changed or recognized as a different one. I'd recommend raising a support ticket for this issue, if you're sure the SQL server version actually matches one in the backup. Please let us know the results of the investigation.

      
                
                
                    
                                                    Mon, 12/10/2018 - 09:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina was my fault i thought that the database is 2008 but was 2012. Everything ok!

      
                
                
                    
                                                    Wed, 01/02/2019 - 15:05
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stilianos wrote:

Ekaterina was my fault i thought that the database is 2008 but was 2012. Everything ok!


Good to know, thank you for an update / feedback!  

      
                
                
                    
                                                    Thu, 01/03/2019 - 09:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
