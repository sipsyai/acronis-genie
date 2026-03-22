# Issues After Upgrading from Acronis 16.0 Build 39314 to 39938 – Web Console and Services Not Working

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/issues-after-upgrading-acronis-160-build-39314-39938-web-console-and-services-not-working

## Original Post
**Author:** Unknown

Issues After Upgrading from Acronis 16.0 Build 39314 to 39938 – Web Console and Services Not Working

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jens
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone,
After upgrading from Acronis Cyber Protect 16.0 Build 39314 to Build 39938, we encountered several critical issues.
Following the upgrade, some Acronis services stopped working entirely. Most notably:

The web console could no longer be opened.


The Storage Node service failed to start under Windows.

In an attempt to resolve the issues, we went as far as reinstalling all dependent components on our server, including SQL Server and related entries. Unfortunately, this did not help.
Has anyone else experienced similar problems with Build 39938? Any suggestions or known fixes would be greatly appreciated.
Thanks in advance!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/22/2025 - 07:28

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Backup Advanced 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jens,
I've raised a ticket with our team to investigate the situation.
This issue shouldn't occur during the upgrade process.
Our team will contact you as soon as possible.
Thank you!
 

      
                
                
                    
                                                    Thu, 05/22/2025 - 11:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrey Sh
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I experience the same.
now backup server is broken.
upgrade was from 39376 to 39938
I can't rollback to the previous build.
Is there a fix or workaround?

      
                
                
                    
                                                    Fri, 06/06/2025 - 00:05
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andrey Sh wrote:

I experience the same.
now backup server is broken.
upgrade was from 39376 to 39938
I can't rollback to the previous build.
Is there a fix or workaround?


I recommend downloading the agent again and repairing the current installation (please do not uninstall it).
If the issue persists, I suggest raising a ticket with our team so we can investigate further.
Best regards.

      
                
                
                    
                                                    Fri, 06/06/2025 - 06:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
