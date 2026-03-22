# Backup Error - Faulting Application Name

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/backup-error-faulting-application-name

## Original Post
**Author:** Unknown

Backup Error - Faulting Application Name

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniele Di Ianni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
i have a problem with a new installed agent 12.5.12110. Only 6 Server have this problem (i have a 100 server on my cloud acronis for providers).
The error is this:
Faulting application name: service_process.exe, version: 12.5.1.12110, time stamp: 0x5bb627c7 Faulting module name: MSVCR120.dll, version: 12.0.40660.0, time stamp: 0x577e0cc7 Exception code: 0xc0000409 Fault offset: 0x0000000000074890 Faulting process id: 0x261c Faulting application start time: 0x01d47b93d5d7f3ec Faulting application path: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe Faulting module path: C:\Windows\SYSTEM32\MSVCR120.dll Report Id: eec4168b-b276-4a3e-a77e-2de964795cf3 Faulting package full name: Faulting package-relative application ID:
 
I try to update a C++ component but nothing...i reinstall the agent, take 2 backup and after failed again with the same errors.
 
This is the log:
 
MODULO
309
MESSAGGIO
Backup non riuscito

Informazioni aggiuntive:
------------------------
Codice errore : 61
Modulo: 309
LineInfo: 0x4A8728DC8A1C9583
Campi: {"$module":"mms_vsa64_12110"}
Messaggio: Command has failed. Command=Backup plan 'BackupSRVFAGGI'; 
------------------------
Codice errore : 22
Modulo: 309
LineInfo: 0x8D165E86FB81959B
Campi: {"$module":"mms_vsa64_12110","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Messaggio: TOL: Failed to execute the command. Backup plan 'BackupSRVFAGGI'
------------------------
Codice errore : 22
Modulo: 309
LineInfo: 0x8D165E86FB81959B
Campi: {"$module":"agent_protection_addon_vsa64_12110","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Messaggio: TOL: Failed to execute the command. Backup plan 'BackupSRVFAGGI'
------------------------
Codice errore : 41
Modulo: 307
LineInfo: 0xE6792A5EE190DE27
Campi: {"$module":"agent_protection_addon_vsa64_12110"}
Messaggio: Failed to execute the command.
------------------------
Codice errore : 53
Modulo: 309
LineInfo: 0x2E7E9E174F1FB719
Campi: {"FailCount":"2","$module":"agent_protection_addon_vsa64_12110"}
Messaggio: 2 activities have not succeeded. One of them is displayed.
------------------------
Codice errore : 78
Modulo: 309
LineInfo: 0x7564DA35B0F1EAF3
Campi: {"$module":"mms_vsa64_12110"}
Messaggio: The activity has failed due to a restart of the service.
------------------------
Codice errore : 10001
Modulo: 20
LineInfo: 0xFB0B530E27842356
Campi: {"$module":"mms_vsa64_12110"}
Messaggio: Faulting application name: service_process.exe, version: 12.5.1.12110, time stamp: 0x5bb627c7
Faulting module name: MSVCR120.dll, version: 12.0.40660.0, time stamp: 0x577e0cc7
Exception code: 0xc0000409
Fault offset: 0x0000000000074890
Faulting process id: 0x261c
Faulting application start time: 0x01d47b93d5d7f3ec
Faulting application path: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
Faulting module path: C:\Windows\SYSTEM32\MSVCR120.dll
Report Id: eec4168b-b276-4a3e-a77e-2de964795cf3
Faulting package full name: 
Faulting package-relative application ID: 
------------------------
Codice errore : 10001
Modulo: 20
LineInfo: 0xFB0B530E27842357
Campi: {"Computer":"HYPERv-2.faggi.local","providerName":"Application Error","providerGUID":"","$module":"mms_vsa64_12110","Channel":"Application","EventID":"1000"}
Messaggio: Faulting application name: service_process.exe, version: 12.5.1.12110, time stamp: 0x5bb627c7
Faulting module name: MSVCR120.dll, version: 12.0.40660.0, time stamp: 0x577e0cc7
Exception code: 0xc0000409
Fault offset: 0x0000000000074890
Faulting process id: 0x261c
Faulting application start time: 0x01d47b93d5d7f3ec
Faulting application path: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
Faulting module path: C:\Windows\SYSTEM32\MSVCR120.dll
Report Id: eec4168b-b276-4a3e-a77e-2de964795cf3
Faulting package full name: 
Faulting package-relative application ID:
 
Thanks for now

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/14/2018 - 10:12

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Daniele!
 
Thank you for using the Forum!
 
So it appears that the service_process.exe crashes while backing up and you are using the latest available build 12110.
The issue is known and is solved in the builds starting with 12210, soon to be publicly available for download in all  DCs.
Until then, please use the below link for direct download of a Full Installer that you can use to update the agents manually (including a way to create an MSI package for remote upgrade)
32-bit Windows64-bit Windows
 
In general, in case any process acrashes, please refer to the following article on the matter -> Troubleshooting Application Crashes

      
                
                
                    
                                                    Wed, 11/14/2018 - 13:21
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daniele Di Ianni
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you very much for the response...i try to update and i tell if all ok..
thanks for now

      
                
                
                    
                                                    Thu, 11/15/2018 - 15:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andreas Kirschner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello everyone,
i ve got the same problem.
my Server is standalone and the backup goes on NAS.
at the momment we have 12.5.11010.0  Build von acronis Backup.
I ve downloded the newest agent from the here provided Link and i ve started the installation.
 
But:
the Software i m trying to install is with the Product not compatible.
The newest Build that i can download is alredy installed.
 
Thank you very much in advance!
 
Marko
 


      
                
                
                    
                                                    Wed, 01/30/2019 - 11:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andreas Kirschner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            And the Log File:
 
2019-01-29T21:00:05:467+01:00 7500 I0135003A: Der Benutzer '' (clientProfileID=; clientSessionID=5DD9B967-C359-426D-AAF8-24A8186D485C) führt gerade den Befehl 'Backup-Plan 'HGCAD1v4d'' aus.
2019-01-29T21:00:26:122+01:00 4652 I0135003A: Der Benutzer '' (clientProfileID=; clientSessionID=5DD9B967-C359-426D-AAF8-24A8186D485C) führt gerade den Befehl 'Backup' aus.
2019-01-29T21:00:26:175+01:00 4652 I00000000: I00000000: Backup Inclusions list:
2019-01-29T21:00:26:182+01:00 4652 I00000000: I00000000: Windows (C:)
2019-01-29T21:00:26:187+01:00 4652 I00000000: I00000000: Daten (D:)
2019-01-29T21:00:26:193+01:00 4652 I00000000: I00000000: EFI system partition
2019-01-29T21:00:26:199+01:00 4652 I00000000: I00000000: Recovery
2019-01-29T21:00:26:205+01:00 4652 I00000000: I00000000: Archive: //10.1.2.13/CAD/\XXXXXXXXXXXXXXXX-087DD017-1FEE-4C89-875C-7B6750536824-23E20240-01CD-4484-9792-8694FF8DA8BEA
2019-01-29T21:00:54:779+01:00 4652 I00000000: Using ar_io_local to open '\\10.1.2.13\CAD\' with token 0000000000001F04
2019-01-29T21:01:24:267+01:00 4652 I00000000: <bold>Erstelle ein differentielles Backup </bold><endl/><tabpoint value=30><indent value=4>Von:     <indent value=10><textcolor value="navyblue">Laufwerk '1', Laufwerk '2'</textcolor></indent><indent value=4><endl/>Zu Datei:     <indent value=10><textcolor value="navyblue">"file://10.1.2.13/CAD/HG-SRV-CAD.hans-goetz.intra-087DD017-1FEE-4C89-875C-7B6750536824-23E20240-01CD-4484-9792-8694FF8DA8BEA.tibx"</textcolor></indent><indent value=4><endl/><textcolor value=0x00ff0000>Kennwortgeschützt</textcolor><endl/>Komprimierung:     <indent value=10><textcolor value="navyblue">Normal</textcolor></indent><indent value=4><endl/>Ausschluss:     <indent value=10><textcolor value="navyblue">Durch Ausschlussmaske erfasste Dateien</textcolor></indent><indent value=4><endl/>Kriterium:     <indent value=10><textcolor value="navyblue">*&#92;System Volume Information&#92;*{3808876B-C176-4e48-B7AE-04046E6CC752}; ...</textcolor></indent><indent value=4><endl/>Nach dem ersten Medium fragen:     <indent value=10><textcolor value="navyblue">Nein</textcolor></indent><indent value=4><endl/></indent>
2019-01-29T21:16:30:606+01:00 7500 E0135004E: Fehler 0x135004e: Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen.
| Ablaufverfolgungsebene: Fehler
| Channel: tol-activity#C764B0D9-B32B-43C0-B1DD-C167095983C3
| Zeile: 0x7564da35b0f1eaf3
| Datei: e:\21\enterprise\common\tol\activity_workshop.cpp:89
| Funktion: Tol::BaseRepairConditions::Result
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842356
| Datei: e:\21\core\winex\event_log.cpp:316
| Funktion: EventToCommonError
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842357
| Datei: e:\21\core\winex\event_log.cpp:317
| Funktion: EventToCommonError
| providerName: Application Error
| providerGUID:
| EventID: 0x3e8
| Channel: Application
| Computer:XXXXXXXXXXXX
| $module: mms_vsa64_11010
2019-01-29T21:16:30:616+01:00 7500 E01350016: Fehler 0x1350016: TOL: Failed to execute the command. Backup workflow
| Ablaufverfolgungsebene: Fehler
| Channel: tol-activity#C764B0D9-B32B-43C0-B1DD-C167095983C3
| Zeile: 0x8d165e86fb81959b
| Datei: e:\21\enterprise\common\tol\command\command.cpp:461
| Funktion: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: F30407D6-601F-11E0-9C67-FF46DFD72085
| $module: mms_vsa64_11010
|
| Fehler 0x1350016: TOL: Failed to execute the command. Backup workflow
| Zeile: 0x8d165e86fb81959b
| Datei: e:\21\enterprise\common\tol\command\command.cpp:461
| Funktion: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: F30407D6-601F-11E0-9C67-FF46DFD72085
| $module: gtob_backup_command_addon_vsa64_11010
|
| Fehler 0x1490002: Schritt 'Backup' ist fehlgeschlagen.
| Zeile: 0x8edc81ea38fabaa4
| Datei: e:\21\enterprise\managers\gtob\backupers\backup_command\impl\backup_workflow_command.cpp:664
| Funktion: `anonymous-namespace'::BackupWorkflowCommand::ProcessWorkflowSteps
| TraceLevel: 0x1
| StepType: 0x2
| $module: gtob_backup_command_addon_vsa64_11010
|
| Fehler 0x1350016: TOL: Failed to execute the command. Tol::IsolateCommand
| Zeile: 0x8d165e86fb81959b
| Datei: e:\21\enterprise\common\tol\command\command.cpp:461
| Funktion: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: 4504F8D4-2727-42AB-BB4F-A42EDBB790A0
| $module: mms_vsa64_11010
|
| Fehler 0x1350039: TOL: Process 'service_process.exe' has failed.
| Zeile: 0x997a6f2085ead0ae
| Datei: e:\21\enterprise\common\tol\isolate_command\isolate_command.cpp:144
| Funktion: Tol::`anonymous-namespace'::DisconnectCallback::OnDisconnected
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842356
| Datei: e:\21\core\winex\event_log.cpp:316
| Funktion: EventToCommonError
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842357
| Datei: e:\21\core\winex\event_log.cpp:317
| Funktion: EventToCommonError
| providerName: Application Error
| providerGUID:
| EventID: 0x3e8
| Channel: Application
| Computer: XXXXXXXXXXXXXXX
| $module: mms_vsa64_11010
2019-01-29T21:16:30:637+01:00 7500 E0135003D: Fehler 0x135003d: Befehl 'Backup-Plan 'HGCAD1v4d'' ist fehlgeschlagen.
| Ablaufverfolgungsebene: Fehler
| Channel: tol-activity#C764B0D9-B32B-43C0-B1DD-C167095983C3
| Zeile: 0x4a8728dc8a1c9583
| Datei: e:\21\enterprise\common\tol\gating_activity.cpp:221
| Funktion: Tol::`anonymous-namespace'::BusinessActivityTracker::OnCompleted
| $module: mms_vsa64_11010
|
| Fehler 0x1350016: TOL: Failed to execute the command. Backup-Plan 'HGCAD1v4d'
| Zeile: 0x8d165e86fb81959b
| Datei: e:\21\enterprise\common\tol\command\command.cpp:461
| Funktion: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: D332948D-A7A9-4E07-B76C-253DCF6E17FB
| $module: mms_vsa64_11010
|
| Fehler 0x1350016: TOL: Failed to execute the command. Backup-Plan 'HGCAD1v4d'
| Zeile: 0x8d165e86fb81959b
| Datei: e:\21\enterprise\common\tol\command\command.cpp:461
| Funktion: Tol::`anonymous-namespace'::MakeFailResult
| CommandID: D332948D-A7A9-4E07-B76C-253DCF6E17FB
| $module: agent_protection_addon_vsa64_11010
|
| Fehler 0x1330029: Ausführen des Befehls fehlgeschlagen.
| Zeile: 0xe6792a5ee190de2c
| Datei: e:\21\enterprise\managers\gtob\protection\agent_engine\protect_command.cpp:218
| Funktion: `anonymous-namespace'::ProtectCommand::SafeExecute
| $module: agent_protection_addon_vsa64_11010
|
| Fehler 0x1350035: 2 Aktivitäten konnten nicht erfolgreich abgeschlossen werden. Eine davon wird angezeigt.
| Zeile: 0x2e7e9e174f1fb719
| Datei: e:\21\enterprise\common\tol\replica\event_processor.cpp:110
| Funktion: Tol::`anonymous-namespace'::CreateCumulativeError
| FailCount: 0x2
| $module: agent_protection_addon_vsa64_11010
|
| Fehler 0x135004e: Die Aktivität ist aufgrund eines Dienst-Neustarts fehlgeschlagen.
| Zeile: 0x7564da35b0f1eaf3
| Datei: e:\21\enterprise\common\tol\activity_workshop.cpp:89
| Funktion: Tol::BaseRepairConditions::Result
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842356
| Datei: e:\21\core\winex\event_log.cpp:316
| Funktion: EventToCommonError
| $module: mms_vsa64_11010
|
| Fehler 0x142711: Name der fehlerhaften Anwendung: service_process.exe, Version: 12.5.1.11010, Zeitstempel: 0x5bc06a3f
| Name des fehlerhaften Moduls: MSVCR120.dll, Version: 12.0.21005.1, Zeitstempel: 0x524f83ff
| Ausnahmecode: 0xc0000409
| Fehleroffset: 0x0000000000074a30
| ID des fehlerhaften Prozesses: 0x2e0
| Startzeit der fehlerhaften Anwendung: 0x01d4b80d42e489d5
| Pfad der fehlerhaften Anwendung: C:\Program Files\Common Files\Acronis\BackupAndRecovery\Common\service_process.exe
| Pfad des fehlerhaften Moduls: C:\windows\SYSTEM32\MSVCR120.dll
| Berichtskennung: 1da4691a-3f5d-4ca2-b0e8-f9b7830e9960
| Vollständiger Name des fehlerhaften Pakets:
| Anwendungs-ID, die relativ zum fehlerhaften Paket ist:
| Zeile: 0xfb0b530e27842357
| Datei: e:\21\core\winex\event_log.cpp:317
| Funktion: EventToCommonError
| providerName: Application Error
| providerGUID:
| EventID: 0x3e8
| Channel: Application
| Computer: XXXXXXXXXX
| $module: mms_vsa64_11010
 
Marko

      
                
                
                    
                                                    Wed, 01/30/2019 - 12:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Andreas/Marko, you might be using the Acronis Backup 12.5. The products are siblings, but not twins, note that the build is 11010, while Acronis Backup Cloud here is 12110. The numerals may even intertwine, but the products are not compatible.
Please raise your issue through the support system at account.acronis.com

      
                
                
                    
                                                    Wed, 01/30/2019 - 13:43
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Andreas Kirschner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fedor,
 
you are right, i haven t noticed that all!
Sorry!

      
                
                
                    
                                                    Wed, 01/30/2019 - 14:38
