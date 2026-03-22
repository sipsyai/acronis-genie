# Acronis storage gateway with Azure backend setup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-storage-gateway-azure-backend-setup

## Original Post
**Author:** Unknown

Acronis storage gateway with Azure backend setup

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    eric ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have install a acronis storage gateway at azure with azure backup configured. I can register it to the Acronis backup cloud console, but find that the status of the acronis-stoage-gateway services are show "active (exited)", and can't find tcp 44445 is listening from netstat, detail as follow:
$ systemctl status acronis-storage-gateway
● acronis-storage-gateway.service - SYSV: Acronis Storage Gateway
   Loaded: loaded (/etc/rc.d/init.d/acronis-storage-gateway)
   Active: active (exited) since Mon 2016-06-20 10:15:15 HKT; 21min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 1002 ExecStop=/etc/rc.d/init.d/acronis-storage-gateway stop (code=exited, status=0/SUCCESS)
  Process: 1011 ExecStart=/etc/rc.d/init.d/acronis-storage-gateway start (code=exited, status=0/SUCCESS)
 
also, I would like to clarify the following:
1. The parameter <HomePath> inside the acronis-storage-backed-azure.xml, does it refer to the container name of the azure storage? so, if I have a container 'backup' inside the azure storage, should I define it as <HomePath>/backup</HomePath> in the file?
2. how to read the log file in /var/log/Acronis/..., the format is .blg and it is all binary. do I need a tools to read it?
 
Thanks very much for your help.
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/20/2016 - 02:52

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Eric,
Thank you for your posting! As far as I see the issue is still investigated by our support team. Could you please confirm once the issue is resolved, so that we can share the solution with other users.
Thank you!

      
                
                
                    
                                                    Mon, 06/27/2016 - 14:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    eric ngun
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Finally, service provider team find out that the error is due to the xml file format are generate incorrectly. problem fix after fixing the xml format.

 1. For the format of the parameter <HomePath>, it should be starting with a "/" + azure storage container name, like my example <HomePath>/backup<?HomePath> where your azure container name is 'backup'. 
2. For how to read the log file, I am still searching for it and not idea at the moment.
these are the information I got up to now

      
                
                
                    
                                                    Tue, 06/28/2016 - 02:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for details, Eric!

      
                
                
                    
                                                    Fri, 07/01/2016 - 08:40
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
