# Backup plans for  1 TB size jobs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-plans-1-tb-size-jobs

## Original Post
**Author:** Unknown

Backup plans for  1 TB size jobs

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
What would you say is best practise when it comes to larger backups over 1 TB
Im talking files
 
Woulld you split it up in several jobs?  Im thinking about the long time to get the first full backup
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 02/25/2016 - 17:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fredrik,
Here you have at least 4 options on how to proceed:
1) Create one backup plan for all 1 TB. Acronis Backup Cloud technology allows you to interrupt backups (both intentionally and accidentally) while keeping the already backed up part in the cloud. When backup plan is started again it checks what has already been backed up (takes some time too) and then proceeds with the remaining part until full backup is uploaded. You can check how much data is already in the cloud for your backup plan by browsing Web Restore (download files recovery option) and checking Interrupted backups option.
Advantage: minimal effort for setup
Drawback: no recovery is possible until first full backup is done
 
2) Create one backup plan for initially just small part of your data. Once the first full backup is done, modify the plan and append more source data to it. Thus you can do it gradually in shorter periods of time.
Advantage: recovery is possible after first quick full backup
Drawback: high effort to setup until all is done
 
3) Create different backup plans for different parts of the data.
Advantage: quick first backup of most important data
Drawback: high effort to setup and manage afterwards all the different plans
 
4) Use the Initial Seeding feature if you have a fast connection to the cloud storage from a different machine. Here are a couple of articles on how to use it and how to set it up.
Advantage: quick upload of any large backup
Drawback: high effort to set up and need to physically transfer the media with data
 
I'm sure one of the options would be perfect for you. Let me know if you have any questions.
Best regards,

      
                
                
                    
                                                    Thu, 02/25/2016 - 20:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.
