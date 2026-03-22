# Agents keep dissapearing from console

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/agents-keep-dissapearing-console

## Original Post
**Author:** Unknown

Agents keep dissapearing from console

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ruben Pires
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            So this is what I have been dealing with this week: I install 1 machine with the most recent version of Acronis Backup, register it and perform a backup. I install another machine with most recent version of Acronis Backup, register it and perform a backup.
Suddenly the 1st machine stops appearing on the console sometime after performing the backup on the 2nd machine. When I try to register the 1st again it says its already registered so i follow this suggestion so the machine appears again. Problem is now the 2nd machine also disappears. And it just keeps going round and round.
At the moment this is happening between 4 machines, so i could really use some idea's.
Thanks
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/24/2018 - 17:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ruben!
 
It's Evgeny from Acronis Service Provider Support. 
The behaviour is strange and I can suggest you check two main things:
 
1) Check if you have same MMSCurrentMachineID and InstanceID on the machines where you installed the Agent. 
https://kb.acronis.com/content/56493 
 
Every time an Agent is installed, a new entity is created in Acronis software and the machine is displayed in the Backup management console. When the Agent is reinstalled, a second entry might appear for the same machine and new backup archives for this machine will be created once old backup plans are applied. To prevent these duplicates from appearing, leave Remove the logs and configuration settings (Windows) or Clean up all product traces (Linux) cleared.
 
2) Check if you installed the Agent on a cloned or replicated VM
 
If these two points are not matching, then I suggest you contact our Support per the template
 
Have a good day! 
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Thu, 10/25/2018 - 14:21
