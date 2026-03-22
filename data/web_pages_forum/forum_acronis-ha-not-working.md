# Acronis HA not working

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-ha-not-working

## Original Post
**Author:** Unknown

Acronis HA not working 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Zane Ali Mahomed
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hiya, I am trying to get HA configured but keep getting no where. I select the nodes and select the 3 I need for the HA and it goes through a configuration but nothing happens after. It just goes back to the create HA configuration. I have looked at the logs and can not find any entries relating to the HA. Has anyone ever encountered this and is there a work around?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/07/2022 - 11:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Zane, 
I see that the issue has been addressed in a support ticket. Sharing here the outcome for other users to find it -
The validator on HA MN creation requires to have all infra networks with 'vm_public' traffic type enabled to be assigned on each node in HA MN configuration. Meanwhile, Development team has acknowledged software-related issue regarding absence of error in UI upon failed HA configuration - the error has been added in the Update 5.4. 


      
                
                
                    
                                                    Tue, 02/14/2023 - 09:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
