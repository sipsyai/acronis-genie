# Plesk Extension: Failed to install the backup agent

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/plesk-extension-failed-install-backup-agent

## Original Post
**Author:** Unknown

Plesk Extension: Failed to install the backup agent

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Krishan Cvitkovic
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
my problem is that the Backup-Agent cannot be installed, after installing the Acronis Plesk extension successfully.
This is the log output i got:
2023-06-22T09:46:10+0200 backup_agent Start.
2023-06-22T09:46:10+0200: 
2023-06-22T09:46:10+0200:Start 15.0.35739
2023-06-22T09:46:11+0200:Default text converter created OK.
2023-06-22T09:46:11+0200:Use options file /opt/psa/var/modules/acronis-backup/srv/tmp/options_file.
2023-06-22T09:46:11+0200:Cmd line opt:'/backup_agent'
2023-06-22T09:46:11+0200:Cmd line opt:'--auto'
2023-06-22T09:46:11+0200:Cmd line opt:'--strict'
2023-06-22T09:46:11+0200:Cmd line opt:'--options-file'
2023-06-22T09:46:11+0200:Cmd line opt:'/opt/psa/var/modules/acronis-backup/srv/tmp/options_file'
2023-06-22T09:46:11+0200:Cmd line opt:'--packages-bundle'
2023-06-22T09:46:11+0200:Cmd line opt:'/opt/psa/var/modules/acronis-backup/srv/tmp/backup_agent'
2023-06-22T09:46:11+0200:File opt:'/backup_agent'
2023-06-22T09:46:11+0200:File opt:'--rain=https://cloud.acronis.com'
2023-06-22T09:46:11+0200:File opt:'--login=XXX@XXXXXXX.de'
2023-06-22T09:46:11+0200:File opt:'--password=XXXX'
2023-06-22T09:46:11+0200:FileReport: Using /var/log/AcronisRemoteInstall/acroinst2_bootstrap.out, SkipReporting=1
2023-06-22T09:46:11+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:11+0200:Unattended install mode.
2023-06-22T09:46:11+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:12+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:13+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:13+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:13+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:13+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:13+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:14+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:14+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:rpm package detected
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:Looking for sed in RPM DB, called command 'rpm -q sed 2>&1', RetCode:1, Output:
package sed is not installed
2023-06-22T09:46:15+0200:Will use custom RPM DB
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:RPM DB was not found in /var/lib/Acronis. Trying to detect its location.
2023-06-22T09:46:15+0200:Location of RPM DB was not detected.
2023-06-22T09:46:15+0200:Could not detect location of RPM database on Debian system during update.
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:This installer product version: AB_CLOUD 15.0.35739 VENDOR_ACRONIS
2023-06-22T09:46:15+0200:Already installed product version: AB_NONE 0.0.0 VENDOR_NONE
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:check_kernel_version finished OK.
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:deb11 system detected, flags = 8421379
2023-06-22T09:46:15+0200:prepare_transaction finished OK.
2023-06-22T09:46:15+0200:Dependencies check finished OK.
2023-06-22T09:46:15+0200:Getting module information for 'snumbd26'...
2023-06-22T09:46:15+0200:Found: name 'snumbd26', memory '32768', usecount '3'
2023-06-22T09:46:15+0200:snumbd26 module usecount = 3
2023-06-22T09:46:15+0200:Mount points of kernel module 'snumbd26' are detected. Unmount them manually, and then repeat the installation.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      trueimage-setup.log.jpg

                      18.36 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/22/2023 - 08:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Krishan.
Welcome to the forum.
Please apply the solution of this KB: https://kb.acronis.com/content/65311 . 
Please let us know if the issue was resolved.
Thanks in advance!

      
                
                
                    
                                                    Fri, 06/23/2023 - 13:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
