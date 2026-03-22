# save on rdx failed the first time but not the second or manually

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/save-rdx-failed-first-time-not-second-or-manually

## Original Post
**Author:** Unknown

save on rdx failed the first time but not the second or manually

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    gaetan lagraviere
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Sorry if my English language is bad, i will do my best to be well understood by all.
 
I got a problem : when one of my job (save on rdx) is running, it failed because of the read and write access on the tibx file on only one VM for the specified user but when the second try on the same job is going, the error will not appear and the job is done.
If i start this job manually, the job is done at the first try.
 
Somebody can help me with this error? I don't understand why the error is here and why the second try is ok and manually is ok too. What is the different in these jobs?
 
Thx for your help

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 10/30/2025 - 10:28

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Gaetan,
What product are you using?
From your description, it seems to be either Acronis Cyber Protect Cloud or Acronis Cyber Protect 15/16.
The first scheduled attempt likely fails because the RDX drive or archive isn’t yet accessible — by the time the second attempt runs, it’s already ready.
Also, please confirm that the account used by the scheduled task is the same one you use when running the job manually. If they’re different, permission differences could explain why the manual run succeeds while the scheduled one fails.
Best regards.

      
                
                
                    
                                                    Thu, 10/30/2025 - 11:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    gaetan lagraviere
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello José Pedro,
Thank you for your answer.
 
The product seems to be Acronis Cyber Protect Cloud, sorry for the mistake.
The job is the same : the 2 planified attempts and manually.
The job restart a second time if the first failed and manually, i click on this job to start so the user is the same.
 
Best regards

      
                
                
                    
                                                    Thu, 10/30/2025 - 11:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            gaetan lagraviere wrote:

Hello José Pedro,
Thank you for your answer.
 
The product seems to be Acronis Cyber Protect Cloud, sorry for the mistake.
The job is the same : the 2 planified attempts and manually.
The job restart a second time if the first failed and manually, i click on this job to start so the user is the same.
 
Best regards


That’s probably due to insufficient permissions on some of those VMs.
Please contact our support team so we can review the logs in detail.
Best regards.

      
                
                
                    
                                                    Thu, 10/30/2025 - 13:23
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
