# Restoration of Licensed Software

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/restoration-licensed-software

## Original Post
**Author:** Unknown

Restoration of Licensed Software

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Pranab BG
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We use Acronis Cyber Cloud for your Company. Recently, one of our Computers crashed. I want to know, if we had taken backup of "Entire Machine", could Acronis Cyber Cloud have restored all data + Licensed Software and applications that were installed on that machine? For e.g. We had a paid version of a video editing software. Will Acronis Cyber Cloud restore the software along with the license? Does "Entire Machine" mean Image Backup?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/26/2019 - 12:12

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bobbo_3C0X1
                            

                            
                    
                        Forum Hero
                    
                
            
                        
                
                    Posts: 70
                
            
            
                
                    Comments: 8331
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I don't have that particular backup application.  However, backup images that contain the entire OS disk, when restored, should be "exactly" like the original system in most cases - as this is how it works with True Image, SnapDeploy and Backup 12.X products. 
Only if you are changing hardware (motherboards), do certain software applications sometimes not license, but that's due to the application having its own checks and balances (many that are proprietary or unknown to the user) to make sure you're not trying to install the software on multiple machines.
"Entire machine" usually means that your backup task will backup all internal disks in a computer under a certain job.  Another option to use could be to do a disk or partition backup, which only backups up the specific physical disks (or partitions) that you specifically choose.
-------------------------
I usually don't use "entire machine", but instead, prefer to use the Disk backup so that I can specifically  choose the physical disk or a physical array if using a RAID setup and always no exactly what I'm backing up in each dedicated backup task.  That's a personal preference, but I don't like having multiple disks with different types of data in one backup.  Although it might sound convenient to backup everything in one job, it may be more trouble when it comes time to restore if you only need/want to restore portions of the content within that one job - KISS - Keep it Simple Silly, is very practical when it comes to backup and recovery.  The more you squeeze into one backup job, the less simple it becomes when it comes time to restore. 
Plus, by backing up all disks in one job, that means the backup will take longer and the recovery will take longer because you have to wade through all of the content in that backup - even if you exclude some of it in the recovery.
Instead, if you break each backup job out by physical disk, then you can schedule your backups as needed and when it comes time to recover, then you only have to deal with the particular disks needed.

      
                
                
                    
                                                    Thu, 09/26/2019 - 17:36
                                                                            
                                
                            
                                            
                                            
    
                    
                (01). MVP WinPE Builder              (02). MVP LogViewer
(03). MVP Google Drive                 (04). Cleanup Utility
(05). Cloning Correctly                  (06). Clone vs Backup
(07). Community Tools                 (08). Contact Support
(09). Product Documentation    (10). OS MBR vs UEFI
(11). BOOT MBR vs UEFI               (12). Common OEM Drivers

            
                            
                Products: 
                True Image / Snap Deploy / Revive / Disk Director

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Pranab BG
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi @Bobbo_3C0X1 Thanks for that explanation.
I'm however, still a little bit unsure, whether taking a backup of "Entire Machine" backs up system registry as well, which means including Software and their associated licenses.
Hoping someone at Acronis Support takes notice, and clarifies this.
 
Good day!

      
                
                
                    
                                                    Fri, 09/27/2019 - 10:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Pranab BG,
every disk-level backup contains all data physically stored on the imaged drive (disk structure, registry, data) unless explicitly excluded by a user. Whether the reactivation of the installed soft is needed or not mainly depends on how your software is licensed e.g. you may need to reactivate the software on the new system, if that software activation is based on the hardware signature where it was installed.

      
                
                
                    
                                                    Fri, 09/27/2019 - 13:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
