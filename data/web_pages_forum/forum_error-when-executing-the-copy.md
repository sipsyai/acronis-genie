# Error when executing the copy.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-when-executing-copy

## Original Post
**Author:** Unknown

Error when executing the copy.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Roger
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, 
We are recently starting to use this program for our client's backups and we have some errors, like this one:
MENSAJE
Error al realizar copia de seguridad

Información adicional:
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"mms_vs_4492"}
Mensaje: TOL: Failed to execute the command. Plan de copias de seguridad "Archivos/carpetas para Cloud Storage"
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"agent_protection_addon_vs_4492"}
Mensaje: TOL: Failed to execute the command. Plan de copias de seguridad "Archivos/carpetas para Cloud Storage"
------------------------
Código de error: 41
Módulo: 307
Información de línea: 0xE6792A5EE190DDE7
Campos: {"$module":"agent_protection_addon_vs_4492"}
Mensaje: No se pudo ejecutar el comando.
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"mms_vs_4492"}
Mensaje: TOL: Failed to execute the command. Backup workflow
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"F30407D6-601F-11E0-9C67-FF46DFD72085","$module":"gtob_backup_command_addon_vs_4492"}
Mensaje: TOL: Failed to execute the command. Backup workflow
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"4504F8D4-2727-42AB-BB4F-A42EDBB790A0","$module":"mms_vs_4492"}
Mensaje: TOL: Failed to execute the command. Tol::IsolateCommand
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"D77E80BD-410A-468E-B593-FC8467A0D91B","$module":"service_process_vs_4492"}
Mensaje: TOL: Failed to execute the command. Running Python script
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"D77E80BD-410A-468E-B593-FC8467A0D91B","$module":"pybind_tol_supp_vs_4492"}
Mensaje: TOL: Failed to execute the command. Running Python script
------------------------
Código de error: 1
Módulo: 573
Información de línea: 0x202058661174692F
Campos: {"$module":"pybind_tol_supp_vs_4492"}
Mensaje: Failed to run Python script 'pyvfs:staging?calculate_backup_set'.
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"3CC14D08-3D75-46C4-AB00-431B0E3868A3","$module":"mms_vs_4492"}
Mensaje: TOL: Failed to execute the command. Getting information about backups
------------------------
Código de error: 22
Módulo: 309
Información de línea: 0x8D165E86FB819595
Campos: {"CommandID":"3CC14D08-3D75-46C4-AB00-431B0E3868A3","$module":"staging_command_vs_4492"}
Mensaje: TOL: Failed to execute the command. Getting information about backups
------------------------
Código de error: 203
Módulo: 161
Información de línea: 0x0B320396ADFE423D
Campos: {"IsReturnCode":"1","$module":"disk_bundle_vs_4492"}
Mensaje: No se pudo obtener información acerca de las copias de seguridad.
------------------------
Código de error: 203
Módulo: 161
Información de línea: 0xD5796A33131EEC48
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje: No se pudo obtener información acerca de las copias de seguridad.
------------------------
Código de error: 803
Módulo: 349
Información de línea: 0xA14D72EEB8F971B2
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje: No fue posible ejecutar una tarea.

------------------------
Código de error: 803
Módulo: 349
Información de línea: 0xA14D72EEB8F971B2
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje: No fue posible ejecutar una tarea.
------------------------
Código de error: 507
Módulo: 64
Información de línea: 0xA1D3981537C68861
Campos: {"id":"SERVER-5898F86F-2235-4551-AFF3-A98EA8AE8F8F-027D397C-6CC1-4013-B380-FF6B30524224AF.TIB","$module":"disk_bundle_vs_4492"}
Mensaje: No fue posible abrir el archivo de copia de seguridad por la ID.
------------------------
Código de error: 853
Módulo: 64
Información de línea: 0x6A1198D1B8BE2C30
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje: Failed to open archive 'SERVER-5898F86F-2235-4551-AFF3-A98EA8AE8F8F-027D397C-6CC1-4013-B380-FF6B30524224AF.TIB'.
------------------------
Código de error: 17
Módulo: 357
Información de línea: 0x9F743FAE3DCD8E82
Campos: {"$module":"SystemStateAgentProvider_vs_4492"}
Mensaje: No se encontró un flujo con los metadatos del archivo comprimido.
------------------------
Código de error: 2
Módulo: 64
Información de línea: 0x68F47D89A6C2B915
Campos: {"path":"SERVER-5898F86F-2235-4551-AFF3-A98EA8AE8F8F-027D397C-6CC1-4013-B380-FF6B30524224AF.tib.meta","$module":"disk_bundle_vs_4492"}
Mensaje: No se pudo abrir el archivo comprimido para su lectura.
------------------------
Código de error: 17
Módulo: 4
Información de línea: 0x5E37827EF93FC216
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje: El archivo especificado no existe.
------------------------
Código de error: 40
Módulo: 152
Información de línea: 0xA46E8D7BA5BB85F2
Campos: {"$module":"disk_bundle_vs_4492"}
Mensaje:
Would someone know how to solve it?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 11/22/2017 - 10:13

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Roger
The error "The specified file does not exist" usually refers to when the source folder set which was suppose to have been backed up was deleted or moved from its original location.
You have two ways of resolving this:
1. Find the source folder set which was deleted or moved and exclude it in the backup set or alternatively reconfigure the backup set to include the folder in the new path
2. The easiest way will be to recreate the backup set, you may revoke the current plan as it will keep the backup history and data etc. And then recreate the backup plan.
Regards

      
                
                
                    
                                                    Thu, 11/23/2017 - 13:42
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
