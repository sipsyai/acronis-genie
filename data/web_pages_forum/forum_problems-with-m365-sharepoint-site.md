# Problems with M365 Sharepoint site

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/problems-m365-sharepoint-site

## Original Post
**Author:** Unknown

Problems with M365 Sharepoint site

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Christine Clabots
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi Everybody, 
I'm fairly new to acronis, so please be patient with me.
I'm using acronis cyber protect for a client of mine.   Backups for the mailboxes and onedrive are running smoothly.  Now I want to backup a sharepoint-site.  But the problem is I can't find the site. 
I looked in devices -> groups -> all groups,
devices -> public folders -> all public folders and
devices -> site collections -> all site collections
Do I have to enable something in the microsoft-admin-page?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 01/26/2024 - 15:58

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to our community.
Please check if the version of SharePoint is supported: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#supported-microsoft-sharepoint-versions.html#kanchor1413
Also, check the following prerequisites and limitations:
Limitations:
Titles and descriptions of sites/subsites/lists/columns are truncated during a backup if the title/description size is greater than 10000 bytes.
You cannot back up previous versions of files created in SharePoint Online. Only the latest versions of the files are protected.
You cannot back up the Preservation Hold library.
You cannot back up sites created in the Business Productivity Online Suite (BPOS), the predecessor of Microsoft 365.
You cannot back up the settings for sites that use the managed path /portals (for example, https://<tenant>.sharepoint.com/portals/...).
Information Rights Management (IRM) settings of a list or a library can be recovered only if IRM is enabled in the target Microsoft 365 organization. (Source: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#protecting-sharepoint-online-sites.html#kanchor162)
Also, check if you are adding the site properly according to this user guide: https://www.acronis.com/en-us/support/documentation/CyberProtectionService/#selecting-sharepoint-online-data.html
If all the prerequisites are met, please raise a ticket with our support at https://kb.acronis.com/content/8153
Best regards.

      
                
                
                    
                                                    Tue, 01/30/2024 - 12:35
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
