# Office365 - Sharepoint team site - files not found during recovery

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/office365-sharepoint-team-site-files-not-found-during-recovery

## Original Post
**Author:** Unknown

Office365 - Sharepoint team site - files not found during recovery

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    x x
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, 
I need to restore a single file from a Sharepoint site, but I can't find any file in the backups.
The sharepoint site has been created using the "team site" template in Microsoft365, no Teams attached to it.
In Acronis the site is visibile in the "Groups" menu, not Site collections.
I could see all the backups and the size of each run tells me that the data is actually being transferred.
However, when I try to browse the backup to restore the file, I can only see a section called "Pages" and nothing else.
I tried
Acronis guide to restore a sharepoint site doesn't address this issue. 
Does anybody know how to find the files and folders?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/09/2025 - 13:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    x x
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            SOLUTION:
Rebuild the index.
Backup Storage -> select the location -> select the backup and click con "Rebuild Index".
After 1 hour 30 minutes I was able to see the files and folders.
It would be nice for Acronis to automatically check for corrupted index, since it can slow down the recovery time, failing our RTO

      
                
                
                    
                                                    Wed, 07/09/2025 - 16:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello and welcome to the forum!
Thank you for reaching out.
Please refer to the following Knowledge Base article for more information on the issue:
? Acronis Cyber Protect Cloud: Unable to browse or recover SharePoint data because the recovery points are empty
Our Development Team is actively working on a fix.
Best regards.

      
                
                
                    
                                                    Thu, 07/10/2025 - 06:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
