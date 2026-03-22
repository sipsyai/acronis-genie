# Backup schlägt dauerhaft fehl

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-schlagt-dauerhaft-fehl

## Original Post
**Author:** Unknown

Backup schlägt dauerhaft fehl

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Woran kann dies liegen?
FEHLER IST FOLGENDER:
Backup ist fehlgeschlagen
Die Syntax für den Pfad '\\?\UNC\192.168.101.2\backup\FIRE-SRV01\.tmp.FFCBC63C-3BCD-4C67-A1C8-891D37A45758.Fire-SRV01.FireSafe.Local-173D61F2-4775-4BE3-B949-D1A56E17837F-3337D188-0050-43FE-9A11-D051A01861E6A.xml' ist falsch.
Fehler
DATUM UND ZEIT
21. September 2018, 11:34:44
MODUL
309
NACHRICHT

Zusätzliche Informationen:
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"service_process_vsa64_4492"}
Nachricht: TOL: Failed to execute the command. Backing up
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"gtob_backup_command_addon_vsa64_4492"}
Nachricht: TOL: Failed to execute the command. Backing up
------------------------
Fehlercode: 207
Modul: 161
Zeileninfo: 0x0B320396ADFE3CD4
Felder: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_4492"}
Nachricht: Failed to create an archive in location 'arl:/9111138B-CF43-4EF8-962D-5FE77DE50E42/917E9711-EDF7-4EC9-ABB3-C4EEF7E6085C'.
------------------------
Fehlercode: 26
Modul: 161
Zeileninfo: 0xA0F87A51D6F9CFAA
Felder: {"$module":"disk_bundle_vsa64_4492"}
Nachricht: Failed to save the archive metainfo. You either do not have write access to the folder or it is unavailable at the moment.
------------------------
Fehlercode: 5
Modul: 523
Zeileninfo: 0x93DDF24CF210E731
Felder: {"$module":"disk_bundle_vsa64_4492"}
Nachricht: Failed to create file '.tmp.FFCBC63C-3BCD-4C67-A1C8-891D37A45758.Fire-SRV01.FireSafe.Local-173D61F2-4775-4BE3-B949-D1A56E17837F-3337D188-0050-43FE-9A11-D051A01861E6A.xml'.
------------------------
Fehlercode: 9
Modul: 4
Zeileninfo: 0xF35F747B3B21F786
Felder: {"path":"\\\\?\\UNC\\192.168.101.2\\backup\\FIRE-SRV01\\.tmp.FFCBC63C-3BCD-4C67-A1C8-891D37A45758.Fire-SRV01.FireSafe.Local-173D61F2-4775-4BE3-B949-D1A56E17837F-3337D188-0050-43FE-9A11-D051A01861E6A.xml","function":"CreateFileW","$module":"disk_bundle_vsa64_4492"}
Nachricht: Error occurred while renaming the file.
------------------------
Fehlercode: 65520
Modul: 0
Zeileninfo: 0xBD28FDBD64EDB8F1
Felder: {"$module":"disk_bundle_vsa64_4492","code":"2147942523"}
Nachricht: Die Syntax für den Dateinamen, Verzeichnisnamen oder die Datenträgerbezeichnung ist falsch

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/21/2018 - 09:36

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Oliver,
Vielen Dank für Ihre Nachfrage! Gibt es eventuell irgendwelche Begrenzung für den Pfadnamen\Dateinamen in der Zielfreigabe? (mehr Information unter Filename is limited on encrypted Synology NAS drive).
Auch würde ich testweise den Pfad direkt über eine IP-Adresse eingeben und prüfen, ob der Archiv in diesem Fall erfolgreich erstellt wird. 

      
                
                
                    
                                                    Fri, 09/21/2018 - 12:41
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
