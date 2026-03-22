# Simple pre-command batch file fails with error code 66,610

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/simple-pre-command-batch-file-fails-error-code-66610

## Original Post
**Author:** Unknown

Simple pre-command batch file fails with error code 66,610

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tom Dacon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I do backups during the night to a Synology NAS. To wake it up from its sleep state I'm trying to run a simple pre-command batch file to copy a small text file to a directory on the NAS. For something that should be so simple it's been driving me crazy for four or five days.
The batch file succeeds when run from within the UI, but fails when run from the scheduled backup with error 66,610. I haven't been able to find those error codes anywhere on the Acronis site.
Details:
source directory C:\_DISKSTATION containing the batch file and the text file:
WakeUp.bat
WakeUp.txt
batch file contents:
copy C:\_DISKSTATION\WakeUp.txt \\DISKSTATION\WakeUp\WakeUp.txt /Y
target directory: \\DISKSTATION\WakeUp
 
Both the source directory and the target directory on the NAS have been given full control for 'everyone' to avoid any permission issues, since I don't know what credentials the backup task scheduler runs under.
In the backup settings:
Command:            C:\_DISKSTATION\WakeUp.bat
Working directory: C:\_DISKSTATION
Do not perform operations until the command's execution is complete
Abort the operation if the user command fails
 
Couldn't be simpler, right? 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/02/2023 - 18:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thanks for contacting.
Please raise a ticket with our support sharing the pre-command and the system report : https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Mon, 12/04/2023 - 14:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
