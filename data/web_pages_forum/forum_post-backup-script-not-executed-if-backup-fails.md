# Post-backup script not executed if backup fails

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/post-backup-script-not-executed-if-backup-fails

## Original Post
**Author:** Unknown

Post-backup script not executed if backup fails

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, we have many servers where we setted pre/post-backup scripts where mainly on pre-backup stop one o more services and on post-backup restart them.
Unfortunately we notice that if backup fails does NOT run post-backup script with important services that remain stopped and must be restart manually the next morning causing problems for customers.
I did a fast search but I not found a wait to solve it (except doing them in fixed time scheduler out of backup that is not good).
Is there a way to execute the post-backup script even if backup fails that I not found?
Thanks for any reply and sorry for my bad english.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/17/2019 - 10:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Emilio
What are the function of the pre/post scripts, are they there for MySQL or stopping services of non-VSS-aware application before snapshot and starting them after backup. Basically why do you have the scripts in place?
With what error message does the backup fail?
 

      
                
                
                    
                                                    Wed, 06/19/2019 - 07:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, thanks for reply. The pre/post-backup script stop/start services that significantly slow down the backup and/or make the backup fail due to lack of memory (it seems about big storage differences from the snapshot onwards).
Here a screenshot from activity of one backup failed that not had executed post-backup script:

I saw also another important issue, on some backups where there are unexpected case seems block backup for long time (also 20-30 hours before continue or give backup error and terminate), latest weekend I saw it in a total of 7 servers, all with cloud backup, in 3 different clients (therefore not due to the connection of a single customer) 5 failed (and with post-backup script not executed) and 2 completed correctly like this:

Note: 1 had already number of retry in errors settings to 3; so I suppose that change the number of retry and its interval in the backup plan not solves these issue...

      
                
                
                    
                                                    Wed, 06/19/2019 - 08:49
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio,
currently, the execution of a post-backup command directly depends on the successful completion of the related backup task. I've added this forum topic as a vote for the existing change request (internal ID for ref ABR-63219)
> block backup for long time (also 20-30 hours before continue or give backup error and terminate)
I'd recommend raising a support ticket for this issue, so that our engineers can look into the situation and help. 
 

      
                
                
                    
                                                    Mon, 06/24/2019 - 14:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dominique Bünzli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Is it possible to have any news on this important feature request ? Thanks !
currently, the execution of a post-backup command directly depends on the successful completion of the related backup task. I've added this forum topic as a vote for the existing change request (internal ID for ref ABR-63219)
I can add my vote to it if necessary.
 

      
                
                
                    
                                                    Sat, 05/07/2022 - 19:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dominique,
added your vote, thank you! Unfortunately, there is currently no ETA we could share, the feature request is still under consideration.

      
                
                
                    
                                                    Sun, 05/08/2022 - 10:26
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dominique Bünzli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Any news on this ? Is it really not possible to launch a script if the backup fails ?
Thanks !

      
                
                
                    
                                                    Wed, 02/01/2023 - 13:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dominique,
I'm afraid we don't have any update to share regarding this request. Currently, the post-command is always executed following the backup task. 

      
                
                
                    
                                                    Mon, 02/13/2023 - 15:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
