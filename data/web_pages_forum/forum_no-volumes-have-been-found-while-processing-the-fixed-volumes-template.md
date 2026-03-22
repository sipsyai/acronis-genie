# No volumes have been found while processing the 'Fixed Volumes' template.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/no-volumes-have-been-found-while-processing-fixed-volumes-template

## Original Post
**Author:** Unknown

No volumes have been found while processing the 'Fixed Volumes' template.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Ladies and gentlemen,
first of all, wish you all a happy new year.
now to the topic:
I have a Linux server where I get the error "No volumes have been found while processing the 'Fixed Volumes' template" when i try to backup the whole machine.
I worked through the solution approaches from an old topic. With the command "modprobe snapapi26" i get the message that it can not be found.
Thats why i tried to install the agent again.
The installation ends incorrectly:
Installation of the Backup Agent packages has finished.
The following problems occurred:
- failed to start service 'acronis_agent'.
- failed to build the SnapAPI kernel module. Operations with disk-level backups will not be available.
- failed to load the SnapAPI kernel module.
the environment:
Linux version 4.4.159-73 (OpenSuse)
Acronis Agent 12.5.12210 (trying to install)
 
Need help.........

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/04/2019 - 10:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes,
 
The issue is most likely caused by not fulfilling the prerequisites for installation. SnapApi wasn’t compiled  due to lacking necessary packages, so the Agent can’t detect any disks without it. Please check the following User Guide article for details on Linux packages:https://www.acronis.com/en-us/support/documentation/BackupService/index.html#42021.html
 
While the User Guide article doesn’t specify the names of packages for Open Suse, three of them – perl, gcc and make – should be the same. The other two – Kernel-headers and Kernel-devel – might be named differently, but the logic behind it is the same: both packages must be installed and must match the Kernel version itself.
 
Once you’ve fulfilled the prerequisites, you might either reinstall the agent or compile SnapApi manually by following the steps from the Knowledge Base article at https://kb.acronis.com/content/41283. 
Once done, please check if the disks are detected correctly. The simplest way to do it is to create a “disk” level backup and attempt to select the disks.

      
                
                
                    
                                                    Fri, 01/04/2019 - 13:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
since Linux is not my hobby and my experiences with the OS are not much, I have the requirements based on the (known) instructions probably fulfilled.
However, the installation still ends with the known errors:
- failed to start service 'acronis_agent'.
- failed to build the SnapAPI kernel module. Operations with disk-level backups will not be available.
- failed to load the SnapAPI kernel module.
For further processing of my problem. Here more information about the system:
Linux version 4.4.159-73-default (geeko@buildhost)
gcc version 4.8.5 (SUSE Linux)
GNU Make 4.0
Perl 5, version 18, subversion 2 (v5.18.2) built for x86_64-linux-thread-multi
RPM version 4.11.2
kernel-devel-4.4.165-81.1.noarch
kernel-headers = linux-glibc-devel-4.4-6.3.1.noarch
 
If tried to compile SnapApi manually but this failed too.
Help :-(

      
                
                
                    
                                                    Tue, 01/08/2019 - 15:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello again,
problem was solved.
Error was in the system itself.
Support from the Linux system has found a deep error.
After fixing this error, the installation went through without error.
Backups from the whole machine work too.

      
                
                
                    
                                                    Fri, 02/01/2019 - 14:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes,
thanks for the update, good to hear the problem is resolved and hope it stays that way for you!

      
                
                
                    
                                                    Mon, 02/04/2019 - 08:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
