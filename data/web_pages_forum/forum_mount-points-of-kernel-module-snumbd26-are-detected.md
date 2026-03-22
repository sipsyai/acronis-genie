# Mount points of kernel module 'snumbd26' are detected.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/mount-points-kernel-module-snumbd26-are-detected

## Original Post
**Author:** Unknown

Mount points of kernel module 'snumbd26' are detected.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
I have currently about 20 servers where I can not update the agent. When I try to update it manually, I get the following error:
 
Mount points of kernel module 'snumbd26' are detected. Unmount them manually, and then repeat the installation.
 

Is rebooting really the only solution? This are production servers where reboots are not so easy.
 
Regards
Michael

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/04/2022 - 08:55

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kristian Popov
                            

                            
                    
                        Acronis Support Engineer
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 19
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael,
Hope all is well.
To answer your question, a restart of the machine will be the easiest and fastest way but there is an alternative to fixing this - you need to check "snumbd26" use count in /proc/modules.
If it is not zero - try to stop all processes which use the module and retry the update.
Would like to wish you a great day ahead!

      
                
                
                    
                                                    Fri, 01/14/2022 - 15:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Kristian Popov | Acronis Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
