# Error when adding SharePoint site to backup: "Query parameter 'resource type' has invalid value 'SITE'."

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/error-when-adding-sharepoint-site-backup-query-parameter-resource-type-has-invalid-value-site

## Original Post
**Author:** Unknown

Error when adding SharePoint site to backup: "Query parameter 'resource type' has invalid value 'SITE'."

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Scott Beeson
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            When I edit "SharePoint sites to Cloud storage" and add the new SharePoint site (which I created weeks ago), then hit save, I get the error "Query parameter 'resource type' has invalid value 'SITE'.".
I tried to insert and upload a screenshot, but neither seemed to work. Awesome forums.
What would be causing this error?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 01/25/2025 - 21:00

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Welcome to the forum.
There is an ongoing issue on the the forum the sometimes won't allow you to upload pictures. We are trying to solve it asap.
Regarding the issue you need to review the following: 
- Permission Issue: The account used in Acronis to access SharePoint may not have sufficient permissions to interact with the new site.
- Quotas issues: 
Make sure the account has the quotas enabled:
Microsoft 365 seats
Microsoft 365 SharePoint online
Microsoft 365 Teams
https://www.acronis.com/en-us/support/documentation/AcronisCyberCloud/#…
- The site doesn't meet the pre-requisites:
Limitations
Titles and descriptions of sites/subsites/lists/columns are truncated during a backup if the title/description size is greater than 10,000 bytes.
You cannot back up previous versions of files created in SharePoint Online. Only the latest versions of the files are protected.
You cannot back up the Preservation Hold library.
You cannot back up sites created in the Business Productivity Online Suite (BPOS), the predecessor of Microsoft 365.
You cannot back up the settings for sites that use the managed path /portals (for example, https://<tenant>.sharepoint.com/portals/...).
Information Rights Management (IRM) settings of a list or a library can be recovered only if IRM is enabled in the target Microsoft 365 organization.
- https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
Make sure you follow the user-guide and all the instructions when adding the site: https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
If the issue persists, it needs to be investigated, please contact our support or your service provider so we can investigate the issue.
Best regards.

      
                
                
                    
                                                    Mon, 01/27/2025 - 14:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
