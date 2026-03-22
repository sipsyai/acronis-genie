# SQL server databases suddenly go missing

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/sql-server-databases-suddenly-go-missing

## Original Post
**Author:** Unknown

SQL server databases suddenly go missing

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Set up a acronis cyber cloud for this company for days already and its working fine with all the backups. 
Yesterday backup prompt me a critical error and tells me the backup has failed.
went in devices > Microsoft SQL and check the databases . What i saw was there's no databases for me to choose from. But i was able to back up those databases for the pass 15 days. And the machine SQL server databases still there . We never change any setting to anything.
Is there a way to refresh the microsoft sql tab ? 
The database shouldn't suddenly disappear from the cloud after we successfully set it up. 
I have a log file error for it . 
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      logs (1).zip

                      2.26 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/25/2019 - 02:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Jianzhi Low
Can you please confirm the following for us, 
1. How did you setup the backup of SQL Database? Did you setup application aware backup from All Devices > Backup > Enabled Microsoft SQL Server?
OR
Did you go from under Devices > Microsoft SQL?
OR
Are you using both of these methods?
Then lastly can you confirm that the databases you are trying to backup is still actually in SQL Studio? Can you navigate to the database and open it?
Regards

      
                
                
                    
                                                    Mon, 07/29/2019 - 14:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays ,
Thanks for dropping in. 
I am using this method > Go under Devices > Microsoft SQL
And yes i am still able to navigate to the database and open it in the SQL studio. 
And i this problem has being solved by the their engineer.
Apparently my sql vsswriter is not on. So the engineer went to the sql vss writer service and change the user from domain administrator to local system and my the cloud is able to see the database in the sql section again..
Refer to : https://kb.acronis.com/content/60241  
 

      
                
                
                    
                                                    Thu, 08/01/2019 - 06:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day
 
Glad to hear you issue has been resolved.
 
Kind regards

      
                
                
                    
                                                    Thu, 08/01/2019 - 06:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Katarienr
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You can detach the database data and transaction log files and then re-attach them to the same or another SQL ide instance.

      
                
                
                    
                                                    Fri, 11/05/2021 - 20:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Giovanna Fiscella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I've been using the said path my entire life. But, my SQL database server also went missing a couple of days ago. What could be the issue? Everything was just fine, and all of a sudden, I couldn't find the damn database. But, I asked a friend of mine to try and see if he could find it. 

      
                
                
                    
                                                    Tue, 12/14/2021 - 16:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Giovanna
From my own past experience with similar issues it seems to always be related to the SQL VSS Writer Service, either it is not running or running under the wrong logon, I have had more serious issues such as a problem with the actual instance but this is very rare and has only happened once that I can remember
I would first recommend that you check if the service is running, if it is not running please start it and check if the device shows again,
If the service is running check that it is running under the local system, for some reason when running under a domain admin it from time to time gives issues,
As per the comment above from jianzhi low, the Acronis engineer also pointed him in this direction to resolve and you can refer to the below article:
https://kb.acronis.com/content/60241
Kind regards

      
                
                
                    
                                                    Mon, 12/20/2021 - 10:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
