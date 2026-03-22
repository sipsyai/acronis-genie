# Unable to select folder

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/unable-select-folder

## Original Post
**Author:** Unknown

Unable to select folder

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Tristan Le Louedec
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
I need to backup a Mac OS X. When i'm trying to select folder there is a message :
Informations additionnelles:
------------------------
Code d'erreur: 2
Module: 38
LineInfo: 0xEA40B4277FBFB9ED
Champs: {"$module":"disk_bundle_macia64_3917","string":"\r"}
Message: URI non valide : Caractère incorrect rencontré.
 
 
Can you help me ? I don't understand why...

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 06/21/2017 - 08:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Tristan,
I see, that you already work on this issue with Acronis support team. I'll post the outcome here for other users.
"URI is invalid: Incorrect symbol encountered" error message means that backup source contains special symbols in name which could not be represented properly in unicode, therefore browsing of the folder failed. 
The issue with incorrect symbol parsing has been reported to the dev team, the internal number for reference is ABR-118934. 
The root cause for this error is when some file in the folder contains control character in its name (https://en.wikipedia.org/wiki/Control_character)
If you see that this is indeed the case, you may want to apply the following workarounds while the issue is being fixed on our side: 
- rename original files, if possible (in example, if there are only few of them) 
- select entire disk for backup and then set up appropriate file filters options (http://www.acronis.com/en-us/support/documentation/Acronis_Backup_Cloud/index.html#19769.html) 
A permanent fix will be in the next agent-related release. 
 

      
                
                
                    
                                                    Thu, 06/29/2017 - 09:33
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Edward Smith
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello, has this been resolved?  Attempting to complete file/folder backups on Mac OS 10.11 and cannot browse user's directory.  Latest client installed.
 
URI is invalid: Incorrect symbol encountered.
DATE AND TIME
Sep 13, 2017, 04:01:22 PM
CODE
0x00260002
MODULE
38
MESSAGE
Error

Additional info:
------------------------
Error code: 2
Module: 38
LineInfo: 0xEA40B4277FBFB9ED
Fields: {"string":"\u000b","$module":"disk_bundle_macia64_3917"}
Message: URI is invalid: Incorrect symbol encountered.

      
                
                
                    
                                                    Wed, 09/13/2017 - 20:10
