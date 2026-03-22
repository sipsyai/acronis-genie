# VM Replication slowed since server power disruption

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/vm-replication-slowed-server-power-disruption

## Original Post
**Author:** Unknown

VM Replication slowed since server power disruption

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Neil_L
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We had a power outage in our datacentre last week and ever since this happened my VM replications on my own VCentre have ground to a halt.
All servers are up and showing no errors.
I have also tried cancelloing all running jobs and setting up a new local replication and this is also painfully slow - 45 hours plus for 100GB .
I have also tried rebooting the agent server.
Any ideas?
My next move is to reboot everything in the vcentre but that will take some organising.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/27/2017 - 10:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Greetings Neil!
It's Evgeny from Acronis Service Provider Support.
As far as I understand after a power outage the replications of VMs done by Acronis Backup Cloud started running for unacceptably long time.
I will be glad to assist you.
The power outage could have affected the local datastores (connection to them from the Agent or the IO operations). Could you please check the performance of the connection and IO to/from the datastores (QSAN-Backup as well as 3MALING_CT_BKUP_QSAN)? It is also a good idea to check the ESXi server logs - please start off with /var/log/syslog.log which is generally containing useful info for the troubleshooting.
If the issue proves to be related to our Agent, please gather the debug logs per our KB 57128 and reproduce the issue. After that please contact us via mail - mspsupport@acronis.com with reference to this thread. We will collect the sysinfo from the Agent and investigate it further. 
 
If you have other questions, please feel free to reach out to our Support.
Evgeny Ryuntyu | Expert Support Engineer
Acronis | Dolgoprudnenskoe shosse 3, Moscow, Russia 141700
 
 

      
                
                
                    
                                                    Wed, 11/29/2017 - 08:45
