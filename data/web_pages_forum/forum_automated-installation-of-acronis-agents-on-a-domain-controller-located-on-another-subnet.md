# automated installation of Acronis agents on a domain controller located on another subnet

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/automated-installation-acronis-agents-domain-controller-located-another-subnet

## Original Post
**Author:** Unknown

automated installation of Acronis agents on a domain controller located on another subnet

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    FRANCESCO SCHIAVONE
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello everyone, I have this question to ask you. I'm trying to do an automatic installation of the acronis edr agent on machines connected to this domain controller of a customer where however the machines are located on another subnet. Is there a way to make the agent detect the machines connected to the domain controller even if on different subnets to avoid physically installing the agent on each individual machine one by one?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/27/2025 - 07:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Francesco!
Remote installation of agents is supported for Windows devices only.
Agent installation on multiple devices is only available for devices that are in the same network and discovered by the same discovery method.
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Best regards.

      
                
                
                    
                                                    Tue, 05/27/2025 - 12:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    FRANCESCO SCHIAVONE
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            thx for your help 


      
                
                
                    
                                                    Tue, 05/27/2025 - 12:52
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            FRANCESCO SCHIAVONE wrote:

thx for your help 



You are welcome! 

      
                
                
                    
                                                    Tue, 05/27/2025 - 12:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
