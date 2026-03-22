# DirectAdmin Module Broken - CloudLinux 9.5

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/directadmin-module-broken-cloudlinux-95

## Original Post
**Author:** Unknown

DirectAdmin Module Broken - CloudLinux 9.5

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
CloudLinux pushed version 9.5 earlier this week and now the DA Control Panel plugin does not work and looks like this:

DA Version: 1.672
Acronis Module version: 1.2.2.181
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 12/06/2024 - 14:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
Issues with third-party integrations must be reported to the team, as they are typically communicated and investigated with the provider.
This may be related to an unsupported environment: System Requirements.
Please raise a ticket so the team can review the issue.
Best regards.

      
                
                
                    
                                                    Mon, 12/09/2024 - 08:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            the article you provided me says you do not support CloudLinux 9 when you do, its just 9.5 you're having issues with.
 
Please provide me with an update as this has been over a week now with this bug.

      
                
                
                    
                                                    Tue, 12/10/2024 - 14:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

the article you provided me says you do not support CloudLinux 9 when you do, its just 9.5 you're having issues with.
 
Please provide me with an update as this has been over a week now with this bug.


Hello!
The documentation I shared is from the official user guide.
It states that the specified version is not supported for the plugin or a regular agent (while installation might work, the OS is not officially supported):
Supported Operating Systems and Environments
Supported versions (for Acronis Cyber Protect Cloud Agent):
CloudLinux 5.x, 6.x, 7.x, 8.x*, 9.4*
Supported systems for DirectAdmin integration:
AlmaLinux 8
Red Hat Enterprise Linux 7 and 8
RockyLinux 8
Ubuntu 20.04 LTS
For more details, please refer to the Supported Operating Systems and Environments.
There is a feature request (RM-9497) to integrate CloudLinux 9.5, but there is no ETA at this time.
Regarding Updates
As advised earlier, please raise a ticket or ask your MSP to do so. This ensures your request is kept in the registries, as the forum is not connected to our support team.
Best regards.

      
                
                
                    
                                                    Tue, 12/10/2024 - 14:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
Can you share on these forums for everyone on where support are up to fixing this issue?

      
                
                
                    
                                                    Tue, 12/17/2024 - 11:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
 
I see this is still not supported in 24.11 39130 build you released last week!
For now we will move modern servers to another solution away from acronis and just backup legacy solutions using acronis.

      
                
                
                    
                                                    Mon, 12/23/2024 - 10:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

Hi
 
I see this is still not supported in 24.11 39130 build you released last week!
For now we will move modern servers to another solution away from acronis and just backup legacy solutions using acronis.


Hello Chris,
As mentioned above, there is a difference between the backup agent and the plugin.
Our product supports the OS, but the plugin does not yet. Sometimes, updates for plugins may take longer, particularly when new operating system versions are released, as third-party providers need to test and ensure compatibility before updating their plugins.
You can contact your service provider and leave your comments with them so they are kept on record with a ticket.
Best regards,

      
                
                
                    
                                                    Mon, 01/06/2025 - 12:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
Thanks for the reply
As far as i'm aware the DirectAdmin control panel plugin is developed by Acronis and no one else?  I was actually part of your beta testing for the DA module and it was only DA Developers i worked with back then to make this module.
Surely you could ask internally where you guys are up to with fixing the plugin for DirectAdmin with Cloudlinux 9.5?

      
                
                
                    
                                                    Tue, 01/07/2025 - 11:46
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Danks wrote:

Hey Jose,
Thanks for the reply
As far as i'm aware the DirectAdmin control panel plugin is developed by Acronis and no one else?  I was actually part of your beta testing for the DA module and it was only DA Developers i worked with back then to make this module.
Surely you could ask internally where you guys are up to with fixing the plugin for DirectAdmin with Cloudlinux 9.5?


Hello!
I’ve made a request, but I haven’t received any ETA yet. I’ll follow up with the team again to check for any updates.
As soon as I have more information, I’ll update this thread.
Best regards.

      
                
                
                    
                                                    Tue, 01/07/2025 - 13:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you, I appreciate it :)

      
                
                
                    
                                                    Tue, 01/07/2025 - 13:22
