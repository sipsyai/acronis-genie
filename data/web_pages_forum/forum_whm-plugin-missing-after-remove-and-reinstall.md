# WHM plugin missing after remove and reinstall

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/whm-plugin-missing-after-remove-and-reinstall

## Original Post
**Author:** Unknown

WHM plugin missing after remove and reinstall

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Chris Jutting
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Our WHM server is running on Ubuntu. I had our WHM server set up with the Acronis agent before finding out there was a WHM plugin, so I installed the plugin while the agent was installed but the plugin wouldn't load anything after logging in to it. So I removed the agent, and the plug in disappeared. I removed and reinstalled the plugin but it is still not listed. I have tried everything and it still doesn't list under plugins, even though the service is running per the ps aux | grep acronis_backup_srv command. I am at a loss what to do here. Any input?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 05/03/2023 - 16:41

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Chris.
Please check if this procedure was followed and installed properly:
- https://www.acronis.com/en-us/support/documentation/WHMCPanel/#installi…
- https://www.acronis.com/en-us/support/documentation/WHMCPanel/#installi…
If you use the version v110 of the plugin, please check this KB and apply the solution: https://kb.acronis.com/content/72127
Let me know if that resolved the issue.
If everything is settled correctly according to the manual and the issue persists, I would advise you to raise a ticket with our support or contact your service provider to do it, because this would need to be investigated. https://kb.acronis.com/content/8153
Thanks in advance!

      
                
                
                    
                                                    Wed, 05/03/2023 - 17:03
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Chris Jutting
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I followed that guide, but it did not work. The plug in isn't showing in WHM after running the script. The issue referenced in the KB does not apply for me.

      
                
                
                    
                                                    Wed, 05/03/2023 - 19:09
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Chris Jutting wrote:

I followed that guide, but it did not work. The plug in isn't showing in WHM after running the script. The issue referenced in the KB does not apply for me.


Hello Chris. 
Thanks for the reply.
Then I suggest you raising a ticket with our support describing the behavior, because the issue should be investigated.
Please let me know if you face any issues during that process.
Thanks again.

      
                
                
                    
                                                    Thu, 05/04/2023 - 08:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
