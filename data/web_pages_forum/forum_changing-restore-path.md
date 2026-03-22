# Changing Restore Path?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/changing-restore-path

## Original Post
**Author:** Unknown

Changing Restore Path?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Samuel Gan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Where do I go to change the path where backups are restored?
Currently I have restores heading to D:\Hyper-V but I need to change this to D:\Hyper-V\Virtual Machines.
 
Thanks.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 07/29/2018 - 23:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Samuel,
Welcome to Acronis Forum! Could you attach a screenshot that shows settings in your recovery job. Are you restoring a virtual machine as a set of files (Recover > Files/folders) or as virtual machine (Recover > Entire machine)? 
Thank you, 

      
                
                
                    
                                                    Mon, 07/30/2018 - 13:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hello Samuel,… by Ekaterina
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Samuel Gan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina,
So the issue I discovered is when restoring the entire virtual machine, if Flashback is enabled, our restores would fail. I am assuming this is because the restores are being downloaded to D:\Hyper-V while our VHD files are in D:\Hyper-V\Virtual Hard Disks. Once I moved the VHD I was restoring out of the Virtual Hard Disks subfolder and into its parent folder, the restore completed without issue. I am wondering if there is a setting on the web interface to change what folder the restores are downloaded to.
 

      
                
                
                    
                                                    Tue, 07/31/2018 - 04:07
