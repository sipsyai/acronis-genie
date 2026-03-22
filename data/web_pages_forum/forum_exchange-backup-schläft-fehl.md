# Exchange Backup schläft fehl

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/exchange-backup-schlaft-fehl

## Original Post
**Author:** Unknown

Exchange Backup schläft fehl

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo zusammen,
 
ich bin dabei bei einem Kunden die Exchange DB zu sichern. Es wird auch jede einzelne Datenbank angezeigt. Sobald ich aber den Backup Job starte, wird der Button "Jetzt Ausführen" grau und bleibt dies auch. Die Fehlermeldung ist folgende:
 
NACHRICHT
Backup ist fehlgeschlagen

Zusätzliche Informationen:
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"mms_vsa64_4492","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Nachricht: TOL: Failed to execute the command. Backup plan 'COLOGNEDC_DB -> NAS'
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"agent_protection_addon_vsa64_4492","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Nachricht: TOL: Failed to execute the command. Backup plan 'COLOGNEDC_DB -> NAS'
------------------------
Fehlercode: 41
Modul: 307
Zeileninfo: 0xE6792A5EE190DDE7
Felder: {"$module":"agent_protection_addon_vsa64_4492"}
Nachricht: Failed to execute the command.
------------------------
Fehlercode: 53
Modul: 309
Zeileninfo: 0x2E7E9E174F1FB719
Felder: {"$module":"agent_protection_addon_vsa64_4492","FailCount":"2"}
Nachricht: 2 activities have not succeeded. One of them is displayed.
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
Fehlercode: 103
Modul: 623
Zeileninfo: 0x94F5F955B13DDE83
Felder: {"$module":"arx_agent_fork_vsa64_4492","IsReturnCode":"1"}
Nachricht: A generic error of Microsoft Exchange backup component.
------------------------
Fehlercode: 17
Modul: 91
Zeileninfo: 0x7EDADE4ED07D5114
Felder: {"$module":"arx_agent_fork_vsa64_4492","IsReturnCode":"1"}
Nachricht: Failed to back up the information store.
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"service_process_vsa64_4492","CommandID":"C4DFD066-D6B5-48BF-ACA4-D9F03FB01337"}
Nachricht: TOL: Failed to execute the command. Managing Microsoft Exchange server
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB819595
Felder: {"$module":"arx_agent_fork_vsa64_4492","CommandID":"C4DFD066-D6B5-48BF-ACA4-D9F03FB01337"}
Nachricht: TOL: Failed to execute the command. Managing Microsoft Exchange server
------------------------
Fehlercode: 1059
Modul: 91
Zeileninfo: 0xACF6DC4C960B8D20
Felder: {"$module":"exchange_management_vsa64_4492"}
Nachricht: The Exchange management operation has failed.
------------------------
Fehlercode: 1052
Modul: 91
Zeileninfo: 0x8DE328702E57F65F
Felder: {"$module":"exchange_management_vsa64_4492"}
Nachricht: Failed to initialize the PowerShell adapter.
------------------------
Fehlercode: 1001
Modul: 91
Zeileninfo: 0x8DE328702E57F65F
Felder: {"$module":"exchange_management_vsa64_4492"}
Nachricht: Beim Verbinden mit dem Remoteserver ist folgender Fehler aufgetreten: Eine angegebene Anmeldesitzung ist nicht vorhanden. Sie wurde gegebenenfalls bereits beendet. Weitere Informationen finden Sie im Hilfethema "about_Remote_Troubleshooting".
------------------------
Fehlercode: 65520
Modul: 0
Zeileninfo: 0xBD28FDBD64EDB8F1
Felder: {"$module":"exchange_management_vsa64_4492","code":"2147943712"}
Nachricht: Eine angegebene Anmeldesitzung ist nicht vorhanden. Sie wurde gegebenenfalls bereits beendet

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/09/2018 - 07:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Oliver
My German is very rusty but I will try my best to help you:
Die Fehlermeldung Eine angegebene Anmeldesitzung ist nicht vorhanden. Es möglicherweise bereits beendet hat, bezieht sich normalerweise auf falsch angegebene Anmeldeinformationen beim Herstellen einer Verbindung mit der Exchange-Datenbank. Ich würde empfehlen, dass Sie den Sicherungsplan entfernen und neu erstellen, und wenn Sie die anwendungsspezifische Sicherung für Exchange auswählen, stellen Sie sicher, dass Sie sich bei einem Domänenadministratorkonto authentifizieren, das über vollständigen Zugriff auf Exchange verfügt. Das Konto, das für die Authentifizierung verwendet wird, sollte den folgenden Zugriff haben:
Administrators
Domain admins
Domain Users
Organizational management of Exchange 
Acronis Remote users of your local Active Directory
Ich hoffe das hilft dir
Grüße

      
                
                
                    
                                                    Fri, 03/09/2018 - 10:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
