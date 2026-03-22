# cPanel toggle in Application backup (EAP)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cpanel-toggle-application-backup-eap

## Original Post
**Author:** Unknown

cPanel toggle in Application backup (EAP)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
On a cPanel server running CloudLinux 8.10, cPanel 120.0.16 and the Acronis cPanel plugin v1.9.0.773 I created a new Backup Plan via cloud.acronis.com and instead of using pre/post data capture commands I enabled the cPanel toggle in Application Backup as described in the latest release log: https://www.acronis.com/en-gb/support/updates/changes.html?p=41411
However, backups succeed with warnings, and the warning is:
Failed to run a pre-capture script.
Additional info:

------------------------
Error code: 66912258
Fields: {"$module":"webcp_aavb_lxa64_38338"}
Message: Command 'mv /usr/lib/Acronis/BackupAndRecovery/hosting_agent.log /opt/Acronis/hosting_agent.log' has failed with exit code 1 and the following output: mv: cannot stat '/usr/lib/Acronis/BackupAndRecovery/hosting_agent.log': No such file or directory

------------------------
I don't see any file called /usr/lib/Acronis/BackupAndRecovery/hosting_agent.log neither on this server, nor on others running the stable version of the Acronis cPanel plugin 1.8.2.766
Since I also have no pre/post data capture commands set, this must be a file that the "cPanel" Application Backup tries to move, so I'm reporting this here in case it's a bug.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/19/2024 - 20:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello George,
Thank you for reaching out.
I've checked the records and found only one case reporting this issue, but the client actually had a script with a pre-command.
Could you please raise a ticket with the team at https://kb.acronis.com/content/8153 so we can connect with you and investigate further?
Best regards.

      
                
                
                    
                                                    Wed, 08/21/2024 - 09:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
