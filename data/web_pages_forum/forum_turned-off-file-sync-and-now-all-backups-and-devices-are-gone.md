# Turned off File Sync and now all backups and devices are gone.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/turned-file-sync-and-now-all-backups-and-devices-are-gone

## Original Post
**Author:** Unknown

Turned off File Sync and now all backups and devices are gone.

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Raymond Sue
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a partner that is testing Cyber Cloud.  They have been running backups on several devices for the past couple of weeks.  They enabled File Sync when creating the customer but did not want it.  We turned off File Sync at the customer level and now all of his backups and devices are gone.  Everything has been reset to zero.  Is this a known bug?  Is there a way to resolve this?

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Capture Family (002).JPG

                      81.59 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 09/15/2020 - 17:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Raymond,
Thank you for submitting your request on Acronis Forum.
I tried to find a known bug for this issue behavior but can't relate it to something similar.
Could you please share the affected login name of the "Family" customer tenant and DC.
We can check the events in the Audit Log and find useful information of what happened.
Thank you.

      
                
                
                    
                                                    Thu, 09/17/2020 - 12:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Raymond Sue
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 14
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ivaylo,
We found the issue.  We removed the File Sync admin account but that was also the backup admin account. 
 
Ivaylo Tsvetkov wrote:

Hello Raymond,
Thank you for submitting your request on Acronis Forum.
I tried to find a known bug for this issue behavior but can't relate it to something similar.
Could you please share the affected login name of the "Family" customer tenant and DC.
We can check the events in the Audit Log and find useful information of what happened.
Thank you.



      
                
                
                    
                                                    Tue, 09/22/2020 - 20:35
