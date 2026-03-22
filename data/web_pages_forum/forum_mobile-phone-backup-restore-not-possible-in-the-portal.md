# Mobile Phone Backup restore not possible in the portal

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/mobile-phone-backup-restore-not-possible-portal

## Original Post
**Author:** Unknown

Mobile Phone Backup restore not possible in the portal

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
A customer does backup his mobile phone with Acronis. The backup works, and he can restore it over the app on his mobile phone. But if he want to restore something in the portal (cloud.acronis.com), then he get the following error message:
Cannot access the mobile backup: either you have no access rights, or the backup was removed.
Is this a bug, or is there really a special access right needed to restore? Restores for his Windows workstation are working over the portal, only mobile restore not.
Regards
Michael

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 03/29/2022 - 06:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Michael,
thank you for your posting! Normally, this message is shown when a user is logged in to the Cyber Protect web console with a wrong account. Only the owner of a device has access to backups of this device. You can check the account used to create a backup in the details of a backup plan

If the account corresponds to the one shown in the backup plan details, I'd recommend raising a support ticket for this issue.

      
                
                
                    
                                                    Thu, 03/31/2022 - 12:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina
 
It looks like when the user has the "company admin" rights, then it works. With "read-only admin" rights it does not work. For me this looks like a bug.
 
Regards
Michael

      
                
                
                    
                                                    Mon, 04/04/2022 - 08:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Moataz A
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael, 
Thank you for the feedback.
Mobile backups are only accessible to the user that created the backup, this is by design, see below document:
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…?
 
The data backed up from mobile devices registered under your account is available only under this account. Nobody else can view or recover your data.
Since mobile backups are only accessible to the user the device is registered to, a read-only role will be insufficient to recover data, see role description below:
Read-only administrator
The role provides read-only access to all objects of the Cyber Protection service. Such users can access data of other users of the organization in the read-only mode.
I'd recommend opening a support case with reference to this forum thread as the restore from the app works, and we'll be happy to review further.
Thank you!

      
                
                
                    
                                                    Tue, 04/19/2022 - 15:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Moataz Aboghalia | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
