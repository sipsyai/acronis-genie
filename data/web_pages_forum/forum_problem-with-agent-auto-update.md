# Problem with Agent Auto Update

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/problem-agent-auto-update

## Original Post
**Author:** Unknown

Problem with Agent Auto Update

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    DominikD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
today we wanted to update all our Backup Cloud Agents to the new 4560 build. But it failed on about 80% of our servers. i investigated the logfiles and saw the following line in the log on all affected servers:
Jan 29 17:01:19 ns1 acronis_mms[31054]: #033[0m2018-01-29T17:01:19+0100 linux_agent ERROR: Lock file /tmp/trueimage_inst.lock is found. Installer is running already.
The trueimage_inst.lock has a file date of Jan 15. That was the exact the we succesfully upgraded to Agent build 4500. Seems this 4500 update left a installation lock file which was not removed.
How can this happen? This is a HUGE problem, as we now need to login in almost all servers and remove the lock file manually. All affected systems are running a Debian Linux.
Greetings,
Dominik

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 01/29/2018 - 20:08

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dominik,
Fedor here.
Thank you for a good description of the issue.
It matches to what we have uncovered in the recent time, this is a known issue.
Upgrading to 4560 manually would lift up the lock. Apologies for I understand the impact of the issue.
There aren't any known workarounds that would ease the resolution.
Please log a support case with Acronis with reference to this forum article and mention the id of the issue - ABR-152138

      
                
                
                    
                                                    Mon, 02/05/2018 - 15:59
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
