# Backup failed because a third-party VSS provider had an unexpected error.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-failed-because-third-party-vss-provider-had-unexpected-error

## Original Post
**Author:** Unknown

Backup failed because a third-party VSS provider had an unexpected error. 

        
  



    
  


  
          
  
    Tutorial
  


          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Heinrich Dehning
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good day everyone.
Has anyone experienced this issue and if yes how did you resolve it:


Backup failed because a third-party VSS provider had an unexpected error. 


 
I have run the VSS Acronis tool and get all green.
 
Kind regards
Heinrich

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/29/2023 - 13:14

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  





            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Heinrich,
Welcome to the forum.
Just because everything appears to be green doesn't mean there are no issues. You need to download the report and check the bottom section, as that is where error codes are usually presented.
Please follow these steps in the command prompt:

Run the command "vssadmin list writers" (you can find more information about it here: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin-list-writers). If any errors are displayed, you should address the respective error or contact Microsoft for assistance.


Reboot your device. Sometimes the writers or provider can experience issues, and a simple reboot can resolve them.


Reschedule the backup. If you are running a backup when the machine is overloaded, it can cause the VSS to crash or fail. Try rescheduling the backup at a time when the machine is not under heavy load.


Check the event viewer for errors. Look for any error codes that may indicate the actual issue.


Disable the VSS option in the backup plan settings. Go to the backup plan, click on Edit, navigate to Backup options, select VSS, and disable it. You can find more information on this in our documentation here: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#volume-shadow-copy-service.html#kanchor658

Please let me know if these steps resolve the issue for you.
If not, please contact our support team and provide screenshots of all the tests you performed, showing that everything appears to be in order with the VSS. You can reach our support team here: https://kb.acronis.com/content/8153
Thanks.
 

      
                
                
                    
                                                    Mon, 05/29/2023 - 14:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
