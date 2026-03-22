# Hyper-V Agent Backup mit Host und VMs in verschiedenen VLANs

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/hyper-v-agent-backup-mit-host-und-vms-verschiedenen-vlans

## Original Post
**Author:** Unknown

Hyper-V Agent Backup mit Host und VMs in verschiedenen VLANs

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Jörg Schwarzrock
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hallo,
ich schreibe die Frage auf Deutsch da ich diese damit besser formulieren kann.
Mein Plan ist:
----------------------------------------------------------
Hyper-V Host ( MS Server ) mit Hyper-V Agent : VLAN 1
- NAS VLAN 1
- USB RDX Laufwerk an Hyper-V Host
-----------------------------------------------------------
VMs : VLAN 2
-----------------------------------------------------------
Frage:
Hat ein einer VM zugewiesener Backup Plan Zugriff auf das NAS sowie das USB Laufwerk über den Agent ?
Über das Netzwerk geht ja nicht da unterschiedliche VLANs...
 
Oder muss der Backup Plan dem Hyper-V Host zugewiesen sein ?
-> Wäre in dem Fall teurer da eine VM zu sichern günstiger ist als einen Server
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/19/2023 - 14:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
Hallo!
Das hängt davon ab. Es gibt zwei Arten von Agenten für VMs: agentenloses Backup bedeutet, dass der Agent nur auf Hyper-V-Ebene installiert ist, oder Sie können einen regulären Agenten für Windows/Linux in jeder VM installieren. Die Agentenkomponenten verbinden die VM mit dem Backup-Speicherort. Wenn Sie die Geräte in verschiedenen VLANs verwenden, können Sie in Betracht ziehen, in jeder VM einen eigenen Agenten zu installieren. Das könnte wahrscheinlich helfen. Ich würde Ihnen vorschlagen, ein Ticket bei unserem Support unter https://support.acronis.com/ zu eröffnen, damit wir Ihnen weiterhelfen können. Beste Grüße.

      
                
                
                    
                                                    Tue, 12/19/2023 - 15:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
