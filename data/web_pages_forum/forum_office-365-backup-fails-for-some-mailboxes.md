# Office 365 backup fails for some mailboxes

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/office-365-backup-fails-some-mailboxes

## Original Post
**Author:** Unknown

Office 365 backup fails for some mailboxes

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    chell solutions
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
I have random office 365 mailboxes fail backup with error. Windows error: (0x80070057) The parameter is incorrect.
Acronis cloud
A single system is backing up all office 365 mailboxes. some work correctly others don't. I have deleted the backups and the backup files and it still occurs.
Multiple customers have the same problem so it can't be the site or the office 365 domain.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 02/03/2018 - 16:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello there!
I gathered from your description that the backup is running to a local storage, is that correct?
If it is, then judging by your step "deleted backups and retried", it may indicate that the storage media may be at fault, I would advise you to check that as the first step.
Windows error 0x80070057 in general indicates impossibility to make a certain command to a storage.
Reasons behind may vary:
Misconfigured registry keys
 - can be fixed by 3rd party tools
damaged system reserved partition
 - can be fixed by chkdsk if you assign a letter to the partition
Misconfigured decimal symbol settings
 - The error is likely to occur if the decimal symbol is not set to ‘.’ (dot).
If these advises would be helpful, please let me know.
If you would need further assistance, please create a support request so we could have a deeper look - we would need to know the Login name to check the environment and gather system information report.

      
                
                
                    
                                                    Mon, 02/05/2018 - 13:57
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
