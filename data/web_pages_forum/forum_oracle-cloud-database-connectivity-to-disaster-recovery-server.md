# Oracle Cloud Database connectivity to disaster recovery server

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/oracle-cloud-database-connectivity-disaster-recovery-server

## Original Post
**Author:** Unknown

Oracle Cloud Database connectivity to disaster recovery server

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Sfr
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            My primary server has OCI database connectivity. Whats is the procedure to follow during the creation disaster recovery server to get the same connectivity to OCI database.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 04/30/2024 - 09:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please review the following user-guide and check if the Oracle OS you use is supported for DR: https://www.acronis.com/en-us/support/documentation/DisasterRecovery/#s…
Also check this KB: https://kb.acronis.com/content/56187
https://www.acronis.com/en-us/support/documentation/DisasterRecovery/#n…

Site-to-site Open VPN connection
This type of connection requires a VPN appliance deployment on the local site.
The Site-to-site Open VPN connection allows to extend your networks to the cloud and retain the IP addresses.
Your local site is connected to the cloud site by means of a secure VPN tunnel. This type of connection is suitable in case you have tightly dependent servers on the local site, such as a web server and a database server. In case of partial failover, when one of these servers is recreated on the cloud site while the other stays on the local site, they will still be able to communicate with each other via a VPN tunnel.
Cloud servers on the cloud site are accessible through the local network, point-to-site VPN, and public IP addresses (if assigned).

If you have any questions please contact the team at : https://kb.acronis.com/content/8153
Thanks in advance!

      
                
                
                    
                                                    Tue, 05/07/2024 - 16:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
