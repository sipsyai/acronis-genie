# Internal error: An expression test has failed.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/internal-error-expression-test-has-failed

## Original Post
**Author:** Unknown

Internal error: An expression test has failed.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    muhammed najath
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Dear all ,
how to resolve this error :Internal error: An expression test has failed.deatils  are given below
DATE AND TIME
Apr 15, 2018, 09:47:29 AM
CODE
0x01350016+0x01350016+0x01330029+0x01350035+0x015D0323+0x015D001F
MODULE
309
MESSAGE
Backup failed

Additional info:
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"mms_vsa64_4670"}
Message: TOL: Failed to execute the command. Backup plan 'SQL data to Cloud SH01'
------------------------
Error code: 22
Module: 309
LineInfo: 0x8D165E86FB819595
Fields: {"CommandID":"D332948D-A7A9-4E07-B76C-253DCF6E17FB","$module":"agent_protection_addon_vsa64_4670"}
Message: TOL: Failed to execute the command. Backup plan 'SQL data to Cloud SH01'
------------------------
Error code: 41
Module: 307
LineInfo: 0xE6792A5EE190DDE7
Fields: {"$module":"agent_protection_addon_vsa64_4670"}
Message: Failed to execute the command.
------------------------
Error code: 53
Module: 309
LineInfo: 0x2E7E9E174F1FB719
Fields: {"$module":"agent_protection_addon_vsa64_4670","FailCount":"4"}
Message: 4 activities have not succeeded. One of them is displayed.
------------------------
Error code: 803
Module: 349
LineInfo: 0xA14D72EEB8F971B2
Fields: {"$module":"ArsAgentProvider_vsa64_4670"}
Message: Failed to execute a task.
------------------------
Error code: 31
Module: 349
LineInfo: 0x0DE48F7195FCD16A
Fields: {"$module":"ArsAgentProvider_vsa64_4670","Expression":"CurrentChunks->IsValid()"}
Message: Internal error: An expression test has failed.
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Sun, 04/15/2018 - 08:27

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dear Muhammed!
 
Let me first give you a short answer - You could use such archive for recovery purposes, however further backups will fail. To resolve this issue, please start a new backup job (needs to be a new archive).
 
A permanent solution to this issue would be available in the upcoming Acronis Backup Cloud 7.7 release. The date for the release is not scheduled yet, but it will be in Q2 2018.
We will then introduce a new format of the archive that would store the data a bit differently, avoiding issues like this.
 
Have I answered your question?

      
                
                
                    
                                                    Mon, 04/16/2018 - 13:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud
