# Hypervisor Level backup and Guest backups

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/hypervisor-level-backup-and-guest-backups

## Original Post
**Author:** Unknown

Hypervisor Level backup and Guest backups

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all :)
 
I've been experimenting with the Hyper-V agent to carry out backups of both the Host and Guest VM's
 
In order to save Cloud space, can you see any issues with the following method?:
 
Create an "Entire Machine" backup of the Host but filter out VHDX, VHD and HRL files, leaving in the Virtual Machine Config Files intact
Then backup each Guest VM, "Entire Machine"
 
As I see it, from this I would have the ability to:
1. Restore a VM  either entirely or files&folders
OR
2. In the event of a total failiure of the Host, I could restore the Host OS, with Virtual Machine config files, then restore the Guest backup as a VM and attach the VHDX file to the VM in the hypervisor.
 
What I'm trying to avoid is having to backup both the Guest AND the Host in full, as to me that seems like un-needed duplication (backing up the VHDX, VHD, HRL files on the Host when a Disk/Volume level backup has been made of the Guest)
 
As always, your feedback would be most appreciated :)
 
Thanks,
 
Phil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 01/19/2019 - 22:18

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
thank you for your posting! Yep, basically you can filter out the VM files in the backup of the Hyper-V host and protect VMs separately to avoid duplicating the data. Here our product manager also recommends this scheme. 
Thank you, 

      
                
                
                    
                                                    Fri, 02/01/2019 - 13:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
