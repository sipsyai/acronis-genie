# Restore of M365 mailbox

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/restore-m365-mailbox

## Original Post
**Author:** Unknown

Restore of M365 mailbox

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Allan Mosegaard Møller
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello all
I'm new to this forum and to the acronis cyber protect cloud solution so i have what i think to be a noob question :-)
We have some mailboxes that are missing mails older mail from all folders (probably caused by some retention fuck up). The mailbox i question is missing all mails from feburary 3 2021 to january 6 2023. I would like to just do a complete maibox restore to the users mailbox so they will get their mail back without any other hassle, but our supplier says that if we do it that way me might end up with a lot of duplicates because the system can't just restore the part that is missing or a delta restore. This sounds very strange to me if this is not possible so could anybody please clarify if our supplier is right or if they are wrong.
Kind regards
Allan Mosegaard Møller

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 09/25/2024 - 11:27

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
It depends on your backup configuration. If you're backing up the M365 organization specifically, you can recover the mailboxes by following the steps in this user guide: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#recovering-mailboxes-52550.html.
Keep in mind that everything depends on the retention rules set in your backup plans. Since the emails you're referring to are from a long time ago, there’s a chance the backups may have been deleted, so it's important to review that first.
If you're backing up disks (assuming you're not performing cloud backups) and not specifically mailboxes, the only way to retrieve that data would be by recovering the backups as individual files and folders or by extracting them: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#extracting-files-from-local-backups.html.
Best regards.

      
                
                
                    
                                                    Wed, 09/25/2024 - 11:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Allan Mosegaard Møller
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The mails are all there in an old backup because they were deleted within the last couple of months. But is there some way to restore them so that it is only the mails that are missing that will be restored ?

      
                
                
                    
                                                    Wed, 09/25/2024 - 12:54
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Allan Mosegaard Møller wrote:

The mails are all there in an old backup because they were deleted within the last couple of months. But is there some way to restore them so that it is only the mails that are missing that will be restored ?


As mentioned above, it depends on the type of backups you have. There are specific backups for the O365 organization ( Cloud to Cloud ) and regular disk backups.
If you performed regular disk backups, it’s not possible to directly restore those old mailboxes. However, if you have a backup file, you can manually extract the data and recover it as files and folders, which is the only proper method I see for doing this.
If you executed a specific OneDrive backup with the organization added in the console ( cloud-to-cloud ), you can recover the mailbox by following the user guide I referenced earlier: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#recovering-mailboxes.html . 
Please note that if the backup has been deleted, it will not be possible to recover any data.
Best regards.
 
 

      
                
                
                    
                                                    Wed, 09/25/2024 - 14:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
