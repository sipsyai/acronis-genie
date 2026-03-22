# How to obtain source folder list an their sizes?

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-backup-cloud-forum/how-obtain-source-folder-list-their-sizes

## Original Post
**Author:** Unknown

How to obtain source folder list an their sizes?

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                
                    
                        
            Hello,
Is there any way to obtain the Files/Folders list of a Backup Plan and their original sizes?... or maybe obtain the total size of the files/folders/drives that are configured to make backup in origin? Maybe using command line interface?
Thank you so much.

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Mon, 06/03/2019 - 17:16

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Good day
If you are referring to obtaining a list of what you are backing up in a files/folder selection then the only to get the information is from the console be clicking on the backup set and browsing what you have selected for backup,
Regarding sizing if you are referring to RAW data size you will need to obtain this from the source of data and if you are referring to compressed/de-duplicated data then this is obtained from the backup management console under backups and then browsing the location of where the data is storage. This will show you how large the backed up data is once it has been compressed/de-duplicated etc.
I hope this helps you
Kind regards

      
                
                
                    
                                                    Tue, 06/11/2019 - 13:19
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok,
I am refering to origin raw data size of selected files/folders.
 
Thank you

      
                
                
                    
                                                    Tue, 06/11/2019 - 14:15
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Jays
                            

                            
                    
                        Forum Member
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 96
                
            
                                                    
            
              



        

                                
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The raw data size before backup will need to be obtained from the source prior to backup as there is no way of getting this information in the backup management console during the setup of a backup plan. Only after a backup has completed and data is stored either in cloud or local in tib/tibx format will the backup management console provide you more information on the size of the compressed/de-duplicated data 
 

      
                
                
                    
                                                    Tue, 06/11/2019 - 14:29
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,

Jason,
Acronis Certified Engineer,

Information provided AS-IS with no warranty of any kind.

To contact Acronis support, please follow http://www.acronis.com/en-us/support/

            
                            
                Products: 
                I work with all Acronis products

            
            
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    rlopez
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 3
                
            
            
                
                    Comments: 4
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Ok Jason,
Thank you very much.

      
                
                
                    
                                                    Tue, 06/11/2019 - 14:31
