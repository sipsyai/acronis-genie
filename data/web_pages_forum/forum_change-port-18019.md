# Change Port 18019

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/change-port-18019

## Original Post
**Author:** Unknown

Change Port 18019

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jrubin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello. I am running Acronis Cyber Protect 16.3.39376. I need to change port 18019 that is currently being used by one of the services as it is interfering with another application that uses that port. 
Port 18019 is a local port, used for internal communication between different parts of Acronis Cyber Protect responsible for peer-to-peer updates.
Can anyone help me with this?
J Rubin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 04/19/2025 - 12:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
Changing the ports used by the protection agent
Some of the ports required by the protection agent might be in use by other applications in your environment. To avoid conflicts, you can change the default ports used by the protection agent by modifying the following files.
In Linux: /opt/Acronis/etc/aakore.yaml
In Windows: \ProgramData\Acronis\Agent\etc\aakore.yaml
If you have any questions, please contact our support so the team can guide you during the process.
Best regards.

      
                
                
                    
                                                    Tue, 04/22/2025 - 07:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
