# MMS Service will not start

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/mms-service-will-not-start

## Original Post
**Author:** Unknown

MMS Service will not start

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kevin Johnston
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Anytime I try to restart the MMS service I get the Windows error 1053.
I've attempted to reset the Service timeout period to double what it was originally set to, however what's strange is that during a service start, it immediately fails.
When checking event viewer, I can see that Acronis throws an error which tells me there was an "Error while writing to the file". Further in the error it calls out a file, "e:\72\file\windows\win32_file.cpp:247". However there is no E drive present on this machine.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 07/29/2019 - 14:22

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Kevin
Can you please advise what service logon you are using for the MMS service?
Regards

      
                
                
                    
                                                    Mon, 08/05/2019 - 15:34
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kevin,
First of all, please check if the user account under which Acronis Managed Machine service (MMS) is running has required rights according to the following KB:
https://kb.acronis.com/content/56202
 
“e:\72\file\windows\win32_file.cpp:247” in this case is the internal path of failing process. 
 
If MMS could not start by LocalSystem and LocalAdmin user please collect the crashdump (https://kb.acronis.com/content/45631) and system report (https://kb.acronis.com/content/54608) from the affected machine and raise a support ticket for investigation.
 

      
                
                
                    
                                                    Thu, 08/08/2019 - 10:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
