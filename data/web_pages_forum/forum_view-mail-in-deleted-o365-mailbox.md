# View mail in deleted O365 mailbox?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/view-mail-deleted-o365-mailbox

## Original Post
**Author:** Unknown

View mail in deleted O365 mailbox?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nic Gotrel
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
We backup our O365 mailboxes daily and have done so for many months using Acronis Cyber Protect.
I've been asked if I can view the mail for a user who left the company a few months ago. The AD account and mailbox have long been deleted.
On Acronis, if I go into Devices > Microsoft 365, the mailbox I am looking for is no longer there. A user who has not been deleted in AD has backups going back months as expected.
If I go into Backup Storage > Backups > Cloud Application Backups, the mailbox I am looking for is no longer there.
I would have thought that historic backups of mailboxes would be retained unless I manually deleted them. Am I looking in the wrong place ? Or are they gone totally.
Thanks

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/20/2024 - 15:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
According to Microsoft policy, when a user, group, or site is removed from the Microsoft 365 graphical user interface, it remains available via an API for a few days. During this period, the removed item is inactive (grayed out) in the Cyber Protect console and is not backed up. When the removed item becomes unavailable via the API, it disappears from the Cyber Protect console. Its backups (if any) can be found at Backup Storage > Cloud applications backups.
If you can't find the backups directly in the backup storage, please contact the team at https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Thu, 06/20/2024 - 22:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
