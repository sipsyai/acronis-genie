# Deleted Incremental Backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/deleted-incremental-backups

## Original Post
**Author:** Unknown

Deleted Incremental Backups 

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Greetings,
I have a question regarding incremental backups, specifically deleting links in the chain.
Given a chain of incremental backups 1 through 10. Backups are stored on local network disk. Backup 5, 7, 8, and 9 were deleted manually from the web console. Is it possible to repair the chain? How to remedy or restart given limited disk space to handle the movement. Initial need was to clean up disk space due to a incorrect/previous retention policy filling up disk. I understand that Backups 1-5 in this example should be in tact 6, and 10 are useless and can be deleted, the next backup (11) will be a true incremental on top of 5.
Thanks for reading,

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/10/2024 - 20:37

                                                          
                                                            
                                                                                        
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Unfortunately, once backups are deleted, it is not possible to reverse the procedure unless you have a second location where they were also stored. If no secondary location exists, the backups are permanently deleted from your local premises.
To prevent such scenarios, we offer an immutable storage feature, but it is only available for backups stored in the cloud. You can find more information here: Immutable Storage.
Regarding the backup sequence, new incremental backups will build on the latest remaining backup that has not been deleted.
Best regards.

      
                
                
                    
                                                    Wed, 12/11/2024 - 08:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
Regarding the backup sequence, new incremental backups will build on the latest remaining backup that has not been deleted.

Are you saying that the chain remains OK after deleting a backup and that I can restore from any remaining backup? 

      
                
                
                    
                                                    Wed, 12/11/2024 - 18:46
                                                                            
                                
                            
                                            
                                            
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            RW Smith wrote:

Hello Jose,
Regarding the backup sequence, new incremental backups will build on the latest remaining backup that has not been deleted.

Are you saying that the chain remains OK after deleting a backup and that I can restore from any remaining backup? 


If backups are deleted within the app, the remaining backups should remain intact.
However, if backups are deleted outside the app ( if the user deletes them manually in the storage, for example ), it could corrupt the entire backup chain.
Best regards.

      
                
                
                    
                                                    Thu, 12/12/2024 - 08:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Backups were deleted inside the web console. (https://us-cloud.acronis.com/ui/#/backup-console/backups/vaults-locatio…). Is there documentation on this?
Thank you,

      
                
                
                    
                                                    Tue, 12/17/2024 - 03:09
                                                                            
                                
                            
                                            
                                            
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            RW Smith wrote:

Backups were deleted inside the web console. (https://us-cloud.acronis.com/ui/#/backup-console/backups/vaults-locatio…). Is there documentation on this?
Thank you,


Hello!
You can also review the following Knowledge Base articles for a detailed technical explanation:
Retention rules: how and when they work
Acronis Cyber Protect Cloud version 12: backup format archive3
Deleting backups
Please note that the web interface will not allow you to delete backups if it would break their dependencies. The error message "Please insert the last volume of the multi-volume backup archive" typically occurs when backups were deleted outside of the program.
If the issue persists, kindly respond to the ticket our support team sent you 5 days ago, as they are still awaiting your reply.
Best regards.
 
 
 

      
                
                
                    
                                                    Tue, 12/17/2024 - 10:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RW Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Jose,
This is different from what support was saying and so I greatly appreciate the verification via documentation.
I will try to Validate the Backup and reproduce the error again ("Please insert the last volume of the multi-volume backup archive") as the backups in my case were in fact deleted using the Acronis web console UI.
The validation can only be performed within certain time windows for us. I appreciate the patience.
 

      
                
                
                    
                                                    Tue, 12/17/2024 - 16:12
                                                                            
                                
                            
                                            
                                            
    
                    
                RW Smith
 

            
                            
                Products: 
                Acronis Cyber Protect 16
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            RW Smith wrote:

Thank you Jose,
This is different from what support was saying and so I greatly appreciate the verification via documentation.
I will try to Validate the Backup and reproduce the error again ("Please insert the last volume of the multi-volume backup archive") as the backups in my case were in fact deleted using the Acronis web console UI.
The validation can only be performed within certain time windows for us. I appreciate the patience.
 


Hello!
I’ve updated the support ticket and requested the team to review the entire situation to determine if any misunderstanding occurred.
You can expect a reply as soon as possible.
Best regards.
 

      
                
                
                    
                                                    Tue, 12/17/2024 - 19:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
