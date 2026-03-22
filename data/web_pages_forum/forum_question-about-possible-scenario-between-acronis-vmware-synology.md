# Question about possible scenario between acronis, vmware, synology

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/question-about-possible-scenario-between-acronis-vmware-synology

## Original Post
**Author:** Unknown

Question about possible scenario between acronis, vmware, synology

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Hoygen 83
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I was looking for a feature.
Is it possible to backup a virtual machine wich is inside a vmware esxi host, and restore it inside a synology virtual machine manager of course using acronis?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/18/2021 - 06:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rajeev Sharma
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Yes you can but its not straight forward. You need to create NFS share on your synology and mount to your VM directly or by adding datastore on host. Per my understanding you can only do file level recovery.

      
                
                
                    
                                                    Tue, 11/23/2021 - 14:21
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Hoygen 83
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Per file level is not enough in this case, but I will check with synology to figure out if it is possible to have the VM vritten from cloud to the Synology device, and then if it can handle it somehow. Thank you very much.

      
                
                
                    
                                                    Thu, 12/02/2021 - 09:00
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Hoygen 83
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If I perform a virtual machine backup, of the whole machine, do I get a
VMDK (VMware Virtual Machine Disk)
file?
according to this:
kb.synology.com / en-uk / DSM / tutorial / How_to_turn_physical_OS_into_virtual_machines
I would be able to restore it.

      
                
                
                    
                                                    Thu, 12/02/2021 - 09:05
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rajeev Sharma
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            VMDK is file extension of vmware virtual machine's disk AND acronis backup file extension is .tib or .tibx. If you do VM level backup of your virtual machine it will be saved on NAS as .tib or .tibx. 
You can use your synology as iSCSI by creating a LUN but that will be mounted over software iscsi initiator to your esxi host. This will be another datastore in VMFS.
If you want to get vmdk then browse the datastore and download to a local machine or to NAS

      
                
                
                    
                                                    Thu, 12/02/2021 - 18:07
