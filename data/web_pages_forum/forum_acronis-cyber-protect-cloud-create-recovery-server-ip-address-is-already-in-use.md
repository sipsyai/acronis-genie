# Acronis Cyber Protect Cloud - Create Recovery Server - IP address is already in use

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cyber-protect-cloud-create-recovery-server-ip-address-already-use

## Original Post
**Author:** Unknown

Acronis Cyber Protect Cloud - Create Recovery Server - IP address is already in use

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Manos Pantelidakis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good Day,
You may be able to advise on the following issue we face as we test failover and DR in our Acronis Cloud subscription/environment:
As you will see in screenshot below, when we try to create a recovery server (as part of a test failover) for one of our servers that is is protected/backed up to cloud, we see the error message that the IPaddress of the server in production network (192.168.1.1) is already in use.
We don't have any other VM / recovery server on the cloud so we suspect that the IP address is in use by the VPN gateway that is setup to allow VPN connections in order for someone to access the DR environment...
Is this correct at your opinion? Is there a way to change the config of the vpn gateway in order to not user IP address 192.168.1.1 as for us it is critical to have the same IP address for the Recovery Server as the one at the production network?


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/28/2023 - 09:11

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please refer to the following information: 
https://www.acronis.com/en-us/support/documentation/DisasterRecovery/#c…

Specify the IP address that the server will have in the production network. By default, the IP address of the original machine is set.
If you use a DHCP server, add this IP address to the server exclusion list in order to avoid IP address conflicts.
If you use a custom DHCP server, you must specify the same IP address in IP address in production network as the one configured in the DHCP server. Otherwise, test failover will not work properly, and the server will not be reachable via a public IP address.

If the issue persists and those pre-requisites are fulfilled please raise a ticket with our support or request your service provider to do it: https://kb.acronis.com/content/8153
Best regards!

      
                
                
                    
                                                    Thu, 09/28/2023 - 11:10
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Manos Pantelidakis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
Thank you for your answer but this is not our case, we do have the guidelines to create a recovery server and the Acronis documentation is very clear and helpful.
We need to know whether specific IP address 192.168.1.1 can be available / free in the cloud / DR network in order to be used by a Recovery Server which already is in use in production nettwork.
Thanks and Regards,
Manos

      
                
                
                    
                                                    Thu, 09/28/2023 - 11:43
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello.
So I assume the following pre-requisite is fulfilled right? ** If you use a DHCP server, add this IP address to the server exclusion list in order to avoid IP address conflicts. **
First, confirm that the IP address 192.168.1.1 is indeed in use by your VPN gateway. You can do this by checking the configuration of your VPN gateway and ensuring that it's using this IP address.
If the VPN gateway is indeed using 192.168.1.1, you will need to reconfigure your VPN gateway to use a different IP address that doesn't conflict with your production network.
Please also note that when you use the VPN gateway all the machines in the production and test networks get the network configuration (IP addresses, DNS settings) via DHCP. Every time a cloud server will get the same IP address from the DHCP server. If you need to set up the custom DNS configuration, you should contact the support team. https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Thu, 09/28/2023 - 13:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Manos Pantelidakis
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
Thank you again for your answer and suggestions!
I tried reconfiguring / editing the VPN gateway but unfortunately it seems that the IP address of the gateway cannot be changed, it is there by default / design, if someone chooses network 192.168.1.0/24 the gateway will always be 192.168.1.1 and cannot be edited.
See screenshots below:



      
                
                
                    
                                                    Fri, 09/29/2023 - 15:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thanks for the details.
Seems we need to add our DR experts in the case to help you configuring the primary server.
Please raise a ticket or ask your service provider to do it so we can take a session with you and check it.
Best regards.

      
                
                
                    
                                                    Mon, 10/02/2023 - 12:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
