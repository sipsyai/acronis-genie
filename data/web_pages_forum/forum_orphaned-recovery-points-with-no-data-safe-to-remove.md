# Orphaned recovery points with no data - safe to remove?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/orphaned-recovery-points-no-data-safe-remove

## Original Post
**Author:** Unknown

Orphaned recovery points with no data - safe to remove?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good morning,
 
We have encountered an issue with one of our tenants wherein there are recovery points that go back further than the retention policy - the backup type is incremental.
 
These points do not exist in Webrestore
Attempting to access them in the recovery console results in the following error (note I have replace any account login info with xxxxxx):
"Failed to open backup 'avfs:/online?account%3dxxxxxxx%2540xxxxxxx.co.uk%26computer%3d1%26provider%3dAcronis#arl:/00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000/3578010F-1A70-6340-6A46-B7BE83F0BBD1/C22573B1-EB67-4B23-A283-C9E7C2779545?archive_name%3dMCI-DATA2-4D3A3733-7C2C-4F1A-86CA-EEE324FA88D7-89FC5BD5-4106-46FE-A94F-C5551C6AB586A' for browse.Cannot find a backup with key 'avfs:/online?account%3dxxxxxxxx%2540xxxxxxxx.co.uk%26computer%3d1%26provider%3dAcronis#arl:/F4A8E129-1708-42B5-BC98-0E4ACAEE04CC/8F44EB8E-E15E-4B3E-BBC4-40924F7EE303/3578010F-1A70-6340-6A46-B7BE83F0BBD1/C22573B1-EB67-4B23-A283-C9E7C2779545?archive_name%3dMCI-DATA2-4D3A3733-7C2C-4F1A-86CA-EEE324FA88D7-89FC5BD5-4106-46FE-A94F-C5551C6AB586A'.Error code 0x00A100F4+0x00A10008+0x00A10008+0x00A100CB+0x00A10006
Nov 09, 2020, 09:09
 
My question is, can I attempt to remove these from the Backup console without any affect on the backup chain?
 
Kind regards,
Phil

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 11/09/2020 - 09:03

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  2 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mikhail Rozhkov
                            

                            
                    
                        Support Engineer 
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 21
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil.
Please try to click on refresh button at the top right of backups tab, it will force the agent to check the meta of the archives stored on cloud storage and update the information about them in backups tab.
 
 

      
                
                
                    
                                                    Mon, 11/16/2020 - 14:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Mikhail,
 
Well, that'll teach me for looking for a technical reason for a simple issue! Many thanks for pointing me at that button - that's sorted it.
 
Out of interest, does this polling happen automatically at any point or is it always a manual refresh?
 
Thank you again for your help :)
 
Phil

      
                
                
                    
                                                    Mon, 11/16/2020 - 16:50
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
