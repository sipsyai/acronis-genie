# Always incremental - can I still send copies to tape? Storage Node required?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/always-incremental-can-i-still-send-copies-tape-storage-node-required

## Original Post
**Author:** Unknown

Always incremental - can I still send copies to tape? Storage Node required?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                
                    
                        
            The Acronis Cyber Protect best practices and the user guide both feature the "Always incremental" backup scheme.
It requires random-access reads and writes on the backup device, so SFTP is no choice, nor is tape.
Is it still possible to implement copies sent to a tape device?
Are there other caveats or requirements when opting for this backup strategy, e.g. does it require Acronis Storage Node, or can I utilize a NFS backup location?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 08/25/2025 - 14:02

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
The Always incremental (single-file) backup scheme is not available when backing up to an SFTP server or a tape device.
For tapes you have the following options: 
Always full
Weekly full, Daily incremental
Monthly full, Weekly differential, Daily incremental (GFS)
Custom (F-D-I)
Best regards.

      
                
                
                    
                                                    Mon, 09/01/2025 - 08:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jose, thank you.
so "Always incremental" should be possible on a simple NFS destination, right?
No option to replicate from disk backups to tape (D2D2T), regardless of the level?
Kind regards, Tom

      
                
                
                    
                                                    Mon, 09/01/2025 - 12:18
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tom wrote:

Jose, thank you.
so "Always incremental" should be possible on a simple NFS destination, right?
No option to replicate from disk backups to tape (D2D2T), regardless of the level?
Kind regards, Tom


Hello!
Replication to a tape is possible, but not from NFS.
You can see the full list of supported sources for replication here:https://www.acronis.com/en-us/support/documentation/AcronisCyberProtect_15/#backup-replication.html#kanchor211
Best regards.

      
                
                
                    
                                                    Mon, 09/01/2025 - 12:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Tom
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 37
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            putting all together: will the following be possible:
backup with schedule "Always incremental" to a NFS destination
with this NFS destination being a "Local folder" on the host where the tape dev is present ...
stage this "Local folder" to tape
 

      
                
                
                    
                                                    Mon, 09/01/2025 - 13:44
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Tom wrote:

putting all together: will the following be possible:
backup with schedule "Always incremental" to a NFS destination
with this NFS destination being a "Local folder" on the host where the tape dev is present ...
stage this "Local folder" to tape
 


Hello!
1.     Yes, that’s possible.
2/3.  Not exactly supported out of the box, but you can try the following approach as a test:

Mount the NFS export as a local folder on the tape host
	Replication/staging to tape is only available when the source is a local folder on the same host that has the tape device. If you mount the NFS share so the OS sees it as a local path (for example, /mnt/backup on Linux or a mapped drive mounted as a folder on Windows), the backup agent should recognize it as a valid replication source.


Stage that local folder to tape
	Once the NFS share is mounted and treated as local storage, you can configure a staging/replication plan to copy the backup chains to tape.

Note: Performance may be slower since you’ll be reading from NFS and writing to tape on the same host.
Best regards.

      
                
                
                    
                                                    Tue, 09/02/2025 - 07:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
