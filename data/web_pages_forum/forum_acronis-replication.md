# Acronis replication

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-replication

## Original Post
**Author:** Unknown

Acronis replication

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Steve Vos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I’m looking for this feature for many years and I don’t understand this is not possible with acronis:
 
we’re using Acronis Cyber protect to backup our servers, we use our own storage boxes with Acronis abgw deployed on it which works fine.
Now i want to replicate those backups to a 2nd remote location with immutable storage like wasabi.
But for some reason you can only replicate to local storage and not to a second cloud location.
We’re an msp ald we can’t deploy local storage boxes with each customer.
 
Can someone explain me why this isn’t possible or maybe i’m missing something.
 
tx

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 07/21/2023 - 11:31

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Steve.
That's not possible by design.
Each MSP tenant/account just have 1 cloud storage by default. Second cloud locations aren't supported. The product is designed to support backups stored in our own Cyber Infrastructure. That's specified here: https://www.acronis.com/en-us/support/documentation/AcronisCyberCloud/i…
We don't have any plans to integrate that feature in a near future but I passed the message to the team.
Feel free to contact our support if you have any additional questions. https://kb.acronis.com/content/8153
Thanks.
 

      
                
                
                    
                                                    Tue, 07/25/2023 - 14:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
