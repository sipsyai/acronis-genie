# Backups to Cloud - Verification

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backups-cloud-verification

## Original Post
**Author:** Unknown

Backups to Cloud - Verification

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Robert Pearman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Since we enabled verification on our backup to cloud jobs, performance has dropped and the time to run the jobs can reach 24+ hours. 
It also seems to be maxing out our DOWNLOAD speeds, can someone confirm how the verification works?
Our expectation was it would be verifying some sort of hash of the incremental job, but it appears to be downloading the entire job history (in some cases 00s of GBs) each time the job runs. That cannot be right!

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 07/01/2020 - 15:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Robert,
Welcome to Acronis forums!
This behavior is expected. You turned on Backup Validation  
Validation is a time-consuming process an incremental or differential backup even for small size files. This is because the operation validates not only the data physically contained in the backup, but all of the data recoverable by selecting the backup. This requires access to previously created backups, including a full backup.
We recommend running validation as a separate plan (this functionality is available with Advanced license type) and schedule these operations for off-peak hours to minimize network bandwidth consumption.
 

      
                
                
                    
                                                    Thu, 07/02/2020 - 14:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Robert Pearman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            So, how can we be sure a backup that completes successfully, is actually useable without verification?
Also there is no warning when turning that option on, about your reccomendations!

      
                
                
                    
                                                    Fri, 07/03/2020 - 09:38
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Robert.
The off-host data processing separate plans for validation available with Acronis Cyber Backup 12.5 Advanced license. For other licenses, we recommend that you schedule backup with enabled validation on off-peak days and hours.

      
                
                
                    
                                                    Mon, 07/06/2020 - 07:18
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Péter Szatmári
                            

                            
                    
                        Frequent Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 619
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Robert!
Verification is mostly there to double check the backup and ensure it wasn't corrupted during storage. In my experience backups rarelly succeed if something goes wrong.
As an extra precaution you could try converting the backup to a VM, run it and check if it's working as expected, but it's more like an extra precaution not a substitute.
What Maria suggested can be found here (6.3.5) along with other tips.
Side story (why to try running the backup): I had a machine that had a pending windows backup that when rebooted and installed would make the machine unbootable (this was a serious windows update bug at the time). Unfortunately all the backups I had from the machine (since the pc wasn't powered down for several months) already contained this and when restored, it became unbootable. So it's perfectly possible to have validated backups that are not usable, not because the backup solution is inadequate, but because of the complexity of a computer configuration.
-- Peter
 

      
                
                
                    
                                                    Mon, 07/06/2020 - 07:50
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup 12.5
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Robert Pearman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I'm using the MSP system, so i don't have the option of off-host processing.
There is also no option for a seperate validation plan in that system.
Again, there is no warning that enabling verification is detrimental to performance, and to be honest i think this is the first time i have known a product to function that way. It seems to me like, downloading the entire image chain to verify is really short sighted, why cant acronis process the chain in the cloud to perform validation? Or is the ideal solution that we enable the system whose name i forget... the business continuity bit where you have the VM in the cloud.
Because i agree, doing that is the best solution all round, but, that should be added to documentation.
Peter, i agree and understand what you are saying, but it seems to me that if i have a full DR situation, and any local backups are gone, when i turn to the cloud versions i want to know they have integrity a failing patch making a machine unbootable is one thing, a corrupt backup in the cloud that cannot be restored is something else entirely.

      
                
                
                    
                                                    Mon, 07/06/2020 - 07:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Mischa Künzle
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 11
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Robert Pearman wrote:

I'm using the MSP system, so i don't have the option of off-host processing.
There is also no option for a seperate validation plan in that system.
Again, there is no warning that enabling verification is detrimental to performance, and to be honest i think this is the first time i have known a product to function that way. It seems to me like, downloading the entire image chain to verify is really short sighted, why cant acronis process the chain in the cloud to perform validation? Or is the ideal solution that we enable the system whose name i forget... the business continuity bit where you have the VM in the cloud.
Because i agree, doing that is the best solution all round, but, that should be added to documentation.
Peter, i agree and understand what you are saying, but it seems to me that if i have a full DR situation, and any local backups are gone, when i turn to the cloud versions i want to know they have integrity a failing patch making a machine unbootable is one thing, a corrupt backup in the cloud that cannot be restored is something else entirely.


FYI, the implementation of a separate validation plan for the MSP solution has been requested under RM-49. 
Support didn't give me an ETA on it, though.

      
                
                
                    
                                                    Fri, 01/29/2021 - 09:14
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Cloud - Evaluation
