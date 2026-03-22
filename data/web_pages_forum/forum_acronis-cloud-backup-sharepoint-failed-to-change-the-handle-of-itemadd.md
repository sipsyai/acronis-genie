# Acronis Cloud Backup - Sharepoint: "Failed to change the handle of Item/Add."

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/acronis-cloud-backup-sharepoint-failed-change-handle-itemadd

## Original Post
**Author:** Unknown

Acronis Cloud Backup - Sharepoint: "Failed to change the handle of Item/Add."

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Adrian Kjellquist
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello Acronis Forum!
I've unfortunately encountered an error message when we run Cloud backups from our customers Sharepoint. Here is the information I got and I hope it is sufficient enough for you guys to help me understand the issue.

Location in the Acronis website: Manage accounts > Devices > Microsoft Office 365
Error message:
-START-
 
Error title: Backup plan 'Sharepoint sites to Cloud storage (4)'
Status: Succeeded with warnings
Duration: 1 min
-
Backing up '[insert sharepoint site name here]'
 
Warning: Failed to change the handle of Item/Add.
Warning: Failed to change the handle of Item/Add.
-END-
Unfortunately I have not understood this message. This is what I've tried to do to resolve this issue myself:
1) Checked: https://kb.acronis.com/backup-cloud-known-solutions (Didn't find what I looked for)
2) Checked: https://kb.acronis.com/acronis-backup-cloud (Did not find anything there either, now even when I expanded the views.
3) Checked: https://kb.acronis.com/acronis-backup-cloud (Could not get any results regarding this issue)
I hope someone else has experienced this and can share what they have found out. I am asking you first as this issue is not urgent and does not cause backup failures.
Kind regards,
Adrian Kjellquist from ECIT 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 04/05/2019 - 11:58

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Adrian,
welcome to Acronis forums! I've checked in our internal systems if there are any known issues with a similar description and found one that looks quite similar. According to the issue description, it occurs on SharePoint sites with many sub catalogs and is caused by the OneNote documents with hierarchical structure. This issue is expected to be fixed in the latest Update Acronis Data Cloud 7.9, however I'd still recommend raising a support ticket, so that our engineers can take a look at the diagnostic information and confirm whether it's a known issue or not. 

      
                
                
                    
                                                    Thu, 04/11/2019 - 13:11
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Adrian Kjellquist
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ekaterina wrote:

Hello Adrian,
welcome to Acronis forums! I've checked in our internal systems if there are any known issues with a similar description and found one that looks quite similar. According to the issue description, it occurs on SharePoint sites with many sub catalogs and is caused by the OneNote documents with hierarchical structure. This issue is expected to be fixed in the latest Update Acronis Data Cloud 7.9, however I'd still recommend raising a support ticket, so that our engineers can take a look at the diagnostic information and confirm whether it's a known issue or not.  


Thank you for your reply, Ekaterina!
I hope the latest update will fix this issue and the other ones that is quite simular.
I will also follow your advice and contact your support.
Again, thank you for your information about this issue. I think this will help others that experiences the same problem and I will also notify my colleagues about this too.
Kind regards,
Adrian Kjellquist

      
                
                
                    
                                                    Mon, 04/15/2019 - 07:19
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            You are welcome, Adrian! 
> I will also follow your advice and contact your support.
Please share with us the outcome, thank you in advance! 

      
                
                
                    
                                                    Mon, 04/15/2019 - 13:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
