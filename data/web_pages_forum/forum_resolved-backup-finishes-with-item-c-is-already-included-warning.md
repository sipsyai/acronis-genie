# [RESOLVED] Backup finishes with “Item 'C:/' is already included” warning

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/resolved-backup-finishes-item-c-already-included-warning

## Original Post
**Author:** Unknown

[RESOLVED] Backup finishes with “Item 'C:/' is already included” warning 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Stefan Zweig
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi guys,
 
I have file-level backup task, which seems to be completed successfully, but it throws a warning message “Item 'C:/' is already included”. What am I doing wrong? What will happen if I try to recover this backup, considering that I receive this warning?
 
Stefan

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/29/2016 - 16:51

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andrey Zonov
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Stefan,
 
Don’t worry, this is just a warning message which usually means that two folders ‘C:\Documents and settings’ and ‘C:\Users’ are included in one backup plan. It can happen if you upgrade from Windows XP or Windows Server 2003 to a newer OS – in that case old ‘Documents and settings’ is moved by operating system to ‘C:\Users’. So, the first folder becomes a link to a second folder, which has been already included to the backup plan. That is why you receive this warning message.
 
To get rid of this message, you can simply remove folder ‘C:\Documents and settings’ from the backup plan. And yes, your backup is healthy for recovery even with this warning message.
 
__________________
 
Andrey Zonov
Acronis Customer Central | Acronis Backup Software
For more answers to your questions, try our Knowledge Base and Video Tutorials
Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

      
                
                
                    
                                                    Fri, 04/29/2016 - 17:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stefan Zweig
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Removed the folder as suggested - seems like it did the trick, thanks

      
                
                
                    
                                                    Sat, 04/30/2016 - 14:37
