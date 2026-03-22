# Replication to cloud - full instead of incemental

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/replication-cloud-full-instead-incemental

## Original Post
**Author:** Unknown

Replication to cloud - full instead of incemental

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Marek Gwozdz
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 30
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Many times replication to cloud is replicationg full, instead of last incremetal backup.
It takes a lot of time and we are paying for space lots money. And f.e.  instead 1 TB for one machine - we are next day .
2 TB space used.
here is today exaple. 23G B space used instead of 1.81 in last replication:

And next replicas are also full.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/19/2024 - 12:31

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
You must check how the replication plan is scheduled.
In "How to replicate," select which backups to replicate. You can choose one of the following:
All backups (default)
Only full backups
Only the last backup
For more information, please refer to: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#backup-replication-acp.html#kanchor796
Additionally, if you are executing a replication of virtual machines, please note that this may be expected. As described in this user guide, the process for virtual machine replication is different from a normal backup. It creates an exact replica of a virtual machine and then maintains the replica in sync with the original machine: https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#replication-of-virtual-machines-acp.html#kanchor1011
If you are planning to replicate exclusively the backups and not the VMs, and the issue persists, please raise a query with the team so we can investigate the issue: https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Thu, 06/20/2024 - 07:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marek Gwozdz
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 30
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I had full backup choosed in replication. But it worked most of the time and only incremental changes was replicated.
Now i have choosen only last backup.
But therea are not a lot of information in documentation. Only:
"

[Optional] In How to replicate, select which backups to replicate. You can select one of the following:
All backups (default)
Only full backups
Only the last backu

"
So when i choose only las backup - would it be sending only last chunk? Or all last chunks not replicated yet?
 
 
 

      
                
                
                    
                                                    Thu, 06/20/2024 - 11:27
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Marek Gwozdz wrote:

I had full backup choosed in replication. But it worked most of the time and only incremental changes was replicated.
Now i have choosen only last backup.
But therea are not a lot of information in documentation. Only:
"

[Optional] In How to replicate, select which backups to replicate. You can select one of the following:
All backups (default)
Only full backups
Only the last backu

"
So when i choose only las backup - would it be sending only last chunk? Or all last chunks not replicated yet?
 
 
 


If you change it to the last backup it will only replicate the last backup anything else.
Best regards. 

      
                
                
                    
                                                    Thu, 06/20/2024 - 23:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
