# Acronis Backup Server failed in backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-backup-server-failed-backup

## Original Post
**Author:** Unknown

Acronis Backup Server failed in backup 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fernando Lopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, i have  buy in Plesk Acronis Bakcup cloud but after the installation, the backup said the error : The SnapAPI kernel module is not loaded for the kernel 4.18.0-240.22.1.el8_3.x86_64 that is running in this system. Install the module for this kernel version, and then retry the backup.
i try to find the module but i don't see how to download and install it, the problem appears after an update of the kernel :
kernel-modules-4.18.0-240.22.1.el8_3.x86_64
kernel-core-4.18.0-240.22.1.el8_3.x86_64
kernel-4.18.0-240.22.1.el8_3.x86_64
The OS is Centos 8 with Plesk.
 
Thank you very much to help me i don't know where to find after hours in google

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 06/05/2021 - 08:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Fernando
The error:
"The SnapAPI kernel module cannot be loaded into the kernel running on this system. Install the module for this kernel version and then retry the backup."
Generally occurs after a kernel update
The first option to resolve this is to install the kernel source which exactly matches your kernel version, then after installing the required sources install the agent for Linux again on your computer
If that does not work I would then recommend logging a support case with Acronis Support Team,
The cause of this seems to be that the module was not correctly rebuilt during the upgrade process
I hope this helps
Regards

      
                
                
                    
                                                    Mon, 06/14/2021 - 08:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fernando Lopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jays, finally as I had bought Acronis on Plesk and that there was no solution neither on the side of Plesk nor Acronis, I will be reimbursed. I will try to make a backup with gzip myself but it seems that this is not a safe method of zipping all folders with active files. It’s too bad Acronis, I wish I had it, it’s safer. From what I understand, Acronis backup is not compatible with Ubuntu 20.4.2, I don’t know if it’s true. Thanks for everything!!

      
                
                
                    
                                                    Mon, 06/14/2021 - 15:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day
So sorry to hear that .you could not be helped with Acronis, yes as far as I am aware the latest supported version would be 18.10
However I would recommend keeping in touch with Acronis as they regularly increase the capability of the solution and I am sure they will release support for the latest version soon.
You can also submit a feature/product request so that newer versions are supported, if sufficient requests are received then I am sure it will be prioritised.
Kind regards

      
                
                
                    
                                                    Tue, 06/15/2021 - 13:07
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fernando Lopez wrote:

Hello Jays, finally as I had bought Acronis on Plesk and that there was no solution neither on the side of Plesk nor Acronis, I will be reimbursed. I will try to make a backup with gzip myself but it seems that this is not a safe method of zipping all folders with active files. It’s too bad Acronis, I wish I had it, it’s safer. From what I understand, Acronis backup is not compatible with Ubuntu 20.4.2, I don’t know if it’s true. Thanks for everything!!


Hello Fernando,
sorry to know about your negative experience! If your support ticket is still open, would you mind sharing the ticket ID with me so that we can look into the situation? Please note that the latest update provides support for Ubuntu 20.04.

      
                
                
                    
                                                    Fri, 06/18/2021 - 12:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fernando Lopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina, the patch in question has been updated since what date? I fear that the error during the installation will come back because of the famous "kernel" to which Acronis must associate. With which Acronis Kernel is it compatible? I hope not to say anything, I start, thank you!

      
                
                
                    
                                                    Fri, 06/18/2021 - 14:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Fernando,
please check out the article 62490: Acronis Cyber Protect Cloud, Acronis Cyber Backup: Backup of a Linux machine fails with "The SnapAPI kernel module is not loaded for the kernel currently running on the system" which might be helpful. If the steps from the article didn't help, I'd advise opening a support ticket with Plesk for the more in-depth investigation. 

      
                
                
                    
                                                    Fri, 06/25/2021 - 11:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
