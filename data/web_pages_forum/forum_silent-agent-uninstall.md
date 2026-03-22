# Silent Agent Uninstall

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/silent-agent-uninstall

## Original Post
**Author:** Unknown

Silent Agent Uninstall

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lesha30
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Is there a way to uninstall the agent silently without any user interaction? 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 12/07/2015 - 22:07

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Lesha30,
Depending on how you actually want to run it and on which/how many OS'es, it can be done in a variety of ways.
On Linux and Mac use terminal and run the uninstallation script that comes with the software.
On Windows one of the ways that would do the work is to run CMD as admin (use PsExec to run it remotely) and use WMI: wmic product where name="Acronis Backup Client" call uninstall. Any other built-in Windows procedure for installed packages would work too.
Do not forget to delete the machine from the Backup Management Console after you uninstall it.
If you have some specific environment or uninstallation scenario please let me know.
Regards,
 

      
                
                
                    
                                                    Tue, 12/08/2015 - 06:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
