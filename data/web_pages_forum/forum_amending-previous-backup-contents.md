# Amending previous backup contents

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/amending-previous-backup-contents

## Original Post
**Author:** Unknown

Amending previous backup contents

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Good afternoon all,
 
A bit of an odd one here that I'm hoping to explore a bit further: If I have backups created that I want to amend the contents of - is this possible?
 
A bit of context: We have a customer who has around 3 months of backups with a 6 month retention cut off - they have realised they have around 500GB of files they don't actually need and therefore don't want to backup anymore - to cut down on the cloud space without blowing away all of the backups, can this 500GB be "cut out" of previous backups?
 
I'm not expecting a "Yes" here - but thought I'd explore the situation Thanks in advance! :)

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 02/05/2019 - 12:29

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Backup Cloud

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Phil,
thank you for your posting! The only way to decrease the size of an Cloud archive would be
deleting recovery point(s) that contain unique data (files/ folders that are not present under other recovery points - when a file is already present in a previous backup, we create a symlink in the next incremental slice instead of backing up the actual data).
	 
 Delete some backup source(s) from the backup plan’s “Items to back up” section: 
For disk backup: uncheck one of the disks
For file backup: uncheck some files/folders
	Once done, wait until longest retention period passes.
 

      
                
                
                    
                                                    Mon, 02/18/2019 - 09:45
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Phil Whitmore
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Ekaterina,
 
Thanks for the feedback - I expected as much but its interesting to know about how the system manages these incremental slices none the less.
 
Kind regards,
 
Phil

      
                
                
                    
                                                    Thu, 02/21/2019 - 17:08
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Backup Cloud
