# Export details of Plans per tenant for use with Backup Contract

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/export-details-plans-tenant-use-backup-contract

## Original Post
**Author:** Unknown

Export details of Plans per tenant for use with Backup Contract

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    CBBW
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, would anyone know:
Is there an ability to print/export/email actual configuration of each backup/protect plan that applies to a tenant estate. This should include all options set for 
Backup options – 
Alerts
Backup Consolidation
Backup Format
Etc.

Basic setup such as – 
What to backup
Items to backup
Where to backup
Schedule
Etc.


( this not to allow import of config for other tenants but to provide documented proof of backup options chosen – this to form part of legal backup agreement with client )
I believe such an ability would be critical for MSP’s to be able to provide clients and form basis for inclusion in backup contract, thereby ensuring that there can be no dispute between client and MSP as to what options where chosen for backup, this critical when data loss occurs and clients start questioning what was backed up.
If points 1 & 2 are not possible, can this be achieved via API ?
 
Any idea’s on how to address this would be so appreciated ?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/10/2020 - 12:29

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Ciaron,
Thank you for your post on Acronis Forum.
We can export protection plans with their complete configurations that are currently set.
This can be done from customer's Protection Console using Plan Management (Plans) feature by selecting and exporting the desired plan: Acronis Protection Console > Plans > Protection > "Plan Name" > Export (see attached screenshot).
Note, that Plan Management is not available only for (Legacy) Cyber Backup – Standard and (Legacy) Cyber Protect – Standard editions, it is supported on all other editions. Also, we can only export plan's configurations into JSON format as by design exported plans are to be used with the Import function that allows applying same plan (with same configurations) into another customer tenants' Protection Consoles. It is not meant to be used for reports but still well structured and descriptive inside the JSON file.
API would do the same, but if you have custom application that can populate JSON data into a report it can help. However Backup API and Plan Management API is not officially published yet. Still under development and documentation is not available.
I hope you find this information useful for the needs of your business and solve your request.

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      559410-206900.png

                      83.45 KB
                  
          
    

                    
    
                
                
                    
                                                    Fri, 11/13/2020 - 10:31
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
