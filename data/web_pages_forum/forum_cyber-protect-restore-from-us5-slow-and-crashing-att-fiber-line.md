# Cyber Protect restore from US5 Slow and Crashing ATT Fiber line

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-restore-us5-slow-and-crashing-att-fiber-line

## Original Post
**Author:** Unknown

Cyber Protect restore from US5 Slow and Crashing ATT Fiber line

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jerimy Roque
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Posting this as not sure where to go with this.   But we can replicate it on two types of Firewalls.  UDM Pro and Fortinet
Layout;
ATT Fiber - 5,000 mbs > Unifi DM > internal network > Computer doing restore
-- on this example, we are only getting about 30 mbps and will crash the ATT network.  Network is stable until we        start the Restore then it works for a bit only to drop the internet on the entire line.
-- ATT modem is bridge mode straight through, no policies on the modem.  No filtering of any Kind.  That is handled  by the UDM.  We are getting max speeds on this network but when we start a restore it works then internet drops.
-- We have tried to reduce the Link Speed from 5000 to 2500 and finally to 1000 mbps all with the same results.  Get about 30mps down then internet crashes.  All other equipment runs at full speed until we start the restore regadless of the link speed. 
So --
We build a network going from the ATT modem with a 1000 mbps link to a Fortinet Firewall then straight out to the computer.  Nothing in between, all links show 1,000 full.  Same thing internet bounces between 20-30 mbps and crashes the internet.
So two questions.  
1. is 30mpbs down the max that US5 can give?
2. Why would doing a restore from Acronis crash the ATT fiber line?
Scratching my head over this.  Especially the line losing internet, that makes absolutely  no sense.  As we can transfer TB's of information on the same UDM network configuration to Wasabi, at way way higher rates.
Also curious if anyone else on here has had anything similar to this with ATT fiber.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/23/2024 - 14:56

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Thank you for contacting us.
Many factors can affect speed, from network issues to local machine and disk overloads. The network speed contracted with your provider isn't necessarily the same when you connect to the datacenter.
You can run the connection tool to check the connections and the speed towards the datacenter: Acronis Connection Verification Tool.
You should check the average data read/write speeds in the output, for example:
Average write speed: 5.96219 MB/s
Average read speed: 22.113 MB/s
Please note that if you are performing full backups of large quantities of data, it is expected to consume significant resources. You should consider splitting the backups and scheduling them at different times so they won't all execute simultaneously.
Additionally, for recovery of large backups, you could try the large-scale recovery and download the backup directly via CMD: Acronis Large Scale Recovery.
Regarding the line crash, you should raise a ticket with the team or request your Service Provider to do so. This is not expected behavior, and you should provide evidence so the team can investigate and assist you: Acronis Support Ticket.
Best regards.

      
                
                
                    
                                                    Thu, 05/23/2024 - 16:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
