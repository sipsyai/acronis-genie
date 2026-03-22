# Storage Locations

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/storage-locations

## Original Post
**Author:** Unknown

Storage Locations

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    DIMITRIS KAMPOURIS
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi all,
How can we indentify in which storage center we are located? (Strasbourg or Frankfurt?)

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 05/10/2018 - 09:23

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Evgeny Ryuntyu
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 56
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Dimitris!
 
It's Evgeny from Acronis Service Provider Support.
You can identify which storage is used by logging into the Management console of Acronis Data Cloud.
1) Connect through your browser to https://cloud.acronis.com
2) Select Management Portal
3) On the left choose the Overview tab
4) Hover over Cloud storage and you will see either baas-fes-eu2.acronis.com or fes-baas.acronis.com
Based on what you see in the Cloud storage you can judge which storage location is used.
You can also find the list of Datacenters and their addresses in the following KB article
 
PS: you can also check which DC your account is attached to by submitting the following API request in the browser:
https://baas.acronis.com/api/1/accounts?login=<your_login&gt;
In the response you will see the Datacenter's prefix. see the similar example (account is fake)
https://cloud.acronis.com/api/1/accounts?login=testttt1
{"server_url":"https:\/\/eu2-cloud.acronis.com","id":0,"login":"testttt1"}If you have any questions, please feel free to ask. 
 
Best regards,
------------------------------------------------------------------------------------------------
Evgeny Ryuntyu | Senior Support Engineer
Acronis 

      
                
                
                    
                                                    Thu, 05/10/2018 - 12:41
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    feijao
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi,
 
Can we change our account DC? We would like to change from UK - London to France 

      
                
                
                    
                                                    Wed, 07/04/2018 - 16:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello feijao,
thank you for your posting! You'll need to contact your service provider to discuss the possibility of changing the storage location. 

      
                
                
                    
                                                    Mon, 07/09/2018 - 08:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
