# How to clean up AtpDatabaseMirror folder (C:\ drive space issue)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/how-clean-atpdatabasemirror-folder-c-drive-space-issue

## Original Post
**Author:** Unknown

How to clean up AtpDatabaseMirror folder (C:\ drive space issue)

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Serios
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I am using Acronis Cyber Protect 16 with the Management Console on a Windows Server.
Backups are working fine to my NAS, but I have a big problem with disk space:

The folder
C:\Users\AllUsers\Acronis\AtpDatabaseMirror\ngmp\v2 keeps growing (tens of 120GB).


As I understand, this is part of Acronis Active Protection and stores antimalware/definition databases.


My problem: The C:\ system drive is filling up, even though backups are saved externally.

My questions:

Is there an official way to clean up or limit this folder?


Can I safely delete this folder after disabling Active Protection?


If I use Microsoft Defender, can I completely disable Acronis Active Protection without affecting backup jobs?


Is there any option for automatic cleanup or size limits for this folder?

System details:

Acronis Cyber Protect 16


Windows Server 2019


Backup target: NAS


Management Console in use

Thank you very much for your help!
Best regards,

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/01/2025 - 11:42

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
For cleaning up the AtpDatabaseMirror folder, we have created a script:KB68544 – Acronis Cyber Protect 15: Backup fails with “Not enough memory” or logs occupy free space on Acronis Management Server
You can also perform a custom installation and remove the security features, as described here:KB73586 – Acronis Cyber Protect 16: Installing agents
Once features such as Anti-Malware/Ransomware protection are removed, you might be able to delete the folder. However, I wouldn’t recommend this approach.
Yes, you can safely disable Acronis Active Protection without affecting your backup jobs, since those are not related.
Regarding your question 4: there are no built-in options for automatic cleanup. I would suggest contacting our support team ( https://support.acronis.com/ ) with your case details, as they may be able to provide a dedicated script or workaround.
Best regards,

      
                
                
                    
                                                    Wed, 10/01/2025 - 15:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Serios
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you José for the detailed reply!
I will try the script from KB68544 as the first solution, this looks like the best way.
I will keep it running for some time and report back with the results in a few weeks.
Thanks again for your help!

      
                
                
                    
                                                    Thu, 10/02/2025 - 04:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Serios wrote:

Thank you José for the detailed reply!
I will try the script from KB68544 as the first solution, this looks like the best way.
I will keep it running for some time and report back with the results in a few weeks.
Thanks again for your help!


You are welcome!
Feel free to update this thread once you have the results.
Best regards. 

      
                
                
                    
                                                    Thu, 10/02/2025 - 08:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
