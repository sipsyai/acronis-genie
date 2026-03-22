# Problem with a backup : The credentials for network share '...' are incorrect.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/problem-backup-credentials-network-share-are-incorrect

## Original Post
**Author:** Unknown

Problem with a backup : The credentials for network share '...' are incorrect.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Xavier Perret
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi ,
I have a problem on a Windows server 2019.
On this server, i use Hyper-V with two VM.
On one VM the backup is ok, but the second VM, the backup'status is failed with a message :The credentials for network share '' are incorrect.
The both VM have same configuration.
If you have a idea or a piece of idea.
Thanks you

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/18/2024 - 07:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Xavier,
Welcome to the forum.
If you are executing an agentless backup and they are under the same plan and Hyper-V agent, there may be an issue with the product, and you must contact the support team to report that issue.
If the issue is in a VM with a local agent installed, please try the workaround suggested in this KB: https://care.acronis.com/s/article/62227-Acronis-Cyber-Protect-Cloud-Acronis-Cyber-Backup-The-credentials-for-path-are-incorrect-or-The-user-name-or-password-is-incorrect?language=en_US .
Also make sure the agents are updated, that can help.
Best regards.

      
                
                
                    
                                                    Thu, 07/18/2024 - 10:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
