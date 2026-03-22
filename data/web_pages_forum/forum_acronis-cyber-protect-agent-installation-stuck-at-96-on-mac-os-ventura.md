# Acronis Cyber Protect Agent installation stuck at 96% on Mac OS Ventura

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-protect-agent-installation-stuck-96-mac-os-ventura

## Original Post
**Author:** Unknown

Acronis Cyber Protect Agent installation stuck at 96% on Mac OS Ventura

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Unknown User
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have tried installing the agent twice on this machine, but it gets stuck at 96%. See screenshot. How can I get it to successfully install?
OS: macOS Ventura 13.5.1 (22G90), Mac is up to date.
Hardware: iMac
Process: 3.5 Ghz Quad-Core Intel Corei5
Graphics: Radeon Pro 575 4 GB
Memory: 8GB 2400Mhz DDR 4
HDD

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      iMacAcronisAgentStuck.png

                      60.56 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 08/31/2023 - 16:59

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum!
Are you installing the correct version of the agent? Because as you use a Intel processor you need to install the version for that processor.
Please try with one of those: 

Agent for Mac OS (64-bit)

https://dl.managed-protection.com/u/baas/4.0/15.0.36119/CyberProtect_AgentForMac_x64.dmg
Agent for Mac OS on ARM CPU (M1chip)
https://dl.managed-protection.com/u/baas/4.0/15.0.36119/CyberProtect_AgentForMac_arm64.dmg
If the issue persists, please raise a ticket with our support so we can investigate the issue https://kb.acronis.com/content/8153 .
Feel free to update the thread of this post.
Best regards.

      
                
                
                    
                                                    Fri, 09/01/2023 - 14:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Unknown User
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I downloaded the agent from within the cyber protect web console. However, it is only ~30MB so it must include a downloader that is failing at 96%.
I tried the 64-bit download link you provided, which is ~500MB, and it also gets stuck at 96%.
I will open a ticket now.

      
                
                
                    
                                                    Thu, 09/14/2023 - 18:45
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Unknown User
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Correction: while trying to open a ticket, I left it at 96% and it finally completed.
Now I'm getting stuck while trying to register.
First the Cyber Protect Monitor window opens and asks to sign in. I click Sign In, then it opens a browser window to a white page with this error:
{"error":"invalid_client","error_description":"Invalid client","state":"501"}The URL does not work from a different location, browser, etc. So the URL is malformed.
I rebooted and I get the same thing. I have tried closing the cyber protect assistant, but that does not help.

      
                
                
                    
                                                    Thu, 09/14/2023 - 19:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thank you for updating the thread.
Please review the following solutions:

Ensure that your Mac is connected to the internet and can access websites without any issues. Sometimes, network problems can interfere with the authentication process.


Ensure that your internet connection does not use a proxy.


Since the issue seems to be related to a browser window opening, try clearing your browser's cache and cookies. This can often resolve problems with malformed URLs or authentication errors.


Make sure that an Acronis account exists, and the product is signed into that account. Check if the email address associated with your Acronis account is displayed under the 'Account' tab in the product. If you accidentally or intentionally used a different email address during purchase, the purchased license may have been automatically registered to that address. Either sign into that Acronis account or move the license between accounts at account.acronis.com, as explained in this KB article: https://kb.acronis.com/content/60194#transfer


Sometimes, third-party software or security tools can interfere with the operation of security software like Acronis Cyber Protect. Temporarily disabling or uninstalling such software may help identify and resolve the issue.

If the issue persists after checking all these prerequisites, please update the ticket to inform our support team so that we can assist you further.
Best regards.

      
                
                
                    
                                                    Fri, 09/15/2023 - 14:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Unknown User
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It took a few months but Acronis finally updated the Mac installer to work with Mac OS 13. Reinstallation was normal after that.

      
                
                
                    
                                                    Tue, 11/28/2023 - 15:42
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Unknown User wrote:

It took a few months but Acronis finally updated the Mac installer to work with Mac OS 13. Reinstallation was normal after that.


Hello!
Thanks for sharing what helped to solve the issue.
Best regards. 

      
                
                
                    
                                                    Tue, 11/28/2023 - 16:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
