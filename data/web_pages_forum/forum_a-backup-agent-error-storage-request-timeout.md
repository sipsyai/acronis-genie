# A backup agent error: 'storage request timeout'

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-agent-error-storage-request-timeout

## Original Post
**Author:** Unknown

A backup agent error: 'storage request timeout'

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Darren Brinksneader
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I am seeing this error dozen of times for both of my customers using Backup Cloud, for almost 24 hours now.

They are both backing Office 365.
The error appears to only be occurring for Office 365 backups.  

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 08/24/2019 - 12:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Darren
Could you please run the cloud connection verification tool within the customers network:
https://kb.acronis.com/content/47145
And provide us with the results as this will show if all required ports and name resolutions are open.
Regards
 

      
                
                
                    
                                                    Mon, 08/26/2019 - 07:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Darren Brinksneader
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            This is not on-prem backup.  This is for Office 365 Backup.  It appears that Microsoft may be throttling the specific customer tenant.  It works for a while, maybe backs up about 10-12 mailboxes/onedrives then starts denying storage requests again.  

      
                
                
                    
                                                    Mon, 08/26/2019 - 12:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Darren
My apologies, I know see that the KB article has slightly changed since the last time I used it, within the article you can click on:
"If you are using Acronis Backup 12/12.5 or Acronis Backup Cloud, please refer to this article"
This will direct you to the right article, regarding throttling I have some large customers running Office 365 backup and they are not experiencing any issues with the amount of mailboxes being backed up. The issue might be more related to a firewall.
Please provide output of above article (Please remove username and password)
Regards

      
                
                
                    
                                                    Mon, 08/26/2019 - 13:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Darren Brinksneader
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Not firewall related. This is straight cloud-to-cloud backup with Acronis Backup Cloud.

      
                
                
                    
                                                    Mon, 08/26/2019 - 13:59
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Darren,
I'd open a support ticket for this issue, as the message "storage request timeout" would likely require investigation of log files from our datacenters. 

      
                
                
                    
                                                    Wed, 08/28/2019 - 06:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
