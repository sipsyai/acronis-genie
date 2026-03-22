# Service Provider Hosted Storage

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/service-provider-hosted-storage

## Original Post
**Author:** Unknown

Service Provider Hosted Storage

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tim Westman-Barth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            In the past I've used Acronis Cyber Protect Cloud and in my opinion it far superior to any competing product I've ever used. Presently I am at a company using Veeam, which is terrible by comparison, I keep finding more and more functionality that I would think is "basic" that Veeam just doesn't have and it keeps causing significant problems for us.
I would like to migrate our environment to using Acronis, I understand of course that basically involves setting everything up again as an entirely new environment. And that's fine. However the company has been using our own servers to store backups for customers, similar to the on-premises installation of Acronis Cyber Protect. However my preferred solution would be using Acronis Cyber Protect Cloud. The use of the "Cloud" version is important, partially because our hardware is aging and may need to be replaced or upgraded soon, so I would prefer to just be able to commit to moving away from our own hardware entirely.
However, for the time being we do have some servers with storage space to accommodate all of our current customers and I'm curious what the best method would be to use the storage on our servers for backup storage for customers over the internet. It would be considerably easier financially for us to switch to Acronis if we could continue to use our servers for storage for our current customers, and simply migrate away from those servers as the storage space ran out or they reached end of life for other reasons.
My understanding is that if we used the self-hosted "on-premises" installation of Cyber Protect, we could use the Cyber Protect Gateway to backup to our servers over the internet without the use of a VPN or other direct network connection. However my understanding is that that option is not available when using Cyber Protect Cloud. Is that accurate? If it is accurate, is there an alternative recommended method to backup to a storage location over the internet?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/29/2023 - 14:07

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tim Westman-Barth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I believe I found reading the documentation that you can in fact use the Cyber Infrastructure Backup Gateway software with the Cyber Protect Cloud service, that it is not limited to only the on-premises Cyber Protect installation. 
https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructu…
So I believe that actually solves the issue. Or rather, it's not an issue at all, just a misunderstanding of the available functionality.
However I am still curious to confirm if a single installation of the Backup Gateway can be used to offer isolated storage to multiple tenants/customers or if I would need to set up a separate Backup Gateway installation in a VM for each customer. I believe that it could be used for a multi-customer scenario with a single installation, but wanted to confirm for certain that is the case.

      
                
                
                    
                                                    Tue, 08/29/2023 - 16:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tim Westman-Barth wrote:

I believe I found reading the documentation that you can in fact use the Cyber Infrastructure Backup Gateway software with the Cyber Protect Cloud service, that it is not limited to only the on-premises Cyber Protect installation. 
https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructu…
So I believe that actually solves the issue. Or rather, it's not an issue at all, just a misunderstanding of the available functionality.
However I am still curious to confirm if a single installation of the Backup Gateway can be used to offer isolated storage to multiple tenants/customers or if I would need to set up a separate Backup Gateway installation in a VM for each customer. I believe that it could be used for a multi-customer scenario with a single installation, but wanted to confirm for certain that is the case.


Hello Tim. 
Once you deploy the gateway you can enable the offering of that location to your clients, you don't need to deploy it client by client. 
Thanks in advance!

      
                
                
                    
                                                    Wed, 08/30/2023 - 13:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tim Westman-Barth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the clarification. We'll be doing some testing internally with Acronis and if all goes well we should be able to migrate our customers over from Veeam. Which will seriously make everything better for us. I'm convinced everyone who uses Veeam has never tried other products, I've literally never seen any software of any sort anywhere that's as poorly designed and buggy.

      
                
                
                    
                                                    Tue, 09/05/2023 - 13:23
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tim Westman-Barth wrote:

Thanks for the clarification. We'll be doing some testing internally with Acronis and if all goes well we should be able to migrate our customers over from Veeam. Which will seriously make everything better for us. I'm convinced everyone who uses Veeam has never tried other products, I've literally never seen any software of any sort anywhere that's as poorly designed and buggy.


Hello Tim.
If you face any issues during the process please let us know so we can take further actions.
Feel free if you have any questions.
Best regards. 

      
                
                
                    
                                                    Tue, 09/05/2023 - 13:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tim Westman-Barth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            There is one thing you can clarify for me, when using Acronis Cyber Infrastructure, there's a per-GB license fee. Is that fee just for using Cyber Infrastructure for Disaster Recovery? Or does it also apply when using exclusively the Backup Gateway for backup storage?
As described here:https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructu…

      
                
                
                    
                                                    Mon, 09/11/2023 - 14:05
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tim Westman-Barth wrote:

There is one thing you can clarify for me, when using Acronis Cyber Infrastructure, there's a per-GB license fee. Is that fee just for using Cyber Infrastructure for Disaster Recovery? Or does it also apply when using exclusively the Backup Gateway for backup storage?
As described here:https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructu…


Hello Tim,
In fact, the DR services, such as storage, aren't free. Unfortunately, I can't provide you with more details regarding the prices as that information is with our sales department. You need to contact your sales manager and request more information about that. They have that information.
Thanks in advance!

      
                
                
                    
                                                    Mon, 09/11/2023 - 14:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
