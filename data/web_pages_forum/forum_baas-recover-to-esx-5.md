# Baas recover to ESX 5

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/baas-recover-esx-5

## Original Post
**Author:** Unknown

Baas recover to ESX 5

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Abdulfattah Reslan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            i add EXSI ver 5.5  host to the Baas I found the virtual machines inside the host but I don't find the host itself to recover image to it 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/01/2015 - 12:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Abdulfattah Reslan,
Your thread has been moved to the Acronis Service Provider Solutions Discussions which is relevant to this product.
If I understand your question correctly, you would like to recover a backup to the ESXi host, not to a virtual machine on this host. Or is it that you want to recover a backup of a virtual machine to a new virtual machine on this host?
Acronis Backup Cloud (formerly Acronis Backup as a Service) does not support ESXi host configuration backup and restore. Agent for VMware will only show you the virtual machines on the host/cluster and will only let you perform backup/recovery operations with them, not with the host. And recovery of a virtual machine from web interface works now only to the original location (in Acronis Backup Cloud v.4.0), in future releases this functionality will be extended with recovery to a new virtual machine.
Now if you want to perform a recovery to bare metal or to a new virtual machine, you would have to use the bootable media, see instructions here.
Let me know if you have more questions,

      
                
                
                    
                                                    Mon, 07/06/2015 - 10:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
