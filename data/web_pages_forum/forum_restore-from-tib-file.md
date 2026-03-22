# Restore from .TIB file

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/restore-tib-file

## Original Post
**Author:** Unknown

Restore from .TIB file

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Maik Brugman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Our company has been testing with Acronis Backup Cloud.
Since we want to test every possible restore method, I wanted to test restoring from the .TIB file.
 
Example:
The customers office has data loss due to a powerloss, this means the cloud won't be reachable at that moment.
If we could download the .tib file from the cloud (Azure  or Acronis) we could restore from a USB EHD.
EDIT: ofcourse one of my co-workers would download the .TIB file in our office, while I'm offering support on location.
 
The problem here is: I cannot for the love of me find a way to restore the .TIB files.
Is there something that I'm missing?
Kind Regards,
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 03/16/2017 - 12:33

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eugene Tanasiev
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 20
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Maik,
I would recommend to use Large Scale recovery (LSR)
LSR will download all backups associated with one agent
https://kb.acronis.com/content/56070
 
Later on you may proceed with disk/volume or file recovery using Bootable media
https://dl.managed-protection.com/u/baas/help/7/admin/en-US/index.html#33518.html
 
I am always at your service should you have any further questions.
Regards,
Eugene

      
                
                
                    
                                                    Thu, 03/16/2017 - 14:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    cmessina@global-systems.com.ar
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I used to have Acronis Cloud Backup, and since we discontinued the contract, I have a tib file than I need to descompress
can you help me?
claudio
 

      
                
                
                    
                                                    Tue, 10/30/2018 - 22:21
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Claudio,
You have the following options:
Install an Agent (here a download link http://dl.managed-protection.com/u/baas/4.0/12.5.12110/Backup_Agent_for_Windows_x64.exe ) and used it to recover data from the .tib
Burn a bootable media and perform recovery under a bootable media http://dl.managed-protection.com/u/baas/4.0/12.5.12110/Boot_media.iso 
 

      
                
                
                    
                                                    Wed, 10/31/2018 - 10:01
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
