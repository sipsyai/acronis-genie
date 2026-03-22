# Always incremental (single-file) Question

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/always-incremental-single-file-question

## Original Post
**Author:** Unknown

Always incremental (single-file) Question

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Michael Gralke Augusto
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,
I am having some difficulty understanding how to properly implement Always incremental (single-file) backups which are advised as the best solution for cloud backups.
I have read a lot of information and am currently running this test:
Where to back up
Cloud storage
Schedule
Every day repeat every 1 hour(s) from 00:00 until 23:45 (Always incremental)
How long to keep
6 hours
It seems that doing it this way a new FULL BACKUP is created every 6 hours and during the next 5 hours incremental backups are also added, is that correct?

But, is this really a new FULL BACKUP (starting from scratch) or is it just adding the 1st incremental backup to the original backup?
In this test any content before Today 13:00 would be lost because it's the 1st FULL BACKUP.
But does that apply also to any following incremental backups?
Please advise,
Michael
 
 
 
 
 
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 12/17/2025 - 18:35

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello,
Thank you for contacting us.
That configuration is not a standard backup scheme for Acronis Cyber Protect Cloud.
Please note that selecting such a short retention period for incremental backups (every 6 hours) may lead to unintended results. Incremental backups always depend on a corresponding full backup as their base. If incrementals (or their base full backup) are deleted too often that's expected.
We recommend reviewing the backup and retention settings to ensure they align with supported and recommended configurations.
If you need help validating or adjusting the setup, please contact our Support team ( or your MSP ) so they can review the configuration in detail ( https://support.acronis.com/ ).
Best regards,

      
                
                
                    
                                                    Thu, 12/18/2025 - 13:59
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Michael Gralke Augusto
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi José,
Many thanks for your quick reply.
Like I said, this was just a quick test for me to understand how it works without waiting too many days or weeks for the results :),
All the best*,
Michael
*FELIZ NATAL e BOM ANO NOVO.

      
                
                
                    
                                                    Thu, 12/18/2025 - 18:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Michael Gralke Augusto wrote:

Hi José,
Many thanks for your quick reply.
Like I said, this was just a quick test for me to understand how it works without waiting too many days or weeks for the results :),
All the best*,
Michael
*FELIZ NATAL e BOM ANO NOVO.


You are welcome Michael!
Feliz Natal para si também.
 

      
                
                
                    
                                                    Fri, 12/19/2025 - 09:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
