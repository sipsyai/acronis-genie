# VMware host recover

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/vmware-host-recover

## Original Post
**Author:** Unknown

VMware host recover

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
 
Would need som help...thinking :)
 
lets say I have a vmwarehost, standalone  with 5 MS servers
What would best practis  be
1 Account to manage all
Install the backupsoftware on 1 MS server or install the agnet on all servers?
recovery
lets say the entire Vmware host goes to dust but i have full backup images
how would i get them back on a new wmware host?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/07/2016 - 12:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 37
                
            
            
                
                    Comments: 352
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fredrik,
I am using the Agent for VMware (Windows-based) in a separate VM for all my VMware hosts.
In case of recovery you can restore the VMware host (to bare metal, from Recure Media) and in step two you can recover all VMs to the recovered VMware host.
If you have different "functions" on the VMs (like Exchange, ADS) it may require a separate Agent in the Guest OS.
 

      
                
                
                    
                                                    Fri, 10/07/2016 - 13:56
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
thanks for your reply
I can only add 1 standalone host / installed vmware agent right?

      
                
                
                    
                                                    Sun, 10/09/2016 - 12:39
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 37
                
            
            
                
                    Comments: 352
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If the hosts are connected to a vCenter Server you can simply add the vCenter to AB12.
For standalone hosts you would need a separate Agent for each host, thats right. This can be a Agent for VMware (Windows) or the Appliance.

      
                
                
                    
                                                    Sun, 10/09/2016 - 13:35
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect
