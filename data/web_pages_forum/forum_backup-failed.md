# Backup failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-failed

## Original Post
**Author:** Unknown

Backup failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Effendy Abdullah
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            

Trying Backup Cloud for the first time. Added a website to test backup via ftp....
FTP credentials all working ok, tested with Filezilla connecting thru SFTP works. But when i click  When i do a backup, it connects and the shows 1% Backing Up, after 5 minutes it shows error.
 
Screenshot and error log below:
 



 
 
Error



Date and time
Feb 24, 2018, 09:14:31 PM






Module
673



Message
 

Additional info:
------------------------
Error code: 500
Module: 673
LineInfo: 0x4AA49F82A59E371A
Fields: {"websiteResourceId":"45493DAE-1964-11E8-A347-0018515D080A","websitePolicyId":"498D85FA-1964-11E8-B64C-0018515D080A","$module":"ams_rest_api_lxa64_5302","websiteR


Message: Backup failed!
------------------------
Error code: 100
Module: 673
LineInfo: 0x0000000000000000
Fields: {"taskId":"51c568a6-fd6a-4133-9295-20552d512599","$module":"website-backup-service 1.1.48"}
Message: Traceback (most recent call last): File "/usr/lib/python3.5/site-packages/website_backup_service/ws_handlers.py", line 771, in backup_task_handler await operation.execute() File "/usr/lib64/python3.5/site-packages/ws_agent/operation.py", line 46, in execute await self._run() File "/usr/lib64/python3.5/site-packages/ws_agent/backup_operation.py", line 49, in _run await self._before_archive() File "/usr/lib64/python3.5/site-packages/ws_agent/ws_backup_operation.py", line 106, in _before_archive await validator.validate_static_connection(self._backup_plan.backup_scope.static_conn_settings, self.log) File "/usr/lib64/python3.5/site-packages/ws_agent/validator.py", line 78, in validate_static_connection logger=logger): File "/usr/lib64/python3.5/site-packages/ws_agent/fs_client.py", line 36, in __aenter__ await self.connect() File "/usr/lib64/python3.5/site-packages/ws_agent/sftp_client.py", line 329, in connect raise conn_exc ws_agent.errors.FsServerUnavailableError
------------------------
Error code: 112
Module: 673
LineInfo: 0x0000000000000000
Fields: {"$module":"website-backup-service 1.1.48"}
Message: Remote file system server unavailable.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 02/24/2018 - 13:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
It's Evgeny from Acronis Service Provider Support.
I am sorry for the delay in response within this thread.
 
I checked the internal records and found that you already contacted us via Support and the current ticket is being investigated.
We will continue assisting within the support request.
 
Best regards,
Evgeny Ryuntyu | Support Engineer
Acronis 

      
                
                
                    
                                                    Thu, 03/01/2018 - 12:28
