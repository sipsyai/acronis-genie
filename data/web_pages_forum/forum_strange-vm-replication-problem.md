# Strange VM Replication problem

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/strange-vm-replication-problem

## Original Post
**Author:** Unknown

Strange VM Replication problem

        
  



    
  


  
              
          
        Thread needs solution      
      
      





    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I'll do my best to explain this one.
VCenter with one live ESXi server, 1 remote backup ESXi server and 1 local backup ESXi server 
Agent is installed on a Windows VM on the Live ESXi server (let's call this machine WinAgent)
 
VM1 is a Linux VM that has 2 replication plans.
"Remote Backup VM1" - goes to the remote server
"Local Backup VM1" - goes to the local server
Jobs have been running for a week fine.
 
Yesterday the job failed with the error "None of the items selected for backup were found." 
On investigation the Replica jobs have disappeared from the VM1 item in Acronis. I can't see anything that relates to them.
The WinAgent machine is trying to run the job on itself according the logs (for 2 days now) but I can't see this job anywhere (jobs are still called "Remote Backup VM1" etc)
So two issues here
1. Why have the jobs disappeared from VM1 but are trying to run from the WinAgent server incorrectly.
2. How can I delete this job from the WinAgent server
For additional information I have other VMs still replicating fine on this server.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/18/2017 - 10:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful
