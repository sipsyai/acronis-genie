# Kernel & Mysql Issue

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/kernel-mysql-issue

## Original Post
**Author:** Unknown

Kernel & Mysql Issue 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    MOHAMMED MANSOUR
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We are currently facing some issues with the Acronis Cyber Backup solution deployed in our environment, and we would appreciate your assistance in resolving them. Below are the details:
 
SnapAPI26 Kernel Module Compatibility
The snapapi26 kernel module is not compatible with the kernel version 6.1.0-33-amd64, although it works correctly with 6.1.0-30-amd64.
The current version of the module is 0.8.52, and the agent version we are using is 25.3.39870.
We believe a module update may be required to support the newer kernel.
 
MySQL Database Recovery Issue
We encountered an issue while trying to recover a MySQL database.
The following error appears:
Agent error -32603 Failed to get the database from the archive up and running. You might want to try again with We tried disabling AppArmor, but the issue persists even after doing so.
```
Agent error -32603 Failed to get the database from the archive up and running. You might want to try again with AppArmor disabled: recovery level 3: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 4: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 5: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 6: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 0: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 1: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished': recovery level 2: 'exit status 1': 'failed to send kill signal to temporary mysqld instance: os: process already finished'. More details in '/var/lib/Acronis/BackupAndRecovery/MMS/mysql-agent-3354915632'
```
 
We found an article that might address the issue, but unfortunately, the link seems to be inaccessible:
https://care.acronis.com/s/article/72599-Acronis-Cyber-Protect-Cloud-MySQL-MariaDB-recovery-finishes-with-Agent-error-32603-Failed-to-get-the-database-from-the-archive-up-and-running?language=en_US
 
We would appreciate your guidance and support to resolve these issues as soon as possible.
 
Thank you in advance for your help!
 
Best regards,
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 04/27/2025 - 07:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Welcome to the forum!
By default, AppArmor blocks the recovery function of the Acronis service, which is causing the issue you are experiencing.
I checked with our internal team and received an update: you can restore the MariaDB instance as files and mount them later without disabling AppArmor.
You can find more information here:https://www.acronis.com/en-us/support/documentation/CyberProtectionService/index.html#recovering-mysql-mariadb-instances.html
Alternatively, you can also restore the entire machine backup without disabling AppArmor.
If these solutions do not meet your needs, please contact your service provider or our support team for further assistance, as a detailed investigation may be required.
Best regards,

      
                
                
                    
                                                    Mon, 04/28/2025 - 09:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    MOHAMMED MANSOUR
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jose,
Thank you for your reply. We have checked and confirmed that AppArmor is disabled and not running.
However, the issue still persists.

      
                
                
                    
                                                    Mon, 04/28/2025 - 11:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            MOHAMMED MANSOUR wrote:

Hi Jose,
Thank you for your reply. We have checked and confirmed that AppArmor is disabled and not running.
However, the issue still persists.


Hello,
Thank you for reaching out.
It appears you're encountering two distinct issues that are unrelated. Here's a breakdown:

Second Error: I've provided a workaround for this issue. If the problem persists, please contact your service provider. This matter requires log analysis, and currently, there's no known solution; it should be formally reported for further investigation.​


Kernel-Related Issue: The error message you've shared doesn't match the logs generated by our program; it seems to be a response or solution suggested by someone else. I recommend reviewing the code and verifying if your kernel version is compatible. For assistance, consider reaching out to the individual who provided that solution.​

Important Tip: Ensure that all affected machines have their agents updated to the latest version. You can find guidance on updating agents here:
? How to Update to the Latest Build​Acronis Support Portal
Best regards,
 

      
                
                
                    
                                                    Mon, 04/28/2025 - 14:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
