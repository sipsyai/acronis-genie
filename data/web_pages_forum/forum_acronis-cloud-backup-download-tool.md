# Acronis Cloud Backup Download tool

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cloud-backup-download-tool

## Original Post
**Author:** Unknown

Acronis Cloud Backup Download tool

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    RJ Cowan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is the Acronis Cloud Backup Download tool available for partners or only for home users?
Need to archive data off Acronis cloud to a NAS device and was made aware of the Acronis backup tool, however it only seems to be available in home versions that are licensed differently than partner accounts. 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 08/06/2023 - 15:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello RJ.
Welcome to the forum!
The SP products are different.
You can download the entire backup file with the large scale recovery in the command line: https://kb.acronis.com/content/56070
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/07/2023 - 07:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    RJ Cowan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I installed archive, in an elevated CMD prompt I go to the folder and run the following command.
C:\Acronis\archive3-1.14.745\vsa64>archive_io_ctl --astor abgw-phx1-arp1.acronis.com>:44445 --cert C:\Users\All Users\Acronis\BackupAndRecovery\OnlineBackup\Default\bradburyacro.crt --copy /1/XXXXXXXX-2-45E7805C-FB9B-4FE8-A593-163B8CA3D0AE-6CE974FB-8A05-4FE4-AD66-24D02A4023CCA.tibx --ls --show-progress --infinite-timeouts --continue
ERROR: Incorrect command line options
Please advise

      
                
                
                    
                                                    Tue, 08/22/2023 - 22:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
This is the command you should use: 
archive_io_ctl --astor storage_address:44445 --cert path_to_certificate.CRT --copy /1/backup_name_only.tibx --show-progress --infinite-timeouts
Please replace storage_address, path_to_certificate.CRT and backup_name_only with the correct information and the download should start.
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/28/2023 - 15:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
