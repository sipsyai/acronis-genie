# Enrolling Machine Owner Key

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/enrolling-machine-owner-key

## Original Post
**Author:** Unknown

Enrolling Machine Owner Key

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Bailey Schafer
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
I'm attempting to install the Cyber Protection agent on a Linux machine running centos 7. I was able to get through the initial install process successfully (registered the agent and everything), until I got to a screen that displayed the following message:
The secure boot mode has been detected on the system. To complete the installation, restart the machine and follow the instructions for enrolling the MOK (Machine Owner Key). (You will be asked to enter the root password.)
I then selected Ok and was asked if I'd like to reboot to which I selected yes. Upon the machine rebooting, I was not prompted any further. I'm also not able to find the machine in the management console. Has anyone experienced this issue before?
 
Thanks!

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Capture.PNG

                      36.65 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/26/2020 - 20:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Bailey,
This prompting message appeared as the Secure Boot Mode has been detected on the system. To complete the installation, you had to restart the machine and follow the instructions for enrolling the MOK (Machine Owner Key). But as I understand you haven't been asked again to enter the root credentials, so it seems it went through.
You should now try to manually register the machine in Cloud, in order to do that please follow instructions from this KB article for the Linux OS section: https://kb.acronis.com/content/55244 under "Acronis Cyber Protect Cloud 7.8 and newer".
This should register the machine in the Backup Console and resolve the issue. If you continue having more issue I would suggest you better open a Support case providing your Cloud account login from the affected tenant and machine details.
Good luck!

      
                
                
                    
                                                    Fri, 05/29/2020 - 07:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
