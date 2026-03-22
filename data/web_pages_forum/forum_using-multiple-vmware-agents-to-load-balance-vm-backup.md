# Using Multiple vmware agents to load balance vm backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/using-multiple-vmware-agents-load-balance-vm-backup

## Original Post
**Author:** Unknown

Using Multiple vmware agents to load balance vm backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                
                    
                        
            For example.
I have 1 vcenter with multiple ESX servers in it and multiple VMs
Now i wanted to install an Agent for Vmware (for Windows) on every ESXi and register them to the Backup Cloud.
Then when i make a job to backup the entire vmware environment the jobs should be load balanced over all the vmware agents to do the backups.
I know that with Acronis Backup 11.x for vmware that could be done..

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 11/05/2016 - 12:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jeremy,
Thanks for posting your question here, I'll be glad to answer.
Acronis Backup Cloud performs automatic load balancing of VMware VM backup when multiple Agents for VMware are connected to the same hypervisor instance. In your case just make sure that all your agents are connected to the vCenter. Agents will be aware of the ESXi server they are installed on top of, and will prioritise to protect it's VMs, but will take over other VMs in the vCetner when necessary.
Let me know if you have further questions on this matter.
Best regards,
 

      
                
                
                    
                                                    Mon, 11/07/2016 - 11:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            OK strange.. here is the case. I have two agent connected to the same ESXi server.
I have two VM backup jobs running.. but only one vm can get backupped @ a time.... the other VM just sits there.. and begins backup only after the other one is finished.
According to the manual i should able to set the amount of simoultanious backups under backup options.. but i do not see them anywhere..

      
                
                
                    
                                                    Fri, 11/11/2016 - 19:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            OK after looking for the 10th time i found the option.
Now my question is.. what is the threshold to balance the jobs? Is it the amount of virtual disk that an agent for vmware VMs can hold?
Because i have 2 agents for vmware connect to esxi. Made a job to backup 5 VM's @ once.. that happend but they where all handled by the first agent for vmware. The second one did not get any work to do..

      
                
                
                    
                                                    Fri, 11/11/2016 - 22:14
