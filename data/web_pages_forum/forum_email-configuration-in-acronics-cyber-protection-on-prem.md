# Email configuration in Acronics Cyber Protection On Prem

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/email-configuration-acronics-cyber-protection-prem

## Original Post
**Author:** Unknown

Email configuration in Acronics Cyber Protection On Prem

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Himanshu Dwivedi
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I have an environment where acrinics cyber protect on prem is installed and customer wants us to configure email services and create an email alert Once any activity/rule is executed, just like a back up is created or maybe the back of his failed, etc. I just want to know the prerequisites to configure and email and the configuration of alerts.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 06/08/2025 - 12:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Yoji
                            

                            
                    
                        Frequent Poster
                    
                
            
                        
                
                    Posts: 26
                
            
            
                
                    Comments: 843
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You sound like a professional doing some work for a customer.. 
If you dont know.. may be RTFM? 
Acronis True Image

      
                
                
                    
                                                    Sun, 06/08/2025 - 21:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
It looks like you may have posted in the wrong forum.
I believe you're referring to Acronis Cyber Protect 16.
Here are the available notification settings:

Quota overuse notifications (enabled by default):
	Notifications when quotas are exceeded.


Scheduled usage reports:
	Usage reports sent on the first day of each month.


Failure, Warning, and Success notifications (disabled by default):
	Notifications about protection plan execution results and disaster recovery operations for each device.


Daily recap about active alerts (enabled by default):
	A daily summary of failed or missed backups and other issues, sent at 10:00 (data center time). If there are no issues, the recap is not sent.

All notifications are sent to the user’s email address.
Note: There are no notifications when a backup starts — only when it finishes.
For more details, please refer to the documentation:Acronis Cyber Protect 16 – Email Notifications
If you have any questions, feel free to contact our support team:https://support.acronis.com/
Best regards.

      
                
                
                    
                                                    Mon, 06/09/2025 - 07:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
