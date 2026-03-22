# Can't access any backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/cant-access-any-backup

## Original Post
**Author:** Unknown

Can't access any backup 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ruben Pires
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Every time i try to access the file backups of a machine i keep getting this error.
Não é possível encontrar o arquivo especificado.



Data e hora
11 Dez, 2018, 10:35:27






Código
0x00A100D4+0x00A100C9+0x00A10007






Módulo
161



Mensagem
Failed to find archive 'avfs:/online?account%3d513462627%26computer%3d1%26provider%3dAcronis#arl:/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000/C074AB80-FA5C-5263-FDA1-F7ECA219B101/3A0F98B5-AE0C-4877-AACF-B3193F616702?archive_name%3dZIPZIP513462627-E41FBC3B-85DD-4D76-A4DD-57EC7BE27138-959C7B5F-F27E-4B84-9A07-325C36C36513A'.

Informações adicionais:
------------------------
Código de erro: 212
Módulo: 161
Informação de linha: 0x0B320396ADFE3E04
Campos: {"IsReturnCode":"1","$module":"disk_bundle_vsa64_12210"}
Mensagem: Failed to find archive 'avfs:/online?account%3d513462627%26computer%3d1%26provider%3dAcronis#arl:/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000/C074AB80-FA5C-5263-FDA1-F7ECA219B101/3A0F98B5-AE0C-4877-AACF-B3193F616702?archive_name%3dZIPZIP513462627-E41FBC3B-85DD-4D76-A4DD-57EC7BE27138-959C7B5F-F27E-4B84-9A07-325C36C36513A'.
------------------------
Código de erro: 201
Módulo: 161
Informação de linha: 0xD5796A33131EEB98
Campos: {"$module":"disk_bundle_vsa64_12210"}
Mensagem: Failed to get information about the archives.
------------------------
Código de erro: 7
Módulo: 161
Informação de linha: 0xD5796A33131EEB91
Campos: {"$module":"disk_bundle_vsa64_12210"}
Mensagem: Não é possível encontrar o arquivo especificado.
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 12/11/2018 - 10:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ruben
Sorry for not replying back last week!
 
In many cases it is important to know what exact steps are performed to reproduce the issue.
Judging from the info provided, I assume that the issue happens when you click on "recover files\folders" from one of the recovery points shown in the general Devices tab.
 
The list over there is not a real-time display, please click the "refresh" button atop the list and wait for a few minutes for the list to populate.
Alternatively, try browsing the backup archive's contents from the Backups tab where the list is acquired at the moment when you click on the archive.
 
If this keeps happening, please submit a support ticket through us or through the Service Provider where you have purchased the solutions for us to have a better look at the scenario and have the full details!
 
Let me know if you have any other questions!

      
                
                
                    
                                                    Mon, 12/17/2018 - 18:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
