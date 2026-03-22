# Acronis cPanel WHM plugin does not uninstall properly

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-cpanel-whm-plugin-does-not-uninstall-properly

## Original Post
**Author:** Unknown

Acronis cPanel WHM plugin does not uninstall properly

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hi,
I am testing Acronis in different ways and I wanted to start from scratch on the test server again, and so I tried to uninstall Acronis with
yum remove acronis-backup-cpanel

and
/usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall

but I still see
[root@cloud ~]# ps aux | grep acronis_backup_srv
root     27330  0.0  0.0 112708   976 pts/0    S+   15:15   0:00 grep --color=auto acronis_backup_srv


[root@cloud ~]# ps aux | grep acronis_backup_srv
root     27333  0.0  0.0 112708   972 pts/0    S+   15:15   0:00 grep --color=auto acronis_backup_srv

What else should I be checking for?
Regards,
Christopher

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 05/10/2019 - 13:14

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            My mistake
I see it removed the one I meant
root     13157  0.1  0.5 1047092 40828 ?       Sl   15:58   0:00 /usr/local/cpanel/base/3rdparty/acronisbackup/python/python -m acronis_backup_srv.app_daemon --config=/usr/local/cpanel/base/3rdparty/acronisbackup/srv/config.ini
The other one, of course, is ok.

      
                
                
                    
                                                    Fri, 05/10/2019 - 14:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
