# Misc network error

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/misc-network-error

## Original Post
**Author:** Unknown

Misc network error 

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                
                    
                        
            Hello, This morning all backups failed with error "Misc network error". Our servers and backup storage server are working fine, so seems to be an issue Acronis end? I'm using self-hosted and using us5-cloud.acronis.com Kind regards, Chris

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 02/02/2020 - 10:06

                                                          
                                                            
                                                                                        
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            It's strange but backup works for some servers but not the others.
If I uninstall the agent and try to reinstall it I get the error
Please update your firewall configuration and restart the installation

But nothing should have been changed unless cPanel has made updates to cause it? Every so often there seems to be something causing a problem with cPanel/WHM Acronis Backup plugin which is not acceptable since Acronis is supposed to be Enterprise backup software. At this rate, I'd be better off running rsync manually. No where near as fast but at least it works :(

      
                
                
                    
                                                    Sun, 02/02/2020 - 12:15
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    HostXNow
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 118
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Seems to be working now though the issue of the On/Off button not working is still a problem and has been since the last few updates. I added an attachment.
 
PS is there server/network status page for Acronis. It would be good to be able to check if there are any issues and subscribe to be notified of any issues Acronis side. Saves customers trying to keep adjusting things to try to get things working unnecessarily. 

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      528509-179045.png

                      44.87 KB
                  
          
    

                    
    
                
                
                    
                                                    Sun, 02/02/2020 - 14:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Acronis Backup Cloud - Server Backup Software for cPanel/WHM by Acronis

Cloud Hosting UK - Cloud Hosting w/ LiteSpeed & Imunify360 Security

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris,
Please, consider opening a support ticket if you are still facing an issue with the On/Off button on cPanel. If it is something related with product's functionality it is worth fixing it. Screenshot won't be enough, sharing logs from cPanel/WHM Acronis Backup plugin would help more on investigating that issue.

As for your second question, we currently don't have the requested page but it is planned for development in the nearest future, can't engage myself with ETA. It will be a public status page from where partners will know what is happening in real time before raising tickets. It will be a publicly available status page with details from each DC separetely.
Regards,
Ivaylo


      
                
                
                    
                                                    Mon, 02/03/2020 - 12:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
