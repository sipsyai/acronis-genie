# Cyber Protect not clearing out old backup files, can't even see that they are there

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/cyber-protect-not-clearing-out-old-backup-files-cant-even-see-they-are-there

## Original Post
**Author:** Unknown

Cyber Protect not clearing out old backup files, can't even see that they are there

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Ian Bakker
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have Cyber Protect Cloud set up to back up some files to a NAS I have onsite, but it's been giving errors recently of no space left, despite the fact that the NAS is about 2TB and the backup size should only be about 6-700GB. The following two screenshots show that physically on the NAS, there are a bunch of old Acronis backup files, and yet in the Acronis web portal it can't see that any of them exist. What are these old files? Can they be safely deleted? Why are they not cleaned up before a new backup starts to allow it enough space?

Here are some screenshots of the backup schedule that it does not appear to be following (the ones from may 19 are a manual test I did today, but I don't know why the other ones that don't appear to fit the schedule are there)


      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 05/19/2025 - 15:20

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  1 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello!
Retention rules are typically applied after backups are completed, to ensure the backup sequence and chain remain intact. Therefore, I wouldn't recommend deleting backups manually at this point.
? Learn more about how and when retention rules are applied
It’s possible that the backup plan was modified or something is misconfigured, which may explain why older backups haven't been removed — and that seems to be the case here.
Issues related to retention rules usually require log analysis, which isn’t possible via the forum.
Please raise a support ticket with Acronis or contact your MSP so we can verify whether the backup plan is functioning correctly and if retention rules are being applied as expected.
Best regards.

      
                
                
                    
                                                    Tue, 05/20/2025 - 09:49
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ian Bakker
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks for your reply. I'm a little confused that retention rules are applied after backups are completed, as it seems to be configured to clean up old files before the backup starts (otherwise there often wouldn't be enough space in the hard drives). Also, I don't think this would account for the errant 200GB files from september, early october, and january even though the web portal can only see a single backup from late october.
As for contacting my MSP, I actually am the MSP trying to solve this issue for a client.

      
                
                
                    
                                                    Wed, 05/21/2025 - 16:26
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ian Bakker wrote:

Thanks for your reply. I'm a little confused that retention rules are applied after backups are completed, as it seems to be configured to clean up old files before the backup starts (otherwise there often wouldn't be enough space in the hard drives). Also, I don't think this would account for the errant 200GB files from september, early october, and january even though the web portal can only see a single backup from late october.
As for contacting my MSP, I actually am the MSP trying to solve this issue for a client.


Retention rules are applied after a backup is created. This approach ensures that the backup process is not interrupted or compromised by cleanup operations. The retention process evaluates the age or number of backups and deletes those that exceed the specified criteria. It's important to note that the timing of the retention process is based on when it starts, not when the associated backup was created. This means that the software checks the backup's age at the moment the retention process begins
The behavior you've described seems unusual. It suggests that the backup plan may not be functioning as intended. An investigation is necessary to identify and resolve the issue.
Best regards.

      
                
                
                    
                                                    Thu, 05/22/2025 - 11:56
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ian Bakker
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Okay, how can I proceed with this investigation?

      
                
                
                    
                                                    Wed, 05/28/2025 - 19:32
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ian Bakker wrote:

Okay, how can I proceed with this investigation?


Hello!
You’ll need to raise a ticket with our support team or contact your service provider (if you're not entitled to direct support), so we can review the logs and identify the issue.
Thanks.

      
                
                
                    
                                                    Thu, 05/29/2025 - 10:04
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ian Bakker
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Again, I actually am the service provider trying to sort this out for one of my clients. I'll raise another support ticket.
Thanks

      
                
                
                    
                                                    Mon, 06/02/2025 - 13:11
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ian Bakker wrote:

Again, I actually am the service provider trying to sort this out for one of my clients. I'll raise another support ticket.
Thanks


Hello!
Feel free to update the thread if there are any updates.
Best regards.

      
                
                
                    
                                                    Wed, 07/09/2025 - 09:43
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
