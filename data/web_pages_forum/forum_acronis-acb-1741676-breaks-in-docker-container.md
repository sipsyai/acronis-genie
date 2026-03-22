# Acronis ACB 17.41676 breaks in Docker container

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-17-forum/acronis-acb-1741676-breaks-docker-container

## Original Post
**Author:** Unknown

Acronis ACB 17.41676 breaks in Docker container

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Martin Boissonneault
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi!
With the demise of Postgre 13, installing in Docker fails. The script AB_AMS_prepare_env_ams.sh fails:

PostgreSQL 13 for RHEL / Rocky Linux / AlmaLinu 2.4 kB/s | 146  B     00:00
Errors during downloading metadata for repository 'pgdg13':
  - Status code: 404 for download. postgresql. org/pub/repos/yum/13/redhat/rhel-9-x86_64/repodata/repomd.xml (IP: 151.101.67.52)
Error: Failed to download metadata for repo 'pgdg13': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
+ echo 'Error: Failed to install initscripts'
Error: Failed to install initscripts
+ exit 1
Error: Failed to install AMS.

I checked and the path "download. postgresql. org/pub/repos/yum/13/" is missing on the server. This must align with the EOL of Postgre 13.
Resources:
download. postgresql. org/pub/repos/yum/
www. acronis. com/en/support/documentation/AcronisCyberProtect_17/#docker-upgrading-management-server.html
www. acronis. com/en/products/cyber-protect/download/v17/

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 03/07/2026 - 20:00

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                ADD 12.5 Home
ACP 15
Many older products
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Martin, thank you for the detailed report and logs.

You are correct — the installer script is trying to use the PGDG PostgreSQL 13 yum repository (…/pub/repos/yum/13/…), and the upstream repository path is no longer available, which results in the 404 metadata error and the AMS install aborting. 
Workaround: install AMS using a supported PostgreSQL major version from the PGDG repository (14+) — e.g., PostgreSQL 15/16 depending on your environment — or use the OS-provided module stream (EL9 includes module streams for 16/15/13). 
Please raise a ticket with our support if the issue persists because this would need deep troubleshooting.
Best regards.

      
                
                
                    
                                                    Mon, 03/09/2026 - 12:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Martin Boissonneault
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi José,
Thanks for replying quickly!
Unfortunately, the problem lies with the Docker image. It no longer starts, and the AB_AMS_prepare_env_ams.sh script fails to complete. The error comes from the start script in the image, not my Ubuntu server itself.
Until the issue is resolved in the start script of the AcronisCyberProtect_17_x64_AMS.image file, the server won't start.
A support ticket was opened at the same time this post was created.
Thanks,
Martin

      
                
                
                    
                                                    Mon, 03/09/2026 - 15:29
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                ADD 12.5 Home
ACP 15
Many older products
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Martin Boissonneault wrote:

Hi José,
Thanks for replying quickly!
Unfortunately, the problem lies with the Docker image. It no longer starts, and the AB_AMS_prepare_env_ams.sh script fails to complete. The error comes from the start script in the image, not my Ubuntu server itself.
Until the issue is resolved in the start script of the AcronisCyberProtect_17_x64_AMS.image file, the server won't start.
A support ticket was opened at the same time this post was created.
Thanks,
Martin


Hi Martin,
Thank you for the clarification — you’re right. In this case the failure is inside the AMS Docker image startup script (it tries to use the pgdg13 repository), so the host OS being Ubuntu is not the root cause.
The upstream PGDG /pub/repos/yum/13/ path is no longer available, which is why the script hits a 404 and the container initialization aborts.
Since this requires the image/start script to be updated, opening a support ticket was the correct approach. If you haven’t already, please include in the ticket:
the exact Acronis image/build you imported (filename + build),
the container startup logs showing the pgdg13 failure.
Best regards.
 

      
                
                
                    
                                                    Mon, 03/09/2026 - 15:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
