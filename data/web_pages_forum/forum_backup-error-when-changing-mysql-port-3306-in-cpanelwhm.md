# Backup error when changing MySQL port 3306 in cPanel/WHM

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-error-when-changing-mysql-port-3306-cpanelwhm

## Original Post
**Author:** Unknown

Backup error when changing MySQL port 3306 in cPanel/WHM

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Emilio CS
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Acronis Cyber Protect Cloud
Cpanel / WHM Plugin
Almalinux 8
When I change the MySQL port in /etc/my.cnf, example:
port=3346

/usr/lib/Acronis/BackupAndRecovery/prepostdata.py does not get the correct port when colleting data and uses de default port 3306 in Command 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;' instead new 3346 port configured in /etc/my.cnf
"text": "Failed to execute command '/usr/lib/Acronis/BackupAndRecovery/webcpprecapture: Command 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;'' returned non-zero exit status 1.\nFor more details please see \"/var/lib/Acronis/AgentCommData/capture-data.log\"Command 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;'' returned non-zero exit status 1.\nCommand 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;'' returned non-zero exit status 1.\nCommand 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;'' returned non-zero exit status 1.\nCommand 'export HOME=/root && mysql --host=localhost --port=3306 --execute='SHOW DATABASES;'' returned non-zero exit status 1.\n'.",

 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/27/2024 - 22:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Emilio!
If any of the ports are closed, the software will display their numbers and the corresponding host names, for which each port should be open.
Have you tried reinstalling the plugin? Because if you executed and configured the agent to reach that port, if you change it, the agent won't gain access to the information.
If the issue persists, I suggest you contact our support at https://kb.acronis.com/content/8153.
Best regards.
 
 
 
 

      
                
                
                    
                                                    Thu, 03/28/2024 - 11:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
