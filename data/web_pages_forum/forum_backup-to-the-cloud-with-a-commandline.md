# backup to the cloud with a commandline

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-cloud-commandline

## Original Post
**Author:** Unknown

backup to the cloud with a commandline

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Voogy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello all,
I try to create a backup script on my workstation to backup a local directory to the cloud.
I'm not sure if i understand the acrocmd help file completely, so far I created the next commandline:
acrocmd.exe backup file --include=c:\test --loc=online:// --credentials="MyLogin",MyPassword --arc=test_archive
In my cloud management console i see the next error:
Failed to create temporary file 'test_archiveF.TIB.meta299FEC4E-BC59-3A29-8B48-479582627501.tmp
MyLogin has admin rights
Any ideas ?
Thanks,
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 02/24/2017 - 16:17

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vyacheslav Bykov
                            

                            
                    
                        Cloud SP Trainer
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Does the command line throw any error message after you execute your acrocmd command? If so, please paste the full error message here. Also, share the picture of the error you see under management console. 
And last, please share the "MyLogin" name.

      
                
                
                    
                                                    Mon, 03/06/2017 - 13:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Vyacheslav Bykov
Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Voogy
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
I just tested the commandline again, but now explicitly with run as administrator. this solved my problem.
thanks,
 

      
                
                
                    
                                                    Mon, 03/06/2017 - 14:52
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
