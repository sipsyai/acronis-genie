# Question about setting "How long to keep"

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/question-about-setting-how-long-keep

## Original Post
**Author:** Unknown

Question about setting "How long to keep"

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi to all!!
I have a question where is this. If i set always incremental setting to my scheme and set in "how long to keep" for an example 1 month after one month what it will do? It will upload a full back-up?

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/02/2019 - 15:17

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Stilianos!
Thanks for the question!
I'v got a short answer and a long one.
Short one - after 1 month, the first recovery point will be removed, but the archive will not have to re-do entire backup from scratch, as the data liable to stay in the archive will be consolidated\merged
 
Long answer - Note that "How long to keep" option has a few sub-options (or a few ways to determine how long a recovery point would be actual - by number of days or by number of backups).
If "by number of days" is chosen, sub-options are "Monthly", "Weekly" and so on. How long to keep is set up for each on separately, defining no more and no less than how long to keep each type of recovery points. With retention rules defined to keep backups 1 month, each backup recovery point that is created before 1 calendar month is eligible to be cleaned up.
Note that always-incremental scheme perform a full-backup only once - when you first run the backup job. When the time to remove old recovery points comes, the data-set that was chosen in the inclusion rules is re-distributed between the recovery points so that you always have a representation of the original files as they were by the time a backup job has made a snapshot.
 
Please refer to the following User-Guide article on the matter -> https://www.acronis.com/en-us/support/documentation/BackupService/index…
 
Hope I was able to cover your question! Let me know if I can assist you further on this topic!
 

      
                
                
                    
                                                    Mon, 01/14/2019 - 14:14
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Fedor Kondrashov
Thanks you very much for your time!
Everything ok with alwasy incremental that have to do with cloud, but i have one more little question.
Because in schedule in local backup plan is there only options "Always full, Weekly full-Daily incremental, and Custom". It do not give me option always incremental, so i must choose a full between a period. So i choose custom and schedule once per 6 month a full and the others incremental. Is there an option always incremental?
Thanks in advanced.

      
                
                
                    
                                                    Tue, 01/22/2019 - 10:38
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stilianos wrote:

Because in schedule in local backup plan is there only options "Always full, Weekly full-Daily incremental, and Custom". It do not give me option always incremental, so i must choose a full between a period. So i choose custom and schedule once per 6 month a full and the others incremental. Is there an option always incremental?
Thanks in advanced. 


Hi! This is normal for existing backups plans, which already use a different backup format. You'll need to create a new plan in order to select Always incremental scheme (which will produce an archive of a Single-file format) 

      
                
                
                    
                                                    Fri, 02/01/2019 - 12:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Stilianos
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 13
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina. Option always single doesnt exists in local setup, only in Cloud.

      
                
                
                    
                                                    Mon, 02/04/2019 - 14:49
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Stilianos wrote:

Hi Ekaterina. Option always single doesnt exists in local setup, only in Cloud.


Just tested this scenario - looks like Always-incremental format is available for the disk-level backups only (local), would it be possible for you to back up disks/partitions instead of files?  
Always incremental scheme for the file-level backups (local) is planned to be added in the next product version. 

      
                
                
                    
                                                    Mon, 02/11/2019 - 16:22
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
