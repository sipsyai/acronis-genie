# Backup of Hyper- V Host creates EventIDs in Guest - How can I Install SQL Agent ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/backup-hyper-v-host-creates-eventids-guest-how-can-i-install-sql-agent

## Original Post
**Author:** Unknown

Backup of Hyper- V Host creates EventIDs in Guest - How can I Install SQL Agent ?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hey there,
I use Cyber Protect Backup 16, most recent version on Management Server and all Clients.
There is a Windows Server 2022 Hypwer-V Host with underlying Windows Server 2022 VM servers.
One of these servers is a Remote Desktop Session Host with Remote Desktop Connection Broker.
As you might know, this RDCB uses the Windows Internal Database (WID).
During a normal backup of the VM (I use the agent within the V) everything seems tobe OK.
If I backup the HyperV I get several Eventlog entries in the VM:
- 12293 VSS
- 1 WIDVDI
- 3041, 18210 MSSQL$MICROSOFT##WDI- 24583 WIDWRITER
Several searches gave me the hint to install the SQL Agent within the VM.
But I cannot do so, as the installer states, that this agent cannot be installed.
Any hints to so so?
Or simply ignore these Eventlog Entries in the VM ?
Regards
S.
.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 01/11/2026 - 15:58

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases


            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sven.
This behavior is expected.
The Windows Internal Database (WID) used by the Remote Desktop Connection Broker does not support SQL Server Agent, and it cannot be installed. Therefore, any guidance suggesting to install SQL Agent does not apply to WID-based deployments.
When backing up the Hyper-V host, Hyper-V Production Checkpoints trigger guest VSS writers, including the WID writer. The resulting Event IDs (12293, WIDVDI, MSSQL$MICROSOFT##WID, WIDWRITER) are informational and commonly observed during host-level, VSS-based backups.
If the backups complete successfully and no restore issues are observed, these events can be safely ignored. No additional configuration inside the VM is required.
Regards,

      
                
                
                    
                                                    Mon, 01/12/2026 - 12:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    SvenT
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 68
                
            
            
                
                    Comments: 232
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hey Jose,
The strange stuff ist:
One of the VMs has a small SQL Server Express für the managementserver of my Antivir but also 2 WID instances. One for WSUS and the other WID instance is for the AMS.
Due to the SQL Sevrer Express, the SQL agent is installed in that VM and during a Hyper-V host backup the WID writer events does not occur....
SO my assumption was, that teh SQL agent prevents this.
S.
 

      
                
                
                    
                                                    Mon, 01/12/2026 - 12:50
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Backup Advanced 15/16 in professional usecases
