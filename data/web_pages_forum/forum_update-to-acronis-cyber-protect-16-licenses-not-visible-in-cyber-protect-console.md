# Update to Acronis Cyber Protect 16 - licenses not visible in Cyber Protect Console

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/update-acronis-cyber-protect-16-licenses-not-visible-cyber-protect-console

## Original Post
**Author:** Unknown

Update to Acronis Cyber Protect 16 - licenses not visible in Cyber Protect Console

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Valerio
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, having upgraded my licenses to Acronis Cyber Protect 16, I've tried to do the same with the software installed on the dedicated server (Windows Server 2022 datacenter) on my VMware infrastructure.
The update has been completed without any issue in the process, BUT the Acronis local console did not acquire the new licenses even if it showed the message "Your licenses are in sync.", hence preventing backup plans from working.
I had to restore the previous version to avoid any service disruption (I took a snapshot before starting the update process).
What should i do in order to let the console "see" the new licenses?
Thank you

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/18/2025 - 08:12

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please refer to the following Knowledge Base article for details:
? https://care.acronis.com/s/article/Acronis-Cyber-Protect-16-Unable-to-allocate-licenses-to-an-online-or-offline-activated-AMS-installation-of-Update-4?language=en_US
Cause:
This issue was caused by a known product defect.
Status:
✅ The issue has been resolved.
Important:
Since updating directly may fail due to a missing license, please first add the license key in Update 4 (build 39929)—which includes a fix for affected users—and only then proceed with the update.
If the problem persists, please raise a support ticket with our team here:
? https://support.acronis.com/
Best regards.

      
                
                
                    
                                                    Mon, 07/21/2025 - 04:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Valerio
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jose,
thanks for you answer.
I tried again this morning without having read this topic; to avoid this issue I've deactivated the management server and activated it manually.
No luck there, until I did as follows:
unassigned the v12.5 licenses (unused);
unassigned the v15 licenses (currently in use, to be replaced by v16);
assigned the v16 licenses.
So now the console apparently has the v16 licenses loaded correctly.
I'm currently deploying the new agents for VMware.
Thank you.
Best regards.
Valerio

      
                
                
                    
                                                    Mon, 07/21/2025 - 10:37
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Valerio wrote:

Hi Jose,
thanks for you answer.
I tried again this morning without having read this topic; to avoid this issue I've deactivated the management server and activated it manually.
No luck there, until I did as follows:
unassigned the v12.5 licenses (unused);
unassigned the v15 licenses (currently in use, to be replaced by v16);
assigned the v16 licenses.
So now the console apparently has the v16 licenses loaded correctly.
I'm currently deploying the new agents for VMware.
Thank you.
Best regards.
Valerio


Hello!
Thank you for your reply.
Indeed, Acronis Cyber Protect 16 is not compatible with licenses from legacy products — they must be removed. Those licenses will only work with the specific version they were issued for.
Best regards.

      
                
                
                    
                                                    Tue, 07/22/2025 - 06:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Valerio
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there.
Yes, that was expected but i find it odd that I had to remove the old licenses in a first step; you can't both assign v16 and revoke v15 (and v12.5) at the same time.
Also in one of my attempts i just tried to unassign the v12.5 licenses from the console, but nothing happened until I changed the type of activation from online to offline.
By the way, now it works so we are good to go ;)
Thanks for your assistance.
Best regards

      
                
                
                    
                                                    Tue, 07/22/2025 - 07:03
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Valerio wrote:

Hi there.
Yes, that was expected but i find it odd that I had to remove the old licenses in a first step; you can't both assign v16 and revoke v15 (and v12.5) at the same time.
Also in one of my attempts i just tried to unassign the v12.5 licenses from the console, but nothing happened until I changed the type of activation from online to offline.
By the way, now it works so we are good to go ;)
Thanks for your assistance.
Best regards


You are welcome! 

      
                
                
                    
                                                    Wed, 07/23/2025 - 10:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
