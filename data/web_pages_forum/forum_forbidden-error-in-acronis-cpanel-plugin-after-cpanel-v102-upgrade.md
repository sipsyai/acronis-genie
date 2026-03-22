# "Forbidden" error in Acronis cPanel plugin after cPanel v102 upgrade

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/forbidden-error-acronis-cpanel-plugin-after-cpanel-v102-upgrade

## Original Post
**Author:** Unknown

"Forbidden" error in Acronis cPanel plugin after cPanel v102 upgrade

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello,
There seems to be a permissions issue causing the Acronis cPanel plugin to stop working with a "Forbidden" error, after upgrading a cPanel server to v102 (RELEASE tier).

According to mspsupport, the issue number is CI-17502
Do we have an ETA when the fix will be released?
Currently the workaround is to chmod 644 /etc/trueuserdomains on the affected server.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 04/04/2022 - 10:21

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi!
Looks that cPanel have published an update in KBA that the issue has been resolved in cPanel & WHM version 102.0.9.
Comment: https://support.cpanel.net/hc/en-us/articles/4780459960727/comments/5088649009687
Change log: https://docs.cpanel.net/changelogs/102-change-log/ 

      
                
                
                    
                                                    Mon, 04/04/2022 - 16:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
