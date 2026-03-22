# error: package BackupAndRecoveryAgent-15.0.27493-1 is not installed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/error-package-backupandrecoveryagent-15027493-1-not-installed

## Original Post
**Author:** Unknown

error: package BackupAndRecoveryAgent-15.0.27493-1 is not installed 

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            I noticed trying to update an agent on a DNS server running CentOS 7 kept failing.
When I uninstalled the agent from the server while leaving * unchecked so it didn't remove config so could resume backup but when try to install again it shows
Cannot find package BackupAndRecoveryAgent.
 
When I try to completely uninstall the agent using below:
 
 [*] Clean up all product traces (Remove the product's logs, tasks, vaults, and configuration settings)
 
It shows
 
error: package BackupAndRecoveryAgent-15.0.27493-1 is not installed

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/13/2021 - 12:17

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Update: I found I was using an outdated agent; didn't realise it was changed from "backup" something to "cyberprotect" something. I downloaded a new one and now it works fine.

      
                
                
                    
                                                    Mon, 10/18/2021 - 22:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security
