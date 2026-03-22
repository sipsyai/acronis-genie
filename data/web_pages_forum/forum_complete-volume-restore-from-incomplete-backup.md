# Complete volume restore from incomplete backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/complete-volume-restore-incomplete-backup

## Original Post
**Author:** Unknown

Complete volume restore from incomplete backup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tim Westman-Barth
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I don't actually have this scenario, but I have computers I'm interested in getting backed up that have issues that often lead to mid-backup disconnects of the network, resulting in incomplete backup files. 
My past experience is that Acronis should continue backing up where it left off when a connection is restored, and eventually finish the backup (at least provided there aren't too many connectivity issues), but what if a restore is needed before the backup finishes entirely? I understand I can access and restore individual files from the backup, but if the backup contains multiple volumes, can an entire volume be restored via the bootable media without all the other volumes having been completed? Or is that one of those cases where the particular method in which the data is stored prevents restoring a complete volume until the backup actually completes?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 09/26/2023 - 15:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
If the backup isn't completed, the file cannot be restored.
Please note that incomplete backups can become corrupted. This software is designed to work with a stable network connection, and that's a prerequisite. For example, if you're backing up to a NAS and the backup isn't completed, you can attempt to restore some files individually. It may work sometimes, but if it doesn't complete, consider those files as corrupted.
Best regards.

      
                
                
                    
                                                    Wed, 09/27/2023 - 08:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
