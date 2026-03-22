# [RESOLVED] How to clean up the retention for existing backup plans (deleting incomplete backup)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-how-clean-retention-existing-backup-plans-deleting

## Original Post
**Author:** Unknown

[RESOLVED] How to clean up the retention for existing backup plans (deleting incomplete backup)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Can anyone tell me how we can clean up the existing retention data for backup plans.
Example: We create a backup plan for a customer wich has 200GB of backup already and the quotum is 250GB.
Now we want to clean up this retention, how can we do this manually?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/25/2016 - 13:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Global-e,
Thank you for your posting! If you understand that the storage is running out of free space soon, you may want to consider the following ways:
Increase the quota
Change retention rules settings
Remove old or incomplete backups using Web Restore
Thank you,

      
                
                
                    
                                                    Mon, 03/28/2016 - 08:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
 
Thank you for replying.
I would like to use the option to "Remove old or incomplete backups using web restore", since this is wat we are searching for.
Can you tell me how we can access the web restore console? Because when i try to perform these action trough the management console i cannot find the option to delete a certain old backup set.

      
                
                
                    
                                                    Tue, 03/29/2016 - 11:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
I've created a screenshot with steps how you can access the WebRestore console:
Backup Management Console > Recover > More ways to recover > Download files > Login with End user credentials
Please make sure to use the credentials of the end user who installed the agent on the protected machine.
If you don't have the end user credentials and cannot login to WebRestore, you only have following options:
Remove single recovery points in the Backup Management Console (works for complete backups only)
Delete the end user with all his data in the cloud including incomplete backups
Let us know if you need more details on this.
Best regards,

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      343500-127132.jpg

                      55.66 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 03/29/2016 - 12:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dmitry,
 
Thank you for the detailed instructions.
This helps us out greatly, the case is resolved!

      
                
                
                    
                                                    Thu, 03/31/2016 - 09:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Great, thanks for your feedback!

      
                
                
                    
                                                    Thu, 03/31/2016 - 09:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            One more question,
 
In the overview there is an option called "Not completed, or unfinisched backups".
There is a lot of data in there wich can be removed.
 
Is this data from failed or incomplete backups? or is this data that is currently building up because of a running job.
In other words, is it safe to delete this data?

      
                
                
                    
                                                    Thu, 03/31/2016 - 10:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi CS,
The Incomplete Backups section includes both failed and incomplete running initial backups. You will see different sections for different archives. It is safe to hit delete for any of those as data for currently running backups will not be affected.
Once the first full backup is complete, all running incremental backups will be written directly to the respective archive and will no longer appear in the Incomplete Backups section.
Best regards,

      
                
                
                    
                                                    Thu, 03/31/2016 - 10:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
