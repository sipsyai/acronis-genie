# Upgrade to Version 16 Feedback

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-16-forum/upgrade-version-16-feedback

## Original Post
**Author:** Unknown

Upgrade to Version 16 Feedback

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I updated to version 16 today. My compliments, this worked without any problems, the amm server, the agents and also the VMware Virtual Appliances were updated without errors.
However, the backup replication to tape didn't work again:

Task timeout expired. The agent that is responsible for processing the task is not accessible.

Only after the timeout in the backup_manager.yml file under archiveReplicationTaskConfig was increased again did the tasks run again. Why not out of the box?
 
Unfortunately, in the new version, nothing is still displayed under "VM replication" under Activities of a plan. These activites can only be found in the dashboard/activities.
And here we come to the next difficulty. Hundreds of warnings from the index service appear there, so that you can no longer see the actual messages.
 
Message
Unbekanntes Backup 'C0F3F129-44A8-477F-92B8-E6364E269037' in Archiv 'C7C3D23A-80E2-48C1-96D5-179F61920747'.

Additional info:
------------------------
Error code: 23789587
Fields: {"$module":"gtob_indexer_commands_addon_vsa64_37391"}
Message: Backup 'bsp://backupsrv/Acronis.Backup.Depot#arl:/A511EC59-59E9-4249-A065-A51B5050A68E/C0F58FA2-838E-4885-A6D9-87979305B118/C7C3D23A-80E2-48C1-96D5-179F61920747/C0F3F129-44A8-477F-92B8-E6364E269037?archive_name%3dintranet-Archiv' will not be indexed because it is deleted.
------------------------
Error code: 21692460
Fields: {"$module":"gtob_indexer_commands_addon_vsa64_37391"}
Message: GXT: Computing has been aborted on the error item.
------------------------
Error code: 22741008
Fields: {"$module":"dms_provider_vsa64_37391"}
Message: Auflösen des Backup-Archivs fehlgeschlagen.
------------------------
Error code: 10551499
Fields: {"$module":"disk_bundle_vsa64_37391","IsReturnCode":1}
Message: Abrufen von Informationen über die Backups fehlgeschlagen.
------------------------
Error code: 2555975
Fields: {"$module":"storage_server_vsa64_37391","IsReturnCode":1}
Message: Fehler beim Abrufen von Informationen über Backups: 'bsp://backupsrv/Acronis.Backup.Depot/#arl:/A511EC59-59E9-4249-A065-A51B5050A68E/C0F58FA2-838E-4885-A6D9-87979305B118/C7C3D23A-80E2-48C1-96D5-179F61920747/C0F3F129-44A8-477F-92B8-E6364E269037?archive_name%3dintranet-Archiv'.
------------------------
Error code: 2555908
Fields: {"$module":"storage_server_vsa64_37391","IsReturnCode":1}
Message: Unbekanntes Backup 'C0F3F129-44A8-477F-92B8-E6364E269037' in Archiv 'C7C3D23A-80E2-48C1-96D5-179F61920747'.


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/27/2024 - 13:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for the feedback.
I suggest that you raise a ticket with our support team so that the entire situation is recorded, enabling the team to create tasks to address each issue accordingly: https://kb.acronis.com/content/8153
Best regards.
 
 
 
 

      
                
                
                    
                                                    Tue, 02/27/2024 - 13:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I had created tickets for all errors identified in the past. Providing all the data and the remote sessions were always very time-consuming. There was never a correct result or an improvement in a new version.
In addition to those mentioned above, the following errors also occur in the new version 16:
 

Error
Elasticsearch returned unsuccessful bulk response with code '400' and message 'failed to execute script'.


Activity 'Recovering virtual machine disks' failed. MFT bitmap is corrupted. 

Backup failed
Connection to VMware ESX(i) or vCenter server failed due to a network error: 'SOAP 1.1 fault "":ServerFaultCode[no subcode] "The object 'vim.VirtualMachine:vm-364148' has already been deleted or has not been completely created" Detail: <ManagedObjectNotFoundFault xmlns="urn:vim25" xsi:type="ManagedObjectNotFound"><obj type="VirtualMachine">vm-364148</obj></ManagedObjectNotFoundFault> '.
 

Activity 'Replikation' failed. XML-Parsing fehlgeschlagen. 


      
                
                
                    
                                                    Wed, 02/28/2024 - 07:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
We have raised a new ticket to investigate the issue.
The reference number is 06288130.
You can expect to be contacted by our support team as soon as possible.
Best regards.

      
                
                
                    
                                                    Wed, 02/28/2024 - 11:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jens
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            @cerberus
Das klingt für mich nicht Hoffnungsvoll.... Uns wird das Update auch aufgrund der Tape Replikationen empfohlen, aber scheinbar bringt es, wie gewohnt, mehr neue Probleme mit sich als Verbesserung.... Dein Lob beim Acronis Update in allen Ehren, das nächste Update wird wahrscheinlich wieder zu einer kompletten Neuinstallation führen :D....
English:
This doesn't sound hopeful to me... The update is also recommended to us because of the tape replications, but apparently, as usual, it brings more new problems than improvements.... All praise for the Acronis update, but the next update will likely result in a complete reinstall :D...
Grüße/Greetings

      
                
                
                    
                                                    Thu, 02/29/2024 - 10:34
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup Advanced 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jens wrote:

