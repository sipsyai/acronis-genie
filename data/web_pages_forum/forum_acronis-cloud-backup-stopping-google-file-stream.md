# Acronis Cloud Backup Stopping Google File Stream

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/acronis-cloud-backup-stopping-google-file-stream

## Original Post
**Author:** Unknown

Acronis Cloud Backup Stopping Google File Stream

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    James Fouracre
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 5
                
            
            
                
                    Comments: 15
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hi, 
Just thought I would post this here as we had to work this out. After updating Acronis Cloud Backup. I noticed it changed to Acronis Cyber Protect. 
Our client contacted us saying their GoogleFileStream (G:) drive no longer worked. 
Anyway it turns out after removing Acronis it fixes the issue. 
I have whitelisted the process now in Acroins, however we can't get it to work on 1 machine now and I am worried about Google File Stream updates, having to whitelist the process when it updates the version and changes the directory.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Fri, 05/01/2020 - 22:06

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello James,
thank you for your posting! I've found a similar issue in our internal records reported recently, it is still under investigation. As the root cause is unknown, I'd strongly recommend raising a support ticket, so that our engineers can look into the situation on your environment. 

      
                
                
                    
                                                    Mon, 05/04/2020 - 09:27
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Haines Friedman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi-
Just to add another voice to this, we noticed exactly the same behavior. We upgraded our agents from 12.5.15300 to 12.5.22210 and Google File Steam immediately broke. Google's support helped us narrow down the issue and uninstalling Acronis fixed the issue. Is anyone aware of a way to resolve the issue while staying on version 22210?

      
                
                
                    
                                                    Mon, 09/14/2020 - 14:22
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Maria Belinskaya
                            

                            
                    
                        Forum Support specialist 
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2012
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Haines,
thank you for posting!
The issue has been fixed in the agent build 22750. Please update the agent to the latest build.

      
                
                
                    
                                                    Mon, 09/14/2020 - 17:06
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Maria Belinskaya | Acronis Forum Support Specialist

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support/

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Haines,
according to https://dl.acronis.com/u/baas/rn/9.0U2/en-US/AcronisCyberCloud_relnotes.htm the issue has been fixed in the Update 2 for Acronis Cyber Cloud 9.0 (build 22750)
[ADP-7742][KERNEL-9308] Google Drive File Stream is blocked.
Unfortunately, I'm not aware of any workarounds for the earlier builds, please open a support ticket, so that one of our engineers can look into the situation and suggest more options. 

      
                
                
                    
                                                    Mon, 09/14/2020 - 19:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Haines Friedman
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Maria and Ekaterina-
 
Thanks for your input! Unfortunately we get Acronis through Kaseya, so we're at their mercy in terms of upgrading. However, I found that this is an error caused by a specific system driver that Acronis Cyber Protect loads. The driver is named "ngscan" and appears to be a virus scanner. We're only using the product for backup, not active protection, but Acronis loads the driver anyway. Disabling it resolved our issue on an older version of the agent without impacting the functionality we care about. Posting in case anyone else is in the same boat with regards to upgrades. Thanks!

      
                
                
                    
                                                    Fri, 09/18/2020 - 16:12
                                                                            
                                
                            
                                            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Haines, thank you for sharing an update\your solution to the issue! I'm sure other users will find it helpful! 

      
                
                
                    
                                                    Tue, 09/22/2020 - 14:17
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support
