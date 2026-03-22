# Merging/Linking existing Virtual Machine Backup to new Virtual Machine

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/merginglinking-existing-virtual-machine-backup-new-virtual-machine

## Original Post
**Author:** Unknown

Merging/Linking existing Virtual Machine Backup to new Virtual Machine

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
 
Quick question: I have a Guest VM (lets call it VMold) with a Full Disk/Volume backup captured from the Host level (agentless)
If I restore "VMold" to a new Host, creating "VMnew", is there a way to link/merge the "VMold"  backups to  "VMnew" and pick up where "VMold" backups left off
Or do I have to start backups again from scratch for "VMnew" on the new Host?
 
Many thanks,
 
Phil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/23/2019 - 09:12

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Phil,
 
It's Evgeny from Acronis Service Provider Support.
 
The exact scenario you want to achieve does not seem to have been tested officially, but I can suggest you a way.
We have tested the scenario on how to continue backing up to an existing archive with a new backup plan, you can find more details in the following Knowledge Base article
Taking into account that you will restore the machine to a new Host, please make sure you have the Agent registered on the same account, managing that host.
Please check if this instruction helps to achieve the result you want.
 
-----------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Wed, 01/23/2019 - 10:09
