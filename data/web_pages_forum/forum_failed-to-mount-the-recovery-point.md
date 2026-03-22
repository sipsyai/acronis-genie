# Failed to mount the recovery point.

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/failed-mount-recovery-point

## Original Post
**Author:** Unknown

Failed to mount the recovery point.

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi
 
When I try to restore files inside the Acronis cpanel plugin, I get the following error message:
Failed to mount the recovery point.
In the mms.0.log I found the following:
2020-11-03T16:56:25:867+01:00 140574684256000 E02BF0005: Error 0x2bf0005: Assertion failed: found || !"mtab not synced", file d:/624/linex/utils/trueimagemnt/wrapper/wrapper_main.cpp, line 418
I'm using agent version 15.0.24647.
How can I fix this?
Regards
Michael
 
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Screenshot (1).png

                      53.3 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Tue, 11/03/2020 - 17:09

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Do you have File Excludes configured in your backup plan?

      
                
                
                    
                                                    Thu, 11/05/2020 - 22:06
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Brunner
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 21
                
            
            
                
                    Comments: 33
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            no, we don't use excludes.

      
                
                
                    
                                                    Fri, 11/06/2020 - 17:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Michael,
Thank you for sharing your issue, the UI error is too generic.
Judging by the error from the mms.0.log I can only assume that there are two backup plans with pre/post data capture commands enabled. It is a scenario that we don't support with the Acronis plugin for cPanel. It looks like trueimagemnt tries to mount a recovery point from one archive while still having recovery points mounted from different archive.
If this is not the case I would suggest submitting an Acronis Support ticket as it would require deeper investigation. We need to look at the logs, applied protection plan and protected machine configurations. Provide the login for the affected customer tenant, name of the affected server and plugin logs from cPanel: Home > Acronis Backup > Dashboard > Download log button on the bottom right.
Thank you in advance.

      
                
                
                    
                                                    Sat, 11/07/2020 - 21:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
