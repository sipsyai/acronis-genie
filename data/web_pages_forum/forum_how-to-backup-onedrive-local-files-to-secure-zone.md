# How to backup OneDrive local files to Secure Zone ?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/how-backup-onedrive-local-files-secure-zone

## Original Post
**Author:** Unknown

How to backup OneDrive local files to Secure Zone ?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Sébastien Majérus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi everyone,
I'm using the cloud to cloud feature of Cyber Protect Cloud to back up OneDrive and other Microsoft 365 stuff but for security reason I would also like to back up a customer's OneDrive to a local Secure Zone destination.
I set up a test plan for this but it doesn't back up anything, the file is almost empty.
I know there is an issue when using the "save disk space" feature of OneDrive as it uses a special NTFS virtual filesystem. But in my case I ask OneDrive to download all files to disk. Sync is complete and all files local.
So my question is : is there a way to bypass this restriction to achieve my goal ?
Thanks a lot,
Seb
 
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 03/15/2024 - 09:19

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Sebastian,
Please check the following KB article where the limitation described by you and the possible workarounds are outlined: https://kb.acronis.com/content/73327
Feel free to contact our support if you have any additional queries at https://kb.acronis.com/content/8153.
Thanks in advance!
 
 

      
                
                
                    
                                                    Fri, 03/15/2024 - 15:28
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sébastien Majérus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jose,
I have read this KB but it doesn't fit exactly my issue.
The backup doesn't fail, no error at all.
All the files are local (files on demand feature is disabled) and synced.
My OneDrive weights about 300GB but the backup file only 175 KB. There is nothing in there except the directory names.
I don't think that support could help me as it is mainly a hard coded functionnality to not allow OneDrive local files backup. I was just looking for a workaround if any.
Please let me know if you experienced the same problem and found a solution.
Thanks a lot,
Seb
 
 
 
 

      
                
                
                    
                                                    Fri, 03/15/2024 - 15:43
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Sébastien Majérus wrote:

Hello Jose,
I have read this KB but it doesn't fit exactly my issue.
The backup doesn't fail, no error at all.
All the files are local (files on demand feature is disabled) and synced.
My OneDrive weights about 300GB but the backup file only 175 KB. There is nothing in there except the directory names.
I don't think that support could help me as it is mainly a hard coded functionnality to not allow OneDrive local files backup. I was just looking for a workaround if any.
Please let me know if you experienced the same problem and found a solution.
Thanks a lot,
Seb
 
 
 
 


Thanks for clarifying.
If you execute a regular files and folders backup and the size appears with only a few KBs but nothing is actually backed up, that's unexpected. It should either work properly or give you an error. This likely means that most of the files are being skipped. I suggest recreating a new plan and reselecting those folders. In the backup options, disable the VSS snapshots and retry the process.
If the issue persists after testing that, I suggest raising a ticket with our support so we can investigate the issue further: https://kb.acronis.com/content/8153
Thanks in advance!

      
                
                
                    
                                                    Fri, 03/15/2024 - 15:58
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Sébastien Majérus
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thank you for your advice but meanwhile I found what I did wrong and backup is now successfull.
I have two OneDrive accounts on my PC, one personal and one professional. They're synced in a folder on a second HDD which path is D:\Cloud.
In the "entire machine" backup, this folder was empty so I followed the KB and tried to back up the folder D:\Cloud instead of the entire machine. This is the back up that was empty and shown no error.
Reading your advice, I set up a new plan but I selected only one OneDrive (a subfolder in D:\Cloud) and that's enough to make it work.
So don't try to backup multiple OneDrive local folders but one at a time in a separate backup plan.
I hope this will help others.
Regards,
Seb
 

      
                
                
                    
                                                    Fri, 03/15/2024 - 16:20
