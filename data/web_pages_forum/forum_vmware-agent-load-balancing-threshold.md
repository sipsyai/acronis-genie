# vmware agent load balancing threshold

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/vmware-agent-load-balancing-threshold

## Original Post
**Author:** Unknown

vmware agent load balancing threshold

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                
                    
                        
            What is the threshold for vmware agents to handoff VMs backup jobs to the next agent?
What is the logic behind it?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/14/2016 - 09:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vasily Semyonov
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 3841
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
The VMs are bind at first to the agent (appliance or Windows Agent) running on the same host as the backed up VM, the 2nd priority is given to agent on another host in the same VMware cluster and the 3rd priority to any other agents.
This priority may be overridden if there are more than 100 (this threshold value can be adjusted in case you run local AMS) VMs managed by one agent - in this case all new VMs from this host may be bind to agent running on another host (if there are no more "local" agents). 
In case there are 2 or more agents running on the same ESXi host, the VMs are distributed between them evenly. For example from 30 VMs running on the same host there will be 10 VMs bind to each of 3 agents.
Thank you.

      
                
                
                    
                                                    Mon, 11/14/2016 - 13:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Vasily
Acronis Virtualization Program Manager

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            check

      
                
                
                    
                                                    Wed, 11/16/2016 - 07:41
