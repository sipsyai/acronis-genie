# Acronis Console - SSL not renewed on cname?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-console-ssl-not-renewed-cname

## Original Post
**Author:** Unknown

Acronis Console - SSL not renewed on cname?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Danks
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
Our SSL on Acronis Console is letsencrypt and its auto renewed without issues for 2 years, however its now expired on  our custom hostname for Acronis Console, when we visit the URL it shows expired SSL, when I view more info it showing the SSL is *.acronis.com and not our own custom hostname on US-5 server.
I visited https://kb.acronis.com/content/58275 like I had done 2 years ago and i run command:
branding-cli set -u MY_USER_HERE -tenantID 79f6*******fc3 -useLetsencrypt -cname MY_ACRONIS_URL
it then asks for my password and then fails with:
request to idp failed: [401] totp_required: TOTP code is required: failed to validate TOTP code:
the CLI tool has no documenation for how to enter the Two Factor authenticaiton and our backups are now failing. The documentation is from 2022 when acronis did not have 2FA so my guess is this tool doesn't support 2FA on command line.
Can you please fix us5 server so it renews our already expired LetsEncyptSSL ASAP + fix documentation is outdated as well as the CLI tool.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 06/20/2024 - 14:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
You can also execute the branding in the console by following this user guide: Configuring Custom URLs.
The branding tool does not support 2FA, so if you have it enabled, the error code you receive is expected. I have requested the team to update the documentation.
If branding in the console doesn't work, please raise a ticket with the team at https://kb.acronis.com/content/8153 so we can help you with the entire process.
Best regards.
 

      
                
                
                    
                                                    Thu, 06/20/2024 - 22:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
