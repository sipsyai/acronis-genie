# Drive Exclusions

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/drive-exclusions

## Original Post
**Author:** Unknown

Drive Exclusions

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Antonios Throuvalas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I have a windows server with an attached storage containing almost 2 TB of Data. I try to setup a system backup of this server, which would exclude the entire drive in question. Adding "D:" in the exclusions list does not exclude the drive, drive D is also included in this backup.
How should I define the string in order to exclude a whole drive? Would eventually "D:*" do the trick?
Thank you in advance.
Regards,
Antonios
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/18/2016 - 13:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raphael
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 37
                
            
            
                
                    Comments: 352
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Antonios,
you can use "D:\*" as file exclusion string. It will show drive D: in the backup archive, but will have no content.
 

      
                
                
                    
                                                    Sat, 11/19/2016 - 12:20
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect
