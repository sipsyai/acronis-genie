# Automatically stop backup schedule when files are crypted

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/automatically-stop-backup-schedule-when-files-are-crypted

## Original Post
**Author:** Unknown

Automatically stop backup schedule when files are crypted

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Mohamed Zaghouani
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Acronis Community,
I have a customer who is interested in backup and restore capabilities of Cyber Protect Cloud but he has already been deploying another solution for anti-malware and anti-ransomware protection. I have got a question from him saying if the anti-ransomware protection failed to detect a ransomware attack which caused the encryption of files how to prevent the backup agent to perform a new backup after this incident as regularly scheduled because the new ones when created may result in the deletion of old healthy backups according to the retention policy. Is there any configuration that should be done so the agent would not start the backup? or is the agent itself able to detect that files are encrypted so it would not start the backup ? or shall I rely on anti-ransomware protection of Acronis Cyber Protect Cloud so there's no way to keep ransomware attacks undetected and files being encrypted?
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/12/2023 - 09:30

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, Mohamed.
Thank you for contacting us.
If they use another antivirus solution and the machine gets compromised, there's no way to avoid a backup. If you install our agent without the antivirus/ransomware feature, our agent won't detect that the machine is compromised, and the backup will be executed according to the schedule.
The only alternative is to recover the machine to a previous date before the attack.
Please feel free to ask if you have any questions.
Thanks in advance!

      
                
                
                    
                                                    Mon, 06/12/2023 - 13:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mohamed Zaghouani
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you Jose Pedro for the answer.

      
                
                
                    
                                                    Mon, 06/12/2023 - 16:55
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Mohamed Zaghouani wrote:

Thank you Jose Pedro for the answer.


Hello Mohamed. I am glad that answered to your question.
Feel free to participate anytime.
Thanks in advance! 

      
                
                
                    
                                                    Tue, 06/13/2023 - 13:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
