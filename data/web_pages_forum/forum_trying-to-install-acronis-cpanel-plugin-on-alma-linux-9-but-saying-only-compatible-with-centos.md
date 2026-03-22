# Trying to install acronis cpanel plugin on Alma linux 9, but saying only compatible with Centos

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/trying-install-acronis-cpanel-plugin-alma-linux-9-saying-only-compatible-centos

## Original Post
**Author:** Unknown

Trying to install acronis cpanel plugin on Alma linux 9, but saying only compatible with Centos

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I try following the instructions to install the cpanel plugin for Acronis backup, but I get the message it's only compatible with CentOS, but when I look in the script I see there is support for Alma Linux and the searching I have done on the forums and elsewhere on the web, tells me it is compatible.
 
Error - Only CentOS/CloudLinux 6, 7 and 8 are supported at the moment
 
Part of install script -
rhel | cloudlinux | cloudlinuxserver | almalinux | rocky)
        # We use the same RPMs for RHEL, CloudLinux, AlmaLinux and RockyLinux as for CentOS
        OS_NAME="CentOS"
 /etc/os-release
NAME="AlmaLinux"
VERSION="9.3 (Shamrock Pampas Cat)"
ID="almalinux"
 
Is there something I am missing?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 04/27/2024 - 16:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Please refer to this thread where the topic was discussed: https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cloud…
Thanks in advance!

      
                
                
                    
                                                    Mon, 04/29/2024 - 08:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks, I saw that topic but I wasn't sure if it was related, because I am not working with cloudlinux and I am working with Alma Linux 9, which according to knowledge base and documentation is supported. 

      
                
                
                    
                                                    Mon, 04/29/2024 - 15:33
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            David Petruzzella wrote:

Thanks, I saw that topic but I wasn't sure if it was related, because I am not working with cloudlinux and I am working with Alma Linux 9, which according to knowledge base and documentation is supported. 


Hello David,
Please check this part: Starting from version 8.4, it is only supported with kernels from 4.18 to 5.19.
I would say that's what's causing the issue in this situation. Also, check if you have downloaded the latest version of the agent.
The agent supports AlmaLinux 9, but the cPanel plugin doesn't yet. So it's expected that you can't install it.
https://www.acronis.com/en-us/support/documentation/WHMCPanel/
If the issue persists, please raise a ticket with the team attaching screenshots of the kernel version from https://kb.acronis.com/content/8153.
Best regards.

      
                
                
                    
                                                    Mon, 04/29/2024 - 17:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I checked and the kernel is 5.14 and it currently has an agent on it, but I am trying to install the cpanel plugin and whenever I try to per the install document it fails at the OS check.

      
                
                
                    
                                                    Mon, 04/29/2024 - 18:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The kernel is version 5.14.

      
                
                
                    
                                                    Tue, 04/30/2024 - 01:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    David Petruzzella
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I was able to install the plugin using the below command referenced on the topic listed below to bypass os detection. https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cloud…
 
My kernel version is as follows 5.14.0-362.24.2.el9_3.x86_64, which is in the supported kernel versions for Alma Linux 9.

      
                
                
                    
                                                    Tue, 04/30/2024 - 02:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            David Petruzzella wrote:

I was able to install the plugin using the below command referenced on the topic listed below to bypass os detection. https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cloud…
 
My kernel version is as follows 5.14.0-362.24.2.el9_3.x86_64, which is in the supported kernel versions for Alma Linux 9.


Hello David,
The agent supports AlmaLinux 9, but the cPanel plugin doesn't yet.
So it's expected that you can't install it.
https://www.acronis.com/en-us/support/documentation/WHMCPanel/
Best regards.

      
                
                
                    
                                                    Tue, 05/07/2024 - 15:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Melis Freag
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 30
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If you’re encountering an error that suggests otherwise, it could be due to several reasons:
You might be using an older version of the plugin that does not have support for AlmaLinux.
There could be a version mismatch between the plugin and your operating system.
The installation script may not be recognizing your OS correctly, despite the script containing conditions for AlmaLinux.

      
                
                
                    
                                                    Tue, 05/07/2024 - 20:55
