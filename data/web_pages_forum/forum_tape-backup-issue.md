# Tape backup Issue

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/tape-backup-issue

## Original Post
**Author:** Unknown

Tape backup Issue

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mahesh Kumar
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
We are doing file level backup to tape while performing getting below error.
 
Event 0x900001: Error code: 14
| Task 'Full backup' execution failed: Error 0x1350016: TOL: Failed to execute the command. Backing up
| | line: 0x8d165e86fb8195bd
| | file: d:\649\enterprise\common\tol\command\command.cpp:495
| | function: Tol::`anonymous-namespace'::MakeFailResult
| | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4
| | $module: service_process_vsa64_29486
| |
| | error 0x1350016: TOL: Failed to execute the command. Backing up
| | line: 0x8d165e86fb8195bd
| | file: d:\649\enterprise\common\tol\command\command.cpp:495
| | function: Tol::`anonymous-namespace'::MakeFailResult
| | CommandID: 8F01AC13-F59E-4851-9204-DE1FD77E36B4
| | $module: gtob_backup_command_addon_vsa64_29486
| |
| | error 0x1490003: Backup has failed.
| | line: 0x1cd98aae889424f9
| | file: d:\649\enterprise\managers\gtob\util\impl\convert_batch_result.cpp:58
| | function: Gtob::Backup::ConvertBatchResult
| | $module: disk_bundle_vsa64_29486
| |
| | error 0x10424
| | line: 0xba19e88dc5fea152
| | file: d:\649\processor\backup\backup_file.cpp:1017
| | function: DaProcessor::Backup::_DoFileOperation
| | $module: disk_bundle_vsa64_29486
| |
| | error 0x29b138d: Unknown error occurred while backing up.
| | line: 0xba19e88dc5fea150
| | file: d:\649\processor\backup\backup_file.cpp:1015
| | function: DaProcessor::Backup::_DoFileOperation
| | $module: disk_bundle_vsa64_29486
| |
| | error 0x29b138d: Input/output error
| | line: 0x5f25c37074a5443a
| | file: d:\649\processor\backup\archive3_file_backup.cpp:745
| | function: `anonymous-namespace'::Archive3FileBackupBuilder::Write::<lambda_12c6d440454d3a29a3d77f17eef56b07>::operator ()
| | function: file_backup_run
| | path: bsp://172.28.59.101/FTO9-MONTHLYTAPEPOOL-NEW/arl:/E0A14A1E-CEC3-4C0C-9994-DB70974A9880/778E81A5-68EB-4A39-9E8A-21AD3913C015/31BEAA61-FAAE-4F55-A0B4-9153BEF52C15
| | $module: disk_bundle_vsa64_29486
| |
| | error 0x40003: Error occurred while writing to the file.
| | line: 0xe59fb8961c9299
| | file: d:\653\enterprise\rsm\streams\multiplexing.cpp:193
| | function: Tapes::Multiplexer::Stream::Write
| | $module: arsm_vsa64_29486
| |
| | error 0x29b138d: Input/output error
| | line: 0xe59fb8961c9298
| | file: d:\653\enterprise\rsm\streams\multiplexing.cpp:192
| | function: Tapes::Multiplexer::Stream::Write
| | function: archive_stream_write
| | path: /tape/Acronis/B190168D-7A49-4C60-9A91-63FB3872D671
| | $module: arsm_vsa64_29486
| |
| | error 0x40005: Error occurred while searching in the file.
| | line: 0xc41defba28f4d0c2
| | file: d:\653\core\backup\tape_device.cpp:261
| | function: OSTapeDrive::Rewind
| | $module: arsm_vsa64_29486
| |
| | error 0xfff0: The device has indicated that cleaning is required before further operations are attempted
| | line: 0xbd28fdbd64edb8f8
| | file: d:\653\core\common\error.cpp:314
| | function: Common::Error::AddWindowsError
| | code: 0x8007048d
| | $module: arsm_vsa64_29486
| trace level: error
 
Please suggest the solution for this issue.
 
Attached screenshots for better understanding.

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      MicrosoftTeams-image (1).png

                      780.81 KB
                  
              
                      MicrosoftTeams-image (2).png

                      824.12 KB
                  
              
                      MicrosoftTeams-image.png

                      779.43 KB
                  
              
                      Screenshot (133).png

                      313.79 KB
                  
              
                      Screenshot (132).png

                      306.13 KB
                  
              
                      Screenshot (131).png

                      292.82 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 08/23/2022 - 10:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Mahesh Kumar,
Thank you for the question, we have forwarded it to the MSP support team and will answer you as soon as we get more details.

      
                
                
                    
                                                    Tue, 08/23/2022 - 11:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kristian Popov
                            

                            
                    
                        Acronis Support Engineer
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 19
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Mahesh,
I would like to provide you with a few KB articles, which you can check out and see which one best fits your scenario:
- https://kb.acronis.com/content/60976
- https://kb.acronis.com/content/62916
- https://kb.acronis.com/content/56541
If the issue still persists, please collect the following logs and open a support case, in order for us to investigate further:
- https://kb.acronis.com/content/54608
Regarding the case opening, you can send an email to "mspsupport@acronis.com" along with the filled-out template https://www.acronis.com/en-eu/support/serviceprovidertemplate/
Or you can open a case through the portal https://kb.acronis.com/content/56079

      
                
                
                    
                                                    Tue, 08/23/2022 - 11:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Kristian Popov | Acronis Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Daria Sorokina
                            

                            
                    
                        Acronis Support
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 487
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Mahesh Kumar,
Please let us know was your problem that you presented here resolved if yes, what helped you?

      
                
                
                    
                                                    Tue, 09/20/2022 - 12:39
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards, Daria Sorokina | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
