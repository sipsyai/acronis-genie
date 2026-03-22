# Log File Build up

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/log-file-build

## Original Post
**Author:** Unknown

Log File Build up

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    thereverendgreen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi All
I have just found 7.5GB of log files in two separate locations, which appear to be the same files duplicated:
C:\Windows\Temp\sysinfo-xxxx\FileProtectorLogs
C:\ProgramData\Acronis\FileProtectorLogs
Anyone know of any settings that prevent these files from duplicating, or get them to purge automatically?
Web console service: v.12.0.3586
Backup management server: v.12.0.5444
Backup management console: v.12.0.7688
Thanks
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/27/2018 - 08:38

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, TheReverendGreen
Apologies for replying with such a delay, but thank you for the post!
 
Those are the logs of Active Protection.
The Temp folder contains a copy of those only when the system information report is being gathered. You can safely remove the temp ones.
The ones in "C:\ProgramData\Acronis\FileProtectorLogs" are stored when the events of suspicious activities are detected. It writes the names or the processes. You can whitelist some of them if you trust them, the logs will be smaller.
There was an issue with the early versions of the Active Protection software, when the logs were not retained. Ensure that you run the latest agent, as it contains all the recent fixes.
 
Also, there is no dedicated Acronis Backup Cloud-related article about Active Protection, but you can refer to the article https://kb.acronis.com/content/60178 - It explains the service as part of Acronis True Image, but Active Protection code is the same in both cases.
 
Please let me know if that covers it!
 
 
 

      
                
                
                    
                                                    Tue, 07/10/2018 - 09:54
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
