# Installing linux agent in another directory

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/installing-linux-agent-another-directory

## Original Post
**Author:** Unknown

Installing linux agent in another directory

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
I have a linux server that the / partition is almost full, and when it starts to back up, I believe because of the logs, the partition gets full. Can I install the backup agent in another directory? Like at home for example? Because the home is in another partition.
 
Thanks

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 09/03/2018 - 15:18

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
It's Evgeny from Acronis Service Provider Support.
 
As far as I understand you are facing an issue with the root partition getting full when you start the backup. You would like to know if the Agent can be installed in another directory.
The Agent has multiple options for the installation configuration which you can see in the following article, but the design of the installer does not allow you to choose another directory for storing the logs.
 
Thinking of this further, let's address the root cause - partition getting saturated during the backup.
In Acronis products we utilize the snapshot technology to create a consistent backup and during the backup a temporary file is created to allow the operation to happen.
Please check the following article of the Knowledge Base that describes the temp file and also provides a solution to change the default folder where this file will be created. See the point "For Acronis Backup Cloud / Acronis Backup 12.5"
 
Let me know if this actually resolves the issue.
If you have other questions, please feel free to ask. 
 
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Tue, 09/04/2018 - 07:29
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the answer.

I did the link procedure, I made the "config" file with the address, but it still did not work.

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      460448-151926.png

                      15.37 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 09/04/2018 - 19:14
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted
