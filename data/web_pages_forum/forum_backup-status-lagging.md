# Backup status lagging?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-status-lagging

## Original Post
**Author:** Unknown

Backup status lagging?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have today backupjobs that says running X % under machines
but when i check activities it says done
had som end users contct me with simular issue
staus under machin says old dates as last backup satus
and activities says todays date that would be correct
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/15/2016 - 17:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Fredrik,
 
in ABC  v5.0 we rely on subsequent incremental updates from agent to management server (and back) and these updates are processed using special queue. If some incremental update is lost (due to network issues or crash or race condition or queue overload) – this piece of data is lost and agent becomes unsynchronized forever until our support comes and run “manual re-sync”.
In ABC v6.0 we perform real-time full re-sync every time agent comes online, so if some data is not synchronized – next time agent comes online it will be synchronized for sure.
	This was one of the major architectural changes we made in v6 (was done more than 2 months ago) and we did not have any complains from Beta1 and Beta2 participants.
As with any major change – there is still little chance of issues, but we will resolve them much faster as this synchronization logic is now encapsulated in the Management Server and we have full control over it (opposite to ABC v5 where synchronization logic is spread between Agent and Management Server), so with ABC v6.0 we can resolve issues much faster with new updates to Management Server.
As a quick workaround for the problem you can log in to client machine and  restart Acronis Managed Machine Service. This will force synchronization and should fix the issue.

      
                
                
                    
                                                    Wed, 06/15/2016 - 19:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
