# Problem recovery SQL database from cloud to another PC

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/problem-recovery-sql-database-cloud-another-pc

## Original Post
**Author:** Unknown

Problem recovery SQL database from cloud to another PC

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi when im going from Devices ->SQL->database that i want and choose recover as file, and then i choose another PC to download it i got this error, but if i leave it as is in Source pc's database is downloading fine. I posted an image of error.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      errorSQL.PNG

                      21.74 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/04/2019 - 10:57

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
The issue is likely caused by the fact that the other machine where the download is attempted doesn’t have Agent for SQL installed.
 
To read an Archive containing some specific kind of backup(Exchange, SQL, Office365), a corresponding Agent needs to be installed. From the description and the screenshot, I suspect that the Agent for SQL isn’t installed on the other device. For this reason, Agent can’t read contents of the Archive and reports it like the Archive doesn’t exist.
 
To solve the issue, please install the Agent for SQL on the machine to which the recovery is performed.

      
                
                
                    
                                                    Fri, 01/04/2019 - 13:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
