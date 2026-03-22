# error when making backup Network disconnected by timeout

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-when-making-backup-network-disconnected-timeout

## Original Post
**Author:** Unknown

error when making backup Network disconnected by timeout

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Failed to open backup 'avfs:/online?account%3dgomides.eustaquio%2540ctcfranquias.com.br%26computer%3d1%26provider%3dAcronis#arl:/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000/3079CF34-D297-565D-2B9A-10630DF2AB44/98FC97CA-EB1C-4ACF-882D-7EAFEEAA2305?archive_name%3dSRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A' for browse.

Additional info:
------------------------
Error code: 244
Module: 161
LineInfo: 0x0B320396ADFE3D5F
Fields: {"$module":"disk_bundle_lxa64_10790","IsReturnCode":"1"}
Message: Failed to open backup 'avfs:/online?account%3dgomides.eustaquio%2540ctcfranquias.com.br%26computer%3d1%26provider%3dAcronis#arl:/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000/3079CF34-D297-565D-2B9A-10630DF2AB44/98FC97CA-EB1C-4ACF-882D-7EAFEEAA2305?archive_name%3dSRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A' for browse.
------------------------
Error code: 8
Module: 161
LineInfo: 0x0AF9C3BAFC04E507
Fields: {"$module":"disk_bundle_lxa64_10790"}
Message: Cannot browse the specified backup.
------------------------
Error code: 8
Module: 161
LineInfo: 0x0AF9C3BAFC04E540
Fields: {"$module":"disk_bundle_lxa64_10790"}
Message: Cannot browse the specified backup.
------------------------
Error code: 507
Module: 64
LineInfo: 0xA1D3981537C68833
Fields: {"$module":"disk_bundle_lxa64_10790","id":"SRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A.tibx"}
Message: Failed to open the backup archive by the ID.
------------------------
Error code: 853
Module: 64
LineInfo: 0x6A1198D1B8BE2C36
Fields: {"$module":"disk_bundle_lxa64_10790"}
Message: Failed to open archive 'SRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A.tibx'.
------------------------
Error code: 2
Module: 64
LineInfo: 0x68F47D89A6C2B91A
Fields: {"$module":"disk_bundle_lxa64_10790","path":"SRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A.tibx"}
Message: Failed to open the archive for reading.
------------------------
Error code: 7
Module: 4
LineInfo: 0x60CCAC0523AC0F47
Fields: {"PcsCode":"13","$module":"archive3_adapter_lxa64_10790","Name":"SRV_CONSTANCE-EB1EC11C-B5E1-4866-A965-ADA4E90DE2FF-4BED14A5-81D9-44A1-BEB5-4C024A42DA45A.tibx"}
Message: Error occurred while opening the file.
------------------------
Error code: 22
Module: 4
LineInfo: 0xC8D8731CE106FA0A
Fields: {"$module":"archive3_adapter_lxa64_10790"}
Message: Network disconnected by timeout.
OK

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 10/09/2018 - 10:16

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Suporte,
 
It's Evgeny from Acronis Service Provider Support. Your ticket has been assigned to me and I will allocate the appropriate resources in order to lead the ticket to resolution. 
As far as I understand you are facing an issue with sporadic backup failures for one PC.
The error itself indicates a network disconnection, but as the message is generic we will rework the way we handle them in Acronis Data Cloud 8.0 (internal reference will be ABR-193696).
To investigate the current cause of the issue we will ask you to submit a support ticket per https://www.acronis.com/en-us/support/serviceprovidertemplate/
Please make sure to provide Wireshark log collected when you reproduce the issue and also provide the online certificate 
It will help us check the MMS.log as well as see more details about the archive itself.
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup

      
                
                
                    
                                                    Tue, 10/09/2018 - 11:35
