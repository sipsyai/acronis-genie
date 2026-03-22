# Storage Gateway Dual NIC/IP

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/storage-gateway-dual-nicip

## Original Post
**Author:** Unknown

Storage Gateway Dual NIC/IP

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Danny van Oijen
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
Is it possible to add a extra NIC with another IP address assigned to the Acronis Storage Gateway?
I need is to listen on port 4445 also.
Why? we have a seperate 10Gb network, i can give the Storage Gateway and the ESX Agent Server a NIC in that network, thatway i can 'fool' the ESX Agent in telling him (edit hosts file) that he can find the Storage Gateway on that ip-address.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/06/2015 - 11:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Danny,
Thanks for your post.
As confirmed by the developers it is possible. The recommended setup is to use 0.0.0.0:44445 as InternetInterface setting.
This means that gateway will listen port 44445 on all network interfaces.
All you need is to change ip address in DNS name of gateway and the traffic will flow to new NIC.
If there are additional questions, please feel free to open a support ticket.
 
Kind regards,
Evgeny Ryuntyu
Acronis Service Providers Support

      
                
                
                    
                                                    Fri, 11/06/2015 - 15:01
