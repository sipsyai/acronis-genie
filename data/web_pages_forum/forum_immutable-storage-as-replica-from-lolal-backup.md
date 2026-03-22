# Immutable storage as replica from lolal backup?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/immutable-storage-replica-lolal-backup

## Original Post
**Author:** Unknown

Immutable storage as replica from lolal backup?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Marek Gwozdz
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 30
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                
                    
                        
            could  be immuable storage as replica from local backup?
F.e.  i have reblica incremental, and i could delete some dates or backups from local sorage.   would immutable storege keep these days?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/09/2024 - 13:17

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Marek.
If the replica is saved as a backup, yes, the immutable storage is applied to all backups if they meet the requisites mentioned in this user guide: 
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect…
https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_16/#immutable-storage.html#kanchor836.
Thanks.

      
                
                
                    
                                                    Thu, 05/09/2024 - 13:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marek Gwozdz
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 30
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            To be clear. I heve on premises acronis infrastructure. And i have acronis cloud license

i want to replicete from local to cloud and use cloud as immutable.
I have found article that it is possible and use infrastrucrure only as a a backup gateway
"This guide describes how to deploy Acronis Cyber Infrastructure on a single node with the sole purpose of creating Backup Gateway endpoints."Introduction – Acronis Cyber Infrastructure 5.4 – Backup Gateway Quick Start Guide
Is it working that way?
Thefirst  question if acronis Infrastructure used as a gateway needs additional licenses?

The second question - are there oteh possibilities?
F.e. I see my cloud location from local installation and can replicate to it.
If i buy one cloud licence and set the same  cloud storage as immutable from cloud console - would be my replicas from local became immutable?
 
 

      
                
                
                    
                                                    Thu, 05/16/2024 - 12:53
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Marek Gwozdz wrote:

To be clear. I heve on premises acronis infrastructure. And i have acronis cloud license

i want to replicete from local to cloud and use cloud as immutable.
I have found article that it is possible and use infrastrucrure only as a a backup gateway
"This guide describes how to deploy Acronis Cyber Infrastructure on a single node with the sole purpose of creating Backup Gateway endpoints."Introduction – Acronis Cyber Infrastructure 5.4 – Backup Gateway Quick Start Guide
Is it working that way?
Thefirst  question if acronis Infrastructure used as a gateway needs additional licenses?

The second question - are there oteh possibilities?
F.e. I see my cloud location from local installation and can replicate to it.
If i buy one cloud licence and set the same  cloud storage as immutable from cloud console - would be my replicas from local became immutable?
 
 


Hello!
The Cyber Infrastructure is a paid Add-on.
You can fill this form in order to know more details: https://www.acronis.com/en-eu/products/cyber-infrastructure/trial/ 
No, local backups can't be immutable. Just the backups stored in the Cloud. Just the replica to the cloud will become immutable.
Best regards.

      
                
                
                    
                                                    Fri, 05/17/2024 - 06:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marek Gwozdz
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 30
                
            
            
                
                    Comments: 42
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I wanted to only replicated backups will be immutable not local.
I have managed to do this by logging to cloud console and set immutable there.
Now i thing replicated copies of backups will be immutable.

      
                
                
                    
                                                    Fri, 05/17/2024 - 12:56
