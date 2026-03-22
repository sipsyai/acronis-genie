# Massive inbound traffic when backing up server

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/massive-inbound-traffic-when-backing-server

## Original Post
**Author:** Unknown

Massive inbound traffic when backing up server

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
On one of our cPanel servers we're seeing massive inbound traffic (6x more than outbound) whenever a backup is running. 
In the attached screenshots you can see a daily graph (blue is outbound, green is inbound), where you can see the amount of traffic I'm talking about and for how many hours it's going on.
I have also attached a yearly graph where you can see the difference of in/out traffic since we switched from R1Soft to Acronis in December. Same server, same amount of data and backup frequency, but a huge difference in the bandwidth bill.
What's weird is that every backup run for this server takes almost 3 hours. Backups on this (and other servers) is configured to run every 7 hours, but this is the only server were so much traffic is exchanged. 
And I'm very certain that there's not that much difference in the filesystem between every backup run, that could cause such an amount of traffic to be exchanged. Other server with similar amount of data (~600GB) take ~15 minutes for the backup run to complete.
This server is running the same backup plan as the other servers that are not experiencing this.
What can I do to further investigate what all this data is, and why it's taking so long for the incremental backups to finish?
Thanks,
George Tasioulis

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      [33946f980a9eeeda18f5bcc9c4f26e2e]_Screenshot%202019-02-14%20at%2011.49.41.png

                      87.4 KB
                  
              
                      [b6c7f9509ccf7fcf82087f7e135edfc1]_Screenshot%202019-02-14%20at%2011.48.59.png

                      78.29 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 02/14/2019 - 09:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hello George!
 
Sorry for missing out on replies!
 
I can think of only one known root cause for such behavior - enabled Backup Validation https://www.acronis.com/en-us/support/documentation/BackupService/index…
However, you have mentioned that only one partiular server faces this behavior.
As a support team representative, I could not request any details info through Forum, but do submit a support request to our team with the following info so that we could investigate:
 - login name
 - names of the machines and backup plans
 - info from the service provider to which IP addresses the traffic flows to (we'll check if they are Acronis ones)
 
Let me know how it goes!

      
                
                
                    
                                                    Thu, 02/21/2019 - 18:57
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stefan Saeys
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, I am experiencing the same behaviour after moving from Acronis US to EU servers (on the 27th).
Although all backup settings and server content are identical, there is a factor 6 on incoming traffic.
Was the issue above solved?
Thanks!
 
Stefan
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      561392-208234.png

                      39.46 KB
                  
          
    

                    
    
                
                
                    
                                                    Wed, 12/09/2020 - 21:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Stefan.
This issue requires investigation.
Please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Mon, 12/14/2020 - 14:36
