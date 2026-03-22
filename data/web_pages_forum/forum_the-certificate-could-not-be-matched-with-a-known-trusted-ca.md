# The certificate could not be matched with a known, trusted CA

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/certificate-could-not-be-matched-known-trusted-ca

## Original Post
**Author:** Unknown

The certificate could not be matched with a known, trusted CA

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cristian Gaune
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good evening, please help me with an error that is occurring a few days ago when trying to run a backup plan that was running without problems.
 
 
Mensaje
Acceso denegado.

Información adicional:
------------------------
Código de error: 20250646
Campos: {"$module":"mms_lxa64_28156","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Mensaje: TOL: Failed to execute the command. Backup plan 'Server (Diaria)'
------------------------
Código de error: 20250646
Campos: {"$module":"agent_protection_addon_lxa64_28156","CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB"}
Mensaje: TOL: Failed to execute the command. Backup plan 'Server (Diaria)'
------------------------
Código de error: 20119593
Campos: {"$module":"agent_protection_addon_lxa64_28156"}
Mensaje: Failed to execute the command.
------------------------
Código de error: 20250677
Campos: {"$module":"agent_protection_addon_lxa64_28156","FailCount":2}
Mensaje: 2 activities have not succeeded. One of them is displayed.
------------------------
Código de error: 20250646
Campos: {"$module":"service_process_lxa64_28156","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Mensaje: TOL: Failed to execute the command. Backing up
------------------------
Código de error: 20250646
Campos: {"$module":"gtob_backup_command_addon_lxa64_28156","CommandID":"8F01AC13-F59E-4851-9204-DE1FD77E36B4"}
Mensaje: TOL: Failed to execute the command. Backing up
------------------------
Código de error: 10551508
Campos: {"$module":"disk_bundle_lxa64_28156","IsReturnCode":1}
Mensaje: Failed to find archive 'ceclsvc-dcapp17-CCAB2344-9F47-421A-8959-FD373C60CE85-69FC6304-01EA-4513-8E33-6360E75161F4A'.
------------------------
Código de error: 262164
Campos: {"$module":"disk_bundle_lxa64_28156"}
Mensaje: Access to the file is denied.
------------------------
Código de error: 33752040
Campos: {"$module":"disk_bundle_lxa64_28156","fesAddress":"acrstorage01.grupogtd.com:44445"}
Mensaje: Failed to read directory.
------------------------
Código de error: 43712915
Campos: {"$module":"disk_bundle_lxa64_28156","function":"find_first","path":"/"}
Mensaje: The certificate could not be matched with a known, trusted CA
------------------------
Código de error: 43712915
Campos: {"$module":"disk_bundle_lxa64_28156","function":"astor_dirlist_1stlevel_start","path":"/"}
Mensaje: The certificate could not be matched with a known, trusted CA
------------------------

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/22/2021 - 01:11

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            What OS are you running on Server (Diaria)? Also, are you the administrator of acrstorage01.grupogtd.com? If yes, what version of ACI are you running?

      
                
                
                    
                                                    Wed, 12/22/2021 - 10:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Cristian Gaune
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The O.S. that needs to be backed up corresponds to a Linux server and it is also presented for some Windows servers, and it is also indicated that I am indeed an administrator of AcronisStorage and its version is 2.4.0 (3266).

      
                
                
                    
                                                    Wed, 12/22/2021 - 11:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Cristian Gaune
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            George_Fusioned wrote:

What OS are you running on Server (Diaria)? Also, are you the administrator of acrstorage01.grupogtd.com? If yes, what version of ACI are you running?



      
                
                
                    
                                                    Wed, 12/22/2021 - 11:45
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Cristian Gaune
Acronis Storage 2.4's Extended Support End Date is past for over a year now (https://www.acronis.com/en-sg/support/lifecycle/business.html) so I'm not sure whether this can be fixed or not, but for starters:
You're running Acronis Storage on CentOS 7, right?
Is it fully updated?
Any chance you have the epel repo active on that server?

      
                
                
                    
                                                    Fri, 12/24/2021 - 06:01
