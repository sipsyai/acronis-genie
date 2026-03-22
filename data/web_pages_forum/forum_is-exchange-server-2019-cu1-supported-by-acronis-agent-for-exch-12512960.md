# Is Exchange Server 2019 CU1 supported by Acronis Agent  for Exch. 12.5.12960 ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/exchange-server-2019-cu1-supported-acronis-agent-exch-12512960

## Original Post
**Author:** Unknown

Is Exchange Server 2019 CU1 supported by Acronis Agent  for Exch. 12.5.12960 ?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Patrick_Berlin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I get the following error:
Backup ist fehlgeschlagen
Cannot collect the metadata of Microsoft Exchange Server. Microsoft Exchange Server is not installed or has an unsupported version. Applikations-Backup ist für Microsoft Exchange Server 2007 (oder höher) verfügbar.
Fehlercode: 143
Modul: 91
Zeileninfo: 0x9CA236D7861B06B8
Felder: {"$module":"arx_agent_fork_vsa64_12960"}
Nachricht: Cannot collect the metadata of Microsoft Exchange Server. Microsoft Exchange Server is not installed or has an unsupported version. Applikations-Backup ist für Microsoft Exchange Server 2007 (oder höher) verfügbar.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 07/07/2019 - 07:08

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Patrick_Berlin
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fehlercode 0x01350016+0x01350016+0x00A100FC+0x01490003+0x00010424+0x01350016+0x01350016+0x005B008F

      
                
                
                    
                                                    Sun, 07/07/2019 - 07:12
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Patrick,
welcome to Acronis forums! 
Currently, only the following Exchange versions are supported in Acronis Cyber Cloud products:
Microsoft Exchange Server 2016 – all editions. 
Microsoft Exchange Server 2013 – all editions, Cumulative Update 1 (CU1) and later. 
Microsoft Exchange Server 2010 – all editions, all service packs. Recovery of mailboxes and mailbox items is supported starting with Service Pack 1 (SP1). 
Microsoft Exchange Server 2007 – all editions, all service packs. Recovery of mailboxes and mailbox items is not supported. 
https://www.acronis.com/support/documentation/BackupService/index.html#33049.html 
Clustered SQL and Exchange support (Exchange 2019) is planned to be implemented in version 8.0 (Acronis Cyber Cloud 7.9 is the current one). Internal ID for reference is ABR-186816.

      
                
                
                    
                                                    Mon, 07/08/2019 - 14:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
