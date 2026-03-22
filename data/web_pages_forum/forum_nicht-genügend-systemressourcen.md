# Nicht genügend Systemressourcen?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/nicht-genugend-systemressourcen

## Original Post
**Author:** Unknown

Nicht genügend Systemressourcen?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo, bekomme beim Backup meiner 2 Server immer diesen Fehler:
Zusätzliche Informationen:
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"service_process_vsa64_4492","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Nachricht: TOL: Failed to execute the command. Backing up
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"gtob_backup_command_addon_vsa64_4492","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Nachricht: TOL: Failed to execute the command. Backing up
------------------------
Fehlercode: 212
Modul: 161
Zeileninfo: 0x0B320396ADFE3EA5
Felder: {"$module":"disk_bundle_vsa64_4492","IsReturnCode":"1"}
Nachricht: Failed to find archive 'Term-Server1.kinderkinder.local-38700E73-7B6F-4260-A4DF-41F08821BB76-0B20AC09-9F21-4F01-A46B-ACB7CBD531F8A'.
------------------------
Fehlercode: 255
Modul: 161
Zeileninfo: 0x3056F99E8B70C97C
Felder: {"$module":"disk_bundle_vsa64_4492"}
Nachricht: Failed to load the metadata of archive 'Term-Server1.kinderkinder.local-38700E73-7B6F-4260-A4DF-41F08821BB76-0B20AC09-9F21-4F01-A46B-ACB7CBD531F8A'.
------------------------
Fehlercode: 6
Modul: 523
Zeileninfo: 0x93DDF24CF210E739
Felder: {"$module":"disk_bundle_vsa64_4492"}
Nachricht: Failed to open file 'Term-Server1.kinderkinder.local-38700E73-7B6F-4260-A4DF-41F08821BB76-0B20AC09-9F21-4F01-A46B-ACB7CBD531F8A.xml'.
------------------------
Fehlercode: 7
Modul: 4
Zeileninfo: 0xF35F747B3B21F78A
Felder: {"$module":"disk_bundle_vsa64_4492","function":"OpenFileW","path":"\\\\?\\UNC\\192.168.178.4\\backup\\Term-Server1\\Term-Server1.kinderkinder.local-38700E73-7B6F-4260-A4DF-41F08821BB76-0B20AC09-9F21-4F01-A46B-ACB7CBD531F8A.xml"}
Nachricht: Error occurred while opening the file.
------------------------
Fehlercode: 65520
Modul: 0
Zeileninfo: 0xBD28FDBD64EDB8F1
Felder: {"$module":"disk_bundle_vsa64_4492","code":"2147943850"}
Nachricht: Nicht genügend Systemressourcen, um den angeforderten Dienst auszuführen

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/12/2018 - 08:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Oliver,
Falls die betroffenen Server tatsächlich genug Systemressourcen haben und während der Sicherung nicht überlastet sind, würde ich das Problem beim Support-Team melden.

      
                
                
                    
                                                    Fri, 11/16/2018 - 15:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
