# VSS error when backuping a VM on hyper-v

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/vss-error-when-backuping-vm-hyper-v

## Original Post
**Author:** Unknown

VSS error when backuping a VM on hyper-v

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a issue with one of my VM. I have this error :
The shadow copy provider timed out while flushing data to the volume being shadow copied. This is probably due to excessive activity on the volume. Try again later when the volume is not being used so heavily.
Error Code : 3
I already updated and reinstall the agent.
Thx for your help !
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 03/06/2017 - 16:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kevin,
The error you're receiving generally means that the backup task took place at the time when machines volumes were under excessive load and therefore Shadow Copy of the machine created during backup process was destroyed since it could not been processed in time. Alternatively there might be a conflict between multiple backup applications set up to run at the same time which causes  conflicts during snapshot's creation (since each product requires sole access to the VSS service).
I'd recommend to change shedule of the backup task to make it start out of business hours (fore example, 12 AM or 3 AM.)

      
                
                
                    
                                                    Mon, 03/06/2017 - 19:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
