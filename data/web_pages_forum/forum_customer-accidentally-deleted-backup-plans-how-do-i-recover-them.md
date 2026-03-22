# Customer accidentally deleted Backup Plans; how do I recover them?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/customer-accidentally-deleted-backup-plans-how-do-i-recover-them

## Original Post
**Author:** Unknown

Customer accidentally deleted Backup Plans; how do I recover them?

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Boreas Jeff
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                
                    
                        
            One of our customers accidentally deleted two key backup plans that backed up files to the cloud with high retention.  So it's vital that we restore the Backup Plans as soon as possible. What's the process to restore a Backup Plan in the cloud gateway?  I can browse and see the backups are still there, but no backup plans...
Thanks,
Jeff

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Tue, 06/25/2019 - 16:48

                                                          
                                                            
                                                                                        
    
                            
                Products: 
                Acronis Cloud Backup 12.5

            
            
                                                    
                    
                
                        
            
                
  
  



    
    


  
  2 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello Jeff,
sorry to know about the issue..I'm afraid the only option would be recreating plans from scratch, unless you've saved the scripts beforehand (exported the config). 

      
                
                
                    
                                                    Wed, 06/26/2019 - 09:30
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Jeff, actually, there is a way, but it involves a bit of effort. In the upcoming Acronis Cyber Cloud 8.0 version it will be easier with the "Archive Name" option.
 
The main purpose of the task, as I understood it, is that you would like to continue backing up to the same archives.
The way the backup plan "chooses" where to back up is defined by a parameter such as an archive name.
Name consists of "machine name" + plan ID + machine ID + the extension (e.g. .tibx).
 
The plan ID is what you need to change for a new "recovered" backup plan.
And the process is descirbed in the following public article -> https://kb.acronis.com/content/60276
 
Hope that helps!

      
                
                
                    
                                                    Thu, 06/27/2019 - 19:22
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Emilio Bruna
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 7
                
            
            
                
                    Comments: 6
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi, can be added as features request the add of export/import backup plans configuration from web console please?
I think is good for restore backup plans accidentally deleted by customers faster and easy and check if there are plans were changed by someone (there aren't full logs of any changes now, at least will be also possibile comparing the two export file for see any changes done)
Thanks for any reply and sorry for my bad english.
 

      
                
                
                    
                                                    Tue, 07/16/2019 - 15:08
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fedor Kondrashov wrote:

Jeff, actually, there is a way, but it involves a bit of effort. In the upcoming Acronis Cyber Cloud 8.0 version it will be easier with the "Archive Name" option.
 
The main purpose of the task, as I understood it, is that you would like to continue backing up to the same archives.
The way the backup plan "chooses" where to back up is defined by a parameter such as an archive name.
Name consists of "machine name" + plan ID + machine ID + the extension (e.g. .tibx).
 
The plan ID is what you need to change for a new "recovered" backup plan.
And the process is descirbed in the following public article -> https://kb.acronis.com/content/60276
 
Hope that helps!


 
Thank you for that, this is very valuable information!

      
                
                
                    
                                                    Mon, 07/22/2019 - 14:42
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ekaterina
                            

                            
                    
                        Forum Moderator
                    
                
            
                        
                
                    Posts: 239
                
            
            
                
                    Comments: 7073
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Emilio Bruna wrote:

Hi, can be added as features request the add of export/import backup plans configuration from web console please?
I think is good for restore backup plans accidentally deleted by customers faster and easy and check if there are plans were changed by someone (there aren't full logs of any changes now, at least will be also possibile comparing the two export file for see any changes done)


Thank you, Emilio. added your comment as a vote for the existing feature request.  

      
                
                
                    
                                                    Mon, 07/22/2019 - 15:13
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ekaterina Surkova | Forum Moderator

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Boreas Jeff
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 4
                
            
            
                
                    Comments: 10
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fedor, yes, the point is to continue backing up to the same archive. Unfortunately I get Access Denied when trying to access that link.  I already recreated the backup plan and so lost the backup chain, but would be nice to see a way to do this in case it happens again.

      
                
                
                    
                                                    Tue, 10/06/2020 - 21:03
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cloud Backup 12.5

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Fedor Kondrashov
                            

                            
                    
                        Professional Services Manager
                    
                
            
                        
                
                    Posts: 6
                
            
            
                
                    Comments: 60
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Heya, Jeff!
 
The process was immensely simplified and is now available from the GUI.
Check the article that goes through the steps -> https://kb.acronis.com/content/59725

      
                
                
                    
                                                    Tue, 10/06/2020 - 21:13
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Protect Cloud

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    George_Fusioned
                            

                            
                    
                        Regular Poster
                    
                
            
                        
                
                    Posts: 13
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Fedor Kondrashov wrote:

Heya, Jeff!
 
The process was immensely simplified and is now available from the GUI.
Check the article that goes through the steps -> https://kb.acronis.com/content/59725


That's a great addition, thank you! Indeed, it's super easy now - great work.

      
                
                
                    
                                                    Tue, 10/06/2020 - 21:32
