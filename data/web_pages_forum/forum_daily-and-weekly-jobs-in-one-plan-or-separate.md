# Daily and weekly jobs in one plan? Or separate?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/daily-and-weekly-jobs-one-plan-or-separate

## Original Post
**Author:** Unknown

Daily and weekly jobs in one plan? Or separate?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I'm confused by the schedules in Acronis.
Question 1: I have one Plan set to daily backup but the overview of that plan lists retention policies for Weekly and Monthly too (see screenshot). If I set the schedule to Schedule > Daily > Run every day, does it do Weekly and Montly backups somewhere too? Because I don't want that for this plan. I only want Daily backups in this plan.

Question 2: suppose I have another VM which needs to backupped daily but also weekly. The retention needs be 7 days for daily and 4 for weekly. Can I achieve that with one plan? Or do I need multiple plans for that.
Thanks in advance.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 10/18/2021 - 12:12

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi dxxSDZX. 
Please refer to the following for question 1 - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…, the explanation appears when you point to Backup Set in the pop up tool tip. 
For question 2 - Please refer to the following - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
If you face any further difficulties please open a case with the support team and we will happily assist. 

      
                
                
                    
                                                    Mon, 10/18/2021 - 13:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            As for question 1 > I've read the link but still don't find an answer to my question, maybe I'm overlooking it. I understand that there are different retention rules for different sets but I want to know, if I select a daily schedule on a VM...will that be the only schedule that's being used for backups for that VM? Or will Acronis also do weekly and monthly?
As for question 2> That link refers to the general info about the scheduling of backups and the moments a job start and doesn't answer my question. I want to know if I can backup a specific VM using one plan but with multiple sets (daily and weekly).

      
                
                
                    
                                                    Mon, 10/18/2021 - 14:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello dxxSDZX,
thank you for posting on Acronis forums!
According to a picture of your backup plan, there are only Daily backups that run every day at 3:00 PM, no monthly, and no weekly backups.
As for question 2> That link refers to the general info about the scheduling of backups and the moments a job start and doesn't answer my question. I want to know if I can backup a specific VM using one plan but with multiple sets (daily and weekly).

A VM could be backed up by several backup plans. However, you can schedule the weekly/daily scheme as here
https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#schedule.html
Furthermore, you can set up retention rules by backup age or by number of backups, not by default as on your picture.
 

      
                
                
                    
                                                    Mon, 10/18/2021 - 18:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    dxxSDZX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @Maria Belinskaya: thanks for your reply. As for question 1 and the picture, thanks for clearing that up.
As for question 2: I think the document you're referring too has 1 backup set as scenario. Not quite sure though. I find some parts of Acronis pretty confusing but maybe I'm just dumb. Either way, I have set up the VM now with two plans: a plan with daily backup and 7 days retention and another plan with weekly backup and 4 weeks retention.

      
                
                
                    
                                                    Wed, 10/20/2021 - 13:39
