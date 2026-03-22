# Info for Post-Restore. Guide, How-To or any docs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/info-post-restore-guide-how-or-any-docs

## Original Post
**Author:** Unknown

Info for Post-Restore. Guide, How-To or any docs

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Giorgio Virginio Pietro Sommaruga
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have two production servers, managed by Cyber Protect.
I would like to do a test restore to verify that everything is working properly.
However, I have some doubts that I will try to explain here by taking one of the two servers as an example.
The "Donald Duck" server:
has its own public IP reachable from the Internet
there is a Plesk installed
there are portals installed (remember, in production) registered in the DNS and reachable from the Internet
Now I activate a new server "Mickey Mouse"; this too has an IP reachable from the Internet and has Plesk, without portals or services.
I'm going to restore on this and therefore I expect to have the "Donald Duck" replica at the end.
How then do I test this new "Donald Duck 2"
The IP is managed by the ISP and even by momentarily deactivating "Donald Duck 1", all Internet references point to the IP of "Donal Duck 1" and therefore would never reach "Donald Duck 2"
Are there any guides to manage this scenario which seems to me to be common in many other business contexts?Of the "White papers", of the "How to..."
Thanks in advance for any suggestion.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 08/18/2023 - 08:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum!
In your described situation, where you want to test a restore of your "Donald Duck" server onto a new server named "Mickey Mouse," there are a few considerations to keep in mind, especially when dealing with public IP addresses, DNS records, and accessibility from the internet.

Isolation Environment for Testing: To perform a test restore without affecting your production environment, it's recommended to set up an isolated environment where you can restore the backup and test the functionality without impacting your live systems.


Change Hostnames and IPs: Since you're restoring onto a new server ("Mickey Mouse"), it's important to ensure that the restored "Donald Duck" server has a new hostname and IP address. This prevents conflicts with the original production server. Adjust the hostname and IP configuration during or after the restore process.


DNS and Firewall Configuration: As you rightly pointed out, DNS records and firewall configurations might still be pointing to the original "Donald Duck" server. To test the restored server ("Donald Duck 2"), you might need to adjust the DNS records temporarily and reconfigure any firewall rules to route traffic to the new server's IP address.


Temporary Network Configuration: In order to avoid conflicts and ensure isolation, you can temporarily disconnect the new server ("Mickey Mouse") from the network before bringing up the restored "Donald Duck 2." This will allow you to verify the functionality of the restored server without affecting your live environment.


Documentation and Communication: It's crucial to document the steps you're taking and communicate with your team, especially if multiple people are involved. This helps ensure consistency and clarity during the testing and restoration process.

While there might not be specific whitepapers or how-to guides tailored to your exact scenario, the general principles of isolated testing, changing hostnames and IPs, and adjusting network configurations are commonly followed best practices.
Should you encounter any technical challenges during the process, don't hesitate to reach out to Acronis Support. They can provide more tailored assistance based on your specific environment and setup. https://kb.acronis.com/content/8153
Remember that every environment is unique, so adjustments may be needed based on your specific network setup and requirements. 
Thanks in advance!

      
                
                
                    
                                                    Mon, 08/28/2023 - 15:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
