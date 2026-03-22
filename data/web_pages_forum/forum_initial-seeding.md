# Initial Seeding

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/initial-seeding

## Original Post
**Author:** Unknown

Initial Seeding

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Antoine DECAUX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                
                    
                        
            HI,
I can make a backup with the option Initial seeding in my clients then I recover the files and then I can not find how to upload the files from my connection to the cloud Can you help me ? I peeled all the KB's likely to help me and I can not find the solution. Thanks Antoine

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 09/22/2017 - 16:15

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Antoine
Can you please provide clarity on the following:
Which version of Acronis Backup are you using?
Was "Initial Seeding" in backup option enabled before the backup was made and left enabled afterwards?
Did the seed loading backup complete successfully?
To which device was the seed loading device made? (Local machine, external device etc)
Which Acronis cloud are you using?
With this information I will be able to advise you on how to proceed to upload the data to the cloud.
Best regards

      
                
                
                    
                                                    Tue, 09/26/2017 - 09:21
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Antoine DECAUX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Jays,



Finally, I managed to upload my backup. I followed the KB56070 : https://kb.acronis.com/content/56070
I had a problem with Python installation.

The procedure remains complicated for a novice like me ;-)Best regards
 




      
                
                
                    
                                                    Thu, 09/28/2017 - 10:07
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Antoine
I am glad you have managed to upload your data to the cloud. The process going forward is very simple if you require it in future:
1. Create backup set with the seed loading option enabled
2. Point backup to an external device
3. Once backup is complete plug the external device into the machine where you have installed Python
4. Open CMD as admin and run the following commands:
is_info <path> (To find the IS token)
is_me <path> (To execute the upload)
Please also take note of the following
1. You do not need to install Python every time you want to perform a seed loading you can keep using the same machine were Python is installed on
2. You can run multiple seed loading jobs at the same time but I would recommend that you limit one job per 20 MB of internet speed
3. Please do not delete the initial seeding backup plan as without this incremental backups will not continue 
Please feel free to inbox me if you require any further assistance or require any additional information I will be glad to assist you.
Regards

      
                
                
                    
                                                    Thu, 09/28/2017 - 14:25
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Antoine DECAUX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            I take note of your information

Thank you very much for the follow up 

      
                
                
                    
                                                    Thu, 09/28/2017 - 14:31
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Antoine DECAUX
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 3
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi everyone,
 
I have uploader my initial seeding (see below) but I can not start
incremental backups now.I have the following error message : Cannot create an incremental backup because file 'Inetdéco-5A21Axxx.TIB' has a zero size.
Code d'erreur 0x01350016+0x01350016+0x00A100FC+0x01490003+0x00010424+0x00010424+0x000003F8


Can you help me ? 
 

      
                
                
                    
                                                    Tue, 10/10/2017 - 15:56
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Antoine,
Looks like the issue described in Acronis Backup Cloud: incremental to an initial seeding backup fails with "Failed to create an incremental backup in backup archive".

      
                
                
                    
                                                    Wed, 10/11/2017 - 08:54
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
