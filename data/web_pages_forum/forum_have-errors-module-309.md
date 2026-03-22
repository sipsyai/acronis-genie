# Have errors module 309.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/have-errors-module-309

## Original Post
**Author:** Unknown

Have errors module 309.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    TOO ТК Мегаполис-Казазстан Щербина А.С.
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            МОДУЛЬ
309
СООБЩЕНИЕ
Ошибка резервного копирования

Дополнительные сведения:
------------------------
Код ошибки: 22
Модуль: 309
LineInfo: 0x8D165E86FB81959B
Поля: {"$module":"mms_vsa64_11010","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"}
Сообщение: TOL: Failed to execute the command. Backup workflow
------------------------
Код ошибки: 22
Модуль: 309
LineInfo: 0x8D165E86FB81959B
Поля: {"$module":"gtob_backup_command_addon_vsa64_11010","CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085"}
Сообщение: TOL: Failed to execute the command. Backup workflow
------------------------
Код ошибки: 2
Модуль: 329
LineInfo: 0x8EDC81EA38FABAA4
Поля: {"TraceLevel":"1","StepType":"2","$module":"gtob_backup_command_addon_vsa64_11010"}
Сообщение: Не удалось выполнить шаг "Резервное копирование".
------------------------
Код ошибки: 22
Модуль: 309
LineInfo: 0x8D165E86FB81959B
Поля: {"$module":"mms_vsa64_11010","CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0"}
Сообщение: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Код ошибки: 22
Модуль: 309
LineInfo: 0x8D165E86FB81959B
Поля: {"$module":"service_process_vsa64_11010","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Сообщение: TOL: Failed to execute the command. Резервное копирование
------------------------
Код ошибки: 22
Модуль: 309
LineInfo: 0x8D165E86FB81959B
Поля: {"$module":"gtob_backup_command_addon_vsa64_11010","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Сообщение: TOL: Failed to execute the command. Резервное копирование
------------------------
Код ошибки: 3
Модуль: 329
LineInfo: 0x1CD98AAE889424F9
Поля: {"$module":"disk_bundle_vsa64_11010"}
Сообщение: Сбой при резервном копировании.
------------------------
Код ошибки: 1060
Модуль: 1
LineInfo: 0xBA19E88DC5FEA1B1
Поля: {"$module":"disk_bundle_vsa64_11010"}
Сообщение: 
------------------------
Код ошибки: 25
Модуль: 4
LineInfo: 0xBA19E88DC5FEA1AF
Поля: {"$module":"disk_bundle_vsa64_11010"}
Сообщение: Неизвестная ошибка в процессе резервного копирования.
------------------------
Код ошибки: 25
Модуль: 4
LineInfo: 0x5F25C37074A54450
Поля: {"Archive3Code":"5100","Name":"ALM-DC-02.gkm-kz.local-21693BE6-78B2-489C-93F1-BBB60BAAAFD1-B085F22C-27C1-4A2F-A6EA-0BE1FAE5C6D9A.tibx","$module":"archive3_adapter_vsa64_11010"}
Сообщение: Ошибка резервного копирования.








      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/26/2019 - 04:05

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi! 
Welcome to Acronis forums! The error message is too general to highlight the root cause. I'd start with checking the Windows event logs on the Agent machine for the Acronis related messages - this might be a crash.
If Windows Event logs do not show any relevant information, I'd suggest localizing the issue first 
- Try running backup to another location /  manually copy data to the same location
- If you back up a huge amount of data, try to create a smaller backup to the same location 
- Make sure that Acronis processes are up and running on the Agent machine 
Anyway, for the more in-depth investigation I'd recommend you to raise a support ticket, so that our engineers can analyze the diagnostic information from your system and help. 

      
                
                
                    
                                                    Mon, 07/01/2019 - 17:12
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
