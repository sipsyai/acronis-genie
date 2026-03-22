# We changed backup destination - now getting errors about old destination

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/we-changed-backup-destination-now-getting-errors-about-old-destination

## Original Post
**Author:** Unknown

We changed backup destination - now getting errors about old destination

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    David Cocke
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            For several of our customers (tenants), we recently installed a new NAS to replace ones that are to be retired.  In each case, we gave the new NAS a new IP.  We then changed the backup plans to change the URL to the new NAS and provided the needed credentials.  The backups are working correctly to the new destination. 
We then removed the old NAS from the Backup Storage section within the Acronis Cloud Console.  Now, everyday each computer is attempting to refresh the recovery points, but giving an error about the old NAS URL.  You can also invoke this error by manually going to a particular machine, go to the Recovery section and using the Refresh icon in the upper right corner.
We've also found that the details about this NAS destination (old and new) are stored in XML files found here: c:\ProgramData\Acronis\BackupAndRecovery\MMS\Locations\ but even deleting the file that contained the old NAS and restarting the machine, the errors continue and it still is looking for the old destination.
Attached is a sample of the error message.
Does anyone know how we get the clients to forget this old destination?

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2021-01-04_15-08-46.jpg

                      85.46 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/13/2021 - 19:54

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello David.
This issue requires investigation.
Please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Mon, 01/18/2021 - 14:08
