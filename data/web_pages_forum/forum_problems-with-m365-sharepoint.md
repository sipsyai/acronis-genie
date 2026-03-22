# Problems with M365 Sharepoint

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/problems-m365-sharepoint

## Original Post
**Author:** Unknown

Problems with M365 Sharepoint 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Douglas Alves
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a doubt.
I'm backing up sharepoint 365 and I'm getting this warning:

The activity concluded with warnings
Failed to read "sharepoint_clientes_cria_novo_job" (mailNickname = "sharepoint_clientes_cria_novo_job") from the group.
I'm an admin of the group and it's still generating the warning.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 07/23/2024 - 14:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Douglas.
Please review the limitations for the SharePoint backups: 
Limitations:
Titles and descriptions of sites/subsites/lists/columns are truncated during a backup if the title/description size is greater than 10,000 bytes.
You cannot back up previous versions of files created in SharePoint Online. Only the latest versions of the files are protected.
You cannot back up the Preservation Hold library.
You cannot back up sites created in the Business Productivity Online Suite (BPOS), the predecessor of Microsoft 365.
You cannot back up the settings for sites that use the managed path /portals (for example, https://<tenant>.sharepoint.com/portals/...).
Information Rights Management (IRM) settings of a list or a library can be recovered only if IRM is enabled in the target Microsoft 365 organization.
https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Also make sure you are creating the plan following the instructions: https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
If the issue persists, please raise a ticket with the team at https://kb.acronis.com/content/8153 or contact your service provider.
Best regards.

      
                
                
                    
                                                    Tue, 07/23/2024 - 15:24
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
