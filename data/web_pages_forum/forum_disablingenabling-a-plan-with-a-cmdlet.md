# Disabling/Enabling a Plan with a CMDlet

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/disablingenabling-plan-cmdlet

## Original Post
**Author:** Unknown

Disabling/Enabling a Plan with a CMDlet

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Lukas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
I decided to make a script which first get's me the planID and then enable or disable the plan; each with a separate script.
Here the behaviour:
acrocmd list plans --output=raw
Plan is deactivated: no entries from
Plan is activated: the plan is named and the ID is there
acrocmd disable plan --id XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
See log file
acrocmd enable plan --id XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
See log file
For that I didn't found a solution yet. Maybe reinstall Acronis Cyber Protect, but that is not the way i'd like to solve this problem.

Solved:
It was: "Run as Administrator"...

 


      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      DisablePlan_ClientProtection_0.txt

                      1.25 KB
                  
              
                      EnablePlan_ClientProtection_0.txt

                      163 bytes
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Wed, 03/24/2021 - 14:01

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for contacting us Lukas. 
I am glad to hear you have found a resolution to your query. 
In the future if you need any further assistance please dont hesitate to contact us. 

      
                
                
                    
                                                    Tue, 03/30/2021 - 09:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
