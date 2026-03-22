# Filename is limited on encrypted Synology NAS drive

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/filename-limited-encrypted-synology-nas-drive

## Original Post
**Author:** Unknown

Filename is limited on encrypted Synology NAS drive

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi,

I have an issue with backup storage on our own device. I'm using a Synology backup device with a encrypted share. This encrypted share has a limitation in the name of files, the limit of the filename length is 143.

When creating a backup with Acronis I see in the log that Acronis is trying to create the following file which failed:
".tmp.7A122197-03BE-4957-BC00-B17E24CD061C.VNWB1-NET.domainname.local-1A2D3A2B-1D76-4460-8DDB-B15B94C5FEB4-DA4F926F-864C-4D2B-8DE7-FA820D0B2D6BA.xml".
The length of the temporary file is 148 and contains computername(9 char) and domainname (18 char).

How can I limit the lenght of the filename of Acronis?

Best regards,

Eric

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 10/12/2015 - 14:22

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Dmitry Zelensky
                            

                            
                    
                        Acronis Program Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 166
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Eric,
This temporary file is necessary to create the metadata for the local backup, and there is no way to limit it's length but to limit all non Acronis related parts (computer name and domain name).
A workaround I see for this issue is to create a backup in a non-encrypted share that would allow over 143 characters in a file name, and then use 3rd party tools to copy the created content to the encrypted share (you can even use the post-backup command to initiate this process). In this case you will not be able to select the final destination as a restore point in Backup Management Console, restore would be possible only using Bootable Media.
In any case please submit a support request to report this issue so it can be addressed properly.
Thank you,

      
                
                
                    
                                                    Mon, 10/12/2015 - 15:36
                                                                            
                                
                            
                                            
                                            
    
                    
                Dmitry Zelensky | Product Manager

Acronis Customer Central |  Acronis Backup Software

For more answers to your questions, try our Knowledge Base and Video Tutorials

Our mission is to create Customer success. Our management team welcomes your comments and suggestions on how we can improve the overall support we provide to you. Please send your comments, suggestions, or concerns to Managers or submit your feedback here.

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Eric TH
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok thanks, find a workaround now so problem is solved.

      
                
                
                    
                                                    Tue, 11/03/2015 - 18:40
