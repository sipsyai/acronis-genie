# Error Starting mms.exe and DiskBundle.dll error100

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/error-starting-mmsexe-and-diskbundledll-error100

## Original Post
**Author:** Unknown

Error Starting mms.exe and DiskBundle.dll error100

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    system_account
                            

                            
                    
                        Forum Star
                    
                
            
                        
                
                    Posts: 198
                
            
            
                
                    Comments: 840
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I made the installation of Acronis Cloud Backup 12 (Agent) and it does not allow to register and it shows me the following error
 
Nombre de la aplicación con errores: mms.exe, versión: 12.5.1.15300, marca de tiempo: 0x5df92749
Nombre del módulo con errores: DiskBundle.dll, versión: 12.5.1.15300, marca de tiempo: 0x5df9297e
Código de excepción: 0xc0000094
Desplazamiento de errores: 0x000000000114c619
Identificador del proceso con errores: 0x13b4
Hora de inicio de la aplicación con errores: 0x01d603f75b83c5e7
Ruta de acceso de la aplicación con errores: C:\Program Files\BackupClient\BackupAndRecovery\mms.exe
Ruta de acceso del módulo con errores: C:\Program Files\BackupClient\BackupAndRecovery\DiskBundle.dll
Identificador del informe: 9af5584a-6fea-11ea-941e-e8393520119f
Nombre completo del paquete con errores: 
Identificador de aplicación relativa del paquete con errores: 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      acronis.png

                      118.46 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/27/2020 - 05:31

                                                          
                                                            
                                                                                        
    
                    
                spam

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Richard,
welcome to Acronis forums!
Please open running services on that machine and check if the Acronis Managed Machine service (mms.exe) is present and running. Then please try starting the service. After that, you can proceed with manual registration as described in the respective KB article: https://kb.acronis.com/content/55244
 
 

      
                
                
                    
                                                    Fri, 03/27/2020 - 11:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/
