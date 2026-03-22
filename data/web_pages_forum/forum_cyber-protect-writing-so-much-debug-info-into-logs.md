# Cyber Protect writing so much debug info into logs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-writing-so-much-debug-info-logs

## Original Post
**Author:** Unknown

Cyber Protect writing so much debug info into logs

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jan G.
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I just installed the new version of cyber protect 16 and realized, that disk resources are used continiuosly.
You can see them under Resource Monitor in the system process:
C:\ProgramData\Acronis\AccountServer\Logs\account_server.log
C:\ProgramData\Acronis\BackupManager\Logs\backup-manager.log
C:\ProgramData\Acronis\AMS\logs\curl0.log
Here during idle there constantly written 15kB/s = 1MB/min. = 60MB/h
There is so much useless debugging info like
{"level":"info","time":"2025-02-17T19:29:23.0535462+01:00","msg":"response completed in 0.005s","pid":34336,"request_id":"cupo00v7bd
{"level":"debug","time":"2025-02-17T19:29:23.3565527+01:00","msg":"db pooling not supported, will use single default connection pool
{"level":"debug","time":"2025-02-17T19:29:23.357462+01:00","msg":"opened DB transaction (/idp/token pool) in 0ms","pid":34336,"reque
{"level":"info","time":"2025-02-17T19:29:23.357462+01:00","msg":"AMQP is disabled. Events will not be published.","pid":34336}
{"level":"debug","time":"2025-02-17T19:29:23.357462+01:00","msg":"token requested: TokenRequest{GrantType: \"client_credentials\", C
{"level":"info","time":"2025-02-17T19:29:23.3786287+01:00","msg":"token issued with grant type \"client_credentials\", request scope
{"level":"debug","time":"2025-02-17T19:29:23.3786287+01:00","msg":"closed DB transaction (/idp/token pool) in 0ms","pid":34336,"requ
{"level":"info","time":"2025-02-17T19:29:23.3786287+01:00","msg":"AMQP is disabled. Events will not be published.","pid":34336,"requ
{"level":"info","time":"2025-02-17T19:29:23.3786287+01:00","msg":"Event manager producer has been disabled. Events will not be publi
{"level":"debug","time":"2025-02-17T19:29:23.3786287+01:00","msg":"events published in 0ms","pid":34336,"request_id":"cupo00v7bdooc8
{"level":"info","time":"2025-02-17T19:29:23.3798106+01:00","msg":"response completed in 0.023s","pid":34336,"request_id":"cupo00v7bd
 
Is there any way to change the logging level to "warning" instead of "debug"? Who will ever look in these logs overwritten every 5 hours because the max folder log size of 300 MB is reached?
This much writing is hitting every write-sensitive SSD.
Best regards
Jan

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/17/2025 - 18:39

                                                          
                                                            
                                                                                        
    
                    
                Best regards

Jan

            
                            
                Products: 
                Cyber Protect Workstation 16.3.39376
Cyber Protect Virtual Host
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jan,
Welcome to the forum.
Please refer to the bottom of this KB article, where it says "More information" (it refers to version 12.5, but I believe it is still applicable in ACP 16): https://care.acronis.com/s/article/60392-Acronis-Cyber-Backup-12-5-and-12-how-to-collect-debug-logs-Windows?language=en_US.
If you have any questions during the process, feel free to contact our support team—we'll be happy to guide you through it.
Best regards.

      
                
                
                    
                                                    Tue, 02/18/2025 - 14:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
