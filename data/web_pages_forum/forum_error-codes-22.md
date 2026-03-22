# Error codes 22

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/error-codes-22

## Original Post
**Author:** Unknown

Error codes 22

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    michal luczak
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, does anybody know, how to stop this from happening?
 
Backup is corrupted. Some data in the backup 'PC-BIZ-03-82ABC712-2682-4A59-8468-ED528F69A6BA-F35179C2-5E48-430E-A01F-E3E360C99D93A.tibx' might be damaged because of hardware problems.
DATE AND TIME
May 28, 2021, 09:15:52
MODULE
309
MESSAGE
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8d165e86fb8195bd
Fields: {"$func":"Tol::`anonymous-namespace'::MakeFailResult","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"ervice_process_vsa64_24647","$file":"d:\\642\\enterprise\\common\\tol\\command\\command.cpp","$line":"495"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 22
Module: 309
LineInfo: 0x8d165e86fb8195bd
Fields: {"$func":"Tol::`anonymous-namespace'::MakeFailResult","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4","$module":"tob_backup_command_addon_vsa64_24647","$file":"d:\\642\\enterprise\\common\\tol\\command\\command.cpp","$line":"495"}
Message: TOL: Failed to execute the command. Backing up
------------------------
Error code: 212
Module: 161
LineInfo: 0xb320396adfe3e12
Fields: {"$func":"ArchiveManagement::PrivateArchiveManager::FindArchive","IsReturnCode":"1","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\mms\\managers\\archive\\impl\\private_manager.cpp","$line":"877"}
Message: Failed to find archive 'PC-BIZ-03-82ABC712-2682-4A59-8468-ED528F69A6BA-F35179C2-5E48-430E-A01F-E3E360C99D93A'.
------------------------
Error code: 201
Module: 161
LineInfo: 0xd5796a33131eeb9c
Fields: {"$func":"ArchiveManagement::MetaInfoCache::GetArchivesInfo","$line":"166","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\mms\\managers\\archive\\meta_info_cache\\meta_info_cache.cpp"}
Message: Failed to get information about the archives.
------------------------
Error code: 803
Module: 349
LineInfo: 0xa14d72eeb8f971ae
Fields: {"$func":"AppBackup::Concurrency::Task::Execute","$line":"51","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\applications\\include\\common\\concurrency\\task.h"}
Message: Failed to execute a task.
------------------------
Error code: 803
Module: 349
LineInfo: 0xa14d72eeb8f971ae
Fields: {"$func":"AppBackup::Concurrency::Task::Execute","$line":"51","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\applications\\include\\common\\concurrency\\task.h"}
Message: Failed to execute a task.
------------------------
Error code: 507
Module: 64
LineInfo: 0xa1d3981537c68833
Fields: {"id":"PC-BIZ-03-82ABC712-2682-4A59-8468-ED528F69A6BA-F35179C2-5E48-430E-A01F-E3E360C99D93A.tibx","$func":"Backup::Impl::OpenArchiveById","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\backup\\impl\\location_impl.cpp","$line":"821"}
Message: Failed to open the backup archive by the ID.
------------------------
Error code: 853
Module: 64
LineInfo: 0x6a1198d1b8be2c36
Fields: {"$func":"`anonymous-namespace'::OpenArchive","$line":"242","$module":"isk_bundle_vsa64_24647","$file":"d:\\642\\enterprise\\backup\\impl\\archive_data_creator.cpp"}
Message: Failed to open archive 'PC-BIZ-03-82ABC712-2682-4A59-8468-ED528F69A6BA-F35179C2-5E48-430E-A01F-E3E360C99D93A.tibx'.
------------------------
Error code: 13
Module: 4
LineInfo: 0x8af64b2c0920f7ee
Fields: {"$func":"`anonymous-namespace'::ConvertArchive3Error","$line":"176","$module":"ommon_archive_addon_vsa64_24647","$file":"d:\\642\\core\\resizer\\archive3\\archive3_error.cpp"}
Message: The file is corrupted.
------------------------
Error code: 5003
Module: 667
LineInfo: 0xc3bc4c1eb2299b14
Fields: {"$func":"`anonymous-namespace'::CoOpenArchive","$module":"ommon_archive_addon_vsa64_24647","function":"archive_open","path":"PC-BIZ-03-82ABC712-2682-4A59-8468-ED528F69A6BA-F35179C2-5E48-430E-A01F-E3E360C99D93A.tibx","$line":"362","$file":"d:\\642\\enterprise\\applications\\archiving\\storages\\archive3\\src\\archive3.cpp"}
Message: Data is corrupted: CRC mismatch or internal data structures mismatch

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/27/2021 - 23:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day Michal
The error Data is corrupted: CRC mismatch or internal data structures mismatch usually refers to the backup archive being corrupted
This is usually noted when backing up to a local storage device such as a NAS etc.
Possible causes for this error are as follows:
1. Constant network issues where network drops during data transfer
2. Memory module corruption, especially on a NAS device can cause this issue
3. Storage corruption where the drives themselves become corrupt
To resolve this or attempt to do so I would recommend the following:
1. Perform a memory test on the RAM modules
2. You can also run check disk commands on the disks to verify that they are healthy
3. Lastly you can attempt to run the same backup to another location and see if that works.
Kind regards

      
                
                
                    
                                                    Mon, 05/31/2021 - 12:20
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
