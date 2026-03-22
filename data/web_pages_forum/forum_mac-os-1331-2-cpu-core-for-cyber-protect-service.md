# Mac OS 13.3.1 2 cpu core for "cyber-protect-service"

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/mac-os-1331-2-cpu-core-cyber-protect-service

## Original Post
**Author:** Unknown

Mac OS 13.3.1 2 cpu core for "cyber-protect-service"

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Dietmar Hafner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello
since a few days i experience massive CPU consumption with our Cyber Protect Cloud service.
The service consumption does not stop since days, it's constantly running.
What I did so far:
I uninstalled the agent and re-installed but issue returned to constantly using 2 CPU cores of my 7 core machine MacBook Pro 16inch 2019 model.
Disabled within my protection plan any services of cyber protection cloud, just kept the backup service. -> does not change, sitll running with high CPU load.
Since the process protects itself from stopping, my MacBook constantly makes noise because of high CPU load. 
Please advise how to get this resolved.
Many thanks
Dietmar
 

      
                                                    
            
                            
  
  
      
      
                  Attachment
                  Size
              
    
  
      
              
                      Bildschirmfoto 2023-04-20 um 12.26.19.png

                      978.6 KB
                  
          
    

                    
    
                                            
                
            
                            
                    
                        
                            
                              Thu, 04/20/2023 - 10:28

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Dietmar!
This issues with the performance should be investigated. That behavior is not expected at all and I wouldn't advise to apply any workarounds in this situations.
Please collect the following logs:
-open the Activity Monitor application (from the Utilities folder inside your Applications folder).
After opening Activity Monitor, make sure the CPU tab is selected.
Select the process from the list. To find it easily, search for it using the search field at the top right. Typically you want to sample mms and service_process.
Click the Action pop-up menu (looks like a gear) in the toolbar, then select Sample Process.
A new window will open to display the sample. When Activity Monitor finishes sampling, click Save… to save the result as a text file.
- System report: https://kb.acronis.com/content/54608
- Screenshot showing the overloading activity.
After collecting those logs, please raise a ticket with our support or contact your service provider to do it https://kb.acronis.com/content/8153
Let me know if you have any questions during this process.
Cheers!

      
                
                
                    
                                                    Thu, 04/20/2023 - 10:52
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dietmar Hafner
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
I opened the ticket as mentioned. 
many thanks
Dietmar

      
                
                
                    
                                                    Thu, 04/20/2023 - 13:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Dietmar Hafner wrote:

Hello,
I opened the ticket as mentioned. 
many thanks
Dietmar


Thanks for updating!
Cheers! 

      
                
                
                    
                                                    Thu, 04/20/2023 - 14:05
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
