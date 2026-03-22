# SnapAPI Module Does Not Compile In Ubuntu/Debian Kernel 4.2.x

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/snapapi-module-does-not-compile-ubuntudebian-kernel-42x

## Original Post
**Author:** Unknown

SnapAPI Module Does Not Compile In Ubuntu/Debian Kernel 4.2.x

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    chrone
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi Acronis Backup Cloud,
The Backup Agent for Linux does not compile snapapi module for Linux kernel 4.2.x on Ubuntu or Debian x86_64. Is there any official guide how to perform manual snapapi module installation on newer kernel which not yet supported by Acronis?
 
Kind regards,
/chrone

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/08/2016 - 16:37

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis True Image 2016
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    chrone
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The attached is the dkms build make log on Ubuntu 14.04 with HWE kernel 4.2.0-23-generic and Debian 8 with Proxmox VE 4.1 kernel 4.2.3-pve. Hope this helps.
/chrone

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      321277-124894.zip

                      3.83 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 01/08/2016 - 16:57
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image 2016
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi chrone,
Unfortunately we don't have any guide to install SnapAPI module on unsupported kernel.
Kernel 4.2.x support will be implemented in next major release Acronis Backup Cloud 5.0.
Let me know if you need additional information.
Thanks,

      
                
                
                    
                                                    Mon, 01/11/2016 - 13:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    chrone
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dimitry,
Awesome! Is there any ETA? :D Looking forward to it.
 

      
                
                
                    
                                                    Mon, 01/11/2016 - 14:19
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image 2016
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We don't have any confirmed date, but the release is planned for Q1 2016.
I hope this information helps.
Best regards,

      
                
                
                    
                                                    Mon, 01/11/2016 - 14:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    chrone
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks Dmitry,
Just in time with Ubuntu 16.04 LTS (kernel 4.4.x) release. :)
/chrone

      
                
                
                    
                                                    Mon, 01/11/2016 - 14:38
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis True Image 2016
