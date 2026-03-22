# thin versus thick provisioning - how does Acronis handle unallocated blocks in thick vdisks?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/thin-versus-thick-provisioning-how-does-acronis-handle-unallocated-blocks-thick-vdisks

## Original Post
**Author:** Unknown

thin versus thick provisioning - how does Acronis handle unallocated blocks in thick vdisks?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Even after some searching I did not find an answer to the question about how Acronis Cyber Protect handles unallocated blocks in thick vdisks (e.g. in ESXi): in a full run, will it back up all block and only compression / dedup will reduce the backup volume, or is there some smarter mechanism behind the scenes?
Or in other words: will the choice of thin or thick volumes make a big difference in terms of backup run time and backup tibx volume allocated?
Regards, Tom
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/25/2025 - 12:34

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Acronis Cyber Protect works at the file system level rather than copying raw blocks. This means that during a full backup it does not back up the unused or unallocated blocks inside a thick provisioned disk. Only the actual data present on the file system is captured, so the choice between thin and thick disks won’t make a meaningful difference for backup size or run time.
Where it can matter is if the VM has snapshots or if the guest OS/file system reports the free space incorrectly — in those cases, you could see larger than expected backup sizes. Deduplication and compression will further reduce the stored data.
In short: the backup size and speed are determined mainly by the amount of used data inside the VM, not by whether the disk is thin or thick.
Best regards.

      
                
                
                    
                                                    Mon, 09/01/2025 - 08:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
