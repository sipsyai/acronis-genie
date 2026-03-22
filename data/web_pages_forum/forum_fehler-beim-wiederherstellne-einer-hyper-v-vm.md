# Fehler beim Wiederherstellne einer Hyper-V-VM

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/fehler-beim-wiederherstellne-einer-hyper-v-vm

## Original Post
**Author:** Unknown

Fehler beim Wiederherstellne einer Hyper-V-VM

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Thorsten Tipp
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Bin neu im Thema Acronis, habe sonst Veeam genutzt...
Jetzt bekomme ich beim Wiederherstellen mit Acronis Cyber Protect einer VM auf einem Hyper-V-Server ziemlich schnell folgende Fehler:
 

Virtuelle Maschine wird wiederhergestellt


Status:Fehler


Gestartet von:HYPER-V-01\Administrator


Startzeit:25. Februar 2025, 15:28:36


Abschlusszeit:25. Februar 2025, 15:29:24


Dauer:48 Sek.


Das Erstellen des Prüfpunkts der virtuellen Maschine auf der Hyper-V-Host-Ebene ist mit einem Microsoft-spezifischen Fehler fehlgeschlagen: Windows-Fehler: Der Task wurde mit Fehlern abgeschlossen.
 

Das Erstellen des Prüfpunkts der virtuellen Maschine auf der Hyper-V-Host-Ebene ist mit einem Microsoft-spezifischen Fehler fehlgeschlagen: Windows-Fehler: Der Task wurde mit Fehlern abgeschlossen.
Nachricht
Das Erstellen des Prüfpunkts der virtuellen Maschine auf der Hyper-V-Host-Ebene ist mit einem Microsoft-spezifischen Fehler fehlgeschlagen: Windows-Fehler: Der Task wurde mit Fehlern abgeschlossen.
Zusätzliche Informationen:
------------------------
Fehlercode: 20250646
Felder: {"$module":"mms_vsa64_39376","CommandID":"08FF37D8-FB90-49A3-828B-B9A8CDA417B3"}
Nachricht: TOL: Failed to execute the command. Eine virtuelle Maschine wiederherstellen
------------------------
Fehlercode: 20250646
Felder: {"$module":"disk_bundle_vsa64_39376","CommandID":"08FF37D8-FB90-49A3-828B-B9A8CDA417B3"}
Nachricht: TOL: Failed to execute the command. Eine virtuelle Maschine wiederherstellen
------------------------
Fehlercode: 7503969
Felder: {"$module":"disk_bundle_vsa64_39376"}
Nachricht: Fehler beim Wiederherstellen einer virtuellen Maschine.
------------------------
Fehlercode: 20250646
Felder: {"$module":"mms_vsa64_39376","CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0"}
Nachricht: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Fehlercode: 20250646
Felder: {"$module":"service_process_vsa64_39376","CommandID":"6F80C46F-90AC-4F6F-9578-3CAEF754A637"}
Nachricht: TOL: Failed to execute the command. Die komplette virtuelle Maschine wiederherstellen
------------------------
Fehlercode: 20250646
Felder: {"$module":"disk_bundle_vsa64_39376","CommandID":"6F80C46F-90AC-4F6F-9578-3CAEF754A637"}
Nachricht: TOL: Failed to execute the command. Die komplette virtuelle Maschine wiederherstellen
------------------------
Fehlercode: 7503972
Felder: {"$module":"disk_bundle_vsa64_39376"}
Nachricht: Die Wiederherstellung der kompletten virtuellen Maschine ist fehlgeschlagen.
------------------------
Fehlercode: 7503892
Felder: {"$module":"disk_bundle_vsa64_39376"}
Nachricht: Wiederherstellen der virtuellen Maschine 'EX01' mit ID 'vm:4C4D369E-CE41-4DDA-B975-2A8D3949BB2B?type%3dmshyperv' fehlgeschlagen.
------------------------
Fehlercode: 5439609
Felder: {"$module":"hv_srv_vsa64_39376"}
Nachricht: Die virtuelle Maschine 'EX01' konnte nicht vom konfigurierten Template erstellt werden.
------------------------
Fehlercode: 5439515
Felder: {"$module":"hv_srv_vsa64_39376"}
Nachricht: Hinzufügen des neuen Festplattenlaufwerks 'EX01_6_94D44B90-5CAE-4434-8904-ED10372F0555.vhdx' fehlgeschlagen.
------------------------
Fehlercode: 5439515
Felder: {"$module":"hv_srv_vsa64_39376"}
Nachricht: Fehler beim Hinzufügen eines neuen Laufwerks mit dem Namen 'EX01_6_94D44B90-5CAE-4434-8904-ED10372F0555.vhdx' an der Position (BusSCSI0:0).
------------------------
Fehlercode: 5439491
Felder: {"$module":"hv_srv_vsa64_39376"}
Nachricht: Hinzufügen der Ressource zur virtuellen Maschine fehlgeschlagen.
------------------------
Fehlercode: 5439627
Felder: {"$module":"hv_srv_vsa64_39376","ErrorCode":32775,"ErrorDescription":""EX01": Fehler beim Hinzufügen des Geräts "Synthetic Disk Drive" (ID des virtuellen Computers D2FCF924-6E08-4E99-B8D1-9F76C73C4C25).
"EX01": Die Speichermedien können nicht an den Controller angeschlossen werden, da der angegebene Ort bereits verwendet wird (ID des virtuellen Computers D2FCF924-6E08-4E99-B8D1-9F76C73C4C25).","TaskDescription":"Ressource wird hinzugefügt"}
Nachricht: Der Task wurde mit Fehlern abgeschlossen.
 
Was kann das sein?
Irgend welche Ideen?
 



      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/25/2025 - 15:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo!
Es sieht so aus, als ob beim Wiederherstellen der virtuellen Maschine auf deinem Hyper-V-Server ein Problem mit dem Hinzufügen von Festplatten und/oder der Ressourcenzuweisung aufgetreten ist. Der Fehlercode 5439609 und andere verwandte Fehler deuten auf Schwierigkeiten beim Hinzufügen von Festplatten und der Zuweisung von Speichergeräten hin. Hier sind einige mögliche Lösungsansätze:
1. Überprüfe die Konfiguration der virtuellen Maschine und die Ressourcen
Stelle sicher, dass der Hyper-V-Server über genügend Ressourcen (z. B. Speicher, Festplattenplatz) verfügt, um die virtuelle Maschine wiederherzustellen.
Überprüfe die Konfiguration der virtuellen Maschine (VM), insbesondere die Zuweisung der Festplatten und der Controller. Es könnte sein, dass die VM versucht, eine Festplatte an einem bereits verwendeten Controller- oder Bus-Port anzuschließen.
2. Stelle sicher, dass die Festplattendateien verfügbar sind
Überprüfe, ob die VHDX-Dateien der virtuellen Maschine, die wiederhergestellt werden soll, an dem angegebenen Speicherort vorhanden und zugänglich sind.
Achte darauf, dass der Hyper-V-Host Zugriff auf den Ordner hat, in dem sich die Festplattendateien befinden, und dass keine Berechtigungsprobleme bestehen.
3. Virtuelle Festplatte überprüfen
Der Fehlercode "Fehler beim Hinzufügen eines neuen Laufwerks" könnte darauf hindeuten, dass es ein Problem mit der VHDX-Datei gibt. Überprüfe, ob die VHDX-Datei korrekt und nicht beschädigt ist. Du könntest auch versuchen, eine neue virtuelle Festplatte zu erstellen und die VHDX-Datei darauf zu mounten.
4. Template und Festplattenanschluss prüfen
Stelle sicher, dass das verwendete Template für die VM mit der gewünschten Konfiguration kompatibel ist. Es kann auch helfen, eine virtuelle Maschine ohne ein Template zu erstellen und dann die Festplatten manuell hinzuzufügen.
5. Virtuelle Maschine im Hyper-V-Manager überprüfen
Versuche, die VM manuell im Hyper-V-Manager zu erstellen und dabei dieselben Festplatten hinzuzufügen. Überprüfe, ob der Fehler weiterhin auftritt.
6. Acronis-Backup und Hyper-V-Integration
Acronis Cyber Protect verwendet Hyper-V-spezifische Technologien, um virtuelle Maschinen zu sichern und wiederherzustellen. Stelle sicher, dass alle Hyper-V-Integrationstools auf dem Host und der VM korrekt installiert sind und die neueste Version verwenden.
7. Logs und zusätzliche Fehlercodes
Überprüfe die Acronis-Logs auf weitere Details zu den Fehlercodes. Insbesondere könnten zusätzliche Informationen aus den Fehlercodes "20250646" und "5439609" dabei helfen, die Ursache des Problems genauer zu identifizieren.
Falls das Problem weiterhin besteht, wäre es hilfreich, den Acronis Support zu kontaktieren, um das Problem weiter zu diagnostizieren, da sie möglicherweise spezifische Lösungen oder Patches haben, um diese Fehler zu beheben.
Lass mich wissen, wenn du weitere Hilfe benötigst!

      
                
                
                    
                                                    Tue, 02/25/2025 - 17:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
