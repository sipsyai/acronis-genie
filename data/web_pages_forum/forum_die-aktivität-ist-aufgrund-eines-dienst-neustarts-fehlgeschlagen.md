# Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/die-aktivitat-ist-aufgrund-eines-dienst-neustarts-fehlgeschlagen

## Original Post
**Author:** Unknown

Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Bekomme seit paar Tagen bei einer Maschine folgenden Fehler angezeigt:
Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.12110, Zeitstempel: 0x5bb627c7 Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff Ausnahmecode: 0xc0000409 Fehleroffset: 0x0000000000074a30 ID des fehlerhaften Prozesses: 0x46b0 Startzeit der fehlerhaften Anwendung: 0x01d475400cd2818c Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe Pfad des fehlerhaften Moduls: C:\Windows\SYSTEM32\MSVCR120.dll Berichtskennung: d486b2a9-e133-11e8-80de-00155d8ecd01 Vollständiger Name des fehlerhaften Pakets: Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
 
Das seltsame ist das dieser Fehler nur beim Backup auf das lokale Ziel auftritt.
Das Backup in unsere Cloud läuft sauber durch.
Habe den Client schon repariert und auch komplett neu installiert.
Keine Besserung.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/06/2018 - 15:50

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hier nochmal alles im Detail:
 

Fehler



Datum und Zeit
05. November 2018, 20:49:01






Modul
309



Nachricht
 

Zusätzliche Informationen:
------------------------
Fehlercode: 78
Modul: 309
Zeileninfo: 0x7564DA35B0F1EAF3
Felder: {"$module":"mms_vsa64_12110"}
Nachricht: Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen.
------------------------
Fehlercode: 10001
Modul: 20
Zeileninfo: 0xFB0B530E27842356
Felder: {"$module":"mms_vsa64_12110"}
Nachricht: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.12110, Zeitstempel: 0x5bb627c7
Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
Ausnahmecode: 0xc0000409
Fehleroffset: 0x0000000000074a30
ID des fehlerhaften Prozesses: 0x46b0
Startzeit der fehlerhaften Anwendung: 0x01d475400cd2818c
Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
Pfad des fehlerhaften Moduls: C:\Windows\SYSTEM32\MSVCR120.dll
Berichtskennung: d486b2a9-e133-11e8-80de-00155d8ecd01
Vollständiger Name des fehlerhaften Pakets:
Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
------------------------
Fehlercode: 10001
Modul: 20
Zeileninfo: 0xFB0B530E27842357
Felder: {"Computer":"Intern-RDS1.diapersonal.local","EventID":"1000","$module":"mms_vsa64_12110","providerName":"Application Error","providerGUID":"","Channel":"Application"}
Nachricht: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.12110, Zeitstempel: 0x5bb627c7
Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
Ausnahmecode: 0xc0000409
Fehleroffset: 0x0000000000074a30
ID des fehlerhaften Prozesses: 0x46b0
Startzeit der fehlerhaften Anwendung: 0x01d475400cd2818c
Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
Pfad des fehlerhaften Moduls: C:\Windows\SYSTEM32\MSVCR120.dll
Berichtskennung: d486b2a9-e133-11e8-80de-00155d8ecd01
Vollständiger Name des fehlerhaften Pakets:
Anwendungs-ID, die relativ zum fehlerhaften Paket ist:


      
                
                
                    
                                                    Tue, 11/06/2018 - 15:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Johannes,
die Fehlermeldung weißt auf einen Absturz des Prozesses service_process.exe nach. Solche Probleme müssen mit der Hilfe von Acronis Support-Team untersucht werden, da hier höchstwahrscheinlich der Einsatz der Entwicklern benötigt wird. 
Für die Untersuchung bräuchten meine Kollegen die Protokolle und eine Absturzdatei, die nach den Anleitungen aus https://kb.acronis.com/de/content/49298 erstellt werden können.
Vielen Dank, 

      
                
                
                    
                                                    Wed, 11/07/2018 - 15:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Ekaterina,
danke für die Antwort.
Werde dann mal ein Ticket beim Support eröffnen.

      
                
                
                    
                                                    Wed, 11/07/2018 - 15:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marcus Pockrandt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Guten Morgen zusammen,
was kam denn hier raus? Ich habe seit ca. 2 Wochen das gleiche (oder ein ähnliches) Problem:
Additional info
------------------------
Error code: 78
Module: 309
LineInfo: 0x7564DA35B0F1EAF3
Fields: {'$module': 'mms_vsa64_11010'}
Message: Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen.
Es ist die aktuelle Build von 12.5 Adv. Workstation installiert.
Vielen Dank und viele Grüße
Marcus
 

      
                
                
                    
                                                    Thu, 02/21/2019 - 07:58
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Moin Marcus,
der Fehler wurde durch das Update des Agenten behoben.
Zum Zeitpukt des Fehler hatte ich die Version 12.5.12110 in verwendung.
Hatte dann auf 12.5.12210 oder 12.5.12220 gepatched.
Und seit 1-2 Wochen ist auch die Version 12.5.12420 veröffentlicht.
Der Feghler trat auf jedenfall seit dem Update vom Agenten nicht mehr auf.
 
Hoffe es hilft dir weiter.

      
                
                
                    
                                                    Tue, 02/26/2019 - 08:04
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Marcus Pockrandt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Nahmd Johannes,
erst einmal vielen Dank für Deine Rückmeldung!
Bei der Workstation ist 12.5 Build 11010 installiert - es will auch keine neue Version finden?
Selbst der Installer hat weiterhin 11010.
Sehr merkwürden...
Ich hatte aber noch parallel ein Ticket bei Acronis aufgemacht, und hier wurde mir eine Reparaturinstallation angeraten - mal schauen was die heute so bringt.
Viele Grüße
Marcus

      
                
                
                    
                                                    Tue, 02/26/2019 - 18:33
