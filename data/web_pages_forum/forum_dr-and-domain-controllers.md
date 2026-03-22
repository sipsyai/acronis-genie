# DR and Domain Controllers

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/dr-and-domain-controllers

## Original Post
**Author:** Unknown

DR and Domain Controllers

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Simon Scott
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I wonder if anyone can help as this is something I just cannot work out and even AI is giving me mixed messages on how to proceed. We have Cyber Protect Cloud and all servers backup to this nightly. This works great. I have a VPN setup and again this works ok. The local on-prem network and DR network are on different IP ranges and can see each other. What I can't work out is if I have a problem On-Prem with say a domain controller if I bring it up in the cloud it gets a different IP and nothing sees it from On-Prem. What should I do to either give it the same IP in the DR site or to tell the on-prem clients that its on a different IP address, and consequently when its fixed to move it back to on-prem.
All the articles I seem to find assume the DR site is always running which in this case it won't be as its a DR solution.
If anyone can point me in the right direction it would be much appreciated

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/10/2025 - 15:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello! 
Thanks for the detailed question.
Before diving into DR networking design, just a small but important clarification:
Acronis Cyber Protect Cloud does not use an on-premises management server — that applies to Acronis Cyber Protect 17 (the on-premise product line).
The cloud platform is a different architecture and uses agents + cloud services only.

Because of that, the correct DR configuration — especially for Domain Controllers — depends on how your service provider set up your tenant networking and VPN routing.
What you described requires a DR network plan
When a VM is started in the DR site, it will receive an IP based on the DR subnet.
If production clients must reach that restored DC, then:

Subnet mapping and routing need to be pre-defined, or


DNS changes must be handled during failover

These are normally designed and validated with the service provider or support team, since they have access to your network settings in the cloud.
Suggested next step
Please contact your service provider or Acronis Support through your management console so they can:
- Review your DR subnet configuration
- Validate VPN routing and addressing for failover
- Provide best practices for Domain Controller DR testing
They will be able to check the environment directly and guide you through the correct setup.

      
                
                
                    
                                                    Wed, 12/10/2025 - 15:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
