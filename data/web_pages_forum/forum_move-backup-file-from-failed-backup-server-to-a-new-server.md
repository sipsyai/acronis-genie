# Move backup file from failed backup server to a new server

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/move-backup-file-failed-backup-server-new-server

## Original Post
**Author:** Unknown

Move backup file from failed backup server to a new server

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Ok. So let's say a customer is backing up their servers using the Acronis Backup agent but using their own dedicated server to store the Acronis backup data, what to do if the dedicated server hosting the backups crashes/dies...
 
If the server crashes/dies then all data is lost, and the customer would need to backup all the data from scratch again, but that is no good as they'd lose months of backups.
The customer could sync the Acronis backup data from one dedicated server to another dedicated server, but is there an easy way to have a switch which server the Acronis backup data is loaded from, if that makes sense?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 10/09/2020 - 13:35

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Victor Nikoulin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
it is indeed wise idea to have additional copies of backups as nowadays malware search and destroy backup archives. 
It is possible to use Replication in order to have another copy (See https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…)
OR
Archives can be copied to alternate location using other tools 
If customer needs to recover data from another dedicated server then please  use "Add location" feature of "Backup Storage" section.

Victor Nikoulin

      
                
                
                    
                                                    Wed, 10/14/2020 - 06:22
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Looks like that'll do it.
 
Thanks Victor Nikoulin.

      
                
                
                    
                                                    Wed, 10/14/2020 - 19:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You might also want to check out running your own Acronis Cyber Infrastructure cluster, as it provides data redundancy from backup node failures.
https://dl.acronis.com/u/software-defined/html/AcronisCyberInfrastructu… 

      
                
                
                    
                                                    Mon, 10/19/2020 - 09:41
