# Cannot see backup plan

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/cannot-see-backup-plan

## Original Post
**Author:** Unknown

Cannot see backup plan

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Daniel Gama
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I have been faced an issue while i create a new backup plan for an iMac. I want to shcedule a backup for a specific folder and save it on a local hard disk, the problem start when i finish to configure the plan, i click create takes a couple of seconds and it send me back to the backup window but the plan is not there. i've been trying to create several plans and non of them are showned there, it looks like no plan have been created.
However, the agent start doing the back up like if the backup plan were created successfully but the back up stuck at 37% for 24hrs until it send an error:
 
DATE AND TIME
Sep 14, 2018, 05:04:53
CODE
0x01350016+0x01350016+0x01330029+0x01350035+0x01350016+0x01350016+0x01490003+0x00010424+0x00040019+0x00040019
MODULE
309
MESSAGE
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"$module":"mms_macia64_10330","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Plan de copias de seguridad "Archivos/carpetas para Local Storage"
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"$module":"agent_protection_addon_macia64_10330","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Message: TOL: Failed to execute the command. Plan de copias de seguridad "Archivos/carpetas para Local Storage"
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DE2C
Fields: {"$module":"agent_protection_addon_macia64_10330"}
Message: No se pudo ejecutar el comando.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB719
Fields: {"$module":"agent_protection_addon_macia64_10330","FailCount":"2"}
Message: No fue posible completar 2 actividades. Se muestra una de ellas.
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"$module":"service_process_macia64_10330","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Realizando copia de seguridad
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB81959B
Fields: {"$module":"gtob_backup_command_addon_macia64_10330","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Message: TOL: Failed to execute the command. Realizando copia de seguridad
------------------------
Error code: 3
Module: 329
LineInfo: 0x1CD98AAE889424F9
Fields: {"$module":"disk_bundle_macia64_10330"}
Message: La copia de seguridad ha fallado.
------------------------
Error code: 1060
Module: 1
LineInfo: 0xBA19E88DC5FEA1B1
Fields: {"$module":"disk_bundle_macia64_10330"}
Message: 
------------------------
Error code: 25
Module: 4
LineInfo: 0xBA19E88DC5FEA1AF
Fields: {"$module":"disk_bundle_macia64_10330"}
Message: Se ha producido un error al realizar la copia de seguridad.
------------------------
Error code: 25
Module: 4
LineInfo: 0x5F25C37074A5445E
Fields: {"$module":"archive3_adapter_macia64_10330","Archive3Code":"5005","Name":"LEMUS-iMac.local-B3D74852-7D24-4A68-8509-C8FA7320259B-E6112D6E-1B9B-4FBB-9A0F-FB8916615F29A.tibx"}
Message: Se ha producido un error al realizar la copia de seguridad.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/21/2018 - 15:45

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Daniel,
I see that you have an open support ticket for this issue. Would you mind sharing the results of the investigation with the community?
Thank you!

      
                
                
                    
                                                    Thu, 10/11/2018 - 12:51
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
