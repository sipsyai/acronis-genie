# Compression level

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/compression-level

## Original Post
**Author:** Unknown

Compression level

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Fredrik
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 8
                
            
                                                        
    
    
        
    


                
                
                    
                        
            cant find n option when it comes to Compression levels.
Is there an option?
What is the default Compression level in percentage in the cloud?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 12/20/2015 - 06:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fredrik,
Compression level cannot be changed and is by default set to "normal". Higher compression rates do not give big advantage on backup size, but do influence performance a lot, this is why this feature is not yet present in the product, but is planned for future versions.
Compression ratio depends on source data, for SQL database it's ~30%.
Best regards,

      
                
                
                    
                                                    Mon, 12/21/2015 - 07:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    r schon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Beginner here. My first attempt to backup desktop to portable drive using default compression shows 741GB backedup (TI 2016)but external shows 359GB. That's 50 percent. What can I check to determine if the full backup was successful?
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      380303-132190.jpg

                      158.85 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 08/02/2016 - 18:34
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bobbo_3C0X1
                            

                            
                    
                        Forum Hero
                    
                
            
                        
                
                    Posts: 70
                
            
            
                
                    Comments: 8331
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            r schon,  the 741Gb you see is the total size of all backups for that job.  If you have not manually deleted backups in Windows file explorer, if you navigate to your backup folder, right click and look at properties, it should equal about 741Gb.
A full disk backup should be roughly about 30% smaller than the total used space of what's on your main OS drive.  It will vary though, depending upon what items you have filtered out (there are default exceptions in Windows for things like pagefile.sys, hiberfile.sys and more.  I will say, that you want to look and check those exclusions and remove some of them - for insance, Chrome settings - yeah, those may have your favorites!  Then, Acronis uses compression by default, so it will shrink the backup as well.  Not all files can be compressed though - pictures and videos are already compressed so you won't save much space on those particular types of files.
Ultimately, if you really want to know what's in your backup... restore it to a different disk and check it out.  Replace it with the original drive and make sure it boots if you too a full OS disk backup.  That is the best way to determine that the backup is not only good, but also has everything you expect it to have.  DO NOT test on your main drive though - why take the risk?
Short of that, you can double click on a backup .TIB file and it should open in Windows file explorer where you can navigate the contents and check for files/folders.  You can also right click the backup .tib file and "mount" as well.  This will mount it as a drive letter and you can navigate it that way too - probably faster once mounted. 

      
                
                
                    
                                                    Tue, 08/09/2016 - 03:38
                                                                            
                                
                            
                                            
                                            
    
                    
                (01). MVP WinPE Builder              (02). MVP LogViewer
(03). MVP Google Drive                 (04). Cleanup Utility
(05). Cloning Correctly                  (06). Clone vs Backup
(07). Community Tools                 (08). Contact Support
(09). Product Documentation    (10). OS MBR vs UEFI
(11). BOOT MBR vs UEFI               (12). Common OEM Drivers

            
                            
                Products: 
                True Image / Snap Deploy / Revive / Disk Director
