# Linux backup fails

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/linux-backup-fails

## Original Post
**Author:** Unknown

Linux backup fails

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Haupt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
unfortunately I was not able to find a dedicated support contact form for service providers. So I am looking forward to find some help here.
I've been using the volume backup basically for about 6 months without any issues. Since the latest Ubuntu Upgrade -> 20.10) and / or agent update (-> v15) I experience the following issue (some texts are in German only).
--
Activity details:
Additional Information:
------------------------
Fehlercode: 20250646
Felder: {"$module":"service_process_lxa64_24647","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Nachricht: TOL: Failed to execute the command. Backup
------------------------
Fehlercode: 20250646
Felder: {"$module":"gtob_backup_command_addon_lxa64_24647","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Nachricht: TOL: Failed to execute the command. Backup
------------------------
Fehlercode: 21561347
Felder: {"$module":"disk_bundle_lxa64_24647"}
Nachricht: Backup ist fehlgeschlagen.
------------------------
Fehlercode: 66596
Felder: {"$module":"disk_bundle_lxa64_24647"}
Nachricht: Ausführen der Aktionen fehlgeschlagen.
------------------------
Fehlercode: 458785
Felder: {"$module":"disk_bundle_lxa64_24647"}
Nachricht: Erstellen des Volume-Snapshots fehlgeschlagen.
------------------------
Fehlercode: 5832711
Felder: {"$module":"disk_bundle_lxa64_24647","device":"/dev/sda5"}
Nachricht: Erstellen eines Snapshots fehlgeschlagen.
--
Environment:
Ubuntu 20.10
Agent: 15.0.24647

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/27/2020 - 22:04

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Daniel.
This issue requires investigation.
Please submit a support ticket as described by the following link: https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Fri, 11/06/2020 - 08:13
