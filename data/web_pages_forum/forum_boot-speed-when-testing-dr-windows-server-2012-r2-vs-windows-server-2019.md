# Boot speed when testing DR - Windows Server 2012 R2 vs Windows Server 2019

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/boot-speed-when-testing-dr-windows-server-2012-r2-vs-windows-server-2019

## Original Post
**Author:** Unknown

Boot speed when testing DR - Windows Server 2012 R2 vs Windows Server 2019

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Andrew Williams
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,

We've noticed when testing DR that when we restore Windows Server 2012 R2 VM's, they are much slower at booting than when restoring Windows Server 2019 VM's.
I appreciate the test isolation network may be on slower hardware/disks (?) but there is an obvious difference.
Is this just the way it is due to the architectural differences?
Thanks.
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 10/09/2024 - 12:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Andrew.
Windows Server 2019 includes various performance improvements and optimizations that can lead to faster boot times. Additionally, the underlying hardware and storage configurations can significantly impact boot performance.
If you’re consistently experiencing slower boot times with Windows Server 2012 R2, we recommend checking the following:
Hardware Compatibility: Ensure that the hardware drivers for the 2012 R2 VMs are up to date.
Disk Performance: Monitor disk performance during the boot process to identify any bottlenecks.
Resource Allocation: Ensure that the VMs have adequate resources (CPU, RAM) allocated during restoration.
Best regards.

      
                
                
                    
                                                    Wed, 10/09/2024 - 13:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
