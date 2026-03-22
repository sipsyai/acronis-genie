# [RESOLVED] Agent or agentless installation for VMware cluster?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-agent-or-agentless-installation-vmware-cluster

## Original Post
**Author:** Unknown

[RESOLVED] Agent or agentless installation for VMware cluster?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Max Cooper
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a question regarding installing Acronis agent for backup cloud. I have VMware cluster with more than 100 servers for different companies. What I’m trying to figure out is how to install agents properly so that I will be able to see storage used per each company. Is it possible? If yes, how do I set up it properly?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/29/2016 - 14:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrey Zonov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Max,
Thanks you for posting your question here.
As far as I understand you want to find out how to properly install Agents to monitor storage usage and activities for different companies, considering that you have multiple VMs on VMware cluster.
 
Rest assured, it is possible and I will be glad to explain how to do it properly.
 
We have two options of Agent installation for VMware environment:
 
1) Agent-based installation. This is what we need for accomplishing your request. You need to install Agent for Windows inside all the VMs that will be backed up. When you will be installing the Agent, you’ll be asked to specify Backup Account credentials, under which you want these VMs to be registered. The respective account will then show the VMs and Storage Quota that are tied to this account for a particular company. 
 
2) Agentless installation. If you are looking for agent less backups of the VMs using Agent for VMware, then it will not meet your requirements. The agent can connect to the ESXi host or vCenter for continuing with the backups. However, when you add the Agent for VMware to a Backup Account, it will add all the VMs. This will not help you in having the VMs under different account. All of them will be listed under single account. 
 
3) Agentless installation (2). The difference between this option and previous option is that you will have to connect multiple Agents not to VMware vCenter, but to each company's host. This option will work for your request if each individual company has its individual host and individual Agent for VMware.
Which is why I would follow option #1 or #3 for your request, depending on the configuration you have.
 
__________________
 
Andrey Zonov
Acronis Customer Central | Acronis Backup Software
For more answers to your questions, try our Knowledge Base and Video Tutorials
Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

      
                
                
                    
                                                    Fri, 04/29/2016 - 15:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Max Cooper
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Used option #1 - we're all set for now. Thanks

      
                
                
                    
                                                    Wed, 05/11/2016 - 15:13
