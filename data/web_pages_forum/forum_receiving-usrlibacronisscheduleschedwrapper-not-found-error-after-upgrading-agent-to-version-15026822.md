# receiving /usr/lib/Acronis/Schedule/schedwrapper: not found" error after upgrading Agent to version 15.0.26822

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/receiving-usrlibacronisscheduleschedwrapper-not-found-error-after-upgrading-agent-version-15026822

## Original Post
**Author:** Unknown

receiving /usr/lib/Acronis/Schedule/schedwrapper: not found" error after upgrading Agent to version 15.0.26822

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Riccardo Orlandi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We are using Acronis Backup provided by IONOS. After upgrading the Agent version (15.0.26822) on our hosted linux server from the backup web administration panel (there were an alert asking to update it), we started to receive email whose subject is "Cron <root@main> /usr/lib/Acronis/Schedule/schedwrapper -m cron -i 1" (the final number is varyng) and the following content:
/bin/sh: 1: /usr/lib/Acronis/Schedule/schedwrapper: not found
There is already a discussion about this error, but our purpose is not to stop the mail messages or to redirect them: we need to understand what this error menas and how to remove it.
Thanks a lot for the help
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/01/2021 - 10:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Riccardo,
Welcome to Acronis forums!
This could be an old Cronjob Schedule task of the previous Agent's build which is still configured instead of the new PHP script that had to be switched automatically in Crontab.
Please re-deploy the protection plan in the Backup Console to this Agent. If it does not help, please continue the investigation with the support team. 

      
                
                
                    
                                                    Thu, 07/01/2021 - 11:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Riccardo Orlandi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you very much.
Please, how can I re-deploy the three existing plans? Must I revoke them and then reassign again? I cannot risk to delete the plans nor to loose the existing backup archives.
Thank you
 

      
                
                
                    
                                                    Thu, 07/01/2021 - 12:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Riccardo, 
That is correct. 
You must revoke and reapply the existing protection plans. 
There is no risk to the backups during this procedure. 
If you face any difficulties please reach out to our support team.

      
                
                
                    
                                                    Tue, 07/06/2021 - 09:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
