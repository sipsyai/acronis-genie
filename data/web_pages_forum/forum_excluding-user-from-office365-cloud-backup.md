# Excluding User from Office365 Cloud backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/excluding-user-office365-cloud-backup

## Original Post
**Author:** Unknown

Excluding User from Office365 Cloud backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Philip Rabensteine
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all, 
I have setup an Office365 cloud-to-cloud backup for an organization, and foresee several customers more like this, where I want to automatically backup all users moving forward. According to the documentation here the proper method is to setup a "Group Backup". So I have done this. The issue comes into play when I have this selected, but there is a user account in Office365 which does not have a mailbox. It is included in this group backup, and I am getting alerts/errors for it. I do not want these alerts, errors, or to even attempt the user backup. At the same time I want to automatically capture new users moving forward. 
Is it possible to exclude a user, or users, from the group backup? I've tried to find a KB, or article on how-to, with no luck. I cannot seem to modify the backup plan for any user as it says, "The plan is applied to group All Users". (see included Screen snippet.) Is there a different work around to achieve what I'm looking for as default functionality? This setting for the OneDrive backups appears to function the same way also.
Thanks in advance,
PR

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/17/2019 - 22:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Philip,
 
It's Evgeny from Acronis Service Provider Support. 
If a user does not have the mailbox the warning message will be returned in the current version. 
In Acronis Data Cloud 7.8 U2 the backup plan will not be started if the user does not have mailbox or the mailbox is non-licensed. The internal reference that will appear in the release notes will be - ABR-201732
The ETA for the release differs among the Datacenters, but we are going to notify the Partners prior to the release. 
In the meantime, you can revoke the plan from group level and configure individual backup plans for the active mailboxes.
 
-----------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Fri, 01/18/2019 - 12:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Philip Rabensteine
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for the insight Evgeny! I look forward to the addition of this feature, and implementation of 7.8u2 in the us5-cloud datacenter!!!
-Philip

      
                
                
                    
                                                    Fri, 01/18/2019 - 13:50
