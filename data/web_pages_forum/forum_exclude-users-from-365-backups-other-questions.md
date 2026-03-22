# Exclude Users from 365 backups & other questions.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/exclude-users-365-backups-other-questions

## Original Post
**Author:** Unknown

Exclude Users from 365 backups & other questions.

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Nav Sangha
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
Our 365 CSP recommended Acronis to us and after setting up has been next to useless in helping is with the backup solution. I have a few questions.
1. We have a 365 tenancy that is being backed up into the Acronis Cloud, currently the backup is set at a group level. However we have several mailboxes which we don't need backing up, how can i exclude these users from the backup without having to go down the painful route of implementing individual backup plans for each user and ignoring users who i don't want backing up? Currently its a waste of a license.
2. If above isn't possible, is there a way of not importing the 365 user into Acronis in the first place.
 
3. When a 365 user leaves, we need to export the Acronis backup to on site storage, and then we can delete the user and free up a license, how can we do this?
4. When a user leaves, how do we remove a user from Acronis, or do we need to delete the user from the 365 end?
5. If we do delete a user from the 365 end, what happens to the backups in Acronis, do they get deleted or are they kept for the duration of the retention period?
 
Sorry, quite a few questions here i know.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 02/10/2021 - 08:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Nav, 
For questions 1 and 2 please refer to our user guide on all the available options to backup o365 data with the product - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
3. Recover the data to your on site storage using the following guide - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ… and then from the backup console remove the user who is no longer needed from the backup plan. 
4. If you remove the user from 365 end, modify the backup plan to exclude it and delete the archive the user will be completely removed. 
5. Backup will be kept for the duration of the retention period. 
If you have any further questions in regards to this please open a support ticket as per  https://kb.acronis.com/content/56079 . 
Thank you for your time. 

      
                
                
                    
                                                    Thu, 02/11/2021 - 13:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Nav Sangha
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
 
As we bought it from a reseller and its managed by them i dont know what the license keys are.
For 1 & 2, doesnt explain if its possible to exclude a user mailbox from a 365 backup or not.
For 3 - doesnt answer the question, we want to export all data held for a 365 user or has left the company to an onsite location, like a PST file or similar, that we can store on a NAS drive or somewhere similar and can browse it locally if required. Also I dont have an option to delete a 365 user from within Acronis.
For 4 - my backup plan doesnt have an option to exclude a user.
 

      
                
                
                    
                                                    Thu, 02/11/2021 - 15:13
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Nav,
 
On point 1 - The only way to specifically only backup specific user mailboxes is to drill down to "All users" and then select the users you would like to backup. An alternative would be to backup specific "Groups". If no backup plan is applied to a user then it will not consume a license
On point 2 - Acronis is linked with the O365 tenant so all mailboxes in the tenant will be linked with Acronis and will be visible in the console
On point 3 - You can recover the entire mailbox or email messages to cross-user and cross-organization or restore to a custom folder
On point 4 - As per point 1, if you remove the backup plan from the user and NO backup plan is present for that user then a license will not be consumed
On point 5 - If a user is deleted in O365 it will not remove the backup from Acronis, only when you physically remove the backed up data for that user from Acronis will it delete that specific users data.
I hope this helps,
Regards

      
                
                
                    
                                                    Tue, 03/02/2021 - 12:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jovica Zivkovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear experts,
We have many users who are still active on Acronis Cloud Backup with active licences while they were deleted few months ago from M365.
What is the correct procedure to remove users from Acronis Cloud Backup (automatically or manually) when they are removed from M365.
Is there any procedure to force delete and release licences even there are maybe still that users data on teams or sharepoint - I don't need that data.
Thank you

      
                
                
                    
                                                    Wed, 08/02/2023 - 16:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jovica Zivkovic wrote:

Dear experts,
We have many users who are still active on Acronis Cloud Backup with active licences while they were deleted few months ago from M365.
What is the correct procedure to remove users from Acronis Cloud Backup (automatically or manually) when they are removed from M365.
Is there any procedure to force delete and release licences even there are maybe still that users data on teams or sharepoint - I don't need that data.
Thank you


Hello Jovica.
Welcome to the forum!
Our C2C agent detects the users and attribute them a seat by default.
The cloud agent synchronizes with Microsoft 365 every 24 hours, starting from the moment when the organization is added to the Cyber Protection service. If you add or remove a user, group, or site, you will not see this change in the Cyber Protect console immediately. To synchronize the change immediately, select the organization on the Microsoft 365 page, and then click Refresh.
Please refer to the following user-guide: https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
If the issue persists after refreshing the vault manually, please raise a ticket with our support so we can investigate and help you:  https://kb.acronis.com/content/8153
Thanks in advance!

      
                
                
                    
                                                    Thu, 08/03/2023 - 05:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jovica Zivkovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            On other forum I got this reply 
- The other possible reason could be that there are still backups existing that associated with these accounts.
---------------------------------------------------------------------------------------------------
So, in this case is this the only way to remove that users? Also, I guess, we will need to pay for an orphan storage, but why licenses?
Thank you :)
 

      
                
                
                    
                                                    Wed, 08/09/2023 - 09:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jovica Zivkovic wrote:

On other forum I got this reply 
- The other possible reason could be that there are still backups existing that associated with these accounts.
---------------------------------------------------------------------------------------------------
So, in this case is this the only way to remove that users? Also, I guess, we will need to pay for an orphan storage, but why licenses?
Thank you :)
 


Hello,
Please note that if you follow the instructions provided in that knowledge base (KB), everything within the account registered under that user will be deleted and all the machines unregistered. The user of the tenant is not related to the O365 users. The O365 is an independent product managed by Microsoft, our C2C agent just connects with the account and displays the information reported from there.
Additionally, please be aware that even if a Microsoft 365 license is removed from a user, their data can still be backed up, consuming quota. This situation can only be resolved by deleting the user from the Microsoft 365 admin center or by removing them through Active Directory synchronization. You can find more information here: https://learn.microsoft.com/en-us/answers/questions/476061/what-happens-to-the-user-data-if-i-remove-the-lice
I am also including the knowledge base article about quotas here: https://kb.acronis.com/content/69686
If the issue persists after reviewing this process in the O365 organization, kindly raise a support ticket for investigation: https://kb.acronis.com/content/8153
Thank you in advance!

      
                
                
                    
                                                    Wed, 08/09/2023 - 09:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jovica Zivkovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I think the problem is now resolved, the M365 seats number started to drop
https://kb.acronis.com/content/72563

      
                
                
                    
                                                    Tue, 08/15/2023 - 12:35
