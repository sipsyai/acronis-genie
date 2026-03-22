# linux service not start

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/linux-service-not-start

## Original Post
**Author:** Unknown

linux service not start

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I installed acronis on a linux machine, but the system crashed and when I try to start the service again it does not return. i run comand sudo service acronis_mms start but  not start . when i check with command sudo service acronis_mms status , its stopped . 
linux centos .

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 10/21/2018 - 11:06

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Installed agents:
Agent for Linux (64-bit) (12.5.10790)
Operating system:
 
GNU/Linux
CPU:
 
Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz
RAM:
 
62.9 GB

      
                
                
                    
                                                    Sun, 10/21/2018 - 11:07
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ola!
Typically, most common cause would be some missing packages required for Agent for Linux to work.
Check that your system is supported, check that the packages are available - https://www.acronis.com/en-us/support/documentation/BackupService/index…
Check the /var/log/messages for errors.
 
I would recommend to generate a system information report and submit a support request for further checks.
Collecting System Report -> https://kb.acronis.com/content/54608
 
Thanks in advance!

      
                
                
                    
                                                    Mon, 10/29/2018 - 08:56
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
