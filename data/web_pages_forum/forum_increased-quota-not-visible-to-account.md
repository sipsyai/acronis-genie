# Increased quota not visible to account

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/increased-quota-not-visible-account

## Original Post
**Author:** Unknown

Increased quota not visible to account 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
in acronis protect cloud we have increased the quota for cloud backup (added 100 GB), however after more than 4 days, backup plans are failing due to “quota exceeded”. The increased space is visible in the account.
please advice,
 
best regards
K

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 07/21/2024 - 17:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kostas!
Welcome to the forum.
The following error appears in the logs:
"There is no free space on Acronis Cloud Storage. Used space: 300.1 GB; Storage quota: 300 GB. Please upgrade the subscription. Otherwise, further backups will fail."
Please log in to the web restore panel with the administrator account for Systemgraph and check the displayed size: Acronis Cyber Protect Cloud Web Restore or Web Recovery Console.
The backup console might not be showing the correct size because some incomplete backups might be stored and need to be deleted.
Kindly review the following article: Acronis Knowledge Base.
I can see that you have enabled the 400GB quota, but we must ensure that it is not exceeded.
If the issue persists after reviewing the web restore panel and confirming there are no incomplete backups stored, please raise a ticket with the team (or with your service provider/reseller) so we can troubleshoot the issue and help you resolve it.
Best regards.
 
 
 

      
                
                
                    
                                                    Sun, 07/21/2024 - 17:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you very mych,
I checked as you suggested, and found the following:
1. Backup sizes are not visible (tried different browsers, see attached: sizes-not-visible.png)
2. Consumed size is calculated correctly, and not exceeded (backup-sizes-1.png, backup-sizes-2.png). After deleting one backup set entirely, the new size is reflected.
Best regards
Kostas


 


      
                
                
                    
                                                    Mon, 07/22/2024 - 13:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Kostas Backas wrote:

Thank you very mych,
I checked as you suggested, and found the following:
1. Backup sizes are not visible (tried different browsers, see attached: sizes-not-visible.png)
2. Consumed size is calculated correctly, and not exceeded (backup-sizes-1.png, backup-sizes-2.png). After deleting one backup set entirely, the new size is reflected.
Best regards
Kostas


 



Hello.
That must be troubleshooted internally.
Please raise a ticket with the team attaching the cloud certificate so the team can investigate: https://care.acronis.com/s/article/60082-Acronis-cloud-certificate-loca…
Best regards. 

      
                
                
                    
                                                    Mon, 07/22/2024 - 13:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Τhank you,
I started asking questions in the community, because I cannot raise a ticket, no matter which section I select (as partner or business customer), this keeps telling me that "No products are found".
Best regards
Kostas

      
                
                
                    
                                                    Mon, 07/22/2024 - 13:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Kostas Backas wrote:

Τhank you,
I started asking questions in the community, because I cannot raise a ticket, no matter which section I select (as partner or business customer), this keeps telling me that "No products are found".
Best regards
Kostas


If this issue occurs, it might be because you do not have a direct contract with Acronis. If you are working through a service provider or reseller, they will need to raise the issue on your behalf.
Best regards.

      
                
                
                    
                                                    Mon, 07/22/2024 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for your help,
I've reached out to the service provider, they checked our setup, and find everything OK, but the newly added capacity that we add to the customer, is not visible on the customer panel. They said they will create a ticket with Acronis for this.
I will post results for others to benefit as soon as I get them.
 
Best regards
K
 

      
                
                
                    
                                                    Thu, 07/25/2024 - 13:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Kostas Backas wrote:

Thank you for your help,
I've reached out to the service provider, they checked our setup, and find everything OK, but the newly added capacity that we add to the customer, is not visible on the customer panel. They said they will create a ticket with Acronis for this.
I will post results for others to benefit as soon as I get them.
 
Best regards
K
 


Hello Kostas,
As I mentioned above, I have checked the account myself, and indeed the quota set should be enough. There is certainly an issue within the product that must be fixed by our support team.
Best regards.

      
                
                
                    
                                                    Thu, 07/25/2024 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
