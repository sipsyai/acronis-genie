# How to connect different local networks in a site to site DR

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-connect-different-local-networks-site-site-dr

## Original Post
**Author:** Unknown

How to connect different local networks in a site to site DR

        
  



    
  


  
          
  
    Tutorial
  


          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jose Luis Perez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Configured site to site Disaster Recovery with 3 networks on the local site. The three networks added to the appliance and registered do not communicate among them (a server in network 192.168.4.0 cannot reach a server or laptop on network 192.168.10.0 nor 192.168.8.0 from / to the DR server). 
Is there something missing?
Thanks in advance

      
                                            
                
            
                            
                    
                        
                            
                              Mon, 02/10/2025 - 18:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  





            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to our forum.
Here are some key things to check to ensure proper communication between your three networks (192.168.4.0, 192.168.10.0, and 192.168.8.0):
1. Check the Virtual Network Configuration in the DR Cloud Console
Go to the Disaster Recovery section in the Acronis Cyber Protect Cloud console.
Check the Networks tab under the DR site.
Ensure that all three networks are correctly added and mapped.
Verify that inter-network communication is enabled. Some DR configurations may isolate networks by default.
2. Configure Site-to-Site VPN Settings
If you are using a VPN for DR (e.g., IPsec, OpenVPN, or SSL VPN):
Ensure the VPN configuration includes all three networks.
If the VPN only routes a single subnet, add static routes for the missing networks.
Check if NAT is applied—if so, ensure proper exceptions are made.

3. Check Firewall Rules
Acronis DR allows setting up firewall rules in the Disaster Recovery Appliance.
Navigate to Networking > Firewall Rules in the DR appliance.
Ensure there are allow rules for communication between the three networks.
If using custom security groups, verify that they allow traffic between the subnets.
4. Validate Routing Configuration
Open a terminal or command prompt and try traceroute (tracert on Windows, traceroute on Linux/macOS) between machines in different networks.
If routing fails, add static routes to your DR appliance:
Example: 192.168.4.0/24 → 192.168.10.0/24
Add similar rules for other networks.

5. VLAN and Subnet Settings
If VLAN tagging is used, ensure all three networks are properly tagged.
Some environments separate VLANs by default, requiring inter-VLAN routing.
6. Verify Local Network Configuration on Your Devices
Check that each server/laptop:
Uses the correct gateway IP (likely the DR appliance).
Has no conflicting firewall rules blocking inter-subnet traffic.

7. Restart the DR Appliance
If changes were made, restart the Acronis Disaster Recovery Appliance to ensure settings apply correctly.
If the issue persists, please contact our support so we can review the issue with you. If you under another reseller or service provide kindly ask them to raise a ticket.
Best regards.

      
                
                
                    
                                                    Tue, 02/11/2025 - 09:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                            
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jose Luis Perez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Jose Pedro,
I´ll check all that. On the other hand, I was thinking... In order to add the NICs to the appliance we created three separate vswitches each with its own vNIC. I´m guessing the three NICs need to be in the same vswitch so they can communicate with each other. I´ll try that too.
The appliance is running on VMWare ESX. I´ll update this later today hopefully - I rely on customer availability.
 

      
                
                
                    
                                                    Tue, 02/11/2025 - 12:05
