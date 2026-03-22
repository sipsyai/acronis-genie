# Recovery with reboot terminated unexpectedly

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/recovery-reboot-terminated-unexpectedly

## Original Post
**Author:** Unknown

Recovery with reboot terminated unexpectedly

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Noureddine EL MRABTI
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
We got the error bellow while trying to recover an entire physical machine from it's backup (recover to the same machine). Stuck at 15% during recovery, then fail with the error bellow:
MESSAGE
 
Recovery with reboot terminated unexpectedly.
Additional info:
------------------------
Error code: 20250702
Fields: {"$module":"mms_vsa64_37427"}
Message: L'activité a échoué en raison d'un redémarrage du service.
------------------------
Error code: 20250830
Fields: {"$module":"mms_vsa64_37427"}
Message: Recovery with reboot has failed.
------------------------
I belive it's something related to Managed Machine server on the target machine, but there is no much details were to let me start diagnostic. Knowing that the taregt machine still up and running.
FYI: Acronis Cyber Protect version: 16.0
Thank you for help.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 04/09/2024 - 17:23

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
In order to investigate the issue, you need to follow this KB: 
https://kb.acronis.com/content/61650
Alternatively, consider executing the recovery with the bootable media: 

https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#physical-machine.html


https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#recovering-disks-volumes-by-using-bootable-media.html

You can also try the entire process by creating a WinPE bootable media and adding the necessary drivers: https://kb.acronis.com/content/59611
If the issue persists, please contact our support at https://kb.acronis.com/content/8153
Best regards.
 
 

      
                
                
                    
                                                    Wed, 04/10/2024 - 09:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
