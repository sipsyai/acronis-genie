# Cloud Backup erkennt Exchange DB nicht

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/cloud-backup-erkennt-exchange-db-nicht

## Original Post
**Author:** Unknown

Cloud Backup erkennt Exchange DB nicht

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo zusammen,
 
ich habe jetzt schon mehrere male den Agent deinstalliert und neu aufgespielt. Den Server an sich erkennt er in der Management Konsole. Unter Exchange allerdings, taucht der Server nur sehr sporadisch auf. Eine Datenbank des Exchange erkennt er aber trotz der Exchange Erweiterung nicht.
 
Woran kann das liegen? System ist ein SBS2011.
 
 
Besten Dank und Gruß,
Philip

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      1.PNG

                      31.16 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/13/2017 - 08:10

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Oliver,
Vielen Dank für die Anfrage
Ich empfehle Ihnen, zunächst diese Voraussetzungen zu überprüfen:
https://kb.acronis.com/content/56202
https://dl.managed-protection.com/u/baas/help/7.5/user/en-US/index.html…
https://dl.managed-protection.com/u/baas/help/7.5/user/en-US/index.html…
Wenn das Problem weiterhin besteht, wenden Sie sich an den Support

      
                
                
                    
                                                    Wed, 12/13/2017 - 09:30
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hallo Eugene,
 
alles so probiert. Funktionieren tut es immer noch nicht. Der Server taucht kurz unter Exchange auf, verschwindet dann aber wieder?
 
Nach neuladen der Seite ist er wieder im Acronis zu sehen?
 
 

      
                
                
                    
                                                    Wed, 12/13/2017 - 13:20
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Wenn der Server wieder in der Exchange-Ansicht ist, versuchen Sie, einen Sicherungsplan zu konfigurieren.
Sag mir bitte, wenn der Plan erfolgreich ist.
Wenn der Server weiterhin aus der Exchange-Ansicht verschwindet, müssen Sie unbedingt den Systembericht (KB https://kb.acronis.com/content/54608) von diesem Agenten dem Support-Team anzeigen.

      
                
                
                    
                                                    Wed, 12/13/2017 - 13:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Oliver Heymanns
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Den Sicherungsplan kann ich aber nur konfigurieren, wenn ich auf den Server klicke. Sobald ich das mache kommt die Meldung das keine Elemente angezeigt werden können. Dort würden ja dann normalerweise die Datenbanken auftauchen. Tun sie aber nicht...
 
Gruß

      
                
                
                    
                                                    Wed, 12/13/2017 - 13:54
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Aha. Sie müssen sich an das Support-Team wenden.

      
                
                
                    
                                                    Wed, 12/13/2017 - 13:59
