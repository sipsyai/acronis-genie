# Expressesion test has failed with SQL job

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/expressesion-test-has-failed-sql-job

## Original Post
**Author:** Unknown

Expressesion test has failed with SQL job

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Global-e | CS   
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 11
                
            
            
                
                    Comments: 17
                
            
                                                        
    
    
        
    


                
                
                    
                        
            One of our customers receives the following error on an SQL job:
 
Internal error: An expression test has failed.
MODULE
309
BERICHT
Command 'Backing up' has failed.

Aanvullende informatie:
------------------------
Foutcode : 61
Module: 309
LineInfo: 0x4A8728DC8A1C9515
Velden: {"$module":"service_process_vsa64_1621"}
Bericht: Command 'Backing up' has failed.
------------------------
Foutcode : 803
Module: 349
LineInfo: 0xA14D72EEB8F971B5
Velden: {"$module":"ArsAgentProvider_vsa64_1621"}
Bericht: Failed to execute a task.
------------------------
Foutcode : 31
Module: 349
LineInfo: 0x0DE48F7195FCD178
Velden: {"Expression":"!currentBunchChunks.IsNull()","$module":"ArsAgentProvider_vsa64_1621"}
Bericht: Internal error: An expression test has failed.
 
 
Any idea how we can fix this?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 05/10/2016 - 10:32

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Global-e | CS,
Thank you for your posting! As far as I can see the build version of a backup client you are running is a rather old one, I would highly recommend to update to the latest build 2406 and re-attempt backup.
Thank you,

      
                
                
                    
                                                    Wed, 05/25/2016 - 16:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jayaseelan Paulraj
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We are receiving the similar error message and i have uploaded here in the log file
Currently we are at the version 12.0.4560

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      443062-144129.txt

                      1.39 KB
                  
          
    

                    
    
                
                
                    
                                                    Sun, 02/11/2018 - 10:14
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jayaseelan Paulraj
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            We are receiving the similar error. Attached the log files

      
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      443064-144131.txt

                      1.39 KB
                  
          
    

                    
    
                
                
                    
                                                    Sun, 02/11/2018 - 10:18
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jayaseelan,
Your open support ticket has been escalated to the experts team. Please continue investigation with our engineers and if possible, share the outcome here. Thank you! 

      
                
                
                    
                                                    Wed, 02/14/2018 - 10:09
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
