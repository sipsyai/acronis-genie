# Windows error: (0x80070005) Access is denied.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/windows-error-0x80070005-access-denied

## Original Post
**Author:** Unknown

Windows error: (0x80070005) Access is denied.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    RJ Cowan
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Has anyone encountered the following error:
Backup succeeded with warnings, Windows error: (0x80070005) Access is denied

This started appearing after Bitdefender blocked service_process.exe, "C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe" 
I've excluded the files from being scanned and I continue to get this error. 
My question, is the following a warning meaning that data was backed up? Or, was data not backed up on files where access was denied? I've looked through the data and it's hard to tell without actually saving and running a test. 
Would this be files that someone left open on a shared folder on the server? 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      ALLC Access Denied Errors.png

                      22.52 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/25/2023 - 17:37

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please refer to the following KB: https://kb.acronis.com/content/65313
Cyber Protect is not compatible with other solutions that use Bitdefender Traffic Interceptor SDK. Running two security programs simultaneously may affect their operation and cause major problems with the system.
Starting from Acronis Cyber Protect Cloud 21.05, Anti-malware components will be installed on the client computers only if anti-malware protection is selected in the protection plan. If you plan to use a different antivirus, to avoid conflicts, do not select antimalware protection in the protection plan.
You can find more information about cyber protection features in Antimalware and web protection. https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/28/2023 - 15:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
