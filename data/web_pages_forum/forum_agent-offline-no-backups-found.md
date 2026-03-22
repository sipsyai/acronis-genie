# Agent offline, no backups found

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/agent-offline-no-backups-found

## Original Post
**Author:** Unknown

Agent offline, no backups found

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    John Head
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have 7 servers, 4 of which are now reporting no backups found (however they are visible in BACKUP STORAGE, and still backing up daily) and the agent is showing offline in DEVICES.
From the mms log we're seeing;
[ConfigMonitoringComponent][ZmqClient] CONNECTING TO tcp://127.0.0.1:36170 ...
[WebCP] Found at instance `XXX-XXX-XXX-XXX-XXX` application: 1 (with client id)
Webcp: addressServer='https://sg-cloud.acronis.com' upLinkAddress='127.0.0.1'
Webcp: TransportLayer::Authorization: trying to log in to backup console
Webcp: TransportLayer::Authorization: trying to log in to backup console
[ConfigMonitoringComponent][ZmqClient] DISCONNECTED
They have gone "offline" within days of each other but everything been running for over a year.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/20/2024 - 04:44

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
To check whether the backups exist, the most accurate method is to use the Web Restore panel. Please note that Read-Only Administrators cannot log in to the Web Recovery Console. You must log in with an Admin account. Refer to the following guide:
https://care.acronis.com/s/article/60087-Acronis-Cyber-Protect-Cloud-Web-Restore-or-Web-Recovery-Console?language=en_US.
Alternatively, you can use another machine that is online to browse those backups. For more details, see this guide:
https://care.acronis.com/s/article/69264-Acronis-Cyber-Protect-Attempt-to-remove-backup-or-recover-files-fails-with-The-machine-is-offline-or-is-not-available?language=en_US.
Regarding the issue with offline devices, this indicates they are unable to connect to the management server and therefore appear offline. Here are some recommended actions:
Reboot one of the affected machines and check if it comes online.
Ensure all agents are updated to the latest build:
https://care.acronis.com/s/article/Acronis-Cyber-Protect-Cloud-how-to-update-to-the-latest-build?language=en_US.

Check that all services are running:
https://care.acronis.com/s/article/61100-Acronis-Cyber-Protect-Cloud-Windows-Services-and-Processes?language=en_US.
If any service is down and cannot be restarted, it may indicate a local issue, such as a service crash or blockage, which will require further investigation.

Ensure your antivirus or local security software is not blocking connections or services:
https://care.acronis.com/s/article/36429-Acronis-Software-exclude-program-folders-and-executables-from-antivirus-and-other-security-programs?language=en_US.

Run the Connection Verification Tool to check if all required ports are open. If any are closed, they must be opened to enable backups to proceed:
https://care.acronis.com/s/article/47678-Acronis-Cyber-Protect-Cloud-Acronis-Cyber-Protect-15-and-Acronis-Cyber-Backup-12-5-Connection-Verification-Tool?language=en_US.

If the issue persists after performing all these steps, please raise a ticket with our support team:
https://kb.acronis.com/content/8153.
Best regards,
 

      
                
                
                    
                                                    Wed, 11/20/2024 - 15:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    John Head
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So after creating this post the following day everything started working again no actions my end at all.

      
                
                
                    
                                                    Fri, 01/24/2025 - 02:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            John Head wrote:

So after creating this post the following day everything started working again no actions my end at all.


Hello!
This was likely caused by a temporary network issue.
If the problem persists, please feel free to update the thread.
Best regards.

      
                
                
                    
                                                    Fri, 01/24/2025 - 10:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
