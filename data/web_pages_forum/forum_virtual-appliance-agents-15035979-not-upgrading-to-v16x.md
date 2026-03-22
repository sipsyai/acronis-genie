# Virtual Appliance agents 15.0.35979 not upgrading to v16.x

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/virtual-appliance-agents-15035979-not-upgrading-v16x

## Original Post
**Author:** Unknown

Virtual Appliance agents 15.0.35979 not upgrading to v16.x 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil Myers
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 46
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Just got around to upgrading from Acronis Cyber v15.0.35979 to v16.0.37977.
Server and workstation agents have been upgraded from the Management Console (Settings > Agents > Update Agent).
However, the VMware appliance agents don't upgrade. The upgrade process goes through the motions - downloads the update, unpacks, reboots the VA, updates the binaries (or so it says), then brings the appliance back online, says it's completed, but opening the appliance console and clicking About, my appliances are still showing version 15.0.35979.
Why?
Cheers
Neil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/18/2024 - 11:22

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Neil!
You can upgrade from Acronis Cyber Protect 15 to Acronis Cyber Protect 16 Update 1 if you have Acronis Cyber Protect 15 Update 3 (build 28035) or later installed.
If you have an older version of Acronis Cyber Protect 15 installed, upgrade to Acronis Cyber Protect 15 Update 3 (build 28035) and later before upgrading to Acronis Cyber Protect 16 Update 1.
https://care.acronis.com/s/article/73388-Upgrade-to-Acronis-Cyber-Prote…
If the issue persists, please raise a ticket with the team at https://kb.acronis.com/content/8153.
Best regards.
 
 

      
                
                
                    
                                                    Tue, 06/18/2024 - 14:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil Myers
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 46
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'd already checked the upgrade instructions and was running v15 update 6 before upgrading to v16, so that's not the issue.

      
                
                
                    
                                                    Tue, 07/23/2024 - 10:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Neil Myers
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 46
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fixed with a manual update of the Appliance Agent as described here: Updating virtual appliances – Acronis Cyber Protect 16 Update 1 – Web Help
 

      
                
                
                    
                                                    Tue, 07/23/2024 - 11:44
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Neil Myers wrote:

Fixed with a manual update of the Appliance Agent as described here: Updating virtual appliances – Acronis Cyber Protect 16 Update 1 – Web Help
 


Thank you for updating the thread.
We are glad the issue is resolved.
Best regards. 

      
                
                
                    
                                                    Tue, 07/23/2024 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Merrick mk
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Neil Myers wrote:

I'd already checked the upgrade instructions and was running v15 update 6 before upgrading to v16, so that's not the issue.
Thank you for confirming. Since you were previously on v15 update 6 before upgrading to v16, it appears that the problem lies elsewhere. Are there any other probable reasons or troubleshooting actions to consider?



      
                
                
                    
                                                    Thu, 08/22/2024 - 14:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Null Brawl APK

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Merrick mk wrote:

Neil Myers wrote:

I'd already checked the upgrade instructions and was running v15 update 6 before upgrading to v16, so that's not the issue.
Thank you for confirming. Since you were previously on v15 update 6 before upgrading to v16, it appears that the problem lies elsewhere. Are there any other probable reasons or troubleshooting actions to consider?




Hello!
There could be multiple root causes.
Does it update when you run a manual update, or does it fail?
Is the issue occurring right now?
If it persists, please raise a ticket with the team at https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Thu, 08/22/2024 - 14:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
