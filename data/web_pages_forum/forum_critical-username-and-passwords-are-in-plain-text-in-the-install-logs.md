# Critical!  Username and passwords are in plain text in the install logs!

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/critical-username-and-passwords-are-plain-text-install-logs

## Original Post
**Author:** Unknown

Critical!  Username and passwords are in plain text in the install logs!

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Brian
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Acronis, listen up this is a critical item!
When using the Backup_Agent_for_Windows_web.exe and specifying a username and password during the install, the credentials are stored in plain text in the "bootstrapper.log" file.
They are in the 3rd line from the bottom.  Here is what mine shows:
2020-04-17T14:54:26:710-04:00 command line: 'ENABLE_COMMON_ERRORS="1" ADDLOCAL="MmsMspComponents,ActiveProtection,BackupAndRecoveryAgent,CommandLineTool,TotalProtection,TrayMonitor" HTTP_PROXY_DISABLED="1" CURRENT_LANGUAGE="en" REGISTRATION_ADDRESS="us5-cloud.acronis.com" REGISTRATION_TOKEN="XXXX-XXXX-XXXX-XXXX" REGISTRATION_REQUIRED="1" REBOOT="ReallySuppress" TARGETDIR="C:\Program Files\BackupClient" MMS_SERVICE_USERNAME="MyDomain\MyUsername" MMS_SERVICE_PASSWORD="MyPasswordIsHere"'.

 Please let me know that this message has been received and that someone will be addressing this promptly.  Thanks!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/17/2020 - 19:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    IanL-S
                            

                            
                    
                        Forum Hero
                    
                
            
                        
                
                    Posts: 219
                
            
            
                
                    Comments: 5536
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Brian
Hopefully someone from Acronis will see this post. We need to know the application being used, the version and the build number, for example True Image 2020, build . Also the operating system being used, for example Window 10 Pro 64 build 1909. 
May I suggest that you provide feedback from the ATI outlining the issue. To do this, open ATI, click on help on the lower left corner and then select "send feedback". Include a link to this forum thread and the information request above.
Ian

      
                
                
                    
                                                    Sat, 04/18/2020 - 01:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Gigabyte Aorus GA-AX370-Gaming 5 M/B; AMD Ryzen 1700X; 16gig RAM; 2 x 500 gig Samsung 970 EVO PCIe NVMe, 1 x 250 gig Samsung 960 EVO PCIe NVMe drives + other drives (Windows 10 Pro 64)
Gigabyte Aorus B360 Gaming 3M/B, Intel i5 9400; 16gig RAM; 1 x 500 gig Samsung EVO Plus PCIe NVMe +  1 x 250 gig Samsung 960 EVO PCIe NVMe + other drives (Windows 10 Enterprise 64)
Gigabyte Aorus H370 Gaming 3M/B, Intel i5 9400; 16gig RAM; 1 x 500 gig Samsung EVO Plus PCIe NVMe + 3 x Kingston HyerX Fury 240gig RAID 5 + other drives (Windows 10 Enterprise 64)
Synology DS414 NAS 4 x 4TB WD Red HDD

            
                            
                Products: 
                Cyber Protection Home Office (latest build); Disk Director 12.5 

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Brian,
I've passed this topic to the RnD for review, will follow up with an update asap
Thank you! 

      
                
                
                    
                                                    Mon, 04/20/2020 - 14:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Brian
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @IanL-S, thanks for the feedback.  This is using the Cyber Cloud backup product which I think was just renamed to Cyber Protection.  This is using the web installer, but could effect the MSI installer too, not sure yet.
@Ekaterina, thank you.  Let me know if they need any more information.

      
                
                
                    
                                                    Mon, 04/20/2020 - 15:05
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            UPD: the RnD are working on the fix! Internal issue ID for reference ABR-268695.

      
                
                
                    
                                                    Thu, 04/23/2020 - 13:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
