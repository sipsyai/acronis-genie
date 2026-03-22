# Agent install shows port 44445 failures, but backups partly working

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/agent-install-shows-port-44445-failures-backups-partly-working

## Original Post
**Author:** Unknown

Agent install shows port 44445 failures, but backups partly working

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Terry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I’m running Acronis Cyber Protect agent on an Ubuntu 24.04 server with Plesk Obsidian. During installation, I received repeated warnings like this:
Failed to connect to host "2602:80b:6012:10::10c" via port 44445.
...
There are non-critical issues caused by the maintenance in the cloud or the firewall restrictions.
Despite the warnings, the agent installed and registered successfully, and I was able to start a backup.
Here’s what I’ve tested so far:

443 → backup.acronis.com works fine (curl -vk returns HTTP 200 OK).


44445 → backup.acronis.com always times out.


44445 → portquiz.net succeeds immediately.


IPv6 is not configured on my server, so the IPv6 errors during install are expected.


Firewall rules on my server allow all outbound traffic.

According to the documentation, port 44445 is required for data transfer during backup and recovery. If it’s blocked, backups should fail. However, my first backup seems to be transferring, albeit slowly.
Questions:

Are the port 44445 install warnings normal (maybe some Acronis servers don’t answer, but others do)?


Does the agent have a fallback to 443 for data transfer, or is 44445 mandatory?


Should I be concerned about long-term stability of backups if 44445 continues to time out against some Acronis IPs?

Thank you for any clarification.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 08/17/2025 - 00:59

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
Could you let us know the exact version of Acronis Cyber Protect you’re using?
Please note that all versions require specific ports to be open. If they are closed — or if a third-party security application or firewall is blocking them — backups may fail, especially when using a locally deployed Acronis Cyber Infrastructure.
You can find the full list of required ports and their associated services here:https://care.acronis.com/s/article/67276-Acronis-Cyber-Protect-15-Linux-components-services-and-processes?language=en_US&ckattempt=1
If you need further assistance, please contact our support team so we can help you resolve this issue in more detail.
Best regards.

      
                
                
                    
                                                    Sun, 08/17/2025 - 23:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Terry
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks José. I’m on Acronis Cyber Protect Agent 25.5.40077 (Linux, installed via Plesk extension).  
I’ve reviewed the port list, but my concern is a bit more specific:  
- Port 443 works fine to backup.acronis.com.  
- Port 44445 works fine to other hosts (e.g., portquiz.net).  
- But port 44445 to backup.acronis.com times out consistently, even though backups sometimes complete.  
That seems to suggest the block or drop is on certain Acronis IP ranges, not on my firewall or provider (since outbound 44445 is open generally).  
Do you know if the agent has any documented fallback to 443 for data transfer when 44445 is unreachable? Or does it just retry other Acronis nodes until it finds one that answers on 44445?  
I ask because I’ve now had one successful full and one successful incremental, but also a failure when jobs overlapped. I’d like to confirm whether these warnings can be safely ignored, or if I should expect long-term instability.  
Any insight from other admins who’ve seen the same warnings would be very welcome.  
 

      
                
                
                    
                                                    Mon, 08/18/2025 - 14:01
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Terry wrote:

Thanks José. I’m on Acronis Cyber Protect Agent 25.5.40077 (Linux, installed via Plesk extension).  
I’ve reviewed the port list, but my concern is a bit more specific:  
- Port 443 works fine to backup.acronis.com.  
- Port 44445 works fine to other hosts (e.g., portquiz.net).  
- But port 44445 to backup.acronis.com times out consistently, even though backups sometimes complete.  
That seems to suggest the block or drop is on certain Acronis IP ranges, not on my firewall or provider (since outbound 44445 is open generally).  
Do you know if the agent has any documented fallback to 443 for data transfer when 44445 is unreachable? Or does it just retry other Acronis nodes until it finds one that answers on 44445?  
I ask because I’ve now had one successful full and one successful incremental, but also a failure when jobs overlapped. I’d like to confirm whether these warnings can be safely ignored, or if I should expect long-term instability.  
Any insight from other admins who’ve seen the same warnings would be very welcome.  
 


Hello!
Could you try updating the agent to the latest version (40497)?
? Release notes and builds
Once updated, please retry the backup and check if the issue persists.
From your description, the issue looks temporary—likely related to network conditions during consecutive backups, rather than blocked ports.
To investigate further, we would need the logs, specifically the sysreport from that machine, to see what exactly is failing. If the issue continues, please contact our support team or your service provider so we can review the logs and troubleshoot in detail.
Best regards.
 
 
 

      
                
                
                    
                                                    Wed, 08/20/2025 - 19:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
