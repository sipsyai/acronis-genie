# Backup types question

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/backup-types-question

## Original Post
**Author:** Unknown

Backup types question

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello, I have a question regarding backup types. Acronis says that the scheme Always Incremental - Single file is the proposed one.
I have a local backup, followed by a cloud one. Due to issues on the cloud quota (as described to another thread), I need to remove backups from the cloud storage to free space.
I have 38 backups, only the first (May 1) is full, all the others are incremental, up to July 19, which it stops due to quota.
2 questions:
1. If I keep only the full backup, delete all the incrementals, and create a new incremental, is the chain broken between the full (created on May 1), and the Incremental (created July 25)?
2. Is the option Cleanup By number of backups better than the by Backup Age?
 
Best regards
K



      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 07/25/2024 - 14:44

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Kostas,
If you delete all the incremental backups, leaving just the full backup, the chain shouldn't break. It will simply continue.
Regarding your second question, by default, the cleanup is set by age because most of our customers prefer it that way. However, if you believe that in your situation you only need to recover backups made in the shorter term, cleanup by the number of backups can be a suitable option. It depends on your specific needs.
Best regards.
 

      
                
                
                    
                                                    Thu, 07/25/2024 - 14:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you,
Can you please explain in my example, I have set the monthly expiration in 2 months. First monthly backup is May 1. Cleanup will occur at July 31?
Best regards
Kostas 

      
                
                
                    
                                                    Thu, 07/25/2024 - 15:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Kostas Backas wrote:

Thank you,
Can you please explain in my example, I have set the monthly expiration in 2 months. First monthly backup is May 1. Cleanup will occur at July 31?
Best regards
Kostas 


Not necessarily. It should happen once the next full backup is executed. So imagine it will be executed in the 1st of July, once that happens, the retention rules take place. If for example the backup fails, the cleanup will just happen once that full backup is finished. Happens this way to make sure that you will always have a full backup in the structure.
Best regards.

      
                
                
                    
                                                    Thu, 07/25/2024 - 15:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Kostas Backas
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 5
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good answer!
On the Always Incremental - Single file, when it will create Full backups, besides the first day which is started?
 
Best regards
Kostas
 

      
                
                
                    
                                                    Thu, 07/25/2024 - 15:36
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Kostas Backas wrote:

Good answer!
On the Always Incremental - Single file, when it will create Full backups, besides the first day which is started?
 
Best regards
Kostas
 


Hello!
This means that only the first backup is a full backup; subsequent backups are always incremental.
After you create a protection plan, you cannot switch between the Always incremental (single-file) scheme and the other backup schemes. Always incremental (single-file) is a single-file format scheme, while the other schemes are multi-file formats. If you want to switch between formats, you'll need to create a new protection plan.
The pre-set scheme for the program is Monthly full, Weekly differential, Daily incremental (GFS).
For more details, you can refer to this documentation.
Best regards,

      
                
                
                    
                                                    Thu, 07/25/2024 - 15:48
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
