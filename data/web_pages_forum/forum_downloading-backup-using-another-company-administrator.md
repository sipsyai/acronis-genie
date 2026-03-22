# Downloading backup using another company administrator

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-backup-cloud-forum/downloading-backup-using-another-company-administrator

## Original Post
**Author:** Unknown

Downloading backup using another company administrator

        
  



    
  


  
              
          
        Thread needs solution      
      
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                
                    
                        
            I have a company administrator ( A ) that is doing all the backups and at the user form and under its name its has a total of 51GB worth of data.Than i created another company administrator ( B ). B is able to do recovery part of data on the site itself. But when it comes to recovery > more ways to recover > download files > there is no backup to download , using the company administrator ( B ) 's ID and password . Anyway to solve this issue ? Because client wants to able to recover by themselves using the download file function

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Wed, 01/15/2020 - 09:25

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Péter Szatmári
                            

                            
                    
                        Frequent Poster
                    
                
            
                        
                
                    Posts: 16
                
            
            
                
                    Comments: 619
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello jianzhi!
Which product (version/build) are you using?
I'm guessing your talking about Cloud and choosing the option at SelectedMachine > Recovery > More ways to recover > Download files
-- Peter

      
                
                
                    
                                                    Wed, 01/15/2020 - 15:17
                                                                            
                                
                            
                                            
                                            
    
                            
                Products: 
                Acronis Cyber Backup 12.5
            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    jianzhi low
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 8
                
            
            
                
                    Comments: 9
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi peter ,
yes i am using  backup cloud  v12.5.14800. selected the machine > recovery> more ways to recover > download files

      
                
                
                    
                                                    Thu, 01/16/2020 - 07:57
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Ivaylo Tsvetkov
                            

                            
                    
                        Acronis engineer
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 85
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hello jianzhi low,
Acronis' current plan is to replace Web Restore console with a new service in Cloud. If account has "company administrator" role, then it should be possible to have access to backups created by other users in this company through this service. It will be possible to browse, manage data and backups in the Cloud. It will be released in one of the future product versions, still under development.
Currently all this is not possible with Web Restore console, however you could use the Backup Console, all backups are shared between "company administrator" users with limitation of up to 100 MB of archive/files/folder/zips per download.

      
                
                
                    
                                                    Wed, 01/29/2020 - 10:32
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Ivaylo Tsvetkov | API Platform Senior Support Engineer 

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                            
                Products: 
                Acronis Cyber Protect Cloud
