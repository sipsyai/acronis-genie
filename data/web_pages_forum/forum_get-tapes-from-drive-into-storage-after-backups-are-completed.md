# Get tapes from drive into storage after backups are completed?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/get-tapes-drive-storage-after-backups-are-completed

## Original Post
**Author:** Unknown

Get tapes from drive into storage after backups are completed?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Peter Novak
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Managed to make a backup schedule of all our servers onto two backup tapes. One of them goes back to storage, but the other one stays in drive (we have 2 drives). Where can I specify that after the last backup, the tape should be brought back to storage?
I looked at post-commands, but couldn´t find anything that moves the tape.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/10/2025 - 10:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Please take a look at the user guide below regarding tape handling options:
Move a tape back to the slot after each successful backupDefault: Enabled

If this option is disabled, the tape remains in the drive after the operation completes.


If it is enabled, the software returns the tape to its original slot after the backup is finished.


If your protection plan includes additional actions (for example, backup validation or replication), the tape will be moved back to the slot after those actions are completed.

Eject tapes after each successful backupDefault: Disabled

If this option is enabled, the software will eject the tape after the backup is successfully completed.


If additional actions follow the backup, the tape will be ejected after those are completed.


If both this option and “Move a tape back to the slot” are enabled, eject takes priority and the tape will be ejected.

For full details on tape handling options, please refer to:https://www.acronis.com/en-eu/support/documentation/AcronisCyberProtect_16/#tape-management.html#kanchor54
Best regards.

      
                
                
                    
                                                    Mon, 11/10/2025 - 17:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Peter Novak
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            José P. Magalhães wrote:

Hello!
Please take a look at the user guide below regarding tape handling options:
Move a tape back to the slot after each successful backupDefault: Enabled

If this option is disabled, the tape remains in the drive after the operation completes.


If it is enabled, the software returns the tape to its original slot after the backup is finished.


If your protection plan includes additional actions (for example, backup validation or replication), the tape will be moved back to the slot after those actions are completed.

Eject tapes after each successful backupDefault: Disabled

If this option is enabled, the software will eject the tape after the backup is successfully completed.


If additional actions follow the backup, the tape will be ejected after those are completed.


If both this option and “Move a tape back to the slot” are enabled, eject takes priority and the tape will be ejected.

For full details on tape handling options, please refer to:https://www.acronis.com/en-eu/support/documentation/AcronisCyberProtect_16/#tape-management.html#kanchor54
Best regards.


I was looking at those options, but wouldn´t they move the tape after each backup? That would be a big time loss with 50+ servers. 

      
                
                
                    
                                                    Tue, 11/11/2025 - 06:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Peter Novak wrote:

José P. Magalhães wrote:

Hello!
Please take a look at the user guide below regarding tape handling options:
Move a tape back to the slot after each successful backupDefault: Enabled

If this option is disabled, the tape remains in the drive after the operation completes.


If it is enabled, the software returns the tape to its original slot after the backup is finished.


If your protection plan includes additional actions (for example, backup validation or replication), the tape will be moved back to the slot after those actions are completed.

Eject tapes after each successful backupDefault: Disabled

If this option is enabled, the software will eject the tape after the backup is successfully completed.


If additional actions follow the backup, the tape will be ejected after those are completed.


If both this option and “Move a tape back to the slot” are enabled, eject takes priority and the tape will be ejected.

For full details on tape handling options, please refer to:https://www.acronis.com/en-eu/support/documentation/AcronisCyberProtect_16/#tape-management.html#kanchor54
Best regards.


I was looking at those options, but wouldn´t they move the tape after each backup? That would be a big time loss with 50+ servers. 


Hello!
Yes, those options work per backup job. With 50+ servers, this would cause multiple load/unload cycles and slow down the overall process.
In these cases, the recommended setup is:

Backup to disk first, then


Use one replication job to tape (D2D2T).

This mounts the tape only once per cycle.
I would also advise contacting our support team so they can review your setup and confirm if there are alternative workflows that better fit your environment.
Best regards.
 

      
                
                
                    
                                                    Tue, 11/11/2025 - 15:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
