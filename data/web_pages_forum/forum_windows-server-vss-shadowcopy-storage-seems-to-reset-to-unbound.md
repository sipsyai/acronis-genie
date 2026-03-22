# Windows Server: VSS ShadowCopy storage seems to reset to "unbound"?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/windows-server-vss-shadowcopy-storage-seems-reset-unbound

## Original Post
**Author:** Unknown

Windows Server: VSS ShadowCopy storage seems to reset to "unbound"? 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear all
 
We're having the strong suspicion, that the Acronis Cyber Protect resets the ShadowCopy "Max Size" from whatever Value back to unbound (or unlimited) when taking a backup. 
A bit of digging shows that somebody came to the same conclusion in 2018 with Acronis True Image, however it was kind of dismissed by an Acronis MVP. Link
 
Does anyone of you have experienced the same behaviour as well?
Thank you all

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/15/2021 - 15:17

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Rajeev Sharma
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Explain what is happening?

      
                
                
                    
                                                    Thu, 12/02/2021 - 18:17
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Rajeev Sharma wrote:

Explain what is happening?
 


We keep limiting the maximum size of shadhow copy on the c:-drive of multiple servers (e.g 20GB). After a short while (after a backup, it seems), shadowcopy is set to unlimited again.

      
                
                
                    
                                                    Fri, 12/03/2021 - 10:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Everyone,
y design, the shadow storage is set to maximum during backup by SnapAPI, however after the copy has been completed it shall be set back to the defined value. I saw several tickets with this task failing due to some environment issues, but no common root cause - please open a support ticket, so that our engineers can investigate the issue in your systems. 

      
                
                
                    
                                                    Sat, 12/04/2021 - 14:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
