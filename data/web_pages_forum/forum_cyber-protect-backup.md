# Cyber Protect Backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-backup

## Original Post
**Author:** Unknown

Cyber Protect Backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Sven Adam
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            When 'entire machine' backup almost finished the following error is logged:
Error code: 6225920
Fields: {"$module":"mms_lxa64_37802"}
Message: Failed to find a loader in a Boot Order list. Now search everywhere.
On Booting an Acronis loader is listed but it does not seem to work, so I guess a repair or a replacement will be needed. How to on a machine that has a running agent installed?
 
EDIT:
In the meantime I've found an article on issues with DELL PERC H755 drivers not available for bootable recovery media on linux machines. I guess the same cause might have led to above error.
Any ideas on how to render a Dell PowerEdge server running Cloudlinux bootable for Acronis to perform recoveries?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/20/2024 - 10:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please provide us with more details:
Is this a backup or a recovery error?
What version of the product are you using?
Are you executing the backups in the console or with the bootable media?
Did you try to recreate the bootable media and add the drivers manually?
What's the full error code?
Best regards.
 

      
                
                
                    
                                                    Tue, 05/21/2024 - 07:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sven Adam
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
it is a backup error. Agent version is 24.4.37802. I execute via cloud dashboard. As for recreation: I am not sure which drivers to implement for the Linux machine.
The full error code: 
MESSAGE
Failed to find a loader in a Boot Order list. Now search everywhere.

Additional info:
------------------------
Error code: 6225920
Fields: {"$module":"mms_lxa64_37802"}
Message: Failed to find a loader in a Boot Order list. Now search everywhere.
------------------------


      
                
                
                    
                                                    Tue, 05/21/2024 - 10:47
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sven Adam wrote:

Hi,
it is a backup error. Agent version is 24.4.37802. I execute via cloud dashboard. As for recreation: I am not sure which drivers to implement for the Linux machine.
The full error code: 
MESSAGE
Failed to find a loader in a Boot Order list. Now search everywhere.

Additional info:
------------------------
Error code: 6225920
Fields: {"$module":"mms_lxa64_37802"}
Message: Failed to find a loader in a Boot Order list. Now search everywhere.
------------------------



Hello Sven.
Please raise a ticket with our support at  https://support.acronis.com/
That way the team can review with you what's exactly wrong and download the full logs.
Best regards.

      
                
                
                    
                                                    Tue, 05/21/2024 - 12:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sven Adam
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I do not have a salesforce account so I can't login following your link.
Instead I shall raise a ticket via the protect cloud dashboard.
 
Kindest regards,
Sven

      
                
                
                    
                                                    Tue, 05/21/2024 - 18:45
