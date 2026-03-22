# BMR of a customer server without customer login details

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/bmr-customer-server-without-customer-login-details

## Original Post
**Author:** Unknown

BMR of a customer server without customer login details

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
I need to do a full restore of a customer server with the bootable media. The server is registred to the customer account in my partner account. When I boot with the ISO, I can not connect with the credentials of my partner account to the cloud storage. Do I really have to ask my customer for his password to do this full restore?
Regards
Michael

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 01/31/2019 - 07:03

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Michael!
 
It's Evgeny from Acronis Service Provider Support.
 
With the latest bootable media available on DCs updated to 7.8U2 (12420 build) you can choose to either connect with the Customer's credentials OR use the registration token for the connection.
When recovering Windows or Linux, click Tools > Register media in the backup service, and then specify the registration token that you obtained when downloading the media. If you do this, you will not need to enter credentials or a registration code to access the cloud storage.
https://www.acronis.com/en-us/support/documentation/BackupService/index…
To generate the code - connect to the console and click Add. Then scroll down.

 
-----------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis Backup Cloud | #1 Cloud Service Provider Backup
 

      
                
                
                    
                                                    Thu, 01/31/2019 - 07:40
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Great, thanks a lot! In this case I wait for the update in EU2.
Regards
Michael

      
                
                
                    
                                                    Fri, 02/01/2019 - 08:37
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Evgeny
But even with this new solution, I need the login details from my customer to generate the registration token. I can find this part only under "ADD" when I login with the customer login. When I login with my partner login and then go to the customer, I can't find the generate button under ADD.
I need a solution to do a bare metal restore without asking my customer for this login details.
Regards
Michael

      
                
                
                    
                                                    Thu, 02/21/2019 - 15:52
