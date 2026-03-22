# Start backup from client

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/start-backup-client

## Original Post
**Author:** Unknown

Start backup from client

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    chell solutions
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I wish to use a scrip on the client to start the backup. I have found documentation for the standard Acronis products, they don't seem to work for the Acronis cloud. Can it be done?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sat, 07/22/2017 - 18:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi
In short - yes it is possible.
The agent that Acronis uses in Acronis Backup Cloud is the same as the one used in Acronis Backup 12. It will be updated to the one used in 12.5 later with Acronis Backup Cloud version 8.0.
This means that all task-related activities are exactly the same. And there are different ways to actually do scripting for Acronis Backup Cloud:
1. You can create a backup plan in the Cloud Console, find the respective task ID in the local agent and start it with the script > it will run all the settings from Cloud Console, but on your custom triggers. Use acrocmd list tasks to get the ID and acrocmd run task to start it
2. You can use acrocmd to run any custom action on the agent. Acrocmd has been imported to Acronis Backup Cloud as is, so some features, although present, will not work. But most important ones will work OK.
3. More flexibility can be done with some very custom scripts, but this one already requires deeper knowledge of the product > you'll need to parse the DML databases to extract and modify settings, work with the scheduler etc. I don't think you'll ever need this actually.
But if you do need a very custom script I would suggest that you log a call with the Acronis support team and they will be able to direct you in the correct direction.
Regards

      
                
                
                    
                                                    Wed, 08/16/2017 - 07:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products
