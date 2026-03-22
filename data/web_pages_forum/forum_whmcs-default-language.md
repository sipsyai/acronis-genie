# WHMCS default language

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/whmcs-default-language

## Original Post
**Author:** Unknown

WHMCS default language

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    red CLOUD
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
If the user is not logged in to the WHMCS shop the default language for the Acronis module (custom fields by order) is English instead of German.
I've changed the default language in the file «/public_html/modules/servers/AcronisBackupService/app/Acronis/Standard/Helpers/LanguageMap.php»
-> const DEFAULT_LANGUAGE_ISO = 'de';
But it didn't solved my issue.
If I change the code in the file «iso-languages.json» (/public_html/modules/servers/AcronisBackupService/lang/iso-languages.json) like this
"english": "de",
"german": "en",
It doesn't change the langue on the user page. For this reason it seems as if the code will be oversteered by some other, higher ranked code.
Many thanks for your support.
Kind regards
Sybille

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/17/2017 - 13:39

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sybille​,
Thank you for your posting! I see, that you have an open support ticket #02940756. To provide recommendations for your particular case, we'd request the following information:
1. WHMCS version and Acronis version 
2. If it's possible, please provide info about: does WHMCS working on virtual hosting or as a part of cpanel/plesk, or it is clean installation. 
3. PHP error logs, php error logs files and etc. Even though there is no errors in WHMCS logs and on the screen, please make sure that PHP log files does not contain any errors 
4. PHP version 
5. admin account used for provisioning 
Thank you in advance!

      
                
                
                    
                                                    Mon, 04/03/2017 - 12:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
