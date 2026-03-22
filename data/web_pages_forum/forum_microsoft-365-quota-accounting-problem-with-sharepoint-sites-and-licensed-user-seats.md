# Microsoft 365 Quota Accounting Problem with Sharepoint Sites and Licensed User (seats)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/microsoft-365-quota-accounting-problem-sharepoint-sites-and-licensed-user-seats

## Original Post
**Author:** Unknown

Microsoft 365 Quota Accounting Problem with Sharepoint Sites and Licensed User (seats)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Julio Divietro
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Forum Members,
 
I have a costumer where I am trying to understand how ACRONIS and Microsoft are sincronizing the usage quotas.  Actually I have 33 seats available, and 30 of that are been used to Mail Box and OneDrive backups.  Now I've tried to backup a Sharepoint site (Group Site - Modern Site at Sharepoint) where the actual members already are licesend cause they have an mail box and one drive backup associated.   
But as soon I applied and execute the plan the quota jump to a number of seats that is incompatible with the members that have permission to access this sharepoint site.  I am broking my head and cannot find a solution.
Links that I searched for the solutionÇ
https://care.acronis.com/s/article/69686-Acronis-Cyber-Protect-Cloud-Ne…
 
Thanks in advance team!!
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/24/2024 - 18:35

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cyber Protect Cloud 
MSP Partner
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please note that once you add an organization, all users in that organization are added, including inactive ones.
You need to review the organization or site and check the exact number of users there.
Please refer to the following Knowledge Base article where this is explained: https://care.acronis.com/s/article/Acronis-Cyber-Protect-Cloud-OneDrive-Teams-SharePoint-seat-calculation-prerequisites?language=en_US
If you encounter any issues with the user count, please raise a ticket with our team: https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Fri, 10/25/2024 - 06:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Julio Divietro
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            In that case, We assumed that all users sync with M365 are considered but only users with a protect plan are licensed as valid count user.  
The sharepoint group protected with a specific protect plan seems that are considering users that not necessary are part of the group members.  
Probably that sharepoint group has some users not visible on M365 but its considered at ACRONIS quota for M365 users.  How to check the real user part of a M365 group?

      
                
                
                    
                                                    Thu, 10/31/2024 - 01:25
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Cyber Protect Cloud 
MSP Partner
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Julio Divietro wrote:

In that case, We assumed that all users sync with M365 are considered but only users with a protect plan are licensed as valid count user.  
The sharepoint group protected with a specific protect plan seems that are considering users that not necessary are part of the group members.  
Probably that sharepoint group has some users not visible on M365 but its considered at ACRONIS quota for M365 users.  How to check the real user part of a M365 group?


Hello!
Using Microsoft 365 Admin Center:

Go to the Microsoft 365 Admin Center:
Visit admin.microsoft.com and sign in with an account that has the necessary permissions (e.g., Global Admin).


Navigate to Groups:
In the left navigation pane, go to Groups > Active groups.


Select the Group:
Find and click on the M365 group you want to inspect.


View Members:
Go to the Members tab, where you’ll see a list of all users in the group.
Manually check each member for any guest or system/service accounts. Real users will typically have email addresses associated with your organization's domain.

If you find any mismatch between what's shown in M365 admin center and in the Acronis Console, please record a video and screenshots and raise a ticket with our support.
Best regards.
 

      
                
                
                    
                                                    Thu, 10/31/2024 - 08:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
