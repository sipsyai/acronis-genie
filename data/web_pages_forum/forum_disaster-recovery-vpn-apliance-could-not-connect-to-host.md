# Disaster Recovery VPN Apliance Could Not Connect To Host

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/disaster-recovery-vpn-apliance-could-not-connect-host

## Original Post
**Author:** Unknown

Disaster Recovery VPN Apliance Could Not Connect To Host

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mehmet Sarı
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi All,
We do Acronis Cloud Disaster Recovery POC work for our customer.
We distributed our Site To Site VPN device on Hyper-V Host.  We get an error in the register stage. 
Ping communication is provided. The device has internet access and works without filter.
 
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Acronis_DR_VPN_Apliance_Register_Error.png

                      51.95 KB
                  
              
                      Acronis_DR_VPN_Apliance_Register_Curl_Command_info.png

                      84.21 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/15/2020 - 21:02

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                ALL Acronis Products.
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mehmet ,
I see that one of our support engineers is already working with you on this case. Would you mind sharing the solution here with the community? We'd appreciate that! 

      
                
                
                    
                                                    Fri, 06/19/2020 - 10:53
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mehmet Sarı
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Friends,
The reason for the problem was stated to be the service provider. However, from the beginning, I found that there was an attempt to register a wrong server.
Whichever server your Acronis cloud account redirects to,
You must enter the address of that server on the VPN device.
The result is as attached.
 
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      543218-186714.png

                      63.75 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 06/22/2020 - 20:50
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                ALL Acronis Products.
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mehmet, thank you for taking the time to share the results\feedback with the community!

      
                
                
                    
                                                    Thu, 06/25/2020 - 11:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
