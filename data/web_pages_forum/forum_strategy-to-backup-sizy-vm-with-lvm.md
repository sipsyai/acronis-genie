# strategy to backup sizy VM with LVM

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/strategy-backup-sizy-vm-lvm

## Original Post
**Author:** Unknown

strategy to backup sizy VM with LVM

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We are about to backup a VM with about 85 TB vDisks attached (each round 4 TB), within the VM several LVM volume groups.
As we have doubts whether this VM will be good for an all-in-one go, we are considering addressing it with multiple plans, selecting only parts of the whole.
Is this feasable? We already learned that file/directory backups can only be performed via installed agents. If we want to back up via the hypervisor, only "Entire Machine" or "Drives/Volumes" are possible.
With "Drives/Volumes" we probably will not get consistent backups from an LVM point of view.
Advice welcome, Tom.
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/28/2025 - 15:19

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            (P.S. things get even more troublesome as this VM relies on XFS file system, and the support for XFS is still limited, see https://forum.acronis.com/forum/acronis-cyber-protect-premises/full-xfs…)

      
                
                
                    
                                                    Fri, 03/28/2025 - 15:20
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
The best way to handle that would indeed be through different plans and by splitting those backups. The more data a single plan contains, the longer it will take.
Note that these amounts of data are huge, so ensure that the host and VMs have sufficient RAM to handle the operation, as well as adequate bandwidth.
If you have any questions, please contact our support team so we can assist you further.
Best regards.

      
                
                
                    
                                                    Mon, 03/31/2025 - 08:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose,
 
thanks for your reply, the necessity to split up seems clear, but the actual issue is in our assumption
 
> With "Drives/Volumes" we probably will not get consistent backups from an LVM point of view."
 
So again, is it feasable to do splits with the "Drives/Volumes" choice?
 
When we opt for the agent based backup, the performance will probably be much below the option of Hypervisor based backup via the VA.
 
Kind regards, Tom

      
                
                
                    
                                                    Mon, 03/31/2025 - 15:58
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
