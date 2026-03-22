# [RESOLVED] Updating agents via web interface

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-updating-agents-web-interface

## Original Post
**Author:** Unknown

[RESOLVED] Updating agents via web interface

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    T B
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I know the feature to view/update agents via the web interface was released today but is this feature fully functional?  I have tried to update agents via the web interface (for Linux and Windows, both currently running version 11.9.215) and they are not being updated.  No error message is displayed, occasionally I see "Updating..." displayed under the Agent Version column but the agent never actually updates.  If I exit and return to the page, nothing has changed.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/23/2015 - 17:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello T B,
Thank you for posting your question here.
In Acronis Backup Cloud v.4.0 the agent status remains Updating... for the whole period of time while the update is being installed. Once the update is installed agent automatically disappears from the Updates pane in the Backup Management Console. Console will not show any other message or status for the agent, even if update fails.
On the machine side, to perform the update the agent will download the installation file and will execute it. Until the update is installed and the services are running again, the Updating... message will not disappear from the console.
So please make sure that the agent has finished downloading the installation package, installation is complete and services (mms and agent) are running.
You can also perform the update manually, by downloading the installation file from the Backup Management Console, and running it on the agent.
Let me know if it helps or if you have further questions.
Best regards,

      
                
                
                    
                                                    Tue, 06/23/2015 - 22:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    T B
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So I left two different servers (a Windows machine and a Linux machine) "Updating..." overnight.  Today I logged into Acronis Cloud and both of them show as still running version 11.9.215.  If the update is failing how can I tell why it is failing or even that it is failing?  Is this something that will be addressed in the next release?  This looks to be a great feature as it will simplify updating the agents but it does not seem to be working properly yet.

      
                
                
                    
                                                    Wed, 06/24/2015 - 12:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello T B,
While update is running on the agent, you will see the Updating... status. Once the updater exits for any reason, this status is removed and the actual agent build is shown. This is expected behavior and we are not planning to add the error-handling in nearest updates. This functionality may appear in future releases.
So in any case right now you would have to go to the machine directly and troubleshoot the issue either with the package download, or it's execution (MSI log is created by default in C:\ProgramData\Acronis\InstallationLogs\live_update\ in Windows).
Let me know if you need further assistance troubleshooting the issue on agent side.
Have a good day,

      
                
                
                    
                                                    Wed, 06/24/2015 - 15:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    T B
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dmitry, on the Windows machine I checked the path C:\ProgramData\Acronis\InstallationLogs\ and there is no \live_update\ directory present.  Could this be a communication issue, maybe some ports that are blocked?

      
                
                
                    
                                                    Wed, 06/24/2015 - 20:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello T B,
Yes, it could be a communication issue, seems like the MS installer did not start yet and did not create the log.
Make sure that:
1) All ports are open according to https://kb.acronis.com/content/47189, the agent uses one of ports 7770-7800 to download the live_update_installer.exe to C:\Users\USERNAME\AppData\Local\TMP.
2) live_update_installer.exe then downloads the installation files to the same folder through port 80.
Once downloaded, the MSI file is executed and creates the MSI log.
Let me know once you check the ports and the respective folders. Please also submit a support case to get faster responses and assistance from our support team to troubleshoot the issue.
Thank you,

      
                
                
                    
                                                    Fri, 06/26/2015 - 12:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    T B
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for your help.  Although it does not appear in that KB article, the issue was port 80 to 72.21.81.253 was blocked.  We allowed that connection and the update worked.

      
                
                
                    
                                                    Fri, 06/26/2015 - 12:47
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for confirming this!
We will now update the KB accordingly.
Cheers,

      
                
                
                    
                                                    Fri, 06/26/2015 - 13:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
