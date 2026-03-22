# Problem with site-to-site VPN (OpenVPN VM appliance type)

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/problem-site-site-vpn-openvpn-vm-appliance-type

## Original Post
**Author:** Unknown

Problem with site-to-site VPN (OpenVPN VM appliance type)

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Denis Christov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, I was trying the OpenVPN site-to-site solution (witn a VM appliance). I have 192.168.200.0/24 local network and the same in the cloud. All seems fine, but the tunnel does not connect (see picture).
As per instructions, the cloud and local networks should be the same. But what I do not get, is that the VPN gateway has an IP 192.168.200.1, which is the same as the router on the local site. When the S2S is turned on, I cannot ping it from the recovery server (is it trying to reach it via non-working tunnel ?) and when S2S is turned off, I can ping it with no problem.
Anybody had any experience with this ? I must be doing something wrong...
Denis
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      acronis.png

                      22.21 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/03/2023 - 10:34

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Denis Christov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            OK, figured it out. It was a firewall problem. A security featureblocked it, even though the firewall did not report it.

      
                
                
                    
                                                    Thu, 01/05/2023 - 08:31
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Denis thank you for taking the time to share your solution with the community! It may help other users facing a similar issue.

      
                
                
                    
                                                    Fri, 01/06/2023 - 08:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
