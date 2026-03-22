# Open *.Tib file [RESOLVED]

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/open-tib-file-resolved

## Original Post
**Author:** Unknown

Open *.Tib file [RESOLVED]

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a job wich backup data locally. I use the vmware agent. I want to restore some files but on the web console it says that the backup agent is not online and I can't access any restore points. 
I have the *.tib files on my NAS but can't open them. I tried with Acronis true image but it doesn't work.
I need the get one folder back, it's quite critical. 
Can you help me ?
Kind Regards,
Kevin

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/31/2016 - 12:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin,
You have 2 options available to restore a local backup:
From web console:
If you have agents online in the web console, go to Backups tab, select the agent which has access to that NAS folder in Machine to browse from and then Browse new location which would be the folder with this *.TIB file. You can then use this agent to restore files from this backup file in a standard way.
Without web console:
Start any VM from a Bootable Media and use it's interface to restore files from the NAS folder.
 
Let me know if you have any questions.

      
                
                
                    
                                                    Thu, 03/31/2016 - 12:50
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kevin Loos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for your help ! I used the first solution and it worked perfectly.
Regards,
Kevin

      
                
                
                    
                                                    Thu, 03/31/2016 - 13:39
