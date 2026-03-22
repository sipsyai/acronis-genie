# Acronis Storage Gateway backup to local storage failed

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-storage-gateway-backup-local-storage-failed

## Original Post
**Author:** Unknown

Acronis Storage Gateway backup to local storage failed

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Victor Ng
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I setup the Acronis Storage Gateway on a brand new CentOS 7 VM(2 vCPU, 4GB RAM, 127 GB HD) with local storage /var/lib/Acronis/storage. I can see that device on Backup Management Console.
However, when I run a small size (14MB) backup test (from a Win 7 PC to that local /var/lib/Acronis/storage), it failed with the following log:
Error details
Error
DATE AND TIMEJul 12, 2017, 10:59:39 AM
MODULE309
MESSAGE
Additional info:------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"service_process_vsa64_3917","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"$module":"gtob_backup_command_addon_vsa64_3917","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 212
Module: 161
LineInfo: 0x0B320396ADFE3EA3
Fields: {"$module":"disk_bundle_vsa64_3917","IsReturnCode":"1"}
Message: Failed to find archive 'portal-C3F7C341-2352-461C-9C1E-75EDC9E45190-70A636EF-257B-495B-B115-12BCA66AB4D0A'.
------------------------
Error code: 1085
Module: 3
LineInfo: 0x8258202786770DDF
Fields: {"$module":"disk_bundle_vsa64_3917"}
Message: Failed to connect to 128.403.xxx.yyy
 
Error code 0x01350016+0x01350016+0x00A100D4+0x0003043D
 
Please help and suggest.
Thank you

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/12/2017 - 06:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Victor Ng
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            seems I found the solution: shutdown the storage gateway firewall.

      
                
                
                    
                                                    Wed, 07/12/2017 - 07:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Victor, thank you for sharing your solution with the community! 

      
                
                
                    
                                                    Thu, 07/20/2017 - 13:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
