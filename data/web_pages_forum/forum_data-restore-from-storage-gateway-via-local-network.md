# Data Restore from Storage Gateway via local network

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/data-restore-storage-gateway-local-network

## Original Post
**Author:** Unknown

Data Restore from Storage Gateway via local network 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ragesh KC
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello 
We have two IPs configured on our storage gateway server, one for external internet connectivity and another one for internal data traffic. We have followed the below steps, to get the data restored from our storage gateway server quickly ( vial local network interface) but we still see the restore traffic goes all the way to
public IP ( internet ) instead the local network interface which is making our data restore to in-cloud very slow. 
Please let me know if there is any alternate way that i can browse to storage gateway with local IP address and restore the data fast 
Acronis Storage GW can listen on all IPs attached to GW VM. You can direct Agents traffic by DNS.
1.	User should configure 2 different DNSs records with the same DNS name: one for local DC network DNS and one for the global DNS. For example: backups.my.cloud -> 10.0.0.1 for DC connections and backups.my.cloud -> 8.9.20.33 for the other Internet users.
2.	Check that resolving works correct. 10.0.0.1 for DC and 8.9.20.33 for other world.
3.	Configure GW node. Create GW VM with both network links and IPs. For example: 8.9.20.33, 10.0.0.1
4.	Put 0.0.0.0 in the IP section of the GW configuration
5.	Register backups.my.cloud address of GW in Backup Cloud.
Thanks,
ragesh

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/07/2016 - 18:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ruben Gilja
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
As far as I know the best option is to try out Acronis Web Restore Tool, https://kb.acronis.com/content/57596
That was what the support gave me when I asked the same question. The restore time is unbearable when it comes to large data if you cant use the local network to restore. I havent tried the tool myself yet since it required more steps than the KB covered.

      
                
                
                    
                                                    Mon, 10/10/2016 - 20:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ruben Gilja
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I have tried this tool myself now, and the restore times are much better. I don't know if you have looked at the Tool, but you need to open some ports for Acronis Backup Cloud to reach the Web Restore Tool obviously. BUT, you can also reach this tool by using the local IP, it lets you login and download your data. I dont know if this is possible by design, or just a nice coincidence. 
My public DNS name for the Acronis Storage Gateway, resolvs to its local IP internally on the Gateway server and the Web Restore Tool server, so that might also be the reason it works. 

      
                
                
                    
                                                    Fri, 10/28/2016 - 12:24
