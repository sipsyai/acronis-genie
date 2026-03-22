# Falha ao conectar com "abgw-gru2-arp01-r03.acronis.com:44445" porque o acesso ao armazenamento em nuvem foi negado.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/falha-ao-conectar-com-abgw-gru2-arp01-r03acroniscom44445-porque-o-acesso-ao-armazenamento-em-nuvem-foi-negado

## Original Post
**Author:** Unknown

Falha ao conectar com "abgw-gru2-arp01-r03.acronis.com:44445" porque o acesso ao armazenamento em nuvem foi negado.

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Julio Divietro
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear Forum Group,
I am helping a customer and he showed me this error when it run a backup plan to cloud.  The Agent is running at a Windows VM into a Host Server.  Apparently I see a problem with Certificate Authority (CA), but I don't know how to help you solve it. The backup was running normally 2 days ago and now it doesn't run anymore.  
The server name on this process is "servidor de arquivos"
 
Falha ao conectar com "abgw-gru2-arp01-r03.acronis.com:44445" porque o acesso ao armazenamento em nuvem foi negado.
Mensagem
Falha ao conectar com "abgw-gru2-arp01-r03.acronis.com:44445" porque o acesso ao armazenamento em nuvem foi negado.

Informações adicionais:
------------------------
Código de erro: 10551508
Campos: {"$module":"disk_bundle_vsa64_38946","IsReturnCode":1}
Mensagem: Failed to find archive 'Servidor de Arquivos-3CC619F9-BEF7-4B90-B88E-33AD1669881B-EC8F8363-5170-4CBD-BA0A-6D925DA6F12EA'.
------------------------
Código de erro: 262164
Campos: {"$module":"disk_bundle_vsa64_38946"}
Mensagem: Unknown certificate authority.
------------------------
Código de erro: 50332648
Campos: {"$module":"disk_bundle_vsa64_38946","fesAddress":"abgw-gru2-arp01-r03.acronis.com:44445"}
Mensagem: Failed to read directory.
------------------------
Código de erro: 43712915
Campos: {"$module":"disk_bundle_vsa64_38946","function":"astor_dirlist_start","path":"/"}
Mensagem: The certificate could not be matched with a known, trusted CA
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 11/28/2024 - 20:28

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Cyber Protect Cloud 
MSP Partner
            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Julio,
This issue is usually related to the storage certificate. Most likely, it has expired, and the client will need to renew it.
For reference:Article: Acronis Cyber Protect Activity fails with ErrorNotFound - No certificate was found for authority with ID
The client should check the certificate, and if it is confirmed to be expired, the following instructions should be followed:Article: How to update the backup storage certificate in Acronis Cyber Infrastructure
If the issue persists and the certificate is active and up-to-date, please open a support ticket and provide screenshots showing the date.
Best regards.

      
                
                
                    
                                                    Mon, 12/02/2024 - 05:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
