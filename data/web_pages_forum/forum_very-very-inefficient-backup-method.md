# Very Very inefficient backup method

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/very-very-inefficient-backup-method

## Original Post
**Author:** Unknown

Very Very inefficient backup method

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                
                    
                        
            If i want to backup all my VMs in one backup plan.
With first stage backup to nas and then to the cloud.
It goes like this.
Backup VM1 to nas
Sync VM1 backup to Cloud
Backup VM2 to nas
Sync VM2 backup to Cloud..
Whaaaaaaat this will take weeks before all the backups are done for a first time.
It should be something like this.
First backup all the VMs in the job to the NAS
af After that begin syncing to the Cloud. The sync to the cloud should be a continious process.. and not halt the next backup cycle to the local nas.
So actually the replication to cloud thing should always be in a seperate job.. Just like Acronis Backup for Vmware always did... that is one piece of nice software..
The new backup Cloud offering is very weak... or I am doing something wrong...

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 11/11/2016 - 19:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vasily Semyonov
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 3841
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
This behavior can be mitigated with simultaneous VM backup option (Backup Options->Scheduling) - in this case there will be X VMs backed up in parallel and the replication of these backups will also start simultaneously.
P.S. In the next updates for Acronis Backup 12 we're planning to introduce separate independent plans for data movement, i.e. separate backup replication plan with its own schedule, separate convert to VM plans, etc. This should completely solve the scenario you describe.
Thank you.

      
                
                
                    
                                                    Mon, 11/14/2016 - 11:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Vasily
Acronis Virtualization Program Manager

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Nice to hear. When is the next update scheduled?

      
                
                
                    
                                                    Mon, 11/14/2016 - 11:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            And what would happen in the current version.. when the replication task is still running and the new backup time is already @ hand.. will it hold off the backup.. or just start it (like with Acronis Backup for Vmware).

      
                
                
                    
                                                    Mon, 11/14/2016 - 11:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vasily Semyonov
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 3841
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
The next major update is planned for the next year, no exact date is defined yet, but it should in the beginning of the 1st half.
What concerns your question: the replication activity in v12 is tightly tied with the backup plan, so in this situation the backup plan will wait until replication is complete, i.e. it won't start "twice".
Thank you.

      
                
                
                    
                                                    Mon, 11/14/2016 - 12:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Vasily
Acronis Virtualization Program Manager

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            That is a shame.. because that way.. 
 
for example. First full backup to local NAS takes 3 hours. But replication to cloud takes 3 days to finish.. then the next backup incremental backup to NAS will be after 3 days...

      
                
                
                    
                                                    Mon, 11/14/2016 - 12:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Bobbo_3C0X1
                            

                            
                    
                        Forum Hero
                    
                
            
                        
                
                    Posts: 70
                
            
            
                
                    Comments: 8331
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You can pause the Acronis cloud backup manually at any time, which will allow local backups to then run. When the local/NAS backup is done, then unpause the cloud backup and it will continue where it left off.  I took this approach when I pushed my 500Gb family photo archive initially and it took nearly a full 8 days to complete while backing up to the cloud continuously.  

      
                
                
                    
                                                    Tue, 11/15/2016 - 03:13
                                                                            
                                
                            
                                            
                                            
    
                    
                (01). MVP WinPE Builder              (02). MVP LogViewer
(03). MVP Google Drive                 (04). Cleanup Utility
(05). Cloning Correctly                  (06). Clone vs Backup
(07). Community Tools                 (08). Contact Support
(09). Product Documentation    (10). OS MBR vs UEFI
(11). BOOT MBR vs UEFI               (12). Common OEM Drivers

            
                            
                Products: 
                True Image / Snap Deploy / Revive / Disk Director

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I created a Acronis Cloud Backup First to local and then to replicate to Cloud.
After the Backup to local finished... the overall backup stayed on 75%...
And i did not see a seperate Replicate tasks.. which i cloud pause..
 
 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      398282-135220.png

                      59.16 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 11/15/2016 - 10:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Vasily Semyonov
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 22
                
            
            
                
                    Comments: 3841
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
It's not possible to pause a replication task. I believe what Bobbo_3C0X1 was referring to is ability to continue uploading backup to cloud (from either backup or backup replication activity) even if this process was interrupted and task was cancelled/stopped for whatever reasons. This works in Acronis Backup Cloud for entire machine/disk/partition backups, i.e. even if uploading to Acronis Cloud failed and was restarted - it won't start from scratch, but rather will continue from where it stopped last time.
Thank you.

      
                
                
                    
                                                    Tue, 11/15/2016 - 11:00
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Vasily
Acronis Virtualization Program Manager

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Just Another Acronis User
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 109
                
            
            
                
                    Comments: 349
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            hmm OK..

      
                
                
                    
                                                    Tue, 11/15/2016 - 11:03
