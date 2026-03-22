# Calculate required backup space

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/calculate-required-backup-space

## Original Post
**Author:** Unknown

Calculate required backup space 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Antonios Throuvalas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Is there a way to calculate beforehand the required backup online space for a one time backup of e.g a Windows Server and some MS Office files of lets say 100 GB in size?
Is there a rule of thumb in order to define how much backup space would be required in total for a fiven set of data?
Thank you in advance.
Regards,
Antonios
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/21/2018 - 07:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Antonios!
 
Thanks for the question, it's a good one!
But I have to say that an answer is in no means short. First you have to consider that the size depends on many factors.
Starting with your particular example, if the entire server has about 100 Gb of data, most of which is in text format (xls, doc, pdf and such), I would estimate the one-time backup to be somewhere in between 20 Gb and 60 Gb (let me know if I hit the mark :) ).
 
Here's the full version of my response to you:
You need to take several factors into consideration:
Amount of data you want to back up
Size of files and types of files
Schedule of the backups: how often backups should run
Retention policies: how long backups should be kept
Compression level which varies depending on the nature of data
There are three basic scenarios to estimate amount of data stored in an archive:
Each day an incremental backup is not zero size, because the SAME files are CHANGED.
Each day an incremental backup is not zero size, because the NEW data is ADDED to the machine each day.
Mix of the 1 and the 2.
For example, you have created a default backup plan.
Backup schedule is:
In the first case.
The backup to the Cloud grows each day in size equal to 1 incremental (10 Gbs for example).
For the backup set of:
Monthly: 6 months
Weekly: 4 weeks
Daily: 7 days
(which is default) And the backup runs once a day every day
Important side-note: the amount of recovery points may be different each month. See here - You create the backup for the first time - it will be the first Monthly RP. with 6m4w7d rules, this backup will be considered obsolete and liable for being overwritten only when the 7th Monthly backup is create.
One RP may play the role of both Monthly, Weekly and Daily or any other combination like that (m+w, w+d. m+d).
The formula to calculate the amount of RP:
N = M + (W±1) + (D-1),
where M - amount of Monthly rps, W - weekly, D - daily.
W±1 - because some month you will have a scenario when there are 5 Mondays (if Weekly backup is set to Monday, which is default), sometimes there are 4. Some of the Monthly RPs will overlap with Weekly.
D-1 - because one of the Weekly recovery points ALWAYS overlaps with a Daily backup.
It is best to use the general Rule of thumb - HOW LONG TO KEEP defines NOT the amount of recovery points, but rather HOW long a backup of the needed day will be kept.
You need to keep individual daily backups for 13 days - go ahead and set Daily: 13 days.
 
 
Let's say that the initial size of backup is 50 Gbs.
The backup will grow by 10 Gbs every day for a week,
50 Gb (initially done on Monday) +10 Gbs each day x 6 days = 110Gb,
Next day (Monday again) a backup will overwrite the slice of the previous week (if the backup schedule is "daily"), so it will not grow that much, because New Data will be written in place of old data.
Cloud backup is always incremental, so if customer's daily day-to-day data changes are ~10 Gb ( statistically, ~80% of the cases are determined via Normal Distribution, where the size difference between each day's increments can be describe more accurately with more numbers of calculations. Unfortunately, spikes in usage do occur, but statistics say that they are not as frequent). Thus,you can ESTIMATE the size, by expecting the archive to grow normally. Size = Size_of_full first backup + N * E_s, which in this case is Size = 50 Gb + N * 10 Gb = 50 + 20 *10  ≈ 250 Gb after 6 months.
 
In the second case, you backup archive will grow every day when the backup runs.
For the third scenario - the size will be equal to the sum of changes every day and the size calculated in the first part

      
                
                
                    
                                                    Fri, 11/23/2018 - 10:59
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
