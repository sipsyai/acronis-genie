# Prognosis for remaining Backup Time comletely broken

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/prognosis-remaining-backup-time-comletely-broken

## Original Post
**Author:** Unknown

Prognosis for remaining Backup Time comletely broken

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    E. Blos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Backup Monitor shows a prognosis of a few minutes when beginning a backup.
This prognosis is not correct and increases to several hours by the time the backup is running.
It is failing completely and does not allow to estimate the remaining time at all.
A ten year old child would be able to calculate the remaining time if it knows the data size and bandwidth, so Acronis Engineers are not able to do that?
Are you kidding me?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/08/2017 - 20:18

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
My name is Eugene.
I'm from Acronis Service Provider Support team.
Let me inform you that exact backup progress estimation is really raising questions by current design.
Generally backup progress depend of: data size, available disk IOPS, available HW and bandwidth resources.
Since backup process is more like creating a ZIP archive, then accurate time estimation depend even on zlib algorith, where compression is used. ( KB https://kb.acronis.com/content/16791) 
Good news is that Acronis Backup Cloud developers are working on making smooth backup and recovery progress and precise time estimation.
This is expected to be implemented in Q1-Q2 2018 ( check for ABR-104719 in changelog)
Hope that answer your query.
I am always at your service should you have any further questions.

      
                
                
                    
                                                    Wed, 08/09/2017 - 13:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
                    In reply to Hello!… by Eugene Tanasiev
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    E. Blos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank You.

      
                
                
                    
                                                    Sun, 08/13/2017 - 22:22
