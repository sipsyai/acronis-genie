# Acronis Having trouble with Network Archive

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-having-trouble-network-archive

## Original Post
**Author:** Unknown

Acronis Having trouble with Network Archive

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    René Haus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a Problem with Acronis Cloud Backup local archive, i hope somebody has an idea how to fix it or what else to try.
Since the Initial Backup was very big and took almost a month and several tries to finish i would like to avoid another full backup.Since the First Backup was sucsessfully completed, every backup job ends with Warning and the following message :
 
00000000: Failed to resolve instances for slice '//NAS01/Backup/#arl:/7C2505E9-A3EA-4664-AC3D-0B092946ACD2/C62A6C03-012B-4EAA-97B5-9500D7CB8B02/0DFD1CF8-964B-4836-AB1E-6C1DB82F8EC1/1D67FB5B-0A04-42C8-B0A8-3FE82EC84846?archive_name%3dMYSERVERNAME.MYDOMAINNAME.local-926ED3DA-5C22-4C49-B7E5-EFD13AE330D2-F2524BB9-A6FA-4595-8A72-F9C295A691AEA': Fehler 0xf90004: ASYNC: Unidentified job.
 
The Backups themself seem to work fine, browsing the backup works without a hitch.
I allready tried to fix it by running acrocmd validate archive and by deleting the xml file inside the archiv.
Neither helped and the job keeps finnishing sucsessfull with the warning.
 
Full log :
Message
E00000000: Failed to resolve instances for slice '//NAS01/Backup/#arl:/7C2505E9-A3EA-4664-AC3D-0B092946ACD2/C62A6C03-012B-4EAA-97B5-9500D7CB8B02/0DFD1CF8-964B-4836-AB1E-6C1DB82F8EC1/1D67FB5B-0A04-42C8-B0A8-3FE82EC84846?archive_name%3dMYSERVER.MYDOMAIN.local-926ED3DA-5C22-4C49-B7E5-EFD13AE330D2-F2524BB9-A6FA-4595-8A72-F9C295A691AEA': Fehler 0xf90004: ASYNC: Unidentified job.
Zeile: 0xd9612b4aaebb8e3f
Datei: k:\3917\enterprise\common\async\base_job.cpp:40
Funktion: Async::BaseJob::Describe
$module: dms_provider_vsa64_3917
Fehler 0xf9000b: ASYNC: Exception has occurred during work execution.
Zeile: 0x30ad4f7563758c53
Datei: k:\3917\enterprise\common\async\synchronous_action.cpp:32
Funktion: Async::SynchronousAction::Perform
$module: dms_provider_vsa64_3917
Fehler 0x5b001b: Durchsuchen des Backup-Archivs fehlgeschlagen.
Zeile: 0x5422297212e055b2
Datei: k:\3917\enterprise\applications\msexchange\managers\archive\archive_browser_engine.cpp:326
Funktion: `anonymous-namespace'::MsExchangeArchiveBrowsingEngine::GetInformationStoreInfo
IsReturnCode: 0x1
$module: arx_agent_vsa64_3917
Fehler 0xa100d4: Archiv 'MYSERVER.MYDOMAIN.local-926ED3DA-5C22-4C49-B7E5-EFD13AE330D2-F2524BB9-A6FA-4595-8A72-F9C295A691AEA' konnte nicht gefunden werden.
Zeile: 0xb320396adfe3ea3
Datei: k:\3917\enterprise\mms\managers\archive\impl\private_manager.cpp:1022
Funktion: ArchiveManagement::PrivateArchiveManager::FindArchive
IsReturnCode: 0x1
$module: disk_bundle_vsa64_3917
Fehler 0x400024: Einstellen der Anmeldedaten für den Backup-Speicherort fehlgeschlagen.
Zeile: 0x97675718d2b52ce6
Datei: k:\3917\enterprise\backup\places2\impl\utils.cpp:68
Funktion: Places::SetCredentialsOnDir
path: /
user: administrator
$module: disk_bundle_vsa64_3917

Fehler 0x40007: Fehler beim Öffnen der Datei.
Zeile: 0xbd01591c540a1422
Datei: k:\3917\file\windows\winnt_net.cpp:850
Funktion: winnt_net_dir::IOCTL
$module: disk_bundle_vsa64_3917
I Hope anybody has an idea what else i can do to fix this.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/31/2017 - 12:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    René Haus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Further investigation shows that the Backup is failing to do a Appliaction Backup of the Exchange Server.
 

      
                
                
                    
                                                    Mon, 07/31/2017 - 15:45