@cerberus
Das klingt für mich nicht Hoffnungsvoll.... Uns wird das Update auch aufgrund der Tape Replikationen empfohlen, aber scheinbar bringt es, wie gewohnt, mehr neue Probleme mit sich als Verbesserung.... Dein Lob beim Acronis Update in allen Ehren, das nächste Update wird wahrscheinlich wieder zu einer kompletten Neuinstallation führen :D....
English:
This doesn't sound hopeful to me... The update is also recommended to us because of the tape replications, but apparently, as usual, it brings more new problems than improvements.... All praise for the Acronis update, but the next update will likely result in a complete reinstall :D...
Grüße/Greetings


Hello!
As mentioned earlier, if issues are not reported, they will not be documented in our records. Tasks will be created accordingly based on their volume to address them. Therefore, creating tickets is indeed helpful. If you have any queries or technical issues you would like to report, kindly submit them at https://kb.acronis.com/content/8153.
Best regards.
 

      
                
                
                    
                                                    Thu, 02/29/2024 - 12:14
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jens
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 7
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok...We have now also installed the update to version 16. The update itself ran smoothly and everything seemed fine at least. Unfortunately, a lot was not backed up last night, almost 50% in one Vault:
MESSAGE
Cannot write data to the backup file '_.tibx'.
[...]
Error code: 262157
Fields: {"$module":"common_archive_addon_vsa64_37427"}
Message: The file is corrupted.
------------------------
Error code: 43717515
Fields: {"$module":"common_archive_addon_vsa64_37427","function":"archive_open","path":"_.tibx"}
Message: Data is corrupted: CRC mismatch or internal data structures mismatch
 
I will open a ticket as soon as possible. But first, we need to catch up on all the backups in a new vault... Ah, and one more thing to note... Replication is now functioning

      
                
                
                    
                                                    Fri, 03/01/2024 - 07:32
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup Advanced 15
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jens wrote:

Ok...We have now also installed the update to version 16. The update itself ran smoothly and everything seemed fine at least. Unfortunately, a lot was not backed up last night, almost 50% in one Vault:
MESSAGE
Cannot write data to the backup file '_.tibx'.
[...]
Error code: 262157
Fields: {"$module":"common_archive_addon_vsa64_37427"}
Message: The file is corrupted.
------------------------
Error code: 43717515
Fields: {"$module":"common_archive_addon_vsa64_37427","function":"archive_open","path":"_.tibx"}
Message: Data is corrupted: CRC mismatch or internal data structures mismatch
 
I will open a ticket as soon as possible. But first, we need to catch up on all the backups in a new vault... Ah, and one more thing to note... Replication is now functioning


The error does not appear to be related to this version of the backup or to a specific bug. Instead, it appears to be a generic error that could indicate corruption within the backup chain or issues with the disk (or one disk).
You could validate the backup to determine if it has been corrupted or not. If the backup appears to be intact, consider running a disk report on the affected machine, which can be found at: https://kb.acronis.com/content/1638
If the report indicates the presence of the letter "E," it signifies that the respective drive may have issues that need to be addressed.
Thank you in advance for your cooperation!

      
                
                
                    
                                                    Fri, 03/01/2024 - 16:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            If two people independently upgrade to version 16 and end up with corrupt archives, what is most likely to be the cause?
Definitely not a hardware failure. All the backup functions have become far too unreliable. We have now discovered that backup replication to another NAS has not been running since December 2023. No report on this. I think expectations and reality are now very far apart here.
Incidentally, this morning I rediscovered my good old friend, the Backup to Tape error. So this isn't fixed in version 16 after all....
 
03. März 2024, 14:18 Aktivität fehlgeschlagen
Die Aktivität 'Replikation' ist fehlgeschlagen. Backup '8D5C382B-22CC-4688-ADAB-05CD339B0D37' kind mismatching. Initially created as DIFF but now become as FULL.
 

      
                
                
                    
                                                    Mon, 03/04/2024 - 07:10
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Short feedback, support recorded all the data and created a ticket for each error. I'm curious what the result will be.

      
                
                
                    
                                                    Wed, 03/06/2024 - 14:28
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            cerberus wrote:

Short feedback, support recorded all the data and created a ticket for each error. I'm curious what the result will be.


Hello!
You can expect a reply from our support as soon as possible.
Thanks in advance! 

      
                
                
                    
                                                    Thu, 03/07/2024 - 11:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cerberus
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 12
                
            
            
                
                    Comments: 32
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Acronis released version 16 (released 2/21/2024) before Service Pack 6 of version 15 (released 2/28/2024).
However, this must be installed before the upgrade. It's just a shame that it wasn't available at the time.
Last update: 13-03-2024:https://kb.acronis.com/content/73388
Many of my errors are said to have their origins in this. Currently I keep having corrupt archives. This is of course unacceptable for backup software.
Backup is corrupted. Some data in the backup 'bsp://backupsrv/Acronis.Backup.Depot#arl:/A511EC59-59E9-4249-A065-A51B5050A68E/C0F58FA2-838E-4885-A6D9-87979305B118/4CFA62C6-38DD-4C8D-BEB6-9D1B28494E2E/30E990F0-EDFD-4C81-9711-E20AC522004D/arl:/A511EC59-59E9-4249-A065-A51B5050A68E/C0F58FA2-838E-4885-A6D9-87979305B118/4CFA62C6-38DD-4C8D-BEB6-9D1B28494E2E/30E990F0-EDFD-4C81-9711-E20AC522004D' might be damaged because of hardware problems.

 
I should get money for using this software, compensation for pain and suffering 

      
                
                
                    
                                                    Mon, 03/18/2024 - 08:22
