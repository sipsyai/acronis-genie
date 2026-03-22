# Systems not registering in the Acronis portal

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/systems-not-registering-acronis-portal

## Original Post
**Author:** Unknown

Systems not registering in the Acronis portal

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Cath Barr
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            We have a customer that we are rolling out the cyber protect agents.  There are 12 computers on the same network with Windows 10.  All of them worked fine except 4 systems.  They won't register with the portal.  We've tried rolling it out with a script and manual install.  The links all work on the PCs when we pull up the registration url.  But it just sits saying it can't communicate.  Anyone else able to offer ideas?  We can't find any differences with these systems over the ones that work.  Tried rebooting, tried reinstalling at least 3 or 4 times.  Trying to upload the screenshots here but not working either.  Frustrated with this product as we are moving to it from another solution and keep having issues.  

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/19/2024 - 16:24

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Cath,
Welcome to our forum!
Please try the following steps to resolve the issue:

Ensure that the necessary services are running: Acronis Cyber Protect Cloud Services and Processes (e.g., mms.exe, aakore.exe).


Retry the manual registration via the command prompt: Manual Registration of Backup Agent.


If the issue persists, please run the connection tool test and review any errors in the output: Connection Verification Tool.
	(If errors are found, ensure the required ports/IPs are open, as this may prevent successful registration.)


If an antivirus program is being used, please ensure Acronis services are whitelisted and not blocked by the application: Acronis Software Exclusion from Antivirus.


Temporarily disable the antivirus and firewall as a test, then attempt the registration again.

If the issue continues after trying these steps, please raise a support ticket with our team for further investigation: Submit a Support Ticket.
Best regards.
 
 

      
                
                
                    
                                                    Fri, 09/20/2024 - 05:57
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Cath Barr
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for your reply.  We ended up finding some sort of WMI glitch even though when we tested WMI, it stated it was consistent.  It's fixed now.  

      
                
                
                    
                                                    Wed, 09/25/2024 - 13:06
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Cath Barr wrote:

Thanks for your reply.  We ended up finding some sort of WMI glitch even though when we tested WMI, it stated it was consistent.  It's fixed now.  


Hello Cath.
Thank you for updating the thread.
I am glad the issue is solved.
Best regards. 

      
                
                
                    
                                                    Wed, 09/25/2024 - 13:55
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
