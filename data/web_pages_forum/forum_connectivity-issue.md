# Connectivity Issue

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/connectivity-issue

## Original Post
**Author:** Unknown

Connectivity Issue

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Simon Scott
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Morning
We have had Acronis Cyber Protect cloud for a while and all workloads backup ok. I have an IKE VPN connection to our Watchguard Firewall and this comes up ok being green . The cloud and production networks are on different segments. When I bring a server up as Production Failover this boots ok and gets its new IP but its not seeing the production network and vice versa the production network cannot ping the failover appliance. Any ideas as to what might be wrong, or if there is a utility to check the VPN is working correctly. The failover network is 172.16.100.0/24 and the failover appliance is using 172.16.100.1 as DNS which I assume is the VPN gateway. Any advice would be much appreciated

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 01/06/2026 - 10:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Simon,
Thank you for the clarification.
At this stage, further troubleshooting will require reviewing logs and detailed VPN/firewall information, which cannot be collected or analyzed through the forum.
Please proceed as follows:

If you are entitled to direct Acronis support, open a support case and attach the relevant logs from the recovery server and the Acronis management service. Our support engineers will be able to review the failover networking behavior in detail.


If your account is managed by a service provider (MSP), please contact your MSP and provide them with this information so they can escalate the case to Acronis on your behalf.

In the support case, please reference:

The failover subnet (172.16.100.0/24)


VPN Phase 2 / traffic selector configuration on the WatchGuard firewall


Routing tables from both production and failover sides


Firewall logs showing traffic between production and failover during testing

Once the logs are available in a support ticket, the issue can be properly analyzed and addressed.
Kind regards,

      
                
                
                    
                                                    Tue, 01/06/2026 - 14:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
