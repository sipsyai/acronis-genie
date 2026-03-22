# Agent for QNAP

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/agent-qnap

## Original Post
**Author:** Unknown

Agent for QNAP

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Danny van Oijen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is there an Agent for the QNAP NAS?
I allready tried installing the bin fiel but it does not work.
error while loading shared libraries: librt.so.1: wrong ELF class: ELFCLASS32

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 12/04/2015 - 10:53

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Danny,
We don't have a specific Agent for QNAP NAS, and we also didn't test the Agent for Linux on QTS Linux, so we cannot guarantee compatibility. Please check supported distributions here.
If you want to try it anyway, you should make sure you are using correct installation package for your 32-bit or 64-bit OS, then make sure the kernel is supported and then troubleshoot the missing shared library, install missing dependencies, run ldconfig to refresh the links.
Let me know if you need additional specific information.
Best regards,

      
                
                
                    
                                                    Fri, 12/04/2015 - 12:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
