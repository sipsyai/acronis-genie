# Backup eines Linux-Server schlägt fehl

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-eines-linux-server-schlagt-fehl

## Original Post
**Author:** Unknown

Backup eines Linux-Server schlägt fehl

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo Forum,
habe in den letzten Tagen auf mehrere Linux-Server den Agent installiert, in Acronis Data Cloud registriert und einen Backup-Plan erstellt der sauber durchlief und noch immer läuft.
Jetzt habe ich den ersten Server der folgenden Fehler anzeigt:
Keines der zum Backup ausgewählten Elemente konnte gefunden werden.
Fehlercode 70
 
Ich bin genau so vor gegangen wir bei den bisherigen und da verlief, wie bereits erwähnt alles problemlos.
 
 
Hier die Fehlerdetails 
 


Fehler



Datum und Zeit
25. Oktober 2018, 14:35:27






Modul
307



Nachricht
 

Zusätzliche Informationen:
------------------------
Fehlercode: 41
Modul: 307
Zeileninfo: 0xE6792A5EE190DE2C
Felder: {"$module":"agent_protection_addon_lxa64_10790"}
Nachricht: Ausführen des Befehls fehlgeschlagen.
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB81959B
Felder: {"$module":"mms_lxa64_10790","CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94"}
Nachricht: TOL: Failed to execute the command. Resolving items to back up
------------------------
Fehlercode: 22
Modul: 309
Zeileninfo: 0x8D165E86FB81959B
Felder: {"$module":"agent_protection_addon_lxa64_10790","CommandID":"FD79C554-B363-4DB2-97BC-1E5A94094A94"}
Nachricht: TOL: Failed to execute the command. Resolving items to back up
------------------------
Fehlercode: 43
Modul: 307
Zeileninfo: 0xE873A234106E3486
Felder: {"$module":"agent_protection_addon_lxa64_10790"}
Nachricht: ResolveBackupSetCommand: Ausführen des Befehls fehlgeschlagen.
------------------------
Fehlercode: 68
Modul: 307
Zeileninfo: 0x071E35C26B78D645
Felder: {"$module":"agent_protection_addon_lxa64_10790"}
Nachricht: Keine der folgenden Einschlussregeln kann aufgelöst werden: '[Fixed Volumes]'.
------------------------
Fehlercode: 67
Modul: 307
Zeileninfo: 0x071E35C26B78D5FC
Felder: {"$module":"agent_protection_addon_lxa64_10790"}
Nachricht: Kann die Einschlussregel '[Fixed Volumes]' nicht auflösen.
------------------------
Fehlercode: 6
Modul: 377
Zeileninfo: 0x20E8C00E3FF3FA50
Felder: {"$module":"agent_protection_addon_lxa64_10790"}
Nachricht: Bei Verarbeitung der Vorlage 'Fest eingebaute Volumes' wurden keine Volumes gefunden.


 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/25/2018 - 12:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello again,
after I had found a few forum posts where a similar problem was described, I have checked my system based on the suggestions.All necessary components are available.Everything is up to date.but when I dropped the command "modprobe snapapi26" I get the following error:modprobe: ERROR: could not insert 'snapapi26': Required key not available
Unfortunately, I find no further clues to this error on how to proceed.
Help

      
                
                
                    
                                                    Mon, 10/29/2018 - 10:47
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes,
Thank you for sharing additional details! I've searched for similar cases in our internal sources and found the following information about the error message
modprobe: ERROR: could not insert 'snapapi26': Required key not available 
according to the information under below link, this is a general issue in the Linux systems, please see here: https://askubuntu.com/questions/762254/why-do-i-get-required-key-not-available-when-install-3rd-party-kernel-modules 
The easiest way to fix this issue is disabling Secure Boot in UEFI (BIOS) settings. 
Please let me know if it helps or not. 

      
                
                
                    
                                                    Wed, 10/31/2018 - 10:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ekaterina,
thanks for the information.
It was really the secure boot which caused the error.
Thanks for the support.
See you

      
                
                
                    
                                                    Mon, 11/05/2018 - 11:51
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the update / feedback!  Glad that things look to be good again 

      
                
                
                    
                                                    Tue, 11/06/2018 - 13:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
