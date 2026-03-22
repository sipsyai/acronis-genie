# Script in place to substitute retention policy due to limitation

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/script-place-substitute-retention-policy-due-limitation

## Original Post
**Author:** Unknown

Script in place to substitute retention policy due to limitation

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    John Georgiadis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi there,
We have a scenario where we need a script to be run before a backup.
We need to script to utilise acrocmd in order to check the backup archive and delete the oldest.
We in an awkward position where we use 2 TB portable drives for backup on local side, performing full backups with size of just over 650GBs making it impossible to maintain 2 copies on each drive as the retention policy on Acronis Cloud runs only upon completion of a successful backup requiring enough space for 3 copies first.
We did not encounter this problem previously as the client was using ABR11.7, but now that we have them on cloud backup to our storage, we need to use the agent from the Acronis Cloud and "suffer" its limitations.
If anyone can provide help it will be highly appreciated.
Thank you in advance.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/23/2018 - 03:12

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello John!
As far as I understand you are using Acronis Backup Cloud while backing up locally.
In Acronis Backup Advanced 11.7 the retention rules could be applied before the backup execution, so this was sufficient for your use case (you need to delete older TIB to allow the new backup to be created).
In Acronis Backup Cloud this is impossible, so you want to cleanup older backup before execution of backup.
 
You can configure a pre/post option to run a script that will delete the older file from the drive.
Please use the following web-help article for reference.
 
https://www.acronis.com/en-us/support/documentation/BackupService/#3635…
 
Let me know if this helps you achieve the goal.
Best regards,
Evgeny Ryuntyu | Expert Support Engineer
Information provided AS-IS with no warranty of any kind.
To contact support, please follow http://www.acronis.com/en-us/support/
 

      
                
                
                    
                                                    Mon, 01/29/2018 - 10:11
