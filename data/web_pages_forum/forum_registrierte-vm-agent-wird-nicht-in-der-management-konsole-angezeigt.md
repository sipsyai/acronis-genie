# Registrierte VM (Agent) wird nicht in der Management Konsole angezeigt

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/registrierte-vm-agent-wird-nicht-der-management-konsole-angezeigt

## Original Post
**Author:** Unknown

Registrierte VM (Agent) wird nicht in der Management Konsole angezeigt

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Guten Tag,
ich habe aktuell das Probelm das ich bei einer VM-Umgebung mit 11 Maschinen nur 10 in der Management Konsole sehe und sichern kann.
Bei der letzten VM ist es so das die Registrierung am ende des Agent-Setups in einem Time-Out endet.
Die Maschine per CMD-Befehl zu registrieren wird mit Erfolg bestätigt aber die VM wird nicht in der Konsole angezeigt.
(Siehe Bild = Nutzerdaten sind ausgeschwärzt )
Gibt es einen anderen Workaround der in einem solchen Fall helfen kann?
 
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      CMD-Befehl.PNG

                      77.22 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 09/25/2018 - 13:48

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes 
It's Evgeny from Acronis Service Provider Support.
As far as I understand you are facing an issue with the VM not appearing in the console although the machine registers correctly.
Please verify the below points:
Check for firewalls or anti-virus software.
Check connectivity to DC with Connection verification tool.
Try telnet to the AMS port received on previous step (full list of ports/names can be found in the following article)
If nothing helps you troubleshoot the root cause of the issue, please collect the offline sysinfo per the article  and submit a support ticket to us according to the Support Providers Guidelines.
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Tue, 09/25/2018 - 15:50
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Evgeny,
thanks for the information. 
The port check has put me on the right track.The affected VM belongs to a different cloud group in our system and the policy for the group has not been adjusted for the ports.2 necessary ports were not open.The part is done now.
Now I've created a new customer because it's a different cloud group. I do not receive any mail to activate the user.
@ acronis.com is listed under Trusted sender.Is not synonymous with spam / junk.
Is this problem known?

      
                
                
                    
                                                    Wed, 09/26/2018 - 11:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Johannes,
It's worth raising a support ticket for the issue with mails, seems to be related to the particular environment as we are not aware of any known issues affecting emails. 
Thank you, 

      
                
                
                    
                                                    Mon, 10/08/2018 - 15:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Johannes Weisgerber
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The solution was that the DCO admin found our mail-adress in the list "destination unreachable" on mailgun email service (www.mailgun.com). They removed it form this list and now the e-mail arrive again.

      
                
                
                    
                                                    Thu, 10/25/2018 - 12:25
