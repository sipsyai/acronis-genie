# Console with data locked

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/console-data-locked

## Original Post
**Author:** Unknown

Console with data locked

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            
Hello
I have the following problem,
On the console where I have several clients, only one is showing a crash on the date, the last backup column is with the locked date, and the backups are being performed normally.



 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      data backup.png

                      25.21 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/17/2020 - 10:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Daniel
Does this machine only have one backup plan applied to it?
Regards

      
                
                
                    
                                                    Mon, 04/20/2020 - 12:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             

 





Hi, thanks for the feedback,

It has backup plans for Agent SQL and a plan for the operating system, Agent for desktop.https://prnt.sc/s2psnw





      
                
                
                    
                                                    Mon, 04/20/2020 - 13:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel
First thing I would suggest is to check that there are no old activities that are still running for that machine, to do this click on the name of the device > activities > change any status to in progress.
If no activities please follow these steps:
Please remove the device from backup console and register it again as per following KB:
https://kb.acronis.com/content/55244
If you have old activities please let me know and I will give you further information on how to stop those tasks.
Regards

      
                
                
                    
                                                    Mon, 04/20/2020 - 22:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello I found old tasks here, see the print, how can i proceed to stop it?

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      535674-181999.PNG

                      43.22 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 04/21/2020 - 00:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel
To stop tasks you can try the following:
1. Click on the task itself and click cancel on the bottom task, then click cancel on the top task (Please see attached), please note that if you click cancel on the backup task and it does not actually cancel the task then proceed to step 2
2. Download Acronis Scheduler Manager - https://kb.acronis.com/SchedulerManager then follow the steps under Managing scheduled tasks to stop that specific task, if this does not stop the task proceed to step 4
3. Stop the Acronis Managed Service & Scheduler service and wait for the device icon in the management console to change from blue to gray once this has happened start these two services again, the task should then fail and if not proceed to step 4
4. Log a support case with the Acronis Support Team, they can stop the task for you from their end, they have a fantastic support team and will gladly assist you
5. Lastly even after stopping the task the dates on the backup might still not be resolved and you will need to follow the KB article in my previous response: https://kb.acronis.com/content/55244 (Just ensure that you first remove the device from the console, do not uninstall the agent or delete any of the backups just simply remove the device from the console itself)
I hope this resolves your issue,
Kind regards

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      535696-182019.png

                      57.01 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 04/21/2020 - 06:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            
o keep it registered here, the moment I canceled the locked activity, the backups had failures, like the attached figure,
well, i will delete and register the machine again and force incremental and post the result here.


 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      535728-182064.PNG

                      27.04 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 04/21/2020 - 12:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Awesome, let us know if this resolves your issue, please note that it "might" not reflect correctly immediately you will need to run a backup of the machine first for it to update the scheduler
Regards

      
                
                
                    
                                                    Wed, 04/22/2020 - 07:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello good Morning,
Run the procedures and everything went well, how the data was corrected, and the backups were performed at the correct times.

Taking the opportunity to answer a question, I have a backup plan for database, use of agent for BD, lately it has very large increments, or can it happen so that the incremental is so big? considering that the backup windows are very small.
      
                
                
                    
                                                    Wed, 04/22/2020 - 10:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel
Can you share what type of Database you are backing up? (MySQL, SQL, Oracle etc.)
What is the actual size of the DB on the machine?
What is the size of the backed up DB on the management console?
What are the sizes of the incremental backups?
What are the sized of the actual daily changes to the DB?
Is your backup scheme set to "Always Incremental (single-file)?"
Are you backing up the DB server as an entire machine backup with application aware backup of SQL and then a separate backup plan for the databases?
Regards
 

      
                
                
                    
                                                    Wed, 04/22/2020 - 16:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Microsoft SQL 2014 12.0
What is the actual size of the DB on the machine?
114 GB
What is the size of the backed up DB on the management console?
52Gb
What are the sizes of the incremental backups?

several small increments, how often do large backups appear, or what could it be?
https://prnt.sc/s44rr3
Is your backup scheme set to "Always Incremental (single-file)?"
Single-file
Are you backing up the DB server as an entire machine backup with application aware backup of SQL and then a separate backup plan for the databases?
Exactly, as described
      
                
                
                    
                                                    Wed, 04/22/2020 - 17:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel
So if you have a look at the separate backup plan for the database you will notice that the backup scheme is default Weekly full, daily incremental.
Can you double check that the large incrementals you are referring to are recurring on a weekly basis?
Something in the line of:
Monday 30 GB
Tuesday 1 GB
Wednesday 1 GB
Thursday 1 GB
Friday 1 GB
Monday 30 GB
Does this look familiar?
Regards

      
                
                
                    
                                                    Fri, 04/24/2020 - 09:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            
Understanding perfectly,

Below is my backup plan for the database group, so ask that I have a full monthly backup and a full weekly backup, as per the plan below.


 
https://prnt.sc/s56vb9

      
                
                
                    
                                                    Fri, 04/24/2020 - 11:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniel,
Please accept my apologies in advance, my Portuguese is very rusty I have not spoken it in a very long time,
If I understand your screenshot correctly your current retention period (How long to keep) is as follows:
Monthly - 1 Month
Weekly - 4 weeks
Daily - 7 days
And then you have an hourly backup which is kept for 24 hours
Now if I understand your previous response correctly, please do correct me if I am wrong and you want to apply a backup scheme which has a monthly full backup, weekly full backup and I assume daily incrementals
Then what can do is the following
Change the backup scheme under Schedule (Or if I am correct chronograma on your side) to a custom backup scheme. This will allow you to have a monthly full backup at a specific of the month, a weekly full backup at a specific day of the week and a daily incremental backup on specific days of the week
This will then be in the line of a full backup on the last day of the month (This you can configure to which day you wany), a weekly backup on Sunday (This you can configure to any day you want) and incrementals running from Monday to Saturday - Just an example you can specify the days as per your requirements.
You will then notice your How long to keep (Or por quanto tempo manter on your side) wlll change and ask you how long you want to keep the full backups for and how long you want to keep the incrementals for.
Just one last note on this if this is the way you want to go with just note that you will now have x2 full backups so although this methodis a great way of backing up to allow for a very granular recovery it will consume more disk space
I hope this makes sense to you,
Atenciosamente
 

      
                
                
                    
                                                    Fri, 04/24/2020 - 13:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniel Santiago
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            
Hello Jason, perfect explanation, all clear, take the opportunity to ask questions, as times my increments have equal values, there is no compression, it is an instance of the database.


 
https://prnt.sc/s6wjjt

      
                
                
                    
                                                    Mon, 04/27/2020 - 17:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good morning Daniel
When it comes to compression this is a difficult question to answer as literally every single customer is different as each customer I have worked with uses SQL in different ways.
One thing you can check is, what compression level are you using? If this is set to "None" then you will not be compressing the data - Now there are many reasons why this could have been set to "None" as I am not familiar with your environment or if have you taken over the backups from another person and they have set it this way etc.
To check compression level:
Devices > Microsoft SQL > Machine you are backing up > Protect > Backup Options > Compression level
In some cases I have set my customers compression level to "None" - Reason for this was to improve on the performance of the backups, basically making the backups run faster.
So in short you can check the compression level set on the backup and if it is:
None - You can change it to Normal which then uses the Acronis Compression Algorithm
Just keep in mind that IF this is the case and you change it from None - Normal then the backup itself will take longer
Regards

      
                
                
                    
                                                    Tue, 04/28/2020 - 06:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
