# What means Error code: 1

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/what-means-error-code-1

## Original Post
**Author:** Unknown

What means Error code: 1

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Danny van Oijen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            MESSAGE
The activity state has been repaired after unexpected failure.

Additional info:
------------------------
Error code: 1
Module: 309
LineInfo: 0x7564DA35B0F1EB08
Fields: {"$module":"mms_vsa64_1299"}
Message: The activity state has been repaired after unexpected failure.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/06/2015 - 07:40

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Danny,
On high level we do not check the error code or module as they are too generic, we pay more attention to unique LineInfo (search for it in KB) and the error message. The message
     "The activity state has been repaired after unexpected failure."
reports a process crash (see example here). In this case we are taking about process mms.exe, see
     Fields: {"$module":"mms_vsa64_1299"}
So you should either investigate the crash using procmon, or collect this log togerther with the crash dump and system info and escalate the issue to Acronis Support.
Thank you,

      
                
                
                    
                                                    Fri, 11/06/2015 - 07:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
