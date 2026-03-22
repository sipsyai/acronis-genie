# Is there a best practice guide to recover a Physical machine backup (tibx file) to a VHD via bootable media?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/there-best-practice-guide-recover-physical-machine-backup-tibx-file-vhd-bootable-media

## Original Post
**Author:** Unknown

Is there a best practice guide to recover a Physical machine backup (tibx file) to a VHD via bootable media?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dale Harrison
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Been having some issues restoring a Physcial backup of a server to a VHD file via the linux based bootable media.
Tried on a production server with a 60GB backup and also on a test server with a test backup of 11GB.
Recovery allways seems to hang or fail on 21%.
The goal is to create the VHD file and then import into Hyper-V as a guest server, once back into Windows Server.
Ideally I would like to do this task in offline recovery.
Options selected in recovery: Recovering (MBR, SYSTEM, C:\) to (C:\Acronis Recovery\SRV1.VHD)
Virtual Hardware: (Microsoft Virtual PC,IDE Drive, 3GB RAM) Actual Hardware is 8TB space and 32GB RAM.
The location of the tibx file is in a folder on the C:\ drive of the server but also tried from a USB external hard disk as the location of the tibx file.
The server I am trying to create the VHD file on is not the server thats is currently being backed up. This server will be replacing that once the VHD is created and configured on the Guest VM.
Any help would be greatfully appreciated.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/24/2019 - 20:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dale,
thank you for your posting! Please refer to 45856: Acronis Backup: Recovery/Conversion to Virtual Machine Troubleshooting Guide, which provides best practices for all recovery/conversion scenarios and the troubleshooting steps for the most common issues. Should the issue persist, we'd recommend raising a support ticket for investigation. 

      
                
                
                    
                                                    Tue, 10/29/2019 - 09:46
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
