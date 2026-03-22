# Disable Quiesce

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/disable-quiesce

## Original Post
**Author:** Unknown

Disable Quiesce

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Danny van Oijen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is it possible to disable Quiesce for a VM?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/06/2015 - 06:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Danny,
We currently don't have any setting to disable quiescing of VMs in backup options, so the only way would be to disable it on VM side:
you can either uninstall VMware Tools / Hyper-V Integration Services (or their respective VSS function) from the VM so that quiesce-commands are not passed through from the hypervisor
or you can disable respective VSS service inside the VM
If you could describe your usage scenario we could better understand the necessity of this feature.
Thank you,

      
                
                
                    
                                                    Fri, 11/06/2015 - 07:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Danny van Oijen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dmitry,
We have more than 100 vm's and on some of them we have problems backing them up.
We get the message in the log that it could not quiesce the vm.
However that is not that big of an issue wether quiesce is active or not because during backup no one is on that server and working in documetns (Fileserver).

      
                
                
                    
                                                    Fri, 11/06/2015 - 07:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Danny,
Thank you for clarifying your scenario.
It does make sence to disable quiesce as a temporary workaround for numerous problems. But it is still not the best solution since quiesce function works not that much for protecting locked files (we don't do file-based backup of VMs anyway and they cannot be skipped) but to consistently backup file system and applications of the VM. In case you turn off quiesce function, backup is performed in crash-consistent state and may result in some transactional data loss.
As you said, on a fileserver that may not be a big issue, so it's up to you whether to localize the VSS problem (which is the most common root cause for quiescing failure apart from intergration tools problems) or completely disable it.
Best regards,

      
                
                
                    
                                                    Fri, 11/06/2015 - 07:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
