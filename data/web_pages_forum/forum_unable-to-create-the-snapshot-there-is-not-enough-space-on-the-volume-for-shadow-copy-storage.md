# Unable to create the snapshot. There is not enough space on the volume for shadow copy storage.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/unable-create-snapshot-there-not-enough-space-volume-shadow-copy-storage

## Original Post
**Author:** Unknown

Unable to create the snapshot. There is not enough space on the volume for shadow copy storage.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Paolo Bagnoli
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
I've an agent for cloud backup on a Windows 2019 server.
I've this error : Unable to create the snapshot. There is not enough space on the volume for shadow copy storage.
I've 2 disks and I've a lot of space. With the VSS ACronis test it signal an error on the boot partition
Name: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
DeviceId: \\?\Volume{cf826855-0000-0000-0000-100000000000}\
Size: 548 MB
Available: 125 MB
Minimum: 320 MB
IsOk: False
Description: Free space is below required minimum
IsMounted: False
But I can't extend boot partition.
Do you have some suggestions for me ?
My best regards

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/21/2024 - 18:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
It’s important to note that the space on the disk and the space allocated for shadow copy storage are not the same.
To address this issue, you should resize the shadow storage according to Microsoft’s instructions:
Overview of Volume Shadow Copy Service
Resize Shadow Storage Using vssadmin
Once you’ve increased the shadow storage, run the VSS Doctor again and review the output at the bottom of the report. Any Windows-related errors will typically appear there.
Best regards.
 

      
                
                
                    
                                                    Fri, 11/22/2024 - 16:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
