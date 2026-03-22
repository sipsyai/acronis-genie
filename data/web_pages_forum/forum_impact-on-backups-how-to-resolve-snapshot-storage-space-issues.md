# Impact on Backups: How to Resolve Snapshot Storage Space Issues?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/impact-backups-how-resolve-snapshot-storage-space-issues

## Original Post
**Author:** Unknown

Impact on Backups: How to Resolve Snapshot Storage Space Issues?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Pereira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good morning everyone, I’m having an issue with a client. The backup plan named "backup file server" is showing this error. Could you please provide a simple way to explain the solution to the client?
"Unable to create the snapshot. There is not enough space on the volume for shadow copy storage.
Troubleshooting
Free up additional space, increase the snapshot storage size, or move the snapshot storage to another volume. For more information, click on "Get Support."
Does this impact my backups? How can I resolve this issue?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/28/2024 - 11:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
The issue appears to be related to the Volume Shadow Copy Service (VSS). It is critical to ensure that VSS functions properly, as unresolved issues can cause backup failures.
You can address this by following Microsoft's instructions to increase the allocated space for shadow copies: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/vssadmin-resize-shadowstorage
As a temporary test, you can disable VSS in the backup plan. However, please note that this will prevent certain types of backups, such as SQL database backups, from being executed.
If you require further assistance, let us know!
Best regards.

      
                
                
                    
                                                    Thu, 11/28/2024 - 19:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
