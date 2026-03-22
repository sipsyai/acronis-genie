# Error occurred while reading the file.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/error-occurred-while-reading-file

## Original Post
**Author:** Unknown

Error occurred while reading the file.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I received this message what means ? could be the link is off-line at moment of backup ?
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 06/16/2018 - 15:15

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            acitvity log atached

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      453023-148703.txt

                      43.77 KB
                  
          
    

                    
    
                
                
                    
                                                    Sat, 06/16/2018 - 15:16
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Suporte
Based on the log you have provided I can see the following:
Archive 'Servidor-PC-7ABCAA7B-FDC4-424E-9895-3355ADAD2C14-51DEF5F9-9863-4756-B487-2C1B31D3D395A.tibx' is corrupted.
Archive validation error: Error 0xa1006e: Failed to validate archive 'Servidor-PC-7ABCAA7B-FDC4-424E-9895-3355ADAD2C14-51DEF5F9-9863-4756-B487-2C1B31D3D395A'.
As you can see on the above it seems that your archive has become corrupted what I would suggest firstly is to ensure that backup validation is enabled on your backup set and run the backup again. Then please advise if this resolves your issue if not please provide a new log after that backup
Regards

      
                
                
                    
                                                    Tue, 06/19/2018 - 07:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello guys,
 
It's Evgeny from Acronis Service Provider Support.
The issue is known and will be fixed in Acronis Data Cloud 7.7 Update1. It is expected to be released during this summer.
The root cause is related to archive version update procedure is triggered on open and wants to read and write, but the encryption key is not yet provided on archive opening, so opening fails.
The internal reference that will be appearing in the release notes is ABR-165620
 
Best regards,
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis

      
                
                
                    
                                                    Tue, 06/19/2018 - 11:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Suporte
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 24
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you folks, but when this knowned , error o  occurs again, does we have to repeat backup or only skip the error ?
 
Thanks.

      
                
                
                    
                                                    Wed, 06/20/2018 - 17:09
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Aconis Backup Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Suporte,
Sorry for delayed response! If you’re ok with waiting for 7.7U1, it will be possible to continue backing up to the same archive. Otherwise, you can create a new archive and workaround the issue before release of Update 1. I'd recommend waiting for the Update though, it should be available in the shortest time. 
 

      
                
                
                    
                                                    Wed, 07/18/2018 - 08:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
