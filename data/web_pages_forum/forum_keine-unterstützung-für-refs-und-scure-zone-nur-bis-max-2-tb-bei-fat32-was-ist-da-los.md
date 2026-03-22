# Keine Unterstützung für ReFS und Scure Zone nur bis max. 2 TB bei FAT32 - was ist da los?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/keine-unterstutzung-fur-refs-und-scure-zone-nur-bis-max-2-tb-bei-fat32-was-ist-da-los

## Original Post
**Author:** Unknown

Keine Unterstützung für ReFS und Scure Zone nur bis max. 2 TB bei FAT32 - was ist da los?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Drazen Uzelac
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Wir benötigen bei uns die ReFS-Unterstützung und möchten (unabhängig von ReFS) auf den Geräten jeweils die passwortgeschützte SECURE ZONE nutzen, aber ReFS wird nicht unterstützt und die SECURE ZONE nutzt intern das FAT32-Dateiformat, welches auf 2 TB limitiert ist. Ich nahm jetzt an, dass die SECURE ZONE, die wir extra auf einer 8 TB NVMe-SSD angelegt haben, sich selbstständig vergrößert oder bis zu 4 x 2 TB-Partitionen anlegt, damit die ganzen 8TB max. genutzt werden können, was wir auch per Schiebe-Regler auswählen konnten, aber das Backup wurde einfach abgebrochen! Wie kann das sein? In der heutigen Zeit sind doch 2 TB keine adäquate Backup-Größe. Also, wenn das heutzutage die Limits sind, dann kann doch eine Lizenz nicht > 1.000 € pro Server kosten?!? Ich sag mal 32 TB sollten mind. drin sein müssen für so eine SECURE ZONE. Und bitte nicht mit den Alternativen wie "Acronis Cyber Infrastructure" oder so kommen. Für eine schnellstmögliche Wiederherstellung sollte das Backup möglichst lokal verfügbar sein. Wo ist also das Problem, dass Acronis für Business-Zwecke so schlecht Up-To-Date ist?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/28/2024 - 15:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo!
Willkommen in unserem Forum.
Die Secure Zone ist mit dem FAT32-Dateisystem formatiert; andere Dateisysteme werden nicht unterstützt. Da FAT32 eine Dateigrößenbeschränkung von 4 GB hat, werden größere Backups beim Speichern in der Secure Zone automatisch aufgeteilt. Sie bleiben jedoch vollständig nutzbar, und dies beeinträchtigt weder die Wiederherstellungsprozedur noch die Geschwindigkeit.
Diese Funktion eignet sich am besten als Ziel für die Replikation von Backups, nicht jedoch als primärer Speicherort. Zum Beispiel werden Backups in Speicherort A gesichert, während die Secure Zone als Plan B dient, falls Speicherort A nicht verfügbar ist. Aus diesem Grund ist die Funktionalität eingeschränkt.
Weitere Informationen finden Sie hier:Über die Secure Zone - Acronis Cyber Protect 16
Ich habe ein Ticket mit unserem Team erstellt, um Ihre Anliegen genauer zu bearbeiten und eine passende Antwort zu liefern.
Sie werden so bald wie möglich kontaktiert.
Mit freundlichen Grüßen!

      
                
                
                    
                                                    Thu, 11/28/2024 - 18:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Drazen Uzelac
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Vielen Dank für die erste Rückinfo, aber dies war bereits bekannt. Es kann ja aber nicht sein, dass dies so bleibt. FAT32 mit seinen Limitierungen im Jahr 2024 als Basis für die SECURE Zone auf einem Laufwerk > 2TB zu nutzen, wäre ja nun bereits seit mehr als 10 Jahren nicht mehr zeitgemäß. Da hätte je bereits längst eine Anpassung an ein Dateisystem erfolgen müssen, welches mehr als 2 TB erlaubt. Und wenn es schon FAT32 sein muss, dann hätte das System beim Einrichten der SECURE ZONE auf einem 8TB-Laufwerk ja wenigstens 4 "SECURE ZONEs" hintereinander anlegen und verwalten können, so dass der gesamte Speicher auch nutzbar ist. Der Schieberegler in "Cyber Protect 16" lässt sich zumindest auf die vollen 7,86 TB schieben und es erfolgt bei der Einrichtung keine Fehlermeldung und kein Hinweis, dass die 7,86 TB nicht künftig genutzt werden (z. B. in mehreren aneinander gereihten SECURE ZONES). Schöner wäre natürlich auch auf dem gleichen PC in einer versteckten Partition, die auch vor einem Löschen geschützt ist, was bei der SECURE ZONE ja nicht der Fall ist.
Mit freundlichem Gruß!

      
                
                
                    
                                                    Fri, 11/29/2024 - 15:26
