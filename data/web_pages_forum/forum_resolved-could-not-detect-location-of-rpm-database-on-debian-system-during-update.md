# [RESOLVED] Could not detect location of RPM database on Debian system during update

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-could-not-detect-location-rpm-database-debian-system

## Original Post
**Author:** Unknown

[RESOLVED] Could not detect location of RPM database on Debian system during update

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jack DJ
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            When I try to install Acronis Backup Agent for Linux on Debian  3.2.0-4-686 I get:
"Could not detect location of RPM database on Debian system during update"
RPM version 4.10.0
DJack

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/03/2015 - 14:29

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jack,
I'd suggest to rebuild the RPM database. You could check if that or additional RMP manager check is required by trying to install some other RMP package on your system, it should give you the same error.
Let me know if that works or you need further assistance.
Best regards,

      
                
                
                    
                                                    Wed, 11/04/2015 - 08:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jack DJ
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My installation procedure:
#cat /proc/version
Linux version 3.2.0-4-686-pae (debian-kernel@lists.debian.org) (gcc version 4.6.3 (Debian 4.6.3-14) ) #1 SMP Debian 3.2.63-2
#make -v
GNU Make 3.81
#gcc -v
gcc version 4.6.3 (Debian 4.6.3-14)
#rpm
RPM version 4.10.0
#rpm --rebuilddb
#./Backup_Agent_for_Linux_en-US_x86.bin
there is still an above error
Jack

      
                
                
                    
                                                    Wed, 11/04/2015 - 08:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jack,
Seems like it might be an issue in the product. Please check if there is a folder /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall on the system, and remove it (this folder tells the installer that product is already installed, so it tries to find it's trails and fails). Then please re-attempt the installation.
Please let me know the results so we can document the issue.
Thank you,

      
                
                
                    
                                                    Thu, 11/05/2015 - 12:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jack DJ
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You're right. After deleting this folder it is ok.
Thank you.
DJack

      
                
                
                    
                                                    Thu, 11/05/2015 - 12:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for confirming this Jack!
Issue will be fixed in next release of Agent for Linux. It is now also documented here: https://kb.acronis.com/node/57223.
Best regards,

      
                
                
                    
                                                    Thu, 11/05/2015 - 12:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
