# WHM plugin not loading correctly

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/whm-plugin-not-loading-correctly

## Original Post
**Author:** Unknown

WHM plugin not loading correctly 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
             
Hi,
we are installing the WHM backup plugin on one of our servers.
the plugin installed OK.
we then logged in to our services using the WHM plugin. 
Once we logged in it started the install. Pearl and Parted I think off the top of my head.
it then threw up an error about checking the log file that I missed. 
Now when we click on the Acronis icon in WHM it takes us to a greyish screen with a white box at the top with 3 blue lines... nothing to click.
so I thought about removing it it using the 
yum remove command. 
This fails with:
error: %preun(acronis-backup-cpanel-1.0-223.el7.centos.x86_64) scriptlet failed, exit status 1 
Error in PREUN scriptlet in rpm package acronis-backup-cpanel-1.0-223.el7.centos.x86_64 
Verifying : acronis-backup-cpanel-1.0-223.el7.centos.x86_64 1/1
is there a script we can use to remove it or see where the fault is? 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 01/13/2019 - 03:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James,
 
It's Evgeny from Acronis Service Provider Support.
 
Judging by the error message, yum cannot remove the package because a script which should be executed in the %preun section does not exist.
Please try to do "rpm -e --noscripts acronis-backup-cpanel" instead of "yum remove acronis-backup-cpanel"

--noscripts says rpm to avoid executing %preun and %postun scripts (http://ftp.rpm.org/max-rpm/ch-rpm-erase.html). 
 
That should resolve the issue with the plugin removal.
 
BTW,
To reinstall plugin without reinstalling the Backup Agent you can execute "yum reinstall acronis-backup-cpanel". If it doesn't help, please do the following things:
1. export UNINSTALL_BACKUP_AGENT=0
2. yum remove acronis-backup-cpanel
3. Run "ps aux | grep acronis_backup_srv" and kill all found processes.
4. yum install acronis-backup-cpanel
 
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Mon, 01/14/2019 - 13:24
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank You, 
Thats worked, but i need to re add the machine in the cloud console, how can i add it using a token (how do i generate one on cpanel?)
or re run wizard?

      
                
                
                    
                                                    Thu, 01/17/2019 - 00:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi James,
 
If you need to re-add the Agent, you can use the registration tool:
https://kb.acronis.com/content/55244 
 
-----------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Thu, 01/17/2019 - 08:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank You.
 
All done :) 

      
                
                
                    
                                                    Thu, 01/17/2019 - 14:15
