# WHM Plugin Not working

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/whm-plugin-not-working

## Original Post
**Author:** Unknown

WHM Plugin Not working

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
 
I am installing the plugin for WHM, I have 3 servers and apparently with the same configuration, in 2 servers I was able to install the plugin normally and it is already working, but on 1 server I install the plugin and the error "The backup agent is not available. "
Could anyone help how can I solve the problem?
 
thanks

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      2019-05-13_18h15_58.png

                      16.92 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/13/2019 - 21:18

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi there
Can you please confirm if the Acronis Managed Machime service is running on the machine which you are having a problem with?
 

      
                
                
                    
                                                    Mon, 05/20/2019 - 06:38
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
 
Yes, the acronis_backup_srv is running in the server.
 
 
thanks

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      498710-167631.png

                      32.12 KB
                  
          
    

                    
    
                
                
                    
                                                    Tue, 05/21/2019 - 12:45
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day,
Can you please confirm that the following ports are open for the server, I have had in some cases that our clients have restricted certain servers on the firewall with communicating with the backup management server:
443 & 8443 - Used for registering the agents
7770...7800-  Used for communication with the backup management server
You may use the Acronis Connection Verification tool to confirm that you are in fact able to communicate on all required  ports:
https://kb.acronis.com/content/47678
Regards

      
                
                
                    
                                                    Mon, 05/27/2019 - 09:37
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    tvieira
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for the answer.

I checked with the tool and informs that all the doors are open. 
 
thanks

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      499024-167730.png

                      15.54 KB
                  
          
    

                    
    
                
                
                    
                                                    Mon, 05/27/2019 - 12:03
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud

Acronis Service Provider Hosted

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
             
tvieira, have you tried re-installing the Agent? 

      
                
                
                    
                                                    Fri, 06/07/2019 - 16:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
