# File filter does not exclude folders from backup

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/file-filter-does-not-exclude-folders-backup

## Original Post
**Author:** Unknown

File filter does not exclude folders from backup

        
  



    
  


  
              
          
        Thread solved      
          
      
        View Solution      
    
  
      






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    Allan Whitney
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 1
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            while creating a new backup profile I am unable to to select entire machine to cloud for the backup option and exclude a folder location using File filter. 
I am creating a plan for multiple machines and i would like to exclude a Sharepoint site users are syncing to their machines. the folder location I want to exclude is C:\Users\Username\Call Center, Inc\ 
previous attempts to exclude this from a backup(entire machine to cloud) include:
C:\Users\*\Call Center* Inc\*
C:\Users\*\Call Center, Inc
C:\Users\*\Call Center? Inc\
C:\Users\*\Call Center? Inc
C:\Users\*\Call Center? Inc\*
C:\Users\*\Call Center*
whenever i include the comma it changes it to an enter stroke example
C:\Users\*\Call Center, Inc\
C:\Users\*\Call Center
Inc\
 

      
                                                    
                                            
                
            
                            
                    
                        
                            
                              Thu, 09/22/2022 - 17:47

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  

    
    







            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Georgi Dimitrov
                            

                            
                    
                        Support Engineer
                    
                
            
                        
                
                    Posts: 10
                
            
            
                
                    Comments: 49
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Hi Allan, 
Please make sure to exclude as follows - https://www.acronis.com/en-us/support/documentation/CyberProtectionServ…
In case you still face difficulties, please open a case with our support team and let us know at which step and we will happily assist.
Thank you for your time. 

      
                
                
                    
                                                    Mon, 09/26/2022 - 11:02
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Georgi Dimitrov | Support Engineer

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Patrick Linley
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            The documentation says nothing about spaces in the path (that I can find).
So to exclude:
C:\Users\user1\OneDrive - My OneDrive Folder
Is it entered as above, or does it need single or double quotes, or use the old DOS method with ~'s, etc. etc.?

      
                
                
                    
                                                    Sat, 10/19/2024 - 20:16
                                                                            
                                
                            
                                            
                                                                
                            
  






                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Patrick Linley wrote:

The documentation says nothing about spaces in the path (that I can find).
So to exclude:
C:\Users\user1\OneDrive - My OneDrive Folder
Is it entered as above, or does it need single or double quotes, or use the old DOS method with ~'s, etc. etc.?


 Hello!
To exclude that you should enter the path to the folder as you posted above ( C:\Users\user1\OneDrive - My OneDrive Folder ) 
Best regards.

      
                
                
                    
                                                    Sun, 10/20/2024 - 18:44
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                
                            
  

    
    








                        
                                                        
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Patrick Linley
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 2
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            Thanks... I would suggest that the documentation be updated to reflect this information clearly.
 

      
                
                
                    
                                                    Mon, 10/21/2024 - 14:25
