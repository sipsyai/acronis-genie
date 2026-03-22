# Plesk and Acronis Backup Cloud

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/plesk-and-acronis-backup-cloud

## Original Post
**Author:** Unknown

Plesk and Acronis Backup Cloud

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    john.winter@neverseen.ch
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
I am testing Plesk Multi Server and Acronis Backup Cloud.
I managed to install the agent and connected it to my account. Port Check was OK. Now when I want to activate the backup, it tells me that  it "Cannot enable backup". Backup Switch is still "Disabled".  I see the backups which I have created manually in the Backup Cloud console. When I click on this one, it tells me "Cannont access the backup created ..."
I set up a seperate Plesk Webserver too to test it undependent from plesk multiserver.
I followed the manual you provide with the agent.  https://download.acronis.com/pdf/Acronis_Backup_extension_for_Plesk_en-…
Is there something I have missed?
 
Edit on 01.08.2017: Concerning Plesk, the Acronis Backup tool has not been tested on Plesk Server or Plesk Multi Server. Can I assume that the tool is not ready yet?
Quote from Acronis Forum:

"The Acronis Backup Cloud extension is not officially supported yet and it was not properly tested nor with the single Plesk server, nor with the Plesk Multi Server. My recommendation is to wait until we will publish it in our Extensions Catalog ext.plesk.com."
 


Is there an effort to do so in the near future?

Kind regards
John

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/31/2017 - 14:43

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Pavel Podlesny
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello John,
This is Pavel from Acronis Service Providers Support team and I'll be glad to assist you in finding the necessary information or solution.
Although it hasn't been tested yet, your feedback can significantly assist us in finding weak spots and issues. We'll be glad to investigate the issue for you if you could provide us some additional information.
Could you please collect the logs from both the Agent and the Extensions and share it with us via a request to mspsupport@acronis.com ?
Agent logs can be collected via the Console or manually on the device with the Agent installed, following instructions from https://kb.acronis.com/content/54608
Extension logs from Plesk can be located in two main paths:
	/usr/local/psa/var/modules/acronis-backup/srv/log
	/var/log/plesk/panel.log
All those can be put into a single archive and attached to the email sent to mspsupport@acronis.com with a brief description and topic forum link for the reference.
Once the logs are collected we will get back to you via email in the same thread and work until we have a solid solution.

      
                
                
                    
                                                    Tue, 08/01/2017 - 21:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    john.winter@neverseen.ch
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Pavel
Thanks for your reply. The requested files are sent to mspsupport@acronis.com
 
Kind regards
John

      
                
                
                    
                                                    Wed, 08/02/2017 - 16:21
