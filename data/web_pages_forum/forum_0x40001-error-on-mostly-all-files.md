# 0x40001 Error on mostly all files

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/0x40001-error-mostly-all-files

## Original Post
**Author:** Unknown

0x40001 Error on mostly all files

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ramon
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone
We have some frustrating errors in a backupjob of a customer.
Pretty much every file cant be backed-up because of a error with the id 0x40001.
All files are saved on an Synology NAS mapped on an Windows Machine with the IP.
NAS/backup"host" and the Win/Mac Clients supports SMB3
The error appears when some of the Mac OSX users edit an folder. After this event, mostly all and also untouched files cant be saved with the following log-result:
0x40001: Fehler beim Lesen der Datei.
| Zeile: 0xfba06f330018d90d
| Datei: e:\72\file\ntstream_chunker.cpp:244
| Funktion: ChunkNTBackupStream
| $module: disk_bundle_vsa64_4670
|
| Fehler 0x40001: Fehler beim Lesen der Datei.
| Zeile: 0xfba06f330018d84f
Also I dont know what is meant with the partition "e:" in the filepath of the log. There is no such partition on our side.
 
Thanks for your help.
Greetings
Ramon Egger

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 05/11/2018 - 14:36

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ramon,
If the issue occurs exactly at times when the files to back up are in use, then this behavior is likely to be caused by the limitation I mentioned in the earlier post. Network shares are always backed up on a file-level which means the snapshot is not being created before starting the backup process. Without the snapshot data is captured on the fly and therefore all files locked by another processes will be skipped. Difficult to say without the more in-depth analysis why the folder is locked, could be NAS settings or another apps leaving their locks in the target location. I'd suggest opening a support ticket to find the root cause. 

      
                
                
                    
                                                    Wed, 05/16/2018 - 08:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
