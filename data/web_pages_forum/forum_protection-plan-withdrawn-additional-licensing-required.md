# Protection plan withdrawn "Additional licensing required"

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/protection-plan-withdrawn-additional-licensing-required

## Original Post
**Author:** Unknown

Protection plan withdrawn "Additional licensing required"

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            What's going on here Acronis?
Our protection plans for cPanel/Plesk (So Web Hosting Servers license) only have backup features enabled on them.  No anti-malware or anything else (because we have better tools that support Linux properly) and we're seeing them get withdrawn because we need to enable Advanced Antimalware!
I see by going into the service details there is a new quota item "Web Hosting Server (with included features)" which I can enable which allegedly fixes it *BUT* I don't want any anti-malware features, remote access etc.
This new item has an Unlimited Quota *BUT* there is no quota offering under the customer's enabled quotas to restrict them from unlimited devices on this device quota!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/19/2024 - 08:25

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Karl,
In fact, you need a quota for web hosting servers, but that's not related to the protection features such as A.Virus/A.Malware and so on, as they come included in all the editions Acronis Cyber Protection Comparison of Editions.
Those features are enabled or disabled in the backup plans, and it's not mandatory to use them, Creating a Protection Plan either advanced licenses.
If they want to use just the Standard edition, for example, you need to provide them with that offering in their tenant and maybe disable the advanced edition: Active Protection.
If you have any doubts about how to execute this, please contact our support (or your reseller if you are not entitled to direct support) so we can guide you through the process: Acronis Support.
Best regards.

      
                
                
                    
                                                    Fri, 07/19/2024 - 10:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Karl Austin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, thanks for replying, unfortunately none of what you've assumed is correct.
 
1) These tenants had a "web hosting servers" quota which was applied to the devices.
 
2) No advanced editions were enabled for the tenant only "Standard Protection"
 
3) The system decided to withdraw protection plans that were backup only (no other feature than backup turned on), and had been in place for over a year because we needed to "enable Advanced Antimalware"
 
We've been a customer now for many years, we know how it works and these devices have been fine up until the last few days where a new "web hosting servers (included features)" quota item has appeared when clicking device details.
That's the only place it shows up as well, if I click the tenant configuration, there is no "Web hosting servers (included features)" quota item to configure, only "Web hosting servers" - Meaning a tenant can create Plesk/cPanel servers and assign them the new "included features" quota with no limits!
Thanks.

      
                
                
                    
                                                    Fri, 07/19/2024 - 12:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Karl Austin wrote:

Hi, thanks for replying, unfortunately none of what you've assumed is correct.
 
1) These tenants had a "web hosting servers" quota which was applied to the devices.
 
2) No advanced editions were enabled for the tenant only "Standard Protection"
 
3) The system decided to withdraw protection plans that were backup only (no other feature than backup turned on), and had been in place for over a year because we needed to "enable Advanced Antimalware"
 
We've been a customer now for many years, we know how it works and these devices have been fine up until the last few days where a new "web hosting servers (included features)" quota item has appeared when clicking device details.
That's the only place it shows up as well, if I click the tenant configuration, there is no "Web hosting servers (included features)" quota item to configure, only "Web hosting servers" - Meaning a tenant can create Plesk/cPanel servers and assign them the new "included features" quota with no limits!
Thanks.


Thank you for the detailed explanation, which helped review the account and understand what you are talking about.
Included features mean that you don't have backup functionality. The most appropriate quota is assigned automatically when applying the plan because you can create a plan just for backups and a plan just for features. However, if the features are not used, the quota won't be taken or used.
"Server/Virtual Machine/Workstation" = Included features + Backup functionality
"Server/Virtual Machine/Workstation (included features)" = Just the included features and no backup functionality.
We know that the definition is not very clear, and we have already created a task to improve this, UXI-94. You can enable the notifications for product updates; once this is fixed, you will see the information there.
For more information about the advanced packs, please check this article: https://www.acronis.com/en-us/support/documentation/AcronisCyberCloud/#…
Best regards.
 

      
                
                
                    
                                                    Fri, 07/19/2024 - 13:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
